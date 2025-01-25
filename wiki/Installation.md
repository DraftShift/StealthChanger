All sections are required, so please follow all steps carefully.

1. [Klipper Addon](#klipper-addon)
2. [Toolchanger Configuration](#toolchanger-configuration)

**NOTE:** DangerKlipper is not currently supported


**NOTE:** Your klipper version eneds to be newer than Jun 14, 2024 (1591a51)


**NOTE:** Before you start remove your `PRINT_START` and `PRINT_END` macros out of the config as toolchanging requires a specific version of these to initialize and start printing.

## Klipper Addon

You must install [klipper-toolchanger](https://github.com/viesturz/klipper-toolchanger/), Follow instruction on the linked page.


## Toolchanger Configuration

You need `homing.cfg`, `macros.cfg`, `tool_detection.cfg` and `toolchanger.cfg` from [TapChanger Example](https://github.com/viesturz/tapchanger/tree/a277492516af3751aa13f5097a908ab8a88b6eae/Klipper/config-example)

`homing.cfg` assumes you are using sensorless for X axis and a physical switch for Y axis.  It's important to use this file when building your own homing as the order and macros it calls are required.  If you use Hall Effects or switch end stops for both Axis, remove the `_SENSORLESS_HOME_X` call in `[homing_override]` with `G28 X`.  Alternatively if you use sensorless for both you need so update `G28 Y` to use a copy of `_SENSORLESS_HOME_X` but for Y. There is a second place in the homing override that sets your Y rebound.  The default is 20, without keeper you likely want this around 4-5, change `G0 Y{ max_y - 20 } F5000` to `G0 Y{ max_y - 5 } F5000` notice the 20 that changes.  This is something you may need to adjust to figure out the position of your switch.

**NOTE:** when using sensorless Y make sure that the `homing_retract_dist` in the `[stepper_y]` section is set to 0 as per [Voron Docs](https://docs.vorondesign.com/community/howto/clee/sensorless_xy_homing.html)

You can either add them manually to your klipper install, or alternatively, you can integrate them to your config so that moonraker keeps them up to date with your other software if they change. Below are the steps for the integrated way. If you make any changes to the files though, they will be overwritten if you update. If you choose to manually add them, make sure your printer.cfg reflects the location of them.

**On the Klipper System** 
```
cd ~
git clone https://github.com/viesturz/tapchanger.git --no-checkout --depth 1 --filter=blob:none
cd tapchanger
git sparse-checkout init --cone
git sparse-checkout set Klipper
git checkout
cd ~
ln -s ~/tapchanger/Klipper/config-example ~/printer_data/config/tapchanger
```

**Add to moonraker.conf**
```
[update_manager tapchanger]
type: git_repo
path: ~/tapchanger
origin: https://github.com/viesturz/tapchanger.git
primary_branch: main
managed_services: klipper
```
