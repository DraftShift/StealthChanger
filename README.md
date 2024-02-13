# ![](https://github.com/Hellsparks/StealthChanger/blob/main/media/Stealthchanger_logo_sm.png?raw=true) 
StealthChanger: Based on Viesturz's work on [Tapchanger](https://github.com/viesturz/tapchanger)

### WIP - STABLE TESTED AND WORKING BUT STILL WIP. BOM MAY CHANGE

Due to difficulties with heat insert and aligning of bearings and mounts we wanted to try a more simplistic design based on bushings and pins.

This is a very light design, requiring less parts and as such is cheaper and easier to build.  Input shaper tests have shown it to be as rigid if not more than current Tapchanger.

All parts are easily replaceable without reprinting if wear happens, life of the bushings and pins are still being tested.

## Tool compatability
Currently we support the standard Stealth Burner, Dragon Burner, and Rapid Burner.  There are plans in place to add the Mini Stealth Burner, XOL, and Archetype.

## Printing
All print settings are the same as [Voron Standards](https://docs.vorondesign.com/sourcing.html#print-settings) or better.

All parts (screws, magnets, etc) are Voron, and Voron Tap standards.

Print orientation is flat on the parts back with supports enabled currently, we are working on models with integrated supports.

**NOTE: Currently pins may feel very loose, this is by design to allow for room for glue or epoxy (recommended) to set.  Normally press fit is good enough for testined, but for actual use make sure to secure the pins properly.**

**NOTE: D2HW shuttle is not compatible with Hall Effects, and D2HW back plate will affect cooling.**

## Instructions
### Assembly
in order to get proper matching set you should:
- insert pins in your best backplate (straightest)
- press bushings in the shuttle and ensure a smooth mating between the parts.
- if everything feels smooth, pop the bushings out and glue them in place using either superglue or epoxy.
- be sure to test that the mating still feels smooth after the glue sets.
- You can now use the shuttle as a "master blank" for glueing the pins into all your backplates.

### Configs (TO BE DONE)
#### CANbus
https://github.com/Esoterical/voron_canbus this is a preety definitive guide for canbus implementation on klipper.

## BOM
### Shuttle
- [3] 6x3mm magnets
- [2] m3x6 BHCS (tap sensor)
- [4] m3x6 BHCS head (mgn bolts)
- [3] 4x6x6mm brass bushing (4mm id x 6mm od x 6mm tall)
- [2] m3x40 SHCS (Optional: to stiffen the shuttle)
### Back plate x1 per toolhead
- [4] m3 heat inserts
- [3] Ø4x12mm ssRod (dowel pin) with a rounded end **(if it has female threads on the back it will be listed as an M3, but make sure the pin is 4mm OD, that is what is important)**
- [1] 6x3mm magnets
- [2] m3x6 or m3x8 FHCS (Flat head countersunk screw, MUST BE MAGNETIC. no stainless, as per TAP)
#### Dragonburner
- [1] m3x12 BHCS (optional to keep spacer in place)
- [2] m3x35 SHCS
- [2] m3 heat inserts
** Note: Dragonburner extended mount is require depending on extruder**
### Endstop options
- [1] m3x6 BHCS
- [1] m3 heat inserts
- [1] 6x3mm magnet (Hall Effect Sensor ONLY)

**Note: heatsets on the SB version in from the opposite side as the Voron instructions, slightly longer screws on the CW2 attachment may be required**

| Parts   	| Link 1   UK Amazon      	| Link 2 AliExpress                      	| Link 3    US Amazon	  | Link 4 	|
|---------	|-------------------------	|-----------------------------------------	|------------------------ |--------	|
| Bushing 	| https://amzn.to/48jnoPO 	| https://s.click.aliexpress.com/e/_Dkek3Op | https://amzn.to/3RAjKtY |        	|
| Pin     	| https://amzn.to/488gP2v 	| https://s.click.aliexpress.com/e/_DEfc0JB	| https://amzn.to/3GZBSZn |        	|

**note links are affiliates**

## Docks
Currently all docks used with [Viesturz's Tapchanger](https://github.com/viesturz/tapchanger) are compatible.  In the future we might develop our own.

**NOTE: the DB dock in the Tapchanger repo uses custom Cowl that is not compatible or supported by Stealthchanger.  We recommend to always use the original cowls for all tools.  If you mods use that dock please see the [usermod](https://github.com/Hellsparks/StealthChanger/blob/main/UserMods/OstroMa/DB_Cowl_v8_with_TapChanger_Dock_Hooks.stl) for a merged version with proper original bolt locations.**

## Software
[Viesturz's Tapchanger](https://github.com/viesturz/tapchanger).  The only changes will be in the toolhead config which you will find in the klipper directory in this repo.

## Support
[Discord](https://discord.com/channels/1119433664799965186/1187877885235699843)

## Preview
### Printed Parts (Dragonburner) by ZombieHedgehog
![](https://github.com/Hellsparks/StealthChanger/blob/main/media/parts.png?raw=true)
![](https://github.com/Hellsparks/StealthChanger/blob/main/media/parts_together.png?raw=true)
### Assembled Shuttle by TheSin-
![](https://github.com/Hellsparks/StealthChanger/blob/main/media/shuttle.jpg?raw=true)
### Motion (Stealthburner) by TheSin-
![](https://github.com/Hellsparks/StealthChanger/blob/main/media/motion.gif?raw=true)
### Docking (Stealthburner) by fiferboy
![](https://github.com/Hellsparks/StealthChanger/blob/main/media/docking.gif?raw=true)

## Contributors
| Github   	| Discord    	|
|---------	|---------	|
| Hellsparks 	| _hellspark 	|
| TheSin-     	| thessien 	|
| BT123D     	| bt123_ 	|
| fiferboy     	| fiferboy 	|
| paeppi88     	| paeppi88 	|

## Media
### Built on stream by ZombieHedgehog
https://www.twitch.tv/zombiehedgehog
| Episode   |           |
|---------	|---------	|
| 1 | https://youtu.be/YK2Zk2K584Y |
| 2 | https://youtu.be/yOGEAGLlvZc |
| 3 | https://youtu.be/W_r2b8U1J6k |
| 4 | https://youtu.be/cCbIjArKL4M |
