Toolchangers start with number 0, and count up. So for all the configs, make sure you change all sections. IE, in your T1 config, make sure its extruder1, fan1, etc. See the examples.  **NOTE: The only except to this rule is T0 extruder has no number.**

1. [Toolhead Configuration](#toolheads-configuration)
2. [CANbus](#canbus)

## Toolheads Configuration

Please see the repo files for more info on these. [Configuration Files Repo](https://github.com/Hellsparks/StealthChanger/blob/main/Klipper)

You need to add the info in printer.cfg to your your printer.cfg
You need to have a separate toolhead config for each toolhead, then link those in your printer.cfg, as well as removing/moving the current extruder/hotend config from your printer.cfg file. See the examples in the repo for more information and a starting place. You will have to edit them with your own values.


## CANbus

[voron_canbus](https://github.com/Esoterical/voron_canbus) this is a pretty definitive guide for canbus implementation on klipper.

**Example CANbus layout**

![Example CANbus Layout](https://github.com/Hellsparks/StealthChanger/blob/main/media/can_example.jpg?raw=true)
