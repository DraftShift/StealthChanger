1. [Slicer Software](#slicer-software)
2. [Slicer GCODEs](#slicer-gcodes)

## Slicer Software

| Name | Multitool | Issue | Discussion | Notes |
|:------:|:------:|:------:|:------:|------|
| Cura | <span style="color: green;">✓</span> | | | As of 5.8, select new printer, select DraftShift Design, select the size from the voron list, allows up to 8 extruders |
| OrcaSlicer | <span style="color: red;">✗</span> | [2050](https://github.com/SoftFever/OrcaSlicer/issues/2050) | [931](https://github.com/SoftFever/OrcaSlicer/discussions/931) | Upvote the Issue to get support added, beta support [6087](https://github.com/SoftFever/OrcaSlicer/pull/6087) |
| PrusaSlicer | <span style="color: green;">✓</span> | | | |
| Simplify3D | <span style="color: silver;">?</span> | | | |
| Slic3r | <span style="color: silver;">?</span> | | | |
| SuperSlicer | <span style="color: green;">✓</span> | | | See [2197](https://github.com/supermerill/SuperSlicer/issues/2197) |

## Slicer GCODEs

### Prusa

**Start GCODE** - all must be a single line
```
PRINT_START TOOL_TEMP={first_layer_temperature[initial_tool]} {if is_extruder_used[0]}T0_TEMP={first_layer_temperature[0]}{endif} {if is_extruder_used[1]}T1_TEMP={first_layer_temperature[1]}{endif} {if is_extruder_used[2]}T2_TEMP={first_layer_temperature[2]}{endif} {if is_extruder_used[3]}T3_TEMP={first_layer_temperature[3]}{endif} {if is_extruder_used[4]}T4_TEMP={first_layer_temperature[4]}{endif} {if is_extruder_used[5]}T5_TEMP={first_layer_temperature[5]}{endif}  BED_TEMP=[first_layer_bed_temperature] TOOL=[initial_tool]
```

**Tool change GCODE**
```
M104 S{temperature[next_extruder]} T[next_extruder] ; set new tool temperature so it can start heating while changing
```

### Orca

**Start GCODE** - all must be a single line
```
PRINT_START TOOL_TEMP={first_layer_temperature[initial_tool]} {if is_extruder_used[0]}T0_TEMP={first_layer_temperature[0]}{endif} {if is_extruder_used[1]}T1_TEMP={first_layer_temperature[1]}{endif} {if is_extruder_used[2]}T2_TEMP={first_layer_temperature[2]}{endif} {if is_extruder_used[3]}T3_TEMP={first_layer_temperature[3]}{endif} {if is_extruder_used[4]}T4_TEMP={first_layer_temperature[4]}{endif} {if is_extruder_used[5]}T5_TEMP={first_layer_temperature[5]}{endif}  BED_TEMP=[first_layer_bed_temperature] TOOL=[initial_tool]
```

**Tool change GCODE**
```
;Leave blank
```

### Cura

**Start GCODE** - all must be a single line
```
PRINT_START TOOL_TEMP={material_print_temperature_layer_0} T{initial_extruder_nr}_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} TOOL={initial_extruder_nr}
```

**Tool change GCODE**
```
;Leave blank
```

**Pre tool change GCODE** (as of 5.9)
```
M104 S{material_print_temperature} T{extruder_nr}
```
