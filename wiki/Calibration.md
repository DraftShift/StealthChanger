## Z Offset

- Home and QGL
- Set the tool z offset using the paper method
- Add this to the tool config `z_offset`
- For tools after 0, use this value to find the `gcode_z_offset`, which is the difference between this tool and tool 0 offsets.
- Restart Klipper
- Repeat for all tools


## Dock Parking

- Home and QGL
- Remove the tool from the shuttle and place it in the dock
- Move the gantry as if to pick up the tool, as soon as the light on the optotap pcb changes, note the park x/y/z location for the config
- Repeat this for all tools
- Restart Klipper


## X/Y Offset

**Only for tools after 0, T0 will always be 0**

Coming Soon™
