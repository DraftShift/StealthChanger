# Beacon/Carto Mount for Fystec/LDO CNC Shuttle with Top Brace

Work in progress to create a common set of mounting components that provide a mount for multiple X-gantry configurations when using a CNC shuttle with StealthChanger.

- 2020 standard rail with printed/CNC/Carbon-Fiber gantry
- Xbeam rail with CNC gantry

  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/brace_top_ziptie_loose_top.jpg" width="30%" height="30%">

# Notes/Warnings
- This is a work in progress, not all configurations are tested.  My not work with your printer.
- May result in collisions during printer movement, please use caution.
- Pay particular attention to collisions between the USB/CAN cable an gantry components.
- The lock-washers on the M2.5 holding the CNC flag on the shuttle are VERY easy to lose.  Pay close attention to them if you don't want to lose them.  They are not essential on the printer part, but you may want to re-assemble the CNC version at some future date.
- There are components marked "xbeam", "2020" "fystec" and "ldo".  Those without this designation are used for all configurations

# Features
- Supports Beacon and Cartographer (upright) PCBs
- Multiple Z-height options for PCB placement available
- Optional top/rear support for the USB/CAN cable for Beacon/Carto
- Replaces CNC'd flag with mount that integrates with the rear-brace
- Minimize intrusion with X/Y space - Printed parts do not interfere with full X/Y/Z movement (USB cable may require that some gantry components be modified to clear in some cases)
- May be used with the brace for additional clearance.

# BOM
- 5 M3x4.5x4 heat-set inserts
- 2 M3x12 SHCS (M3x10 may be substituted)
- 2 M3x6 BHCS
- 1 M3x8 BHCS (M3x6 may be substituted)
- 3 2x1 zip-ties
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
<p><img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/print_orientation_suggestion.png" width="30%" height="30%"></p>

# Assembly
- install wire-support block heat-set inserts (2 in front face, 2 in spine), ensure all are flush and straight
- (optional if rear brace is used) Install Top-Flag-Plate heat-set insert, ensure top is flush with face
  <p><img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/heatset_inserts_installed.jpg" width="20%" height="20%"></p>
- Install the PCB to the PCB mount of the desired leg-height (multiple are provided to tune your PCB vs hot-end placement.  For reference 1.0mm offset will suit a DragonBurner with a Voron Revo nozzle.
  <p float="left">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/pcb_mount_installed.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/pcb_mount_underside.jpg" width="20%" height="20%">
  </p>
- Temporarily fasten the PCB mount to the wire-support mount WITHOUT the CNC shuttle and off the printer with 2 M3x8 SHCS through the front of the PCB mount to the heat-sets in the face of the wire-support block
  - Plug in the USB/CAN cable to the PCB
  - Route the cable in the wire-support block, leaving slack on the connector between the strain-relief portion of the USB/CAN cable and the JST-style connector
  - Use 2 2x1 zip-ties to fasten the USB/CAN cable to the rear of the wire-support block firmly.  Pushing the square block of the zip-tie back toward the wire-support block.
  - NOTE: the wire support block may be used in this configurtion without the brace or top-plate if desired.
  <p float="left" >
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/wire_support_temp_install_front.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/wire_support_temp_install_zipties.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/wire_support_temp_install_cinched.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/wire_support_temp_install_clipped.jpg" width="20%" height="20%">
  </p>
- (optional) Install the rear-brace to the wire-support block using M3x6 BHCS.
  - Loop the brace over the USB/CAN cable.
  - Ensure the brace is square to the wire-support block.
  <p float="left" >
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/brace_loop_over.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/brace_installed.jpg" width="20%" height="20%">
  </p>
- (optional: if rear brace is used) remove the CNC optoTAP trigger on top of the CNC shuttle by removing the 2 M2.5 pan-head screws being careful to not lose the very small lock washers
  - place the CNC optoTAP trigger in a safe place or discard, it will no longer be used
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/tiny_flag_screws_and_washers.jpg" width="20%" height="20%">
- (optional: if rear brace is used) Install the top-flag-plate to the brace using M3x8 BHCS (M3x6 may also be used)
  - Insert into rear brace
  - Fasten screw
  - Add loose zip-tie
   <p float="left" >
   <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/brace_top_ziptie_insert.jpg" width="20%" height="20%">
   <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/brace_top_ziptie_loose_rear.jpg" width="20%" height="20%">
   <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/brace_top_ziptie_loose_top.jpg" width="20%" height="20%">
   </p>
- Remove temporary screws holding the wire-support block to the PCB mount
  <p><img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/temp_install_undo.jpg" width="20%" height="20%"></p>
- Insert 2 M3x12 SHCS into the inserts for the CNC shuttle
  - There are inserts for the FYSTEC and LDO shuttles separately as they are shaped differently
  - Once the screw is inserted into the printed insert, then insert both into the shuttle
  <p float="left">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/fystec_insert_and_screw.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/fystec_insert_screw_inserted.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/fystec_insert_installed_shuttle.jpg" width="20%" height="20%">
  </p>
- Install the assembly on the shuttle and tighten top zip-tie (if rear brace used)
  - Fasten 2 front insert screws
  - (optional: if rear brace used) Screw the printer top-flag-plate in its place using the 2 M2.5 screws with lock washers removed from the CNC shuttle.
  - Cinch and clip zip-tie on top rear brace
  <p float="left" >
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/assembly_on_shuttle_cinched.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/assembly_on_shuttle_clipped.jpg" width="20%" height="20%">
  </p>  
- Ensure full clearance at extremes of X/Y movement before proceeding under power
  <p float="left" >
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/cf_gantry_corner.jpg" width="20%" height="20%">
  <img src="https://github.com/cekim-git/Toolchanger/blob/main/UserMods/cekim/CNCShuttleMount/v1.0/media/printed_2020_gantry_corner.jpg" width="20%" height="20%">
  </p>

