# StealthChanger Xol-Toolhead (Experimental)
by [MikeYankeeOscarBeta](https://github.com/MikeYankeeOscarBeta/) (VoronDesign Discord: #MikeyMike V2.5796, Voron Toolchangers Discord: MikeyMike - Github: [MikeYankeeOscarBeta](https://github.com/MikeYankeeOscarBeta/StealthChanger))

[Xol Toolhead](https://github.com/Armchair-Heavy-Industries/Xol-Toolhead) by [Armchair Heavy Industries](https://github.com/Armchair-Heavy-Industries)

### This is EXPERIMENTAL If you have issues, please post them on the tapchanger discord ASAP!

## Description
StealthChanger parts compatible with Xol-Toolhead (Experimental)

Based on StealthChanger StealthBurner Parts.

For crossbar (horizontal 2020 aluminium extrusion in front of printer) only!

Designed to be compatible with all Xol-Toolhead hotend versions as of 2024-01-23. 
(However only Revo Voron and Rapido 2 UHF has been tested)

MCU Toolhead mount only compatible with Sherpa-Mini and EBB36



#### NB! StealthChanger-Rods Xol-Toolhead dock has it's own docking tool-path. Remember to add it and change to 'stealthchanger_xol' in your toolhead config.
```
params_stealthchanger_xol_path: [{'y':59, 'z':17.5},{'y':5, 'z':17.5},{'y':5, 'z':0.2},{'y':0.5, 'z':0.1},{'z':0, 'y':0, 'f':0.5},{'z':-10, 'y':0}, {'z':-10, 'y':16}]
```

Example:
```
[tool T0]
tool_number: 0
extruder: extruder
params_type = 'stealthchanger_xol'
fan: multi_fan T0_partfan
gcode_x_offset: 0
gcode_y_offset: 0
gcode_z_offset: 0
```

## BOM:
| Part                        | Amount    | Description                                                      |
|-----------------------------|-----------|------------------------------------------------------------------|
| 6x3 magnets                 | 6         | (N52 recommended)  2x for dock, 3x for shuttle 1x for plate      |
| M3x6mm FHCS screw           | 2         | Has to be magnetic (not stainless)                               |
| springsteel plate           | 1         | max 10mm wide, max 1mm thick, with M4 hole (I used blades from a [feeler gauge](https://www.biltema.no/en-no/car---mc/car-tools/engine-tools/spark-plug-tools/feeler-gauge-mminches-2000028588) )        |
| M4 screw                    | 1         | Maximum 6.3mm wide screw head                                    |
| M3x14mm screw               | 2         | Recommend BHCS or SHCS, but any M3 screw will work               |
| M3 T-slot nut               | 2         | Any M3 2020 T-Slot Nut will work (recommend springnuts)          |
| M3 heatset nut (5x4x3)      | 8         | (Voron Standard) 6 for Plate and 2 for EBB36 mount               |


## Assembly
- Print
    - Xol-Toolhead_Dock
    - Xol-Toolhead_MaglockFaceplate
    - StealthChanger_Xol-Toolhead_Plate
    - StealthChanger_Xol-Toolhead_EBB36_Mount
    - StealthChanger shuttle (if you haven't already)
- Push and glue in magnets
- Insert springsteel plate into slot in the Dock
- Cut and bend springsteel plate to fit your toolhead
- (optional) apply/mold silicone to the springsteel plate
- Fix the springsteel plate in place with the m4 screw
- Screw it onto the 2020 aluminium extrusion

