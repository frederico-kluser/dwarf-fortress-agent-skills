# Reaction examples

> Fonte: [Reaction examples](https://dwarffortresswiki.org/index.php/Reaction_examples) — Dwarf Fortress Wiki (GFDL/MIT)

Reactions seem to be causing people some issues. As such, examples would probably be useful for those who'd like some help creating what they want. When adding a new reaction, make sure to add a line for it in the entity_default file, under the mountain (first section) section. For example, if adding the adamantine wafer reaction, open entity_default, go to the mountain entry (the first one), scroll down until you see \[PERMITTED_REACTION:something\] (like \[PERMITTED_REACTION:TAN_A_HIDE\]) and add another line that says \[PERMITTED_REACTION:REACTION_NAME\], where REACTION_NAME is whatever is stated in the reaction's REACTION tag, so in this case the entry would read \[PERMITTED_REACTION:FREE_ADAMANTINE_WAFERS\].

## Smelter Emulation

### Smelt Hematite Ore

Simulates the built-in smelting of hematite ore.

`[REACTION:SMELT_IRON_FROM_HEMATITE]`\
`[NAME:Smelt hematite to bars]`\
`[BUILDING:SMELTER:NONE]`\
`[REAGENT:A:BOULDER:NO_SUBTYPE:INORGANIC:HEMATITE]`\
`[PRODUCT:100:4:BAR:NO_SUBTYPE:INORGANIC:IRON][PRODUCT_DIMENSION:150]`\
`[FUEL]`\
`[SKILL:SMELT]`

Results in 4 iron bars, of basic size.

### Smelt Galena Ore

Simulates the built-in smelting of galena ore.

`[REACTION:SMELT_COPPER_FROM_GALENA]`\
`[NAME:Smelt galena to bars]`\
`[BUILDING:SMELTER:NONE]`\
`[REAGENT:A:BOULDER:NO_SUBTYPE:INORGANIC:GALENA]`\
`[PRODUCT:100:4:BAR:NO_SUBTYPE:INORGANIC:COPPER][PRODUCT_DIMENSION:150]`\
`[PRODUCT:50:4:BAR:NO_SUBTYPE:INORGANIC:SILVER][PRODUCT_DIMENSION:150]`\
`[FUEL]`\
`[SKILL:SMELT]`

Results in 4 copper bars, with a 50% chance of a silver bar.

## Plant Reactions

### Brew drink from plant

This is the built-in reaction to brew alcohol from plants.

`[REACTION:BREW_DRINK_FROM_PLANT]`\
`   [NAME:brew drink from plant]`\
`   [BUILDING:STILL:HOTKEY_STILL_BREW]`\
`   [REAGENT:plant:1:PLANT:NONE:NONE:NONE]`\
`       [HAS_MATERIAL_REACTION_PRODUCT:DRINK_MAT] only accept plants that have drinks defined`\
`       [UNROTTEN]`\
`   [REAGENT:barrel/pot:1:NONE:NONE:NONE:NONE]`\
`       [EMPTY]`\
`       [FOOD_STORAGE_CONTAINER] barrel or any non-absorbing tool with FOOD_STORAGE`\
`       [PRESERVE_REAGENT]`\
`       [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]`\
`   [PRODUCT:100:5:DRINK:NONE:GET_MATERIAL_FROM_REAGENT:plant:DRINK_MAT]`\
`       [PRODUCT_TO_CONTAINER:barrel/pot]`\
`       [PRODUCT_DIMENSION:150]`\
`   [PRODUCT:100:1:SEEDS:NONE:GET_MATERIAL_FROM_REAGENT:plant:SEED_MAT]`\
`   [SKILL:BREWING]`

## Bucket/Alcohol Reactions

## Weapon Reactions

### Gemstone Long Sword

Make a long sword out of four rough gemstones of the same type.

`[REACTION:MAKE_GEMSTONE_SWORD_LONG]`\
`[NAME:make gemstone long sword]`\
`[BUILDING:SMELTER:NONE]`\
`[REAGENT:A:4:ROUGH:NO_SUBTYPE:NONE:NONE]`\
`[PRODUCT:100:1:WEAPON:ITEM_WEAPON_SWORD_LONG:GET_MATERIAL_FROM_REAGENT:A:NONE]`\
`[FUEL]`\
`[SKILL:SMELT]`

## Misc Item Reactions

### Craft Windows from Shells

Turns shells into a window made from that animal's shell.

`[REACTION:MAKE WINDOW FROM SHELL]`\
`   [NAME:make shell window]`\
`   [BUILDING:CRAFTSMAN:NONE]`\
`   [REAGENT:shell:3:CORPSEPIECE:NO_SUBTYPE:NONE:NONE]`\
`       [ANY_SHELL_MATERIAL]`\
`       [USE_BODY_COMPONENT]`\
`   [PRODUCT:100:1:WINDOW:NO_SUBTYPE:GET_MATERIAL_FROM_REAGENT:shell:NONE]`\
`   [SKILL:BONECARVE]`

### Cremate Vermin Remains

Incinerates all those non-rotting vermin remains so they stop cluttering up your hallways.

`[REACTION:CREMATE_REMAINS]`\
`[NAME:cremate remains]`\
`[BUILDING:SMELTER:NONE]`\
`[REAGENT:A:1:REMAINS:NONE:NONE:NONE]`\
`[PRODUCT:100:1:BAR:NONE:ASH:NONE][PRODUCT_DIMENSION:150]`\
`[SKILL:SMELT]`\
`[AUTOMATIC]`

Results in 1 bar of ash, and also automatically populates itself in an idle smelter like the loom cloth and tan a hide tasks.

### Create Adamantine Wafers

Creates adamantine wafers, pretty self-explanatory.

`[REACTION:FREE_ADAMANTINE_WAFERS]`\
`[NAME:create adamantine wafers]`\
`[BUILDING:SMELTER:NONE]`\
`[PRODUCT:100:5:BAR:NO_SUBTYPE:INORGANIC:ADAMANTINE][PRODUCT_DIMENSION:150]`\
`[SKILL:SMELT]`

### Create Adamantine Thread

Again, self-explanatory. Also, trains clothesmaking.

`[REACTION:FREE_ADAMANTINE_THREAD]`\
`[NAME:create adamantine thread]`\
`[BUILDING:SMELTER:NONE]`\
`[PRODUCT:100:5:THREAD:NO_SUBTYPE:INORGANIC:ADAMANTINE][PRODUCT_DIMENSION:15000]`\
`[SKILL:CLOTHESMAKING]`

### Burning furniture and other wooden objects

The code below lets you burn furniture and other wooden objects at a wood furnace to obtain charcoal. Normally, a new ID is used for a new reaction. The downside of a new reaction is that a map regen is necessary. The example below shows how a reaction ID of a current game (making billon from raw ores) can be used to add a new reaction without having to start over a map.

In the example below, for each piece of wood furniture, 0.25 charcoal is generated. Since custom reactions can't work in the same way as melting metal, 1 bar of charcoal is generated for 4 units of furniture. Since 4 different reagents are used, this does not necessarily need to be 4 beds, but can be 4 diferent wood objects. in the current code, each type of wooden object is elligible, so it is advisable to create an additional wood furnace and link specific stockpiles to this furnace. This allows you to burn low quality items, while preventing your masterpiece beds going up in flames.

the text below replaces the original 'billon making' reaction in data/save/'your save'/raw/objects/reaction_smelter.txt.

`[REACTION:BILLON_MAKING]`\
`[NAME:burn furniture]`\
`[BUILDING:WOOD:CUSTOM_B]`\
`[REAGENT:A:1:NONE:NONE:NONE:NONE][ANY_PLANT_MATERIAL][HARD_ITEM_MATERIAL][EMPTY]`\
`[REAGENT:B:1:NONE:NONE:NONE:NONE][ANY_PLANT_MATERIAL][HARD_ITEM_MATERIAL][EMPTY]`\
`[REAGENT:C:1:NONE:NONE:NONE:NONE][ANY_PLANT_MATERIAL][HARD_ITEM_MATERIAL][EMPTY]`\
`[REAGENT:D:1:NONE:NONE:NONE:NONE][ANY_PLANT_MATERIAL][HARD_ITEM_MATERIAL][EMPTY]`\
`[PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:CHARCOAL][PRODUCT_DIMENSION:150]`\
`[SKILL:WOOD_BURNING]`

An important thing to note is that the code above works with all wood items. Turning every single wooden bolt into 0.25 charcoal is considered cheaty, so it is up to the user to use the code appropiately. If the user wants more than 4 units per unit of charcoal for better balance, the number of reagents can easily be expanded.
