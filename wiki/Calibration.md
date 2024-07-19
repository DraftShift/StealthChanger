## Z Offset

- Home and QGL
- Set the tool `z_offset` using the paper method
- Add this to the tool_probe config `z_offset`
- For tools after 0, use this value to find the `gcode_z_offset`, which is the difference between this `tool_probe` and `tool_probe` for tool 0 `z_offset`.
- Restart Klipper
- Repeat for all tools


## Dock Parking

**NOTE:** Set the `params_close_y` to your heighest `params_park_y` + 30, and set `params_safe_y` to `params_close_y` + the thickness of your thickest tool + 10 in the `toolcharger.cfg` and remove them from the tool config files.  For `params_safe_y` you could also just make sure when you have a tool on the shuttle you can move freely behind the dock and not hit anyother tools and note that `y` position.

- Home and QGL
- Remove the tool from the shuttle and place it in the dock
- Move the gantry as if to pick up the tool, as soon as the light on the optotap pcb changes, note the park x/y/z location for the config
- Repeat this for all tools
- Restart Klipper


## X/Y Offset

**Only for tools after 0, T0 will always be 0**

Coming Soon™
