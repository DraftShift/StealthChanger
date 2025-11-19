# tool_crash

Work in progress to develop crash detection plugin for klipper-toolchanger that supports inductive as well as tap probes and attempts address issues with existing crash detection

# Usage
- Install
  ```
  wget -O - https://raw.githubusercontent.com/DraftShift/StealthChanger/refs/heads/main/UserMods/cekim-git/ToolCrash/install.sh | bash
  ```
- add [tool_crash] to printer.cfg
  - See [example tool_crash.cfg](./tool_crash.cfg)
  - Suggested initial configuration for inductance Z configurations is no arguments to this section
  - Suggested initial configuration for TAP configurations would be ingore_events: probing
  - [tool_crash] should be added AFTER your toolchanger and tool .cfg files are included in your printer.cfg 
- add start/stop calls to [homing_override] and PRINT_START/PRINT_END as previously with names
  - START_TOOL_CRASH_DETECTION/ STOP_TOOL_CRASH_DETECTION
    - Typical configuration will start during PRINT_HOME and stop during PRINT_END.
    - Docking is implicitly ignored regardless of configuration.  No additional start/stop around docking is required
    - Particularly for inductive (vs TAP) homing, it might make sense to START/STOP within your homing_override as well to detect crashes when manually homing.
  - NOTE: you should remove any calls to existing toolchanger based START/STOP_TOOL_PROBE_CRASH_DETECTION (note the additional "PROBE" in the name)
- If using inductive probing, no TAP trigger should occur during homing... so no further action should be required
- If using TAP probing you can either add STOP/START to your homing_override use use the ignore feature in the [tool_crash] .cfg section
  - ignore_events: probing
- Other configuration variables which can be changed, but should not need to be:
  - watchdog_interval: 0.5  \# seconds between consistency checks
  - watchdog_threshold: 2   \# number of times we must see an error condition prior to reporting it
  - home_timeblock: 1.0     \# time in seconds after a homing event before instant error reporting
  - crash_gcode: \# custom gcode called in place of the hard-shutdown on error... NOT REQUIRED
  - WARNING: adding optional crash_gcode (other than M112) delays the response to a crash event by an amount dependant on what is queued up in terms of "movement" in the print.  Depending on the queued events, this can be seconds or minutes of delay.  For the most rapid response to TAP triggering, remove crash_gcode entirely from your configuration.  In testing, this has allowed it to catch and stop crashes before the head has even left the shuttle.  There is no guarantee it will stop it that fast, it depends on the speed of the "crash" event and the movement around it.
- watchdog_interval is the time in seconds between consistency checks of toolchanger internal state
- watchdog_threshold is the number of times an error condution must be observed by the watchdog before emitting an error
- home_timeblock is the time that must after a home probe event before instant TAP sensor error detection will be reported if "ignore_events: probing" is set.... 
