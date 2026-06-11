# Hemp

> Fonte: [Hemp](https://dwarffortresswiki.org/index.php/Hemp) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hemp plants for their leaves.**
- **Seed**
- **/ Hemp seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Oil:** Hempseed oil
- **Paper:** Hemp paper
- **Powder:** Hemp flour
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

**Hemp** is a highly versatile aboveground crop that supports the food, textile, paper and soap industries. The plants can be processed at a farmer's workshop to produce hemp plant fiber thread, and can also be milled into flour or slurry, the latter of which can be pressed into sheets.

Hemp seeds can be milled into paste at a quern or millstone, which in turn can be pressed into hempseed oil and a press cake at a screw press. Hemp and flax are the only millable plants that can be stored in containers made from their own fibers.

\
Some dwarves like hemp plants for their *leaves*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
For some reason, humans are particularly secretive about their hemp farms, especially when their nobles are around. As dwarven brokers have reported, humans consider milled hemp a highly valued good, though no dwarf knows why.

\

Admired for its *leaves*.

    [PLANT:HEMP] cannabis sativa
        [NAME:hemp plant][NAME_PLURAL:hemp plants][ADJ:hemp plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:PRESS_PAPER_MAT:LOCAL_PLANT_MAT:THREAD]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:ANY_TEMPERATE]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:OIL:PLANT_OIL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen hempseed oil]
            [STATE_NAME_ADJ:LIQUID:hempseed oil]
            [STATE_NAME_ADJ:GAS:boiling hempseed oil]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
            [EDIBLE_COOKED]
        [USE_MATERIAL_TEMPLATE:SOAP:PLANT_SOAP_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:hempseed oil soap]
            [STATE_NAME_ADJ:LIQUID:melted hempseed oil soap]
            [STATE_NAME_ADJ:GAS:n/a]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:hemp flour]
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
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:hemp seed]
            [STATE_NAME_ADJ:SOLID_PASTE:hemp seed paste]
            [STATE_NAME_ADJ:SOLID_PRESSED:hemp seed press cake]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:PRESS_LIQUID_MAT:LOCAL_PLANT_MAT:OIL]
            [PREFIX:NONE]
            [STOCKPILE_GLOB_PASTE]
            [STOCKPILE_GLOB_PRESSED]
        [SEED:hemp seed:hemp seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:leaves]
        [USE_MATERIAL_TEMPLATE:THREAD:THREAD_PLANT_TEMPLATE]
            [STATE_NAME_ADJ:SOLID:hemp]
            [STATE_NAME_ADJ:SOLID_PASTE:hemp slurry]
            [STATE_NAME_ADJ:SOLID_PRESSED:hemp paper]
            [PREFIX:NONE]
            [MATERIAL_VALUE:2]
            [REACTION_CLASS:PAPER_SLURRY]
            [STOCKPILE_GLOB_PASTE]
        [THREAD:LOCAL_PLANT_MAT:THREAD]
        [GROWTH:LEAVES]
            [GROWTH_NAME:hemp leaf:hemp leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
