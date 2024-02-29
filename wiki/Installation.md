# Installation

All sections are required, so please follow all steps carefully.

1. [Klipper Addon](#klipper-addon)
2. [Toolchanger Configuration](#toolchanger-configuration)

## Klipper Addon

You must install [klipper-toolchanger](https://github.com/viesturz/klipper-toolchanger/), Follow instruction on the linked page.


## Toolchanger Configuration

You need `homing.cfg`, `macros.cfg`, `tool_detection.cfg` and `toolchanger.cfg` from [TapChanger Example](https://github.com/viesturz/tapchanger/tree/main/Klipper/config-example)

`homing.cfg` assumes you are using sensorless for X axis.  It's impotrant to use this file when building your own homing as the order and macros it calls are required.  If you use Hall Effects or end stops for both Axis, remove the `_SENSORLESS_HOME_X` call in `[homing_override]` with `G28 X`.

You can either add them manually to your klipper install, or alternatively, you can integrate them to your config so that moonraker keeps them up to date with your other software if they change. Below are the steps for the integrated way. If you make any changes to the files though, they will be overwritten if you update. If you choose to manually add them, make sure your printer.cfg reflects the location of them.

**On the Klipper System** 
```
cd ~
git clone https://github.com/viesturz/tapchanger.git
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
