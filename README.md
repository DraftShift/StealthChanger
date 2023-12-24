![](https://github.com/Hellsparks/StealthChanger/blob/main/media/Stealthchanger_logo_sm.png?raw=true)
# StealthChanger
Based on Viesturz's work on [Tapchanger](https://github.com/viesturz/tapchanger)

### WIP - STABLE TESTED AND WORKING BUT STILL WIP. BOM MAY CHANGE

Due to difficulties with heat insert and aligning of bearings and mounts we wanted to try a more simplistic design based on bushings and pins.

This is a very light design, requiring less parts and as such is cheaper and easier to build.  Input shaper tests have shown it to be as rigid if not more than current Tapchanger.

All parts are easily replaceable without reprinting if wear happens, life of the bushings and pins are still being tested.

## Tool compatability
Currently we support the standard Stealth Burner.  There are plans in place to add the Mini Stealth Burner, Dragon Burner and XOL.

## BOM and Printing
All print settings are the same as [Voron Standards](https://docs.vorondesign.com/sourcing.html#print-settings)

All parts (screws, magnets, etc) are Voron, and Voron Tap standards.

Print orientation is flat on the parts back with supports enabled currently, we are working on models with integrated supports.

### Shuttle
- [3] 6x3mm magnets
- [2] m3x6 button head (tap sensor)
- [4] m3x6 button head (mgn bolts)
- [3] 4x6x6mm bronze bushing (4mm id x 6mm od x 6mm tall)
### Back plate x1 per toolhead
- [4] m3 heat inserts
- [3] 4x12mm ssRod (dowel pin) with a rounded end
- [1] 6x3mm magnets
- [2] m3x8 FHCS (Flat head countersunk screw, MUST BE MAGNETIC. no stainless, as per TAP)
### Endstop options
- [1] m3x6 button head
- [1] m3 heat inserts
- [1] 6x3mm magnet (Hall Effect Sensor ONLY)

**Note: heatsets on the SB version in from the opposite side as the Voron instructions, slightly longer screws on the CW2 attachment may be required**

| Parts   	| Link 1   UK amazon      	| Link 2 AliExpress                      	| Link 3 	| Link 4 	|
|---------	|-------------------------	|-----------------------------------------	|--------	|--------	|
| Bushing 	| https://amzn.to/48jnoPO 	| https://s.click.aliexpress.com/e/_DDdsj8V |        	|        	|
| Pin     	| https://amzn.to/488gP2v 	| https://s.click.aliexpress.com/e/_DEfc0JB	|        	|        	|
| Screw   	|                         	|                                        	|        	|        	|

**note links are affiliates**

## Docks
Currently all docks used with [Viesturz's Tapchanger](https://github.com/viesturz/tapchanger) are compatible.  In the future we might develop our own.

## Software
[Viesturz's Tapchanger](https://github.com/viesturz/tapchanger).  The only changes will be in the toolhead config which you will find in the klipper directory in this repo.

## Preview
### Assembled Shuttle
![](https://github.com/Hellsparks/StealthChanger/blob/main/media/shuttle.jpg?raw=true)
### Shuttle on back plate on Stealth Burner
![](https://github.com/Hellsparks/StealthChanger/blob/main/media/assembled.jpg?raw=true)
### Motion
![](https://github.com/Hellsparks/StealthChanger/blob/main/media/motion.gif?raw=true)
### Docking
![](https://github.com/Hellsparks/StealthChanger/blob/main/media/docking.gif?raw=true)
