## Dragon Burner EBB36 mount for the Orbiter2.0 extruder
This mount for DragonBurner provides a mount for the EBB36 that attaches to the rear of the Orbiter2.0. 

Dragonburner orignal design chirpy2605 here https://github.com/chirpy2605/voron

Traxman25's EBB36 mount takes a different approach and can be found here:
https://github.com/cekim-git/Toolchanger/tree/main/UserMods/traxman25/Dragonburner_EBB36_SC_Mount

## Design Goals:
- Keep the Orbiter 2.0 on the original/shorter exrtuder block, flush with the top of the cowl.
- Provide a CAN cable stress-relief tower with zip-tie holes that is shifted to be in-line with the filament tube for cable harness alignment.
- Provide clearance for the opto-tap PCB without adding over-all height or extending rearward (the EBB36 and OptoTap will be roughly in-line with eachother).
- Remove the need for stand-offs and potentially add rigidity by augmenting the attachment screws with design features fit to the outside of the Orbiter2 stepper motor.
- Support the optional Orbiter2.0 filament sensor via the mount with shorter fingers.

This uses "standard" DragaonBurner cowls - though it is specifically fit for Traxman25's numbered cowls for StealthChanger, it will also fit on a standard cowl.  It also works the V1 back-plate for StealthChanger/DragonBurner and OptoTap.

## BOM:
- 2 m3 (x4x5) heatset-inserts mounted from the opposite side as the EBB36 
- 2 m3x8 BHCS (EBB36 mount)
- (no filament sensor) 2 m3x20 SHCS to replace the Orbiter's stock screws and provide more thread purchase in the ABS.
- (filament sensor) 2 m3x25 SHCS to replace the Orbiter's stock screws

## Printing:
- I print this standing upright as it sits in the machine with organic/tree supports painted on to the most obvious overhangs.
- I use ABS with no adjustmnet for shrinkage from the design files as provided.

## Installation:
- Install heatsets to side opposite the EBB36 mounting face.  Ensure they are straight and the screw-path clear of overmelt after installation
- Remove the 2 m3x16 SHCS holding the stepper motor of the Orbiter2.0 to the gearbox taking care to keep the gearbox assembled while the screws are removed.
- Replace stock gear-box screws with m3x20 screws (or m3x25 if attaching the filament sensor).
- (optional) install the filament sensor to the Orbiter2.0.
- While keeping the stepper motor, optional sensor and gearbox assembly together, slide the rear of the stepper into the mount's cup that is sized to fit around it. 
- Line up the screw-holes on the fingers with the Orbiter's stepper motor fastener holes.
- While pressing this entire assembly together, thread in the m3x20 (or m3x25) screws.  You are simultaneously fastening the Orbiter2.0 stepper to its gear-box and self-tapping the 3mm ABS holes on the mounting bracket, so keep them pressed together the entire time.
- Install EBB36 with 2 m3x8 BHCS to the rear.
- Wire as needed.

<img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/Orbiter2.0_EBB36_Mount.png" width="400" height="465">
<img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/DB_EBB36_Orbiter2.0_Mount.jpg width="400" height="506">
<img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/DB_EBB36_Orbiter2.0_wFSensor_Mount.jpg width="400" height="513">
