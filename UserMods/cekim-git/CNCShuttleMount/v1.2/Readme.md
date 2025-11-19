# Beacon/Carto Mount for Fystec/LDO CNC Shuttle with Top Brace

Work in progress to create a common set of mounting components that provide a mount for multiple X-gantry configurations when using a CNC shuttle with StealthChanger.

- 2020 standard rail with printed/CNC/Carbon-Fiber gantry
- 2020 with Ti-backer plate
- Xbeam rail with CNC gantry

<p float="left">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/tuck_top_ziptie.jpg" width="30%" height="30%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/mount_installed_on_xbeam.jpg" width="30%" height="30%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/qgl.gif" width="30%" height="30%">
</p>
  
# What's new in v1.1/v1.2
- (v1.2) Add support for larger zip-ties (2mm wide with head-size ~4.5mm)
- (v1.1/v1.2) Add additional clearance for carto
- (v1.1) Add support for Ti Backer on 2020 rail (wire-support and top-plate options specifically for 2020+Ti Backer)
- (v1.1) Increased clearance above the brace behind the tool-head - new design is 3mm+ shorter behind the tool-head.
- (v1.1) Using M3x3x5 heat-set for top-plate to achieve this increased clearance

# Notes/Warnings
- This is a work in progress, not all configurations are tested.  My not work with your printer.
- May result in collisions during printer movement, please use caution.  Pay particular attention to collisions between the USB/CAN cable and gantry components.
- Please see companion modifications for [low-profile USB/CAN PG7 mounts here.](../../LowProfileGantryPG7Mount/v1.0)
- Using only the wire-block without the brace is sufficient for functionality and generally provides the maximum clearance as the USB/CAN cable is able to bend out of the way of gantry components at the extremes of movement.  You will have to evaluate your configuration to determine whether the brace is appropriate for you.  Every effort has been made to minimize the space consumed by this mechanism is minimized, but the USB/CAN cable's themselves may exceed the space that exists between the X rail and the rear gantry components.
- Whether braced or not, you will need to provide something between the gantry and the wire-mount/brace to keep the USB/CAN cable from bending down on the build-plate/part. Sleeves and 1mm piano wire work well for this.
- The lock-washers on the M2.5 holding the CNC flag on the shuttle are VERY easy to lose.  Pay close attention to them if you don't want to lose them.  They are not essential on the printer part, but you may want to re-assemble the CNC version at some future date.
- There are components marked "xbeam", "2020" "fystec", "ldo" and "backer".  Those without this designation are used for all configurations
- This version REQUIRES 1 M3x3x5 heat-set inserts vs the voron standard M3x4.5x5

# Features
- Supports Beacon and Cartographer (upright) PCBs
- Multiple Z-height options for PCB placement available
- Optional top/rear support for the USB/CAN cable for Beacon/Carto
- Replaces CNC'd flag with mount that integrates with the rear-brace
- Minimize intrusion with X/Y space - Printed parts do not interfere with full X/Y/Z movement (USB cable may require that some gantry components be modified to clear in some cases)
- May be used without the brace for additional clearance - WARNING... this may result in rubbing/wear at the extremes of movement, the full brace will provide the best protection for your cable.

# BOM
- 1 M3x3x5 heat-set insert
- 4 M3x4.5x5 heat-set inserts
- 2 M3x12 SHCS (M3x10 may be substituted)
- 2 M3x6 BHCS (M3x8 BHCS may be substituted)
- 1 M3x8 BHCS
- 3 2x1mm zip-ties NOTE zip-tie must have no larger than 4.5x4.5mm fastening head.  The zipties included with the Beacon kit will work and zipties with these dimensions are commonly available, but check their dimensions.
- (reused from printed shuttle) M2.5x8 PHCS and lock-washers
- (provided with beacon/carto) M3.5x6 PHCS

# Printing
- Tested with ABS/ASA
- Print with dimensionally accurate settings (ensure the printed part and .step file have the same dimensions)
- No supports required with items printed in intended orientation
- You may need to re-orient for optimal printing, please see the print_orientation_suggestion image
- 4 or 5 perimeters
- 4 or 5 top/bottom layers
- 40% infill
<p><img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/print_orientation_suggestion.png" width="30%" height="30%"></p>

