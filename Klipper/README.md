# Example Setup

Most of the code has been taken from the [TapChanger](https://github.com/viesturz/tapchanger)


## Tapchanger Files

You need `homing.cfg`, `macros.cfg`, `tool_detection.cfg` and `toolchanger.cfg` from [TapChanger Example](https://github.com/viesturz/tapchanger/tree/main/Klipper/config-example)

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


## Klipper Toolchanger

You must install [klipper-toolchanger](https://github.com/viesturz/klipper-toolchanger/), Follow instruction on the linked page.


## Toolheads

Toolchangers start with number 0, and count up. So for all the configs, make sure you change all sections. IE, in your T1 config, make sure its extruder1, fan1, etc. See the examples.

