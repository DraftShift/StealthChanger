1. [Methods](#methods)
2. [FAQs](#faqs)
3. [Build Guide](#build-guide)
4. [Macros](#macros)


## Methods

<a href="https://discord.gg/jJs73c6vSc" target="_blank" alt="Join our Discord">![Discord](https://img.shields.io/discord/1226846451028725821?logo=discord&logoColor=%23ffffff&label=Join%20our%20Discord&labelColor=%237785cc&color=%23adf5ff)</a>


## FAQs


1. After printing the parts make sure that the hex holes look to be proper hexes and that they are very uniform.  If they are misshapen chances are you need to reprint as you will have alignment issues.  It doesn't take much to be out by a lot.  Try printing at a slower speed if you have issues.

2. Calculating available size for tools (number of tools you can fit)
   - Dragon Burners/Yavoth require 60mm per tool (I recommend 5mm between for extruder handles)
   - Blackbird, Stealth Burners and XOL require 76mm per tool
   - The gantry required about 20mm per side to be able to pass the tools.  To know how many tools you can fit it's simple math, measure that top bar -40mm to gantry and then divide the remainder by the size of your toolhead.

3. Adjusting preload... Preload is created with the 2 countersunk screws in the tool plate.  These 2 screws need to be magnetic and will make contact with the magnets in the shuttle.  This adds 2 more wider points of contact at the base while also pre loading the sleeves/bearings.  To adjust them screw them all the way in, then slowly unscrew them 1/4 turn at a time (keeping each side even) until the tool no longer engages its self right away.  Once you reach a point where this happens, screw them back in 1/4 turn.  Each tool needs to be adjusted separately as printing irregularities can happen and this will allow you to compensate for it.  You may want to test and readjust these from time to time.

4. If you run homing on Z or QGL and you are getting lots of restarts or excessive runs.  Make sure you are using **N52** magnets, and check that your umbilicals are properly support and the right length.  If these 3 things aren't checked it will affect the tap precision.

5. A lot of people are asking which toolhead/extruder is recommended. The answer is whatever you want. The changer and tools are completely separate. That being said, using something that is officially supported is going to be the easiest.

6. CAN setup. You are definitely going to want to use CAN to connect your toolheads. Its only 4 wires and much lighter. You don't need anything fancy to split out the signal. Simple WAGO connectors work just fine. Of course, there are options for boards that will split the signal as well if you want something that looks a little more professional. Run wires up to the umbilical from your controller and power supply, then use WAGO's there to split the signal. See the guide [here](Configuration#canbus) for a lot more CAN information.
   
7. If you try to change tools during a print (or when the hotends are active) and it drops off one tool, then waits behind another tool and does nothing, the issue is that its probably waiting for the tool temp to stabilize. Make sure you run a PID tune for each tool and place the info in the corresponding tool config.

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
