This mod is a remixing the endstop carrier from [MrTeliP](https://www.printables.com/model/325765-voron-24r2-pg7-cable-gland-and-endstop) (on Printables)

### Pupose
It move the X and Y endstop switches to a single assembly, which attached to the stock Voron A(Y) motor mount. 

### Assembly
This assembly is held in place by replacing the original two M3x30mm bolts with two M3x35mm bolts, which passed through the holes on the assembly (See the **Images** folder).

### How it works
You might need to mod the homing config to get the right rebound on Y after homing Y.

Look for this line
```
G0 Y{ max_y - 20 } F5000
```

The 20 is the amount of rebound, you'll likely want around 4
```
G0 Y{ max_y - 4 } F5000
```

**NOTE:** the switch arm is not compatible with shuttle keeper, you will need to add 5-6mm to the arm if you are using shuttle keeper or you won't be able to reach the switch.
