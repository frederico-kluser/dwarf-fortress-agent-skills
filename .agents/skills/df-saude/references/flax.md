# Flax

> Fonte: [Flax](https://dwarffortresswiki.org/index.php/Flax) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes flax plants for their flowers.**
- **Seed**
- **/ Flax seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Tropical Grassland Tropical Savanna**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Oil:** Linseed oil
- **Paper:** Linen paper
- **Powder:** Flax flour
- **Processed to:** Thread
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Uses**
- **Flour Oil Thread**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Flax** is an aboveground crop that may be processed into thread at the farmer's workshop or milled into flax flour.

**Flax seeds** can be eaten raw, or milled into paste at a quern or millstone, which in turn can be pressed into linseed oil and a press cake at a screw press.

Flax and hemp are the only millable plants that can be stored in containers made from their own fibers.

Some dwarves like flax plants for their *flowers*.

\

Admired for its *flowers*.

|  |
|----|
| "Flax" in other / Languages / Dwarven / : / engig / Elven / : / quithe / Goblin / : / nonû / Human / : / cegad |

    [PLANT:FLAX] Linum usitatissimum
        [NAME:flax plant][NAME_PLURAL:flax plants][ADJ:flax plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE] *** sprouts edible
            [MATERIAL_REACTION_PRODUCT:PRESS_PAPER_MAT:LOCAL_PLANT_MAT:THREAD]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:GRASSLAND_TROPICAL][BIOME:SAVANNA_TROPICAL]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:OIL:PLANT_OIL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen linseed oil]
            [STATE_NAME_ADJ:LIQUID:linseed oil]
            [STATE_NAME_ADJ:GAS:boiling linseed oil]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
            [EDIBLE_COOKED]
        [USE_MATERIAL_TEMPLATE:SOAP:PLANT_SOAP_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:linseed oil soap]
            [STATE_NAME_ADJ:LIQUID:melted linseed oil soap]
            [STATE_NAME_ADJ:GAS:n/a]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:flax flour]
            [STATE_COLOR:ALL_SOLID:WHITE]
            [DISPLAY_COLOR:7:0:1]
            [MATERIAL_VALUE:20]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL_SOLID:PALE_BLUE]
            [DISPLAY_COLOR:1:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:flax seed]
            [STATE_NAME_ADJ:SOLID_PASTE:flax seed paste]
            [STATE_NAME_ADJ:SOLID_PRESSED:flax seed press cake]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:PRESS_LIQUID_MAT:LOCAL_PLANT_MAT:OIL]
            [PREFIX:NONE]
            [STOCKPILE_GLOB_PASTE]
            [STOCKPILE_GLOB_PRESSED]
        [SEED:flax seed:flax seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:flowers]
        [USE_MATERIAL_TEMPLATE:THREAD:THREAD_PLANT_TEMPLATE]
            [STATE_NAME_ADJ:SOLID:linen]
            [STATE_NAME_ADJ:SOLID_PASTE:linen slurry]
            [STATE_NAME_ADJ:SOLID_PRESSED:linen paper]
            [PREFIX:NONE]
            [MATERIAL_VALUE:2]
            [REACTION_CLASS:PAPER_SLURRY]
            [STOCKPILE_GLOB_PASTE]
        [THREAD:LOCAL_PLANT_MAT:THREAD]
        [GROWTH:LEAVES]
            [GROWTH_NAME:flax leaf:flax leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:flax flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:1:0:1:60000:119999:2]
