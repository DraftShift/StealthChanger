This mod is a remixing the endstop carrier from [MrTeliP](https://www.printables.com/model/325765-voron-24r2-pg7-cable-gland-and-endstop) (on Printables)

### Pupose
It move the X and Y endstop switches to a single assembly, which attached to the stock Voron A(Y) motor mount. 

### Assembly
This assembly is held in place by replacing the original two M3x30mm bolts with two M3x35mm bolts, which passed through the holes on the assembly (See the **Images** folder).

For the software. Add the custom_home.cfg file into your config folder in klipper. Then add `[include custom_home.cfg]` to your printer.cfg. Comment out [safe_z_home] if it is in printer.cfg.

### How it works
This configuration works by adding the `[force_move]` and `[homing_override]` function in klipper's **printer.cfg**, to make sure that the Y-axis is homed before the X-axis.

Note: [safe_z_home] need to be disable for [homing_override] to be used. However, I suggest just commenting it out, rather to deleting the code, in case you need it.
