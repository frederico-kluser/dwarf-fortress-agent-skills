# Slurry

> Fonte: [Slurry](https://dwarffortresswiki.org/index.php/Slurry) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Slurry** is a material used in paper making. Slurry is created at a mill or quern from cloth plants and pressed into paper at a screw press. This also creates seeds.

The labor associated with making slurries is papermaking, under crafts - *not* milling, as one might expect from the building.

Slurry is considered to be a glob in the Stocks menu.

Oddly enough, despite not being food, slurries are stored in the food stockpile as a paste.

Here is a workflow for making plant slurry:

- Build stoneworker's workshop (bot)

- Produce stone quern using stoneworkers workshop (input: stone)

- Build quern (bofq)

- Add plant stockpile near your quern.

- Have your dwarves gather plants.

- Set a work order for your quern to produce 'slurry' if fewer than 10 'globs' exist. Specify "Adj" to be 'paper-slurry items. (input: plants) (Note: You need a dwarf with the 'Manager' role and an office assigned to use work orders. You can do that from n Nobles and Administrators)

## Types of Slurry

The following plants can be turned into slurry:

- Cotton
- Flax
- Hemp
- Jute
- Kenaf
- Pig tail
- Ramie
- Rope reed

## Technical info

Slurry is the [`[SOLID_PASTE]`](/index.php/Material_definition_token#SOLID_PASTE "Material definition token") state of plant fiber and its [`[SOLID_PRESSED]`](/index.php/Creature_token#SOLID_PRESSED "Creature token") state is the paper itself. The structural material has `[MATERIAL_REACTION_PRODUCT:PRESS_PAPER_MAT:LOCAL_PLANT_MAT:THREAD]` to tell the milling reaction to have slurry as the product, and the slurry has class `[REACTION_CLASS:PAPER_SLURRY]` to turn the glob into paper of the same material.

## Bugs

- Slurry stored on the floor in food stockpile (not in a barrel/pot) will trigger a Clean job, resulting in the glob being destroyed.Bug:9884 As a work-around, one can use the custom stockpile feature to disable paste from being stored in food stockpiles, and the slurry will remain safely in the quern/millstone until need at a screw press.
