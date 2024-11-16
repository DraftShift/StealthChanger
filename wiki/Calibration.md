1. [Z Offset](#z-offset)
2. [GCODE Z Offset](#gcode-z-offset)
3. [Dock Parking](#dock-parking)
4. [X/Y Offset](#xy-offset)
5. [Manual Paper Test](#manual-paper-test)

**Before you start calibrating you must "break-in" each tool probe.  Heat soak your machine and run a couple `PROBE_ACCURACY SAMPLES=100` per tool.**

## Z Offset

**NOTE:** Tn is the tool on the shuttle, ie T0

1. Put a tool on the shuttle and run `INITIALIZE_TOOLCHANGER`
2. Run `G28`
3. Run `QUAD_GANTRY_LEVEL`
4. Run `G28`
5. Do a [Manual Paper Test](#manual-paper-test) as normal like a single toolhead head printer and adjust the Z
5. Copy the offset and save this to `z_offset` in `[tool_probe Tn]` of the tool conf file
6. Repeat from `step 1` for all tools (`step 2` and `step 3` are optional after first tool)
7. Run `FIRMWARE_RESTART`


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
8. Do a [Manual Paper Test](#manual-paper-test) as normal like a single toolhead head printer and adjust the Z
9. Once done run `M114` and copy the Z value to `gcode_z_offset` in `[tool Tn]` of the tool conf file
10. Repeat from `step 6` for all tools
11. Run `FIRMWARE_RESTART`


## Dock Parking

**NOTE:** Set the `params_close_y` to your highest `params_park_y` + 30, and set `params_safe_y` to `params_close_y` + the thickness of your thickest tool + 10 in the `toolchanger.cfg` and **remove them from the tool config files**

**NOTE:** For `params_safe_y` you could also just make sure when you have a tool on the shuttle you can move freely behind the dock and not hit any other docked tools and note that `y` position.

1. Put a tool on the shuttle and run `INITIALIZE_TOOLCHANGER`
2. Run `G28` and `QUAD_GANTRY_LEVEL` 
3. Remove the tool from the shuttle and place it in the dock
4. Move the gantry as if to pick up the tool, as soon as the light on the optotap pcb changes
5. Raise Z by 1
6. Run `M114` and record the values to `params_park_x`, `params_park_y` and `params_park_z` in `[Tool Tn]` of the tool conf file
7. Run `G28`
8. Run `SET_TOOL_PARAMETER PARAMETER='params_path_speed' VALUE=300`
9. Run `TEST_TOOL_DOCKING RESTORE_AXIS=XYZ`
10. Run `RESET_TOOL_PARAMETER PARAMETER='params_path_speed'`
11. Repeat this for all tools
12. Run `FIRMWARE_RESTART`

### Docking/Undocking

The Moving using config parameters is as such:

| Current tool | No tool | Next tool |
|--------------|---------|-----------|
|`safe_y`, `park_x` -> `park_z` -> `close_y` -> `path` | `close_y` -> `park_x` | `path` -> `safe_y` -> `t_command_restore_axis` |


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


## Manual Paper Test

The primary bed calibration mechanism is the "paper test". It involves placing a regular piece of "copy machine paper" between the printer's bed and nozzle, and then commanding the nozzle to different Z heights until one feels a small amount of friction when pushing the paper back and forth.

It is important to understand the "paper test" even if one has an "automatic Z probe". The probe itself often needs to be calibrated to get good results. That probe calibration is done using this "paper test".

In order to perform the paper test, cut a small rectangular piece of paper using a pair of scissors (eg, 5x3 cm). The paper generally has a thickness of around 100 microns (0.100mm). (The exact thickness of the paper isn't crucial.)

The first step of the paper test is to inspect the printer's nozzle and bed. Make sure there is no plastic (or other debris) on the nozzle or bed.

**Inspect the nozzle and bed to ensure no plastic is present!**

If one always prints on a particular tape or printing surface then one may perform the paper test with that tape/surface in place. However, note that tape itself has a thickness and different tapes (or any other printing surface) will impact Z measurements. Be sure to rerun the paper test to measure each type of surface that is in use.

If there is plastic on the nozzle then heat up the extruder and use a metal tweezers to remove that plastic. Wait for the extruder to fully cool to room temperature before continuing with the paper test. While the nozzle is cooling, use the metal tweezers to remove any plastic that may ooze out.

**Always perform the paper test when both nozzle and bed are at room temperature!**

When the nozzle is heated, its position (relative to the bed) changes due to thermal expansion. This thermal expansion is typically around a 100 microns, which is about the same thickness as a typical piece of printer paper. The exact amount of thermal expansion isn't crucial, just as the exact thickness of the paper isn't crucial. Start with the assumption that the two are equal (see below for a method of determining the difference between the two distances).

It may seem odd to calibrate the distance at room temperature when the goal is to have a consistent distance when heated. However, if one calibrates when the nozzle is heated, it tends to impart small amounts of molten plastic on to the paper, which changes the amount of friction felt. That makes it harder to get a good calibration. Calibrating while the bed/nozzle is hot also greatly increases the risk of burning oneself. The amount of thermal expansion is stable, so it is easily accounted for later in the calibration process.

**Use manual controls to move the tool**

Using the webUI (Mainsail, Fluidd, Octoprint) or the LCD Controls, move the tool down and stop just before the bed.  Place the paper between the nozzle and bed. It can be useful to fold a corner of the paper so that it is easier to grab. (Try not to push down on the bed when moving the paper back and forth.) Continue to jog the tool down 0.1 at a time. After the nozzle stops moving, push the paper back and forth to check if the nozzle is in contact with the paper and to feel the amount of friction.

If too much friction is found then jog up be smaller increments.

Once you are happy with the results note the Z position (you may also use `M114` to get the location).

*Taken from Klipper [paper test](https://www.klipper3d.org/Bed_Level.html#the-paper-test)*
