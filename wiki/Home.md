# Welcome to the StealthChanger wiki!

- For extra support join our [Discord](https://discord.gg/JhYY5BJe)
- For serial requests please see our [rules and how to](https://discord.gg/CjjZ4B5J)

1. After printing the parts make sure that the hex holes look to be proper hexes and that they are very uniform.  If they are misshapen chances are you need to reprint as you will have alignment issues.  It doesn't take much to be out by a lot.  Try printing at a slower speed if you have issues.

2. Calculating available size for tools (number of tools you can fit)
   - Dragon Burners require 60mm per tool (I recommend 5mm between for extruder handles)
   - Stealth Burners require 80mm per tool
   - The gantry required about 20mm per side to be able to pass the tools.  To know how many tools you can fit it's simple math, measure that top bar -40mm to gantry and then divide the remainder by the size of your toolhead.

3. Adjusting preload... Preload is created with the 2 countersunk screws in the tool plate.  These 2 screws need to be magnetic and will make contact with the magnets in the shuttle.  This adds 2 more wider points of contact at the base while also pre loading the sleeves/bearings.  To adjust them screw them all the way in, then slowly unscrew them 1/4 turn at a time (keeping each side even) until the tool no longer engages its self right away.  Once you reach a point where this happens, screw them back in 1/4 turn.  Each tool needs to be adjusted separately as printing irregularities can happen and this will allow you to compensate for it.  You may want to test and readjust these from time to time.

4. If you run homing on Z or QGL and you are getting lots of restarts or excessive runs.  Make sure you are using **N52** magnets, and check that your umbilicals are properly support and the right length.  If these 3 things aren't checked it will affect the tap precision.

5. A lot of people are asking which toolhead/extruder is recommended. The answer is whatever you want. The changer and tools are completely separate. That being said, using something that is already a tested combination for Stealth Burner or Dragon Burner is going to be the easiest.
