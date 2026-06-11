# Plant token

> Fonte: [Plant token](https://dwarffortresswiki.org/index.php/Plant_token) — Dwarf Fortress Wiki (GFDL/MIT)

The `[OBJECT:PLANT]` token begins the definition of a plant raw file. Following this, each new plant definition begins with the `[PLANT:plant_ID]` token, where plant_ID is a unique identifier for the plant, and that plant's properties are then defined using the tokens listed below.

## Basic tokens

These tokens are specified for all plants and define their most basic characteristics.

[TABLE]

## Environment tokens

These tokens, also applicable to all plants, specify where the plants grow.

[TABLE]

## Growth tokens

These tokens are used for all plants and specify growths growing on a plant.

Edible or otherwise usable growths should have \[STOCKPILE_PLANT_GROWTH\] in their material definitions for proper stockpiling. This also lets them be collected from plant gathering and farming jobs.

[TABLE]

## Tree tokens

These tokens are used only for trees.

[TABLE]

## Shrub tokens

These tokens are used for non-grass, non-tree plants.

[TABLE]

## Grass tokens

These tokens are used only for grasses.

[TABLE]
