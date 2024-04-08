Toolchangers start with number 0, and count up. So for all the configs, make sure you change all sections. IE, in your T1 config, make sure its extruder1, fan1, etc. See the examples.  **NOTE: The only except to this rule is T0 extruder has no number.**

1. [Toolhead Configuration](#toolheads-configuration)
2. [CANbus](#canbus)
3. [Offsets](#offsets)

## Toolheads Configuration

Please see the repo files for more info on these. [Configuration Files Repo](https://github.com/StealthChanger/Toolchanger/blob/main/Klipper)

You need to add the info in printer.cfg from the repo to your your printer.cfg
You need to have a separate toolhead config for each toolhead, then link those in your printer.cfg, as well as removing/moving the current extruder/hotend config from your printer.cfg file. See the examples in the repo for more information and a starting place. You will have to edit them with your own values.

## CANbus

[Esoterical CANbus](https://github.com/Esoterical/voron_canbus) this is a pretty definitive guide for canbus implementation on klipper.

**Example CANbus layout**

![Example CANbus Layout](https://github.com/StealthChanger/Toolchanger/blob/main/media/can_example.jpg?raw=true)

## Offsets

There are 2 places to set offsets in your toolhead config files. There is gcode_(x/y/z)_offset in the [tool] section, and (x/y/z)_offset in the [tool_probe] section. These do different things. The ones in the [tool] section are always relative to a specific tool. IE, if you homed with T0, then the gcode offsets are relative to T0. When you do multi-material prints, you will have to choose 1 tool to always do the homing, even if you don't use it, because all the other offsets need to be set against it. The [tool_probe] offset is only ever applied when homing with that tool. The gcode offsets are applied when changing a tool.

You should set all the [tool_probe] offsets as well though. If you are only using a single tool, you can home with that tool, and it will use the offset in the [tool_probe] section. You won't need to home with your primary tool first then before you start a print. 

To try and further clarify. Lets say you have 3 tools, T0, T1, and T2. We will say that T0 is your "primary" tool. Setup the probe z_offset like you would any other printer. Make sure the offset is set in z_offset (IE, make sure when you home and go to Z0, the nozzle is actually in that spot). Its location in x/y/z is always going to be 0 in relation to the other tools. So after T0 is homed, T1 and T2 (may) need to have their gcode_(x/y/z)_offset changed so they match the location that the primary tool actually is. There are 2 main ways of doing this. You can use a test print to print layers on top of or next to each other (something like this: [Nozzle Alignment Assist](https://www.printables.com/model/109267-nozzle-alignment-assist)) or you can use a camera (something like [kTAMV Klipper Tool Alignment](https://github.com/TypQxQ/kTAMV) or [IDEX Nozzle Calibration Tool](https://github.com/Life0fBrian/Brians-IDEX-Nozzle-Calibration-tool)).
