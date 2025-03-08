1. [Methods](#methods)
2. [FAQs](#faqs)
3. [Build Guide](#build-guide)
4. [Macros](#macros)


## Methods

<a href="https://discord.gg/jJs73c6vSc" target="_blank" alt="Join our Discord">![Discord](https://img.shields.io/discord/1226846451028725821?logo=discord&logoColor=%23ffffff&label=Join%20our%20Discord&labelColor=%237785cc&color=%23adf5ff)</a>


## FAQs


### Check your print quality
After printing the parts make sure that the hex holes look to be proper hexes and that they are very uniform.  If they are misshapen chances are you need to reprint as you will have alignment issues.  It doesn't take much to be out by a lot.  Try printing at a slower speed if you have issues.

### What probes can be use with SC?
TAP is baked in to each tool as part of SC. As of right now no other probes are compatible with the printed parts or with klipper since only open probe can exist at a time.  Thus only TAP can be used.

### How many tool will fit on my printer?
Calculating available size for tools (number of tools you can fit)
   - Dragon Burners/Yavoth require 60mm per tool (I recommend 5mm between for extruder handles)
   - Blackbird, Stealth Burners and XOL require 76mm per tool
   - The gantry required about 20mm per side to be able to pass the tools.  To know how many tools you can fit it's simple math, measure that top bar -40mm to gantry and then divide the remainder by the size of your toolhead.

### Tophat: Is it required?
If you only want to print PLA or filaments that dont require an enclosure there is no need just like on the prusa XL. With ABS ASA ect you will need to enclose it.

**How tall should it be?** for a 350 build we found 250mm, 300 build 225mm and 250 build 200mm additional z height works out well though might need to be higher depending on where you pass through umbilicals. It needs only be enough so that the cables can have a nice arch from back to front so not to collide with others and tangle, while being long enough to reach the farthest corner on the buildplate at layer 1.

### Adjust preload
Preload is created with the 2 countersunk screws in the tool plate.  These 2 screws need to be magnetic and will make contact with the magnets in the shuttle.  This adds 2 more wider points of contact at the base while also pre loading the sleeves/bearings.  To adjust them screw them all the way in, then slowly unscrew them 1/4 turn at a time (keeping each side even) until the tool no longer engages its self right away.  Once you reach a point where this happens, screw them back in 1/4 turn.  Each tool needs to be adjusted separately as printing irregularities can happen and this will allow you to compensate for it.  You may want to test and readjust these from time to time.

### QGL won't finish
If you run homing on Z or QGL and you are getting lots of restarts or excessive runs.  Make sure you are using **N52** magnets, and check that your umbilicals are properly support and the right length.  If these 3 things aren't checked it will affect the tap precision.

### Gantry won't go low enough (Voron-V2)
Some tools are shorter than others and with some of the shorter tools the z-rail carriages reach the end of their travel before the nozzle can reach the bed, this can be a problem for probing, QGL and printing.

There's a few options to solve this:
- remove or modify the Z-belt-covers
- replace stock z-joints with [Rigid Z joint](https://www.printables.com/model/996313-voron-v24-rigid-fixed-z-joint) or [low profile z-joints](https://mods.vorondesign.com/details/1hy4XR47A0UJYaDhizaFg)
- Use taller bed spacers

### Which toolhead/extruder is recommended?
A lot of people are asking which toolhead/extruder is recommended. The answer is whatever you want. The changer and tools are completely separate. That being said, using something that is officially supported is going to be the easiest.

### CAN setup
You are definitely going to want to use CAN to connect your toolheads. Its only 4 wires and much lighter. You don't need anything fancy to split out the signal. Simple WAGO connectors work just fine. Of course, there are options for boards that will split the signal as well if you want something that looks a little more professional. Run wires up to the umbilical from your controller and power supply, then use WAGO's there to split the signal. See the guide [here](Configuration#canbus) for a lot more CAN information.
   
### Make sure you have a good PID
If you try to change tools during a print (or when the hotends are active) and it drops off one tool, then waits behind another tool and does nothing, the issue is that its probably waiting for the tool temp to stabilize. Make sure you run a PID tune for each tool and place the info in the corresponding tool config.

### How to calculate build loss
On a stock Voron you will loose some build volume, that build volume loss is in the Y and Z areas on the front of the build plate.  To determine this you ened to know where you docks are and the dementions of your tool.  We have included an image to help you visualize and calculate the loss under and behind the docks.

![Build loss](https://github.com/DraftShift/StealthChanger/blob/main/media/BuildLoss.png?raw=true)

## Build Guide
**Built on stream by [ZombieHedgehog](https://www.twitch.tv/zombiehedgehog)**

| Episode | |
|--------- |--------- |
| 1 | https://youtu.be/YK2Zk2K584Y |
| 2 | https://youtu.be/yOGEAGLlvZc |
| 3 | https://youtu.be/W_r2b8U1J6k |
| 4 | https://youtu.be/cCbIjArKL4M |

## Macros

| Command | Description |
|------- |------ |
| Tool_Align_Start | This macro will put the toolhead 100mm away from where you set the docking position. |
| Tool_Align_Test | This macro will test the docking/undocking procedure. Start it from the docking position (start a few mm up on z, as the first movement is moving straight back on Y). |
| Tool_Align_Done | This macro will move the toolhead back away from the dock. |

* [Youtube Video](https://www.youtube.com/watch?v=mOSi8zTpu_Q) link showing each one
