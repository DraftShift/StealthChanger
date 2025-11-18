# MajorHack PCB36 Mount for TheSin Backplate & G2SA

This PCB36 mount is designed for use with [TheSin's backplate](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/TheSin-/PCB36_Mount) and provides secure mounting for EBB36, Nighthawk36, and SHT36 toolhead PCBs.

<img src="images/G2SA_backplate.png" width="400">
*PCB36 mount installed on TheSin's backplate with G2SA extruder*

## Compatible Extruders

This mount is **back-compatible** with [TheSin's original PCB36 mount](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/TheSin-/PCB36_Mount), which supports:
- **CNC HGX Sherpa**
- **Orbiter 2** (Orbiter 2.5)

Additionally, this mount **adds support for the [G2SA (Galileo 2 Standalone)](https://github.com/JaredC01/Galileo2/tree/main/galileo2_standalone)** extruder. The G2SA is a drop-in replacement for Orbiter 2.0 or Sherpa Mini extruders, but the motor screw mount locations are slightly different.

## Parts Required

- **PCB Mount**: [`TheSin Backplate - PCBMount - G2SA.stl`](TheSin Backplate - PCBMount - G2SA.stl) or [`TheSin backplate - PCBMount - G2SA.step`](TheSin backplate - PCBMount - G2SA.step) (for CAD)
- **Standoffs**: [`Standoff - M3x17.5.stl`](Standoff - M3x17.5.stl) or [`Standoff - M3x17.5.step`](Standoff - M3x17.5.step) (2 required)
- **Heatset Inserts**: Standard Voron M3 heatset inserts 
   - 2 per standoff
   - 2 for PCB mount

## Printing Notes

- **Print without supports** - both the mount and standoffs print cleanly without supports
- Recommended: 0.2mm layer height, 3-4 perimeters, 30-40% infill

## Installation

1. Install heatset inserts into the standoffs (2 standard Voron M3 heatset inserts per standoff, 4 total)
2. Install the 4 M3x17.5mm standoffs into the PCB mount
3. Attach the PCB mount (with standoffs) to TheSin's backplate using the provided mounting points
4. Screw the PCB mount into the standoffs with M3x6 screws.
5. Place your EBB36, Nighthawk36, or SHT36 board onto the standoffs and secure with M3 screws (M3x6 or M3x8)


## Compatibility Notes

- **Extruders**: Back-compatible with CNC HGX Sherpa and Orbiter 2 (via TheSin's original mount). Adds G2SA support.
- **Standoffs**: Use 17.5mm standoffs for G2SA. Original TheSin mount uses 20mm standoffs.
- **Backplate**: Designed specifically for TheSin's backplate
- **PCB**: Compatible with EBB36, Nighthawk36, and SHT36 boards

## Related Resources

- [TheSin's PCB36 Mount Repository](https://github.com/DraftShift/StealthChanger/tree/main/UserMods/TheSin-/PCB36_Mount)
- [G2SA (Galileo 2 Standalone) Documentation](https://github.com/JaredC01/Galileo2/tree/main/galileo2_standalone)

---

**Author**: MajorHack  
**License**: See main StealthChanger repository license
