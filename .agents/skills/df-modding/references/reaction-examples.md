# Reaction examples

> Fonte: [Reaction examples](https://dwarffortresswiki.org/index.php/Reaction_examples) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

Reactions seem to be causing people some issues. As such, examples would probably be useful for those who'd like some help creating what they want. When adding a new reaction, make sure to add a line for it in the entity_default file, under the mountain (first section) section. For example, if adding the adamantine wafer reaction, open entity_default, go to the mountain entry (the first one), scroll down until you see \[PERMITTED_REACTION:something\] (like \[PERMITTED_REACTION:TAN_A_HIDE\]) and add another line that says \[PERMITTED_REACTION:REACTION_NAME\], where REACTION_NAME is whatever is stated in the reaction's REACTION tag, so in this case the entry would read \[PERMITTED_REACTION:FREE_ADAMANTINE_WAFERS\].

## Smelter Emulation

### Smelt Hematite Ore

Simulates the built-in smelting of hematite ore.

    [REACTION:SMELT_IRON_FROM_HEMATITE]
    [NAME:Smelt hematite to bars]
    [BUILDING:SMELTER:NONE]
    [REAGENT:A:BOULDER:NO_SUBTYPE:INORGANIC:HEMATITE]
    [PRODUCT:100:4:BAR:NO_SUBTYPE:INORGANIC:IRON][PRODUCT_DIMENSION:150]
    [FUEL]
    [SKILL:SMELT]

Results in 4 iron bars, of basic size.

### Smelt Galena Ore

Simulates the built-in smelting of galena ore.

    [REACTION:SMELT_COPPER_FROM_GALENA]
    [NAME:Smelt galena to bars]
    [BUILDING:SMELTER:NONE]
    [REAGENT:A:BOULDER:NO_SUBTYPE:INORGANIC:GALENA]
    [PRODUCT:100:4:BAR:NO_SUBTYPE:INORGANIC:COPPER][PRODUCT_DIMENSION:150]
    [PRODUCT:50:4:BAR:NO_SUBTYPE:INORGANIC:SILVER][PRODUCT_DIMENSION:150]
    [FUEL]
    [SKILL:SMELT]

Results in 4 copper bars, with a 50% chance of a silver bar.

## Brewing Reactions

### Vanilla

This is the built-in reaction to brew alcohol from plants.

    [REACTION:BREW_DRINK_FROM_PLANT]
        [NAME:brew drink from plant]
        [BUILDING:STILL:HOTKEY_STILL_BREW]
        [REAGENT:plant:1:PLANT:NONE:NONE:NONE]
            [HAS_MATERIAL_REACTION_PRODUCT:DRINK_MAT] only accept plants that have drinks defined
            [UNROTTEN]
        [REAGENT:barrel/pot:1:NONE:NONE:NONE:NONE]
            [EMPTY]
            [FOOD_STORAGE_CONTAINER] barrel or any non-absorbing tool with FOOD_STORAGE
            [PRESERVE_REAGENT]
            [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]
        [PRODUCT:100:5:DRINK:NONE:GET_MATERIAL_FROM_REAGENT:plant:DRINK_MAT]
            [PRODUCT_TO_CONTAINER:barrel/pot]
            [PRODUCT_DIMENSION:150]
        [PRODUCT:100:1:SEEDS:NONE:GET_MATERIAL_FROM_REAGENT:plant:SEED_MAT]
        [SKILL:BREWING]

### Custom

There are a few key things to be aware of when making brewing reactions:

- What your brew is made out of.
- If it can already be made into alcohol by default or not. (In vanilla, that's plant matter, fruits, and honey bee honey.)
- The desired receptacle and its maximum capacity.
- If you want the receptacle to be empty or not. (Add or omit the \[EMPTY\] token)

#### Ingredients

For example, plants (PLANT), fruits (PLANT_GROWTH), and honey (LIQUID_MISC) are all separate item types, so they'll need to be referenced as separate reagents (and in their own separate reactions, unless you're making a recipe that requires all of them).

       [REAGENT:plant:1:PLANT:NONE:NONE:NONE]
           [HAS_MATERIAL_REACTION_PRODUCT:DRINK_MAT][UNROTTEN]

       [REAGENT:fruit:1:PLANT_GROWTH:NONE:NONE:NONE]
           [HAS_MATERIAL_REACTION_PRODUCT:DRINK_MAT][UNROTTEN]

       [REAGENT:honey:150:LIQUID_MISC:NONE:CREATURE_MAT:HONEY_BEE:HONEY]
           [UNROTTEN]

As you may have noticed, honey has some additional quirks:

- LIQUID_MISC is the item class for miscellaneous liquids. To correctly identify it as *honey*, you need to specify that it came from a creature (CREATURE_MAT), the creature it came from (HONEY_BEE), and the creature part (HONEY) in its materials definition. You can do this for other liquids, too, such as delicious dwarven tears (LIQUID_MISC:NONE:**CREATURE_MAT:DWARF:TEARS**).
- Because it's a liquid, not a discrete item, you need to multiply the desired amount by its unit dimension (in this case, 150 liquid units per usable unit of honey). You can see the different dimension multipliers under PRODUCT_DIMENSION, below.

\
Additionally, if one of your ingredients is typically **in** a container (such as with honey), you need to add a reagent for the container as well.

       [REAGENT:honey:150:LIQUID_MISC:NONE:CREATURE_MAT:HONEY_BEE:HONEY]
           [UNROTTEN]
       [REAGENT:honey container:1:NONE:NONE:NONE:NONE]
           [CONTAINS:honey]
           [PRESERVE_REAGENT]
           [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]

If you want to make your own brewable plants, there's a lot that goes into it; make sure to reference the existing plants for reference on what kinds of fields are required to make them work the same way (such as the raws for plump helmets). The good news is any product you make with the item type DRINK:NONE is considered an alcohol by default, regardless of material make-up.

#### Containers

In vanilla, brewing 1 plant yields 5 respective swigs of drink. So long as the container you're brewing into has that much or more available space, the reaction should brew as many whole items from the input stack as will fit in the container without going over (and produce a seed for each instance, if applicable). For example, the humble bucket can hold 10 units of drink. If you made a reaction that let you brew plants into a bucket, and you ran it through a stack of 50 plump helmets, it would consume 2 plump helmets and produce 10 plump helmet wine and 2 plump helmet spawn, still leaving you with a stack of 48 plump helmets.

\
If you have a container that can technically hold *more* than a multiple of 5, the reaction will only take and process as many items as it can without going over. Say we wanted to use jugs instead of buckets, which can hold 16 drinks! If we run it through the same test, the reaction would consume *3* plump helmets and produce 15 drink and 3 spawn, leaving us with 1 leftover, unused unit of space in the jug. You could even pour a different drink into the jug and top if off.

\
However, a few containers, notably flasks and goblets, can only hold 3 units of drink max. If you want to brew into these directly, you'll need to reduce the amount of drink produced or things get weird.

       [REACTION:BREW_PLANT_INTO_FLASK]
       [NAME:brew plant into an empty flask/waterskin]
       [ADVENTURE_MODE_ENABLED]
       [REAGENT:plant:1:PLANT:NONE:NONE:NONE]
           [HAS_MATERIAL_REACTION_PRODUCT:DRINK_MAT][UNROTTEN]
       [REAGENT:flask:1:FLASK:NONE:NONE:NONE]
           [PRESERVE_REAGENT][EMPTY]
           [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]
       [PRODUCT:100:3:DRINK:NONE:GET_MATERIAL_FROM_REAGENT:plant:DRINK_MAT] Product reduced from 5 to 3
           [PRODUCT_TO_CONTAINER:flask]
           [PRODUCT_DIMENSION:150]
       [PRODUCT:100:1:SEEDS:NONE:GET_MATERIAL_FROM_REAGENT:plant:SEED_MAT]
       [SKILL:BREWING]

If you try to brew into a container without enough space (whether because it's too small or it's just out of room), the reaction will consume 0 of your brewing inputs, produce only 1 drink, and no seeds. *\[Needs confirmation: Is it 1* drink *- the full 150 liquid units - or only 1 liquid unit of the drink? Does it try to consume 1/150 for liquids?\]*

\
You can calculate the maximum liquid storage of a container by checking its liquid capacity and dividing it by 600 (not 150). Only full integers count, so round any decimals down.

- Flask: 1800 / 600 = 3; holds 3 drinks
- Jug: 10000 / 600 = 16 2/3; holds 16 drinks

\
Strictly speaking, you don't *have* to have your output go into a *liquid* container. That would make sense, yes, but what if you really want an otterskin backpack full of wine? Just finesse your container reagent to be more or less strict. This example below only looks for empty containers, regardless of what it is.

       [REAGENT:container:1:NONE:NONE:NONE:NONE]
           [EMPTY][PRESERVE_REAGENT]
           [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]
       [PRODUCT:100:5:DRINK:NONE:GET_MATERIAL_FROM_REAGENT:fruit:DRINK_MAT]
           [PRODUCT_TO_CONTAINER:container]
           [PRODUCT_DIMENSION:150]

Do note, however, that, if you're too permissive with what you can brew into (say, a sword), it can have the same problems as trying to brew into too-small containers.

\
Worn containers are always omitted from the selection pool, as are items in them. Held containers are valid receptacles, and items **in** containers (held or on the floor) are usually omitted unless specifically called for in the reaction (like with honey, above).

## Weapon Reactions

### Gemstone Long Sword

Make a long sword out of four rough gemstones of the same type.

    [REACTION:MAKE_GEMSTONE_SWORD_LONG]
    [NAME:make gemstone long sword]
    [BUILDING:SMELTER:NONE]
    [REAGENT:A:4:ROUGH:NO_SUBTYPE:NONE:NONE]
    [PRODUCT:100:1:WEAPON:ITEM_WEAPON_SWORD_LONG:GET_MATERIAL_FROM_REAGENT:A:NONE]
    [FUEL]
    [SKILL:SMELT]

## Misc Item Reactions

### Craft Windows from Shells

Turns shells into a window made from that animal's shell.

    [REACTION:MAKE WINDOW FROM SHELL]
        [NAME:make shell window]
        [BUILDING:CRAFTSMAN:NONE]
        [REAGENT:shell:3:CORPSEPIECE:NO_SUBTYPE:NONE:NONE]
            [ANY_SHELL_MATERIAL]
            [USE_BODY_COMPONENT]
        [PRODUCT:100:1:WINDOW:NO_SUBTYPE:GET_MATERIAL_FROM_REAGENT:shell:NONE]
        [SKILL:BONECARVE]

### Cremate Vermin Remains

Incinerates all those non-rotting vermin remains so they stop cluttering up your hallways.

    [REACTION:CREMATE_REMAINS]
    [NAME:cremate remains]
    [BUILDING:SMELTER:NONE]
    [REAGENT:A:1:REMAINS:NONE:NONE:NONE]
    [PRODUCT:100:1:BAR:NONE:ASH:NONE][PRODUCT_DIMENSION:150]
    [SKILL:SMELT]
    [AUTOMATIC]

Results in 1 bar of ash, and also automatically populates itself in an idle smelter like the loom cloth and tan a hide tasks.

### Create Adamantine Wafers

Creates adamantine wafers, pretty self-explanatory.

    [REACTION:FREE_ADAMANTINE_WAFERS]
    [NAME:create adamantine wafers]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:5:BAR:NO_SUBTYPE:INORGANIC:ADAMANTINE][PRODUCT_DIMENSION:150]
    [SKILL:SMELT]