# Assembly
- Insert 2 M3x12 SHCS into the inserts for the CNC shuttle
  - There are inserts for the FYSTEC and LDO shuttles separately as they are shaped differently
  - Once the screw is inserted into the printed insert, then insert both into the shuttle
  <p float="left">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/fystec_insert_and_screw.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/fystec_insert_screw_inserted.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/fystec_insert_installed_shuttle.jpg" width="20%" height="20%">
  </p>
- Install wire-support block heat-set (M3x4.5x5) inserts (2 in front face, 2 in spine), ensure all are flush and straight
- Install M3x3x5 heat-set insert into the lower tab of the rear brace.  It must be installed from the underside (brace flipped on its head).  Ensure it is flush and straight and does not intrude into the space between the lower and upper tab of the rear-brace clamp.
  <p><img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/heatsets_installed.jpg" width="20%" height="20%"></p>
- Loop rear-brace over USB/CAN cable
  <p><img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/loop_brace_over_usb.jpg" width="20%" height="20%"></p>
- Install the PCB to the PCB mount of the desired leg-height (multiple are provided to tune your PCB vs hot-end placement. Using the flat/pan-head cap-screws provided with your beacon/carto. For reference 1.0mm offset will suit a DragonBurner with a Voron Revo nozzle.
  <p float="left">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/pcb_mount_installed.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/pcb_mount_underside.jpg" width="20%" height="20%">
  </p>
- Temporarily fasten the PCB mount to the wire-support mount WITHOUT the CNC shuttle and off the printer with 2 M3x8 SHCS through the front of the PCB mount to the heat-sets in the face of the wire-support block
  - Plug in the USB/CAN cable to the PCB
  - Route the cable in the wire-support block, leaving slack on the connector between the strain-relief portion of the USB/CAN cable and the JST-style connector
  - Use 2x1 zip-tie to fasten the USB/CAN cable to the rear of the wire-support block firmly. Ensuring the ziptie head rests in the cut-out provided for it as well as ensuring the USB/CAN cable is held firmly against the wire-support block.
  <p float="left" >
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/temp_brace_install.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/ziptie_insert.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/ziptie_loose.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/ziptie_cinched_cut.jpg" width="20%" height="20%">
  </p>
- Install the rear-brace to the wire-support block using M3x6 or M3x8 BHCS.
  - Ensure the brace is square to the wire-support block.
  <p float="left" >
    <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/brace_installed.jpg" width="20%" height="20%">
  </p>
- Remove temporary screws holding the wire-support block to the PCB mount
  <p><img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/temp_brace_uninstall.jpg" width="20%" height="20%"></p>
- Replace the CNC optoTAP trigger with the printed top-flat-plate on top of the CNC shuttle
  - remove the 2 M2.5 pan-head screws being careful to not lose the very small lock washers
  - place the CNC optoTAP trigger in a safe place or discard, it will no longer be used
    <p float="left" >
      <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/tiny_flag_screws_and_washers.jpg" width="20%" height="20%">
      <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/top_flag_plate_installed.jpg" width="20%" height="20%">
    </p>
- Install the assembly on the shuttle and tighten top zip-tie (if rear brace used)
  - Fasten 2 front insert screws
  - Fasten the top-flag-plate to the brace using M3x8 BHCS
  <p float="left" >
      <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/fasten_brace_top.jpg" width="20%" height="20%">    
  </p>
- Install top zip-tie
  - Ensure ziptie has routed through brace as shown
  - Tighten ziptie firmly while holding tension on the USB/CAN cable to hold it as tightly as possible to the rear of the brace
  - After tightening and clipping the excess zip-tie, you can rotate the head into the provided recess for additional clearance
   <p float="left" >
   <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/insert_top_ziptie.jpg" width="20%" height="20%">
   <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/top_ziptie_orientation.jpg" width="20%" height="20%">
   <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/cinch_top_ziptie.jpg" width="20%" height="20%">
   <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.2/media/tuck_top_ziptie.jpg" width="20%" height="20%">
   </p>
- Ensure full clearance at extremes of X/Y movement mnaully moving your shuttle/gantry before proceeding under power.
  <p float="left" >
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/cf_gantry_corner.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/CNCShuttleMount/v1.1/media/printed_2020_gantry_corner.jpg" width="20%" height="20%">
  </p>
- (optional) Modify gantry cable mount as requiered to provide additional clearance
  - [Companiion modification for low-profile USB/CAN PG7 mounts here](../../LowProfileGantryPG7Mount/v1.0)
  <p><img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim-git/LowProfileGantryPG7Mount/v1.0/media/printed_gantry_mount.jpg" width="30%" height="20%"></p>
