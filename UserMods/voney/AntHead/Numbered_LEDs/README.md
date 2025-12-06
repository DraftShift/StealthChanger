# AntHead Numbered LEDs – All Sizes Edition

This folder contains 3MF and STEP files for numbered AntHead cowls with rear‑lit
cutouts, matching light diffusers, and light blockers, covering **all current
AntHead cowl variants**.

## Overview

AntHead cowls come in:
- **2 extruder mount styles**: Orbiter 2 and Sherpa Mini
- **3 lengths**: Standard, High Flow (**HF**), and Ultra High Flow (**UHF**)

This gives 6 base cowls. Each base cowl here is provided in **6 numbered
versions (`0–5`)**, for a total of **36 numbered cowls**, each with:
- A **front cowl** with a numeric cutout
- A matching **rear light diffuser**
- A matching **internal light blocker** for the rear‑mounted LED (as supported
  by AntHead’s existing logo cowls)

In addition, this project includes an **optional PTFE tube "negative"** part
used to cut a straight PTFE pass‑through hole in the main body for people who do
**not** want to use AntHead’s Leaf Cutter (filament cutter).

## Contents

- **STEP file** of the full project
  - Combined reference model showing the modified numbered cowls.

- **3MF project files** for each combination of:
	- Mount: `Orbiter 2` / `Sherpa Mini`
	- Length: `Standard` / `HF` / `UHF`
	- Number: `0–5`

	Each 3MF is pre‑arranged to include:
	- The numbered cowl body for the chosen mount/length
	- A **PTFE tube negative** part already positioned and active
- **3MF project files** for the light blockers and light diffusers. Each 3MF file
  contains all parts 0-5.

## Using the PTFE Tube Negative

For users who don’t want to run AntHead’s Leaf Cutter:
- The **PTFE tube negative** is positioned inside the cowl body in the 3MF.
- When sliced as‑is, it will **subtract** the PTFE tube path, leaving a clean,
  printed hole.
- If you *do* want to keep the stock Leaf Cutter arrangement instead, simply
  **delete or deactivate the negative** part in your slicer before slicing.

## Printing Notes

- Refer to the main AntHead documentation for **material, temperature, and
  cooling recommendations**.
- Ensure your **rear LED** is installed as per AntHead’s LED/logo documentation
  – these cowls are drop‑in replacements that reuse the same LED mounting and
  wiring.

## Credits & Attribution

- Based on [**AntHead**](https://github.com/PrintersForAnts/AntHead), by
  [hartk](https://github.com/hartk1213) using v96 [of the official AntHead STEP
  file](https://github.com/PrintersForAnts/AntHead/blob/46a0f00b76af94977a647d08f8f5e4239b60149e/CAD/AntHead_Assembly%20v96.zip).
- Inspired by the earlier [0-5 numbered cowls](../traxman25/Ant%20Head) by
  **Traxman25**, who provided cowls for **Orbiter 2 / Standard length**. This
  variant extends that idea to **all current AntHead cowl mount/length
  combinations**, with matching diffusers and light blockers.
> **NOTE**: The light blockers and diffusers here were made from scratch and are
> **NOT** cross-compatible with Traxman25's work.

AntHead is an independent project with its own licensing and documentation;
please refer to the official AntHead repo/docs for details and updates.

If you have questions or run into issues with these files, you can reach me on
the StealthChanger Discord as **MF-SHROOM**.

## License

These files are **derived from AntHead**, which is licensed under the
**GNU General Public License v3.0 (GPL‑3.0)**. In accordance with that license:

- The STEP and 3MF files in this folder are distributed under **GPL‑3.0**.
- A copy of the **GPL‑3.0 license text** should be included alongside this
  folder (for example as `LICENSE` or `COPYING`).
- The included STEP file represents the **preferred form for modification** of
  these numbered cowls.

This licensing applies to the contents of this folder only and does not change
the license of the broader StealthChanger project, nor my other UserMods.

