# Support for toolchnagers
#
# Copyright (C) 2025 @Contomo and @cekim
#
# This file may be distributed under the terms of the GNU GPLv3 license.

import logging
from .toolchanger import (
    STATUS_CHANGING, STATUS_INITIALIZING,
)

STATE_PROBING     = 'probing'
STATE_TOOLCHANGE  = 'toolchange'
STATE_IDLE        = 'idle'
IGN_PROBING     = 'probing'
IGN_ALL         = 'all'
_ALLOWED_IGNORES = {IGN_PROBING, IGN_ALL}

class ToolCrash:
    def __init__(self, config):
        self.printer     = config.get_printer()
        self.reactor     = self.printer.get_reactor()
        self.config      = config
        self.name        = config.get_name()
        self.gcode       = self.printer.lookup_object('gcode')
        self.toolhead    = None
        self.toolchanger = self.printer.lookup_object('toolchanger')

        # theres probably a proper way to do this with get_choice, or maybe getlist(parser=choice) or something
        raw = {s.strip().lower() for s in config.getlist('ignore_events', [], sep=',') if s.strip()}
        unknown = raw - _ALLOWED_IGNORES
        if unknown:
            allowed = ", ".join(sorted(_ALLOWED_IGNORES))
            bad     = ", ".join(sorted(unknown))
            raise config.error(f"[tool_crash] invalid ignore_events: {bad}. Allowed: {allowed}")
        self.ignore = {IGN_PROBING} if IGN_ALL in raw else raw

        self.gcode_macro = self.printer.load_object(config, 'gcode_macro')
        self.crash_gcode = self.gcode_macro.load_template(config, 'crash_gcode') if config.get('crash_gcode', None) else None
        
        tool_probe_pins = self._parse_pins('tool_probe','pin')
        tool_detect_pins = self._parse_pins('tool','detection_pin')

        if not tool_probe_pins and not tool_detect_pins:
            raise config.error(f"[tool_crash] no trigger pins defined in tool or tool_probe sections")

        self.enabled = False
        self.expected_tool = None
        self.crash_mintime = config.getfloat('crash_mintime', 0.5, above=0.)
        self._watchdog_interval=config.getfloat('watchdog_interval',0.500, above=0.)
        self._watchdog_error_count=0
        self._watchdog_error_threshold=config.getint('watchdog_threshold',2);
        self._home_timestamp=0.0
        self._home_timeblock=config.getfloat('home_timeblock',1.0, above=0.)
        self._state = STATE_IDLE
        self._watchdog_timer = None
        
        self.printer.register_event_handler('klippy:connect', self._on_connect)
        self.printer.register_event_handler('homing:homing_move_begin', self._on_homing_move_begin)
        self.printer.register_event_handler('homing:homing_move_end',   self._on_homing_move_end)

        self.gcode.register_command('START_TOOL_CRASH_DETECTION',
                                    self.cmd_START_TOOL_CRASH_DETECTION,
                                    desc=self.cmd_START_TOOL_CRASH_DETECTION_help)
        self.gcode.register_command('STOP_TOOL_CRASH_DETECTION',
                                    self.cmd_STOP_TOOL_CRASH_DETECTION,
                                    desc=self.cmd_STOP_TOOL_CRASH_DETECTION_help)
        
        buttons = self.printer.load_object(config, 'buttons')
        ppins   = self.printer.lookup_object('pins')

        # use the same state pins that toolchanger will use based on .cfg
        detection_pins = tool_probe_pins if tool_probe_pins else tool_detect_pins

        # allow multi-use and register each pin matching toolchanger polarity
        for pin in detection_pins:
            base = f"{pin['chip_name']}:{pin['pin']}"          
            ppins.allow_multi_use_pin(base)
            base = '!' + base if pin['invert'] else base
            buttons.register_buttons([base], self._on_detect_edge)
        
    def _now_pt(self):
        return self.toolhead.mcu.estimated_print_time(self.reactor.monotonic())
    
    # parse out the requested section for the requested name return a list
    def _parse_pins(self,section_name,pin_name):
        pin_list = []
        ppins   = self.printer.lookup_object('pins')
        if self.config.get_prefix_sections(section_name + ' '):
            for section in self.config.get_prefix_sections(section_name + ' '):
                if section.get(pin_name,None) is not None:
                    p  = ppins.parse_pin(section.get(pin_name), can_invert=True, can_pullup=True)
                    if p:
                        pin_list.append(p)
        return pin_list
    
    def _on_connect(self):
        self.toolhead = self.printer.lookup_object('toolhead')
    
    def _on_homing_move_begin(self, hmove):
        self._state = STATE_PROBING
        self._home_timestamp = self._now_pt()
        
    def _on_homing_move_end(self, hmove):
        self._state = STATE_IDLE
        self._home_timestamp = self._now_pt()
        
    def _ensure_watchdog(self):
        if self._watchdog_timer is not None:
            return
        def _tick(evt):
            if not self.enabled:
                self._watchdog_timer = None
                return self.reactor.NEVER
            self._sync_expected()
            return evt + self._watchdog_interval
        self._watchdog_timer = self.reactor.register_timer(_tick, self.reactor.monotonic() + self._watchdog_interval)

    def _cancel_watchdog(self):
        self._watchdog_error_count = 0
        if self._watchdog_timer is not None:
            self.reactor.unregister_timer(self._watchdog_timer)
            self._watchdog_timer = None

    # Watchdog consistency checks of toolchanger state
    def _sync_expected(self, initial=False):
        # check for fall-through/ignore cases
        if self.toolchanger.status in (STATUS_CHANGING, STATUS_INITIALIZING):
            return
        elif self._state == STATE_PROBING:
            return
        # compare active tool to tap sensor state
        active_tool = self.toolchanger.active_tool
        err_msg = ""
        if active_tool is not None:
            active_count=0
            for tool in self.toolchanger.tool_numbers:
                active_count += 1 if self.toolchanger.tools[tool].detect_state else 0

            # if no active tools, or active tool's state is wrong - then we have crashed
            if active_count==0 or not self.toolchanger.tools[active_tool.tool_number].detect_state:
                self._watchdog_error_count += 1 # note the error
                err_msg = "tool_crash: watchdog detected crash of " + self.toolchanger.active_tool.name
            elif active_count == 1:
                self._watchdog_error_count=0; # reset - all is well
            else: # multiple tools will eventually cause a crash once resolved..  
                self._watchdog_error_count = 0
            
        # check to see if we've seen multiple consecutive failures
        if self._watchdog_error_count >= self._watchdog_error_threshold:
            self._do_crash(err_msg,self._now_pt())

    # Edge detection checks basded on trigger of sensors
    def _on_detect_edge(self, eventtime, is_triggered):
        # if we are not enabled, ignore it
        if not self.enabled:
            return
        # check for toolchange state - ignore it
        if self.toolchanger.status in (STATUS_CHANGING, STATUS_INITIALIZING):
            return
        # check for proximity to state we are ignoring (probe/homing)
        home_event_delta = self.toolhead.mcu.estimated_print_time(eventtime) - self._home_timestamp
        if self._state == STATE_PROBING or (home_event_delta < self._home_timeblock):
            if IGN_PROBING in self.ignore:
                return

        err_msg = "tool_crash detected"
        if self.toolchanger.active_tool is not None:
            err_msg += ' ' + self.toolchanger.active_tool.name

        self._do_crash(err_msg,eventtime)

    def _do_crash(self,msg, etime):
        self.enabled = False
        self._cancel_watchdog()
        self.gcode.respond_info(msg)
        # either halt now or run/queue custom g-code if provided
        if self.crash_gcode is None:
            self.printer.invoke_shutdown(msg)
        else:
            self.reactor.register_callback(lambda _: self._run_crash_gcode(), etime+self.crash_mintime)
            
    def _run_crash_gcode(self):
        try:
            self.crash_gcode.run_gcode_from_command()
        except Exception as e:
            self.gcode.respond_info(f'crash gcode failed. ({e})')
            raise e        
               
    cmd_START_TOOL_CRASH_DETECTION_help = """
    Enable tool crash detection. Optional T=<num>|TOOL=<name> to set the expected tool"""
    def cmd_START_TOOL_CRASH_DETECTION(self, gcmd):
        self.enabled = True
        self._ensure_watchdog()
        gcmd.respond_info(f'tool_crash: enabled')
    
    cmd_STOP_TOOL_CRASH_DETECTION_help = """Disable tool crash detection."""
    def cmd_STOP_TOOL_CRASH_DETECTION(self, gcmd):
        def _disable_cb(_pt):
            self.enabled = False
            self._cancel_watchdog()
        self.toolhead.register_lookahead_callback(_disable_cb)
        gcmd.respond_info('tool_crash: disabled')

def load_config(config):
    return ToolCrash(config)
