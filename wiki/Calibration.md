1. [Z Offset](#z-offset)
2. [GCODE Z Offset](#gcode-z-offset)
3. [Dock Parking](#dock-parking)
4. [X/Y Offset](#xy-offset)

Before you start with calibrations and QGLs, make sure to run `PROBE_ACCURACY SAMPLES=100` or more to brake things in.

## Z Offset

1. Make sure T0 is on the shuttle and run `INITIALIZE_TOOLCHANGER`
2. Run `G28` and `QUAD_GANTRY_LEVEL` 
3. Run `PROBE_CALIBRATE`
4. Do a paper test as normal like a single toolhead head printer and adjust the Z
5. DO NOT SAVE the calibration, just hit ACCEPT on Mainsail. You will see the offset in the console. Copy the offset and save this `[tool_probe T0]` `z_offset` in the configs.
6. Repeat for all tools
7. Restart Klipper

Do this for all tool heads one at a time.

## GCODE Z Offset

**NOTE:** `gcode_z_offset` on Tool 0 is always 0.

1. Set all [`z_offset` first](#z-offset)
2. Make sure T0 is on the shuttle and run `INITIALIZE_TOOLCHANGER`
3. Run `G28` and `QUAD_GANTRY_LEVEL` 
4. Run `G1 Z10 F600`
5. Manually remove T0 and place T1 in its place
6. Do a paper test as normal
7. Once done run `M114` and copy the Z value into `[tool T1]` `gcode_z_offset`
8. Repeat from step 4 for all tools
9. Restart Klipper


## Dock Parking

**NOTE:** Set the `params_close_y` to your heighest `params_park_y` + 30, and set `params_safe_y` to `params_close_y` + the thickness of your thickest tool + 10 in the `toolchanger.cfg` and **remove them from the tool config files**.  For `params_safe_y` you could also just make sure when you have a tool on the shuttle you can move freely behind the dock and not hit anyother tools and note that `y` position.

- Home and QGL
- Remove the tool from the shuttle and place it in the dock
- Move the gantry as if to pick up the tool, as soon as the light on the optotap pcb changes, note the `params_park_x`, `params_park_y` and `params_park_z` and put them in the tool config file
- Repeat this for all tools
- Restart Klipper


## X/Y Offset

**NOTE:** `gcode_x_offset` and `gcode_y_offset` on Tool 0 are always 0.

### [Sexball Probe](Bill-of-Materials#sexball-probe) or [NozzleAlign](https://github.com/viesturz/NozzleAlign)

Follow the guide at [NozzleAlign](https://github.com/viesturz/NozzleAlign)

### [Print STL](https://www.printables.com/model/201707-x-y-and-z-calibration-tool-for-idex-dual-extruder-)

Follow the guide at [Print STL](https://www.printables.com/model/201707-x-y-and-z-calibration-tool-for-idex-dual-extruder-)

### Camera like [kTAMV](https://github.com/TypQxQ/kTAMV)

Follow the guide at [kTAMV](https://github.com/TypQxQ/kTAMV)

### [Nudge](https://github.com/zruncho3d/nudge)

Follow the guide at [Nudge](https://github.com/zruncho3d/nudge)
