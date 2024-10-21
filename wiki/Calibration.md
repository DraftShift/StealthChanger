1. [Z Offset](#z-offset)
2. [GCODE Z Offset](#gcode-z-offset)
3. [Dock Parking](#dock-parking)
4. [X/Y Offset](#xy-offset)

**Before you start calibrating you must "break-in" each tool probe.  Heat soak your machine and run a couple `PROBE_ACCURACY SAMPLES=100` per tool.**

## Z Offset

**NOTE:** Tn is the tool on the shuttle, ie T0

1. Put a tool on the shuttle and run `INITIALIZE_TOOLCHANGER`
2. Run `G28`
3. Run `QUAD_GANTRY_LEVEL`
4. Run `G28`
5. Do a [paper test](https://www.klipper3d.org/Bed_Level.html#the-paper-test) as normal like a single toolhead head printer and adjust the Z
5. Copy the offset and save this to `z_offset` in `[tool_probe Tn]` of the tool conf file
6. Repeat from `step 1` for all tools (`step 2` and `step 3` are optional after first tool)
7. Run `FIRMWARE_RESTART`

Do this for all tool heads one at a time.

## GCODE Z Offset

**NOTE:** Tn is the tool on the shuttle, ie T1

**NOTE:** only home or probe with T0 during this calibration

**NOTE:** `gcode_z_offset` on Tool 0 is always 0.

1. Set [z_offset](#z-offset) for all tools first
2. Make sure T0 is on the shuttle and run `INITIALIZE_TOOLCHANGER`
3. Run `G28`
4. `QUAD_GANTRY_LEVEL` 
5. Run `G28`
6. Run `G1 Z10 F600`
7. Manually remove current tool and place the next tool in its place on the shuttle
8. Do a [paper test](https://www.klipper3d.org/Bed_Level.html#the-paper-test) as normal like a single toolhead head printer and adjust the Z
9. Once done run `M114` and copy the Z value to `gcode_z_offset` in `[tool Tn]` of the tool conf file
10. Repeat from `step 6` for all tools
11. Run `FIRMWARE_RESTART`


## Dock Parking

**NOTE:** Set the `params_close_y` to your highest `params_park_y` + 30, and set `params_safe_y` to `params_close_y` + the thickness of your thickest tool + 10 in the `toolchanger.cfg` and **remove them from the tool config files**

**NOTE:** For `params_safe_y` you could also just make sure when you have a tool on the shuttle you can move freely behind the dock and not hit any other docked tools and note that `y` position.

1. Put a tool on the shuttle and run `INITIALIZE_TOOLCHANGER`
2. Run `G28` and `QUAD_GANTRY_LEVEL` 
3. Remove the tool from the shuttle and place it in the dock
4. Move the gantry as if to pick up the tool, as soon as the light on the optotap pcb changes, note the `params_park_x`, `params_park_y` and `params_park_z` and put them in the tool config file
5. Repeat this for all tools
6. Run `FIRMWARE_RESTART`


## X/Y Offset

**NOTE:** `gcode_x_offset` and `gcode_y_offset` on T0 are always 0

### [Sexball Probe](Bill-of-Materials#sexball-probe) or [NozzleAlign](https://github.com/viesturz/NozzleAlign)

Follow the guide at [NozzleAlign](https://github.com/viesturz/NozzleAlign)

### [Print STL](https://www.printables.com/model/201707-x-y-and-z-calibration-tool-for-idex-dual-extruder-)

Follow the guide at [Print STL](https://www.printables.com/model/201707-x-y-and-z-calibration-tool-for-idex-dual-extruder-)

### Camera or [kTAMV](https://github.com/TypQxQ/kTAMV)

Follow the guide at [kTAMV](https://github.com/TypQxQ/kTAMV)

### [Nudge](https://github.com/zruncho3d/nudge)

Follow the guide at [Nudge](https://github.com/zruncho3d/nudge)
