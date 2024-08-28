# <img src="https://github.com/DraftShift/Stealthchanger/blob/main/media/Stealthchanger_logo.png?raw=true" height="100" align="top" /> StealthChanger

Stealth Changer is a friction and magnetic fit, 3d printing multiple tool changer for the Voron 2.4 printer.

The purpose of a multiple toolhead changer is to allow for mixed material and mixed color printing without having to manually swap filament or purge filament during the swapping of materials. This allows for faster printing and less wasted filament compared to manual swapping and multi-material units like the ERCF or an AMS system.

It consists of a toolhead shuttle, toolhead backplate, and a optotap sensor for Z probing.

Stealth Changer supports a number of popular toolheads by mounting a backplate to the toolhead while using existing toolhead mounting points.

The shuttle replaces the current Voron TAP or Voron X carriage frame while using the TAP optotap sensor.

Mounting of the toolhead with the shuttle is done by using bushings and pins, with magnets to help create a strong mounting connection for high-speed printing while also providing better inputshaping results than TAP.

This is a very light design, requiring less parts and as such is cheaper and easier to build.  Input shaper tests have shown it to be as rigid if not more than current Tapchanger.

All parts are easily replaceable without reprinting if wear happens, life of the bushings and pins are still being tested.

The number of docks that can be installed is based on the width of the printer and the X/Y joins that allow the shuttle to reach the left and right side docks.


## Tool compatability
Currently we support the standard Stealth Burner, Dragon Burner, Rapid Burner, Yavoth, XOL and Archetype. There is also a usermod for the [Mini Stealth Burner](../blob/main/UserMods/jdmontgomer/MiniSB_SC).

## Before you begin

Make sure to visit our [Checklist](Checklist)

There are a few considerations that should be taken into account before you begin this project. First is, yes, you need an optotop board on every tool. The board is needed as thats how klipper knows which board is active. When the tap sensor is triggered, it knows which tool it has. You do not need the other tap parts though, like the MGN9 rail. StealthChanger by design also acts like the normal tap and does z probing.

Are you going to be printing any material that needs an enclosed printer? If the answer is yes, then you will need a tophat on your printer (or longer vertical extrusions). Typically, it adds around 200mm to the top (give or take based on your specific build). 

Canbus is nearly a requirement. While technically you dont need to do canbus, getting that many wires to each tool and doing so in a way that they won't tangle is going to be a nightmare. That being said, cable management is a very big part of the process. Without it, the cables will get wrapped up around each other and cause issues. Having some kind of plan for umbilicals is a must when considering the project.

How are you doing docks? There are a few different ways of doing them, and what you choose is going to influence a lot of things. If you plan on using a stock Voron build, remember that you need to have clearance at the sides of the docks for the front idlers to go beside them. This will also influence number of tools. You also have the option of top rail mounted docks or crossbar docks. Crossbar docks are probably the most stable, as they ultimately can be more stiff. You can also do a crossbar plus topmount for even more rigidity. If you decide to go this route, then you really want to use 2040 extrusions for your front rails. This way you can still use all the stock voron doors/panels etc with the crossbar, as well as not have the idlers hitting the crossbar. Top mounted docks are completely acceptable though, they just have a little more movement to them. As an alternative option the team has created a printable [door buffer](https://github.com/DraftShift/DoorBuffer) that will give you a crossbar without requiremend to replace your current front frame.


1. [Bill of Materials](Bill-of-Materials)
2. [Docks](Docks)
3. [Printing](Printing)
4. [Assembling](Assembling)
5. [Installation](Installation)
6. [Configuration](Configuration)
7. [Calibration](Calibration)
8. [Slicers](Slicers)
9. [Serials](Serials)
10. [Support & FAQs](Support-and-FAQs)
11. [Contributing & Donating](Contributing-and-Donating)
12. [Team & Credits](Team-and-Credits)
