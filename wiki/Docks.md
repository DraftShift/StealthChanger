The team has created their own dock as a solution. It allows for mounting from both the top bar, as well as a crossbar (or both). While its currently still in testing, its an option if you can do some work without having a full readme. You can view it here: [DraftShift Modular Dock](https://github.com/DraftShift/ModularDock)

Currently all docks used with [Viesturz's Tapchanger](https://github.com/viesturz/tapchanger) are compatible.

To calculate how many tools you can fit on the front of your printer you ened to know the tools to use first and the amount of room for your front idlers (stock gantry also can't move the entire length of X so make sure you factor that in as well.

   - Dragon Burners/Yavoth require 60mm per tool (I recommend 5mm between for extruder handles)
   - Blackbird, Stealth Burners and XOL require 76mm per tool
   - The gantry required about 20mm per side to be able to pass the tools.  To know how many tools you can fit it's simple math, measure that top bar -40mm to gantry and then divide the remainder by the size of your toolhead.

Once you have this add it all up and subtracked the length of your front extrusion.

Example: Voron 350 is 470mm total, 5 stealthburners is 76 x 5 = 380 -> 380 + 40 - 470 = 50, so that means you can fit 5 Stealthburners and have 50mm to spare which is not enoguh for any other tools.
