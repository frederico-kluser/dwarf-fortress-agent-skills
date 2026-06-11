# Still

> Fonte: [Still](https://dwarffortresswiki.org/index.php/Still) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Shortcut : b - o - f - l**
- **÷ ═ ╕ o ~ ~ o**
- **Icon**
- **Job Requirement**
- **Brewer**
- **Construction**
- **Materials:** Labors
- **Building material (non- economic ):** Brewing or Plant gathering
- **Materials Used**
- **Barrel Watertight large pot Brewable plant Honey Kobold bulb Vial**
- **Goods Created**
- **Alcohol Gnomeblight**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **still** is the source of all home-made alcohol for a fort and is an essential workshop for any fortress. A still also allows dwarves to extract gnomeblight from kobold bulbs into a glass vial. A dwarf must have the brewer labor activated in order to use a still.

The four tasks available at a still are:

- Extract from Plants
- Brew drink from plant
- Brew drink from fruit
- Make mead

Brewing alcohol requires an available empty barrel or large pot and something to brew, either a brewable plant, fruit, or honey. You may set specific plants and fruits to be used or not used through the y Labor menu in Kitchen tab. Note that you are unable to set honey bee honey to be brewed or not brewed, because making mead is a different task than brewing.

Every unit of plant, fruit, or honey brewed at a still produces 5 units of alcohol. A single stack of plants will be brewed for each task, and the resulting booze will be placed into a single barrel - a stack of *Plump helmet \[5\]* will produce *Dwarven wine \[25\]* and will only occupy a single barrel. Skilled growers, who tend to plant seeds more skillfully and produce larger stacks, can therefore reduce the number of barrels required to store alcohol, which in turn minimizes the required stockpile size. Brewing produces seeds from ingredients that have seeds if the number of those seeds in the fortress is less than the per-plant limit of 200 (this number can be modified in the settings).

    [REACTION:BREW_DRINK_FROM_PLANT]
        [NAME:brew drink from plant]
        [BUILDING:STILL:HOTKEY_STILL_BREW]
        [REAGENT:plant:1:PLANT:NONE:NONE:NONE]
            [HAS_MATERIAL_REACTION_PRODUCT:DRINK_MAT]
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

    [REACTION:BREW_DRINK_FROM_PLANT_GROWTH]
        [NAME:brew drink from fruit]
        [BUILDING:STILL:CUSTOM_F]
        [REAGENT:plant:1:PLANT_GROWTH:NONE:NONE:NONE]
            [HAS_MATERIAL_REACTION_PRODUCT:DRINK_MAT]
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

    [REACTION:MAKE_MEAD]
        [NAME:make mead]
        [BUILDING:STILL:CUSTOM_M]
        [REAGENT:honey:150:LIQUID_MISC:NONE:CREATURE_MAT:HONEY_BEE:HONEY]
            [UNROTTEN]
        [REAGENT:honey container:1:NONE:NONE:NONE:NONE]
            [CONTAINS:honey]
            [PRESERVE_REAGENT]
            [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]
        [REAGENT:barrel/pot:1:NONE:NONE:NONE:NONE]
            [EMPTY]
            [FOOD_STORAGE_CONTAINER] barrel or any non-absorbing tool with FOOD_STORAGE
            [PRESERVE_REAGENT]
            [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]
        [PRODUCT:100:5:DRINK:NONE:GET_MATERIAL_FROM_REAGENT:honey:DRINK_MAT]
            [PRODUCT_TO_CONTAINER:barrel/pot]
            [PRODUCT_DIMENSION:150]
        [SKILL:BREWING]
