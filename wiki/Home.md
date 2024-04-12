# <img src="https://github.com/DraftShift/Stealthchanger/blob/main/media/Stealthchanger_logo.png?raw=true" height="100" align="top" /> StealthChanger

Unlike the name suggests we support more then just stealthburner.

Due to difficulties with heat insert and aligning of bearings and mounts we wanted to try a more simplistic design based on bushings and pins.

This is a very light design, requiring less parts and as such is cheaper and easier to build.  Input shaper tests have shown it to be as rigid if not more than current Tapchanger.

All parts are easily replaceable without reprinting if wear happens, life of the bushings and pins are still being tested.

## Tool compatability
Currently we support the standard Stealth Burner, Dragon Burner, and Rapid Burner.  There are plans in place to add the Mini Stealth Burner, XOL, and Archetype.

## Before you begin

There are a few considerations that should be taken into account before you begin this project. First is, yes, you need an optotop board on every tool. The board is needed as thats how klipper knows which board is active. When the tap sensor is triggered, it knows which tool it has. You do not need the other tap parts though, like the MGN9 rail. StealthChanger by design also acts like the normal tap and does z probing.

Are you going to be printing any material that needs an enclosed printer? If the answer is yes, then you will need a tophat on your printer (or longer vertical extrusions). Typically, it adds around 200mm to the top (give or take based on your specific build). 

Canbus is nearly a requirement. While technically you dont to do canbus, getting that many wires to each tool and doing so in a way that they won't tangle is going to be a nightmare. That being said, cable management is a very big part of the process. Without it, the cables will get wrapped up around each other and cause issues. Having some kind of plan for umbilicals is a must when considering the project.

How are you doing docks? There are a few different ways of doing them, and what you choose is going to influence a lot of things. If you plan on using a stock Voron build, remember that you need to have clearance at the sides of the docks for the front idlers to go beside them. This will also influence number of tools. You also have the option of top rail mounted docks or crossbar docks. Crossbar docks are probably the most stable, as they ultimately can be more stiff. You can also do a crossbar plus topmount for even more rigidity. If you decide to go this route, then you really want to use 2040 extrusions for your front rails. This way you can still use all the stock voron doors/panels etc with the crossbar, as well as not have the idlers hitting the crossbar. Top mounted docks are completely acceptable though, they just have a little more movement to them. As an alternative option the team has created a printable [door buffer](https://github.com/DraftShift/DoorBuffer) that will give you a crossbar without requiremend to replace your current front frame.


1. [Bill of Materials](Bill-of-Materials)
2. [Printing](Printing)
3. [Assembling](Assembling)
4. [Installation](Installation)
5. [Configuration](Configuration)
6. [Docks](Docks)
7. [Slicers](Slicers)
8. [Support and FAQs](Support-and-FAQs)
9. [Contributing](Contributing)
10. [Contributors & Credits](Contributors-and-Credits)