### Create Adamantine Thread

Again, self-explanatory. Also, trains clothesmaking.

    [REACTION:FREE_ADAMANTINE_THREAD]
    [NAME:create adamantine thread]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:5:THREAD:NO_SUBTYPE:INORGANIC:ADAMANTINE][PRODUCT_DIMENSION:15000]
    [SKILL:CLOTHESMAKING]

### Burning furniture and other wooden objects

The code below lets you burn furniture and other wooden objects at a wood furnace to obtain charcoal. Normally, a new ID is used for a new reaction. The downside of a new reaction is that a map regen is necessary. The example below shows how a reaction ID of a current game (making billon from raw ores) can be used to add a new reaction without having to start over a map.

In the example below, for each piece of wood furniture, 0.25 charcoal is generated. Since custom reactions can't work in the same way as melting metal, 1 bar of charcoal is generated for 4 units of furniture. Since 4 different reagents are used, this does not necessarily need to be 4 beds, but can be 4 diferent wood objects. in the current code, each type of wooden object is elligible, so it is advisable to create an additional wood furnace and link specific stockpiles to this furnace. This allows you to burn low quality items, while preventing your masterpiece beds going up in flames.

the text below replaces the original 'billon making' reaction in data/save/'your save'/raw/objects/reaction_smelter.txt.

    [REACTION:BILLON_MAKING]
    [NAME:burn furniture]
    [BUILDING:WOOD:CUSTOM_B]
    [REAGENT:A:1:NONE:NONE:NONE:NONE][ANY_PLANT_MATERIAL][HARD_ITEM_MATERIAL][EMPTY]
    [REAGENT:B:1:NONE:NONE:NONE:NONE][ANY_PLANT_MATERIAL][HARD_ITEM_MATERIAL][EMPTY]
    [REAGENT:C:1:NONE:NONE:NONE:NONE][ANY_PLANT_MATERIAL][HARD_ITEM_MATERIAL][EMPTY]
    [REAGENT:D:1:NONE:NONE:NONE:NONE][ANY_PLANT_MATERIAL][HARD_ITEM_MATERIAL][EMPTY]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:CHARCOAL][PRODUCT_DIMENSION:150]
    [SKILL:WOOD_BURNING]

\
An important thing to note is that the code above works with all wood items. Turning every single wooden bolt into 0.25 charcoal is considered cheaty, so it is up to the user to use the code appropiately. If the user wants more than 4 units per unit of charcoal for better balance, the number of reagents can easily be expanded.
