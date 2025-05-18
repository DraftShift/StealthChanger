# IllFilamentRunout
Side-mounted filament runout sensor that supports 6 filament lines.

![IllFilamentRunout](images/IMG1.jpg)

## BOM
- 12x MR105 Bearings
- 42x DIN912 M3 x 6mm bolts
- 12x M3 heat inserts
- 2x M6 T-nut
- 2x DIN912 M6 x 14mm bolts
- 1x RP2040 board (e.g., AITEWIN ROBOT RP2040 Core Board)
- 1x SN65HVD230 CAN Bus Transceiver
- 1x MP1584EN DC-DC step down voltage regulator
- 2x JST XH2.54mm 2-pin male/female pairs
- 6x EQV Optical speed sensor
- 6x O-rings (10.0 × 7.0 × 1.5 mm)

## Notes
- Install Katapult and Klipper as you would on any RP2040 board. Be sure to note the GPIO pins used for CAN Tx/Rx.
- It’s recommended to connect the sensor's Vcc pin to the DC-DC converter, not directly to the RP2040 board.
- The SN65HVD230 transceiver operates at 3.3V.
- Use GPIO pins 16–21 to connect the optical sensors to the board. You can use different pins, but you’ll need to update the configuration accordingly.

- The input side is designed for a 4mm PTFE tube, while the output side fits a 5mm tube.
- Heat inserts go on the bottom of the sensors to mount them to the SidePanel.

## Credits
This sensor is based on the [Filament Progression and Runout sensor](https://www.printables.com/model/629380-filament-progression-and-runout-sensor-optical-end) by [Fractalengineer](https://www.printables.com/@Fractalengine_242936)