# Example Setup

Most of the code has been taken from the [TapChanger](https://github.com/viesturz/tapchanger) repo.


## Tapchanger Files

You need
- `homing.cfg`, `macros.cfg`, and `toolchanger.cfg` from [TapChanger Examples/per tool probe](https://github.com/viesturz/klipper-toolchanger/tree/main/examples/per%20tool%20probe)
- [`tool_detection.cfg`](https://github.com/viesturz/klipper-toolchanger/blob/main/examples/tool_detection.cfg)

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


## Klipper Toolchanger

You must install [klipper-toolchanger](https://github.com/viesturz/klipper-toolchanger/), Follow instruction on the linked page.


## Toolheads

Toolchangers start with number 0, and count up. So for all the configs, make sure you change all sections. IE, in your T1 config, make sure its extruder1, fan1, etc. See the examples.  **NOTE: The only except to this rule is T0 extruder has no number.**

