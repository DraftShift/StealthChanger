This mod is a remixing the endstop carrier from [MrTeliP](https://www.printables.com/model/325765-voron-24r2-pg7-cable-gland-and-endstop)

### Pupose
It move the X and Y endstop switches to a single assembly, which attached to the stock Voron A(Y) motor mount. 

### Assembly
This assembly is held in place by replacing the original two M3x30mm bolts with two M3x35mm bolts, which passed through the holes on the assembly.

### How it works
This configuration works by adding the `[force_move]` and `[homing_override]` function in klipper's **printer.cfg** to create make sure that the Y-axis is homed before the X-axis.
The code is as follow:

```
[force_move]
    enable_force_move: True

[homing_override]
axes: xyz
gcode:
    ## Trigger variables
    {% set x = 0 %}
    {% set y = 0 %}
    {% set z = 0 %}

    ##  Engage trigger variables according to the input
    {% if params.Y is defined %}
        {% set y = 1 %}    # for y home
    {% endif %}
    {% if params.X is defined %}
        {% set x = 1 %}    # for x home
    {% endif %}
    {% if params.Z is defined %}
        {% set z = 1 %}    # for z home
    {% endif %}

    ## Homing Actions
    {% if x == 0 and y == 0 and z == 0 %}    ## If just G28 is called
        {% if "z" in printer.toolhead.homed_axes %}    # if both z is already homed
            G91                                        # Relative mode 
            G1 Z+2 F1500                               # move Z up 2mm
            G90                                        # Asolute mode
        {% else %}                                     # Otherwise
            SET_KINEMATIC_POSITION Z=0                 # Set curent Z position as 0
            G91                                        # Relative mode 
            G1 Z+5 F1500                               # move Z up 5mm
            G90                                        # Asolute mode
        {% endif %}
        G28 Y
        G28 X
        G1 X175 Y175 F9000
        G28 Z
        G1 Z20 F1000
    {% else %}
        {% if x == 1 and y == 1 %}   # if x and y are both triggered
            {% if "z" in printer.toolhead.homed_axes %}    # if both z is already homed
                G91                                        # Relative mode 
                G1 Z+2 F1500                               # move Z up 2mm
                G90                                        # Asolute mode
            {% else %}                                     # Otherwise
                SET_KINEMATIC_POSITION Z=0                 # Set curent Z position as 0
                G91                                        # Relative mode 
                G1 Z+5 F1500                               # move Z up 5mm
                G90                                        # Asolute mode
            {% endif %}
            G28 Y
            G28 X
        {% else %}
            {% if x == 1 %}                                    # for x home y first then X
                {% if "z" in printer.toolhead.homed_axes %}    # if both z is already homed
                    G91                                        # Relative mode 
                    G1 Z+2 F1500                               # move Z up 2mm
                    G90                                        # Asolute mode
                {% else %}                                     # Otherwise
                    SET_KINEMATIC_POSITION Z=0                 # Set curent Z position as 0
                    G91                                        # Relative mode 
                    G1 Z+5 F1500                               # move Z up 5mm
                    G90                                        # Asolute mode
                {% endif %}
                G28 Y
                G28 X
            {% endif %}
            {% if y == 1 %}    # for y home just y
                {% if "z" in printer.toolhead.homed_axes %}    # if both z is already homed
                    G91                                        # Relative mode 
                    G1 Z+2 F1500                               # move Z up 2mm
                    G90                                        # Asolute mode
                {% else %}                                     # Otherwise
                    SET_KINEMATIC_POSITION Z=0                 # Set curent Z position as 0
                    G91                                        # Relative mode 
                    G1 Z+5 F1500                               # move Z up 5mm
                    G90                                        # Asolute mode
                {% endif %}
            G28 Y
            {% endif %}
            {% if z == 1 %}    # for z home just z
                {% if "xy" in printer.toolhead.homed_axes %}    # if both x and y are defined
                    SET_KINEMATIC_POSITION Z=0                  # Set curent Z position as 0
                    G91                                         # Relative mode 
                    G1 Z+2 F1500                                # move Z up 2mm
                    G90                                         # Asolute mode
                    G1 X175 Y175 F9000
                    G28 Z
                    G1 Z10 F1000
                {% else %}
                    SET_KINEMATIC_POSITION Z=0             # Set curent Z position as 0
                    G91                                    # Relative mode 
                    G1 Z+5 F1500                           # move Z up 5mm
                    G90                                    # Asolute mode
                    G28 Y
                    G28 X
                    G1 X175 Y175 F9000
                    G28 Z
                    G1 Z10 F1000
                {% endif %}
             {% endif %}
        {% endif %}
    {% endif %}
```
Note: [safe_z_home] need to be disable for [homing_override] to be used. However, I suggest just commenting it out, rather to deleting the code, in case you need it.
