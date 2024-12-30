1. [Slicer Software](#slicer-software)
2. [Slicer GCODEs](#slicer-gcodes)

## Slicer Software

| Name | Multitool | Issue | Discussion | Notes |
|:------:|:------:|:------:|:------:|------|
| Cura | <span style="color: green;">✓</span> | | | As of 5.8, select new printer, select DraftShift Design, select the size from the voron list, allows up to 8 extruders |
| OrcaSlicer | <span style="color: green;">✓</span> | | | As of 2.2 |
| PrusaSlicer | <span style="color: green;">✓</span> | | | |
| Simplify3D | <span style="color: silver;">?</span> | | | |
| Slic3r | <span style="color: silver;">?</span> | | | |
| SuperSlicer | <span style="color: green;">✓</span> | | | See [2197](https://github.com/supermerill/SuperSlicer/issues/2197) |

## Slicer GCODEs

### Prusa

Printer -> Custom G-code -> **Start G-code** - all must be a single line
```
PRINT_START TOOL_TEMP={first_layer_temperature[initial_tool]} {if is_extruder_used[0]}T0_TEMP={first_layer_temperature[0]}{endif} {if is_extruder_used[1]}T1_TEMP={first_layer_temperature[1]}{endif} {if is_extruder_used[2]}T2_TEMP={first_layer_temperature[2]}{endif} {if is_extruder_used[3]}T3_TEMP={first_layer_temperature[3]}{endif} {if is_extruder_used[4]}T4_TEMP={first_layer_temperature[4]}{endif} {if is_extruder_used[5]}T5_TEMP={first_layer_temperature[5]}{endif}  BED_TEMP=[first_layer_bed_temperature] TOOL=[initial_tool]
```

Printer -> Custom G-code -> **Tool change G-code**
```
M104 S{temperature[next_extruder]} T[next_extruder] ; set new tool temperature so it can start heating while changing
```

**NOTE**: add this as a second line if you use prime tower
```
G1 X{wipe_tower_x} Y{wipe_tower_y} F{travel_speed*60} ; Move to wipe tower before tool change
```

### Orca

Printer settings -> Machine G-code -> **Machine start G-code** - all must be a single line
```
PRINT_START TOOL_TEMP={first_layer_temperature[initial_tool]} {if is_extruder_used[0]}T0_TEMP={first_layer_temperature[0]}{endif} {if is_extruder_used[1]}T1_TEMP={first_layer_temperature[1]}{endif} {if is_extruder_used[2]}T2_TEMP={first_layer_temperature[2]}{endif} {if is_extruder_used[3]}T3_TEMP={first_layer_temperature[3]}{endif} {if is_extruder_used[4]}T4_TEMP={first_layer_temperature[4]}{endif} {if is_extruder_used[5]}T5_TEMP={first_layer_temperature[5]}{endif}  BED_TEMP=[first_layer_bed_temperature] TOOL=[initial_tool]
```

Printer settings -> Machine G-code -> **Change Filament G-code**
```
;Leave blank
```

### Cura

Machine Settings -> Printer -> **Start G-code** - all must be a single line
```
PRINT_START TOOL_TEMP={material_print_temperature_layer_0} T{initial_extruder_nr}_TEMP={material_print_temperature_layer_0} BED_TEMP={material_bed_temperature_layer_0} TOOL={initial_extruder_nr}
```

Machine Settings -> Printer ->  Tool n -> **Extruder Start G-code**
```
;Leave blank
```

Machine Settings -> Printer ->  Tool n -> **Pre tool change G-code** - 5.10+
```
M104 S{material_print_temperature} T{extruder_nr}
```
