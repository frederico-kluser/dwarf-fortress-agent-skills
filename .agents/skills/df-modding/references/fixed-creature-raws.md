# Fixed Creature RAWs

> Fonte: [Fixed Creature RAWs](https://dwarffortresswiki.org/index.php/Fixed_Creature_RAWs) — Dwarf Fortress Wiki (GFDL/MIT)

This is the project page for making corrections to the vanilla Dwarf Fortress creatures.

## What Are Raws?

Raw files are text files that describe objects in the game using a list of programmed tags, or tokens. These tokens can describe everything from how many eggs it lays, to what kind of blood it has.

## Project Goals

The goal of this project is to go through the raws, and build a 'fixed' list of creatures to enhance game play. For instance, the default raws (as of 34.11) have a missing CHILD tag on the Black Mamba creature, which results in the snakes laying eggs that never hatch! Players will be able to use these adjusted raws to enhance their game, and have more accurate in-game creatures.

## Helpful Tools

- Raw Explorer makes it quick and easy to edit raw files, and individual creatures can be extracted by simply right-clicking (on the creature) and choosing "copy".
- Creature token is a great resource for explaining what each token does and how to use it.

## Creatures

Below are the creatures with fixed raws.

### Black Mamba

------------------------------------------------------------------------

Raw Location: creature_tropical_new.txt

Original: Black mamba/raw

**Changes Made:**

- Added `CHILD:1` to allow eggs to hatch
- Changed `CLUTCH_SIZE:10:30` to 10:25 to match the real animal. Source

### Adder

------------------------------------------------------------------------

Raw Location: creature_temperate_new.txt

Original: Adder/raw

**Changes Made:**

- Added `CHILD:1` and `LITTERSIZE:3:20` and removed egg related tags to allow adders to have 3 to 20 live offspring. Adders (Vipera berus) don't actually lay eggs, they're ovoviviparous, meaning that they keep the eggs internally and then give live birth.
