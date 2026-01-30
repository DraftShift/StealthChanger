# Low-Profile PG7 A-motor Mounts for SC CNC Shuttle Beacon/Carto Mount

Work in progress to provide PG7 gland mounts for the A-motor gantry mount that consume less space than existing mechanisms.  This additional space is needed to provide clearance for the USB/CAN cable attached to the CNC shuttle mount for Beacon/Carto.  Without this modification, the USB/CAN cable affixed to the braced CNC shuttle mount for the Beacon/Carto scanners will tend to collide with the PG7 gland or mount.

<p float="left">
<img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/printed_gantry_mount.jpg" width="30%" height="20%">
<img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/chaotic_cf_zchain_insert.jpg" width="30%" height="20%">
</p>

# Mounts Provided

* Voron 2.4 Standard printed gantry A-motor mount
* Generic CNC gantry matching Voron 2.4 printed gantry dimensions
* Chaotic CNC and Carbon Fiber (CF) A-motor mounts

# Additional Options

* Captured Piano-wire strain-relief mount under the top-face of the mount
* All but the printed part option have an additional option of mounting the piano-wire in the hole above the screw on the side so that the wire is not rubbing on your CNC/CF gantry components
* CNC/CF have an insert on the side to provide additional stabilization/piano wire mounting or mounting for inverted Z-chain
* Inverted Z-chain foot in place of the standard insert for CF/CNC options

# BOM

* Depends on which option you choose
* 1 M3x4x5.4 heat-set insert
* 2 M2.5x12 SHCS (only on CNC/CF gantries)
* 2 M2.5x8 SHCS (only on CNC/CF gantries)
* 1 M3x10 SHCS  (only on printed gantry and CNC gantries matching printed gantry pattern)
* 1 M3x6 BHCS
* Piano Wire
* PG7 Gland

# Printing

* Print dimensionality accurate parts (parts must match design file dimensions after shrinkage)
* 4-5 top/bottom layers
* 40% infill
* Suggest all mount bodies are printed on their head (see image - suggested print orientation
* Suggest supports on elevated 2.5 SHCS counter-bores (see image - green coloring)
* There may be some stringing around the screw-holes and PG7 threads - remove any strings obstructing the screws. The PG7 stringing can be mostly ignored.  Clear that only if it prevents easily screwing in the gland.
* You only need to print the components you are going to use
  - Main mount body (pick only one)
  - insert or z-chain insert

  <p float="left">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/pg7_support_examples.png" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/pg7_support_paint.png" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/pg7_print_orientation_suggestion.png" width="20%" height="20%">
  </p>

# Assembly

* Install heat-set insert into the mount body of the printed gantry mount or the side inserts of the CNC/CF as your configuration requires
* Bend Piano wire to fit into either the hole under the mount head or in insert body (printed gantry option must be under the mount-head.
* Insert piano wire through gland threaded hole and either under the mount head or into the side hole
* Install mount into A-motor mount (printed gantry option will require you rotate the PG7 mount as you put it to clear face into which you installed the heat-set insert)
* Install any insert/z-chain inserts you plan to use
* Install screws
  - M3x10 to fasten mount into A-motor mount from the top (Chaotic option doesn't have this screw)
  - M2.5x12 (CNC/CF gantries) x2 to down through the gantry into the side insert from the top
  - M2.5x8 (CNC/CF gantries) x2 up through the gantry into the side insert from the bottom
  - M3x6 BHCS (non-printed gantry options) into the insert from inside/behind the main mount body into the side insert

  <p float="left">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/cnc_mount_and_insert.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/bend_piano_wire.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/piano_wire_installed_top.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/alternate_piano_wire_and_fastener.jpg" width="20%" height="20%">
  </p>





