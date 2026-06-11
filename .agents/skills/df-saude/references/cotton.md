# Cotton

> Fonte: [Cotton](https://dwarffortresswiki.org/index.php/Cotton) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cotton plants for their flowers.**
- **Seed**
- **/ Cotton seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Oil:** Cottonseed oil
- **Paper:** Cotton paper
- **Processed to:** Thread
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Uses**
- **Oil Thread**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cotton** is an aboveground crop. Once harvested, cotton plants may be processed at a farmer's workshop to produce cotton plant fiber thread.

Cotton seeds can be milled into paste at a quern or millstone (like rock nuts, the seeds of the quarry bush), which in turn can be pressed into cotton seed oil and a press cake at a screw press.

Cotton is not to be confused with cottongrass. While cotton is a harvestable crop, cottongrass is a groundcover grass.

Some dwarves like cotton plants for their *flowers*.

\

Admired for its *flowers*.

|  |
|----|
| "Cotton" in other / Languages / Dwarven / : / îkeng / Elven / : / ethe / Goblin / : / ongu / Human / : / thixil |

    [PLANT:COTTON] Gossypium hirsutum / sp.
        [NAME:cotton plant][NAME_PLURAL:cotton plants][ADJ:cotton plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:PRESS_PAPER_MAT:LOCAL_PLANT_MAT:THREAD]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:ANY_TROPICAL]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:OIL:PLANT_OIL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen cottonseed oil]
            [STATE_NAME_ADJ:LIQUID:cottonseed oil]
            [STATE_NAME_ADJ:GAS:boiling cottonseed oil]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
            [EDIBLE_COOKED]
        [USE_MATERIAL_TEMPLATE:SOAP:PLANT_SOAP_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:cottonseed oil soap]
            [STATE_NAME_ADJ:LIQUID:melted cottonseed oil soap]
            [STATE_NAME_ADJ:GAS:n/a]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL_SOLID:CREAM]
            [DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:cotton seed]
            [STATE_NAME_ADJ:SOLID_PASTE:cotton seed paste]
            [STATE_NAME_ADJ:SOLID_PRESSED:cotton seed press cake]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:PRESS_LIQUID_MAT:LOCAL_PLANT_MAT:OIL]
            [PREFIX:NONE]
            [STOCKPILE_GLOB_PASTE]
            [STOCKPILE_GLOB_PRESSED]
        [SEED:cotton seed:cotton seeds:7:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:flowers]
        [USE_MATERIAL_TEMPLATE:THREAD:THREAD_PLANT_TEMPLATE] *** should be around seed
            [STATE_NAME_ADJ:SOLID:cotton]
            [STATE_NAME_ADJ:SOLID_PASTE:cotton slurry]
            [STATE_NAME_ADJ:SOLID_PRESSED:cotton paper]
            [PREFIX:NONE]
            [MATERIAL_VALUE:2]
            [REACTION_CLASS:PAPER_SLURRY]
            [STOCKPILE_GLOB_PASTE]
        [THREAD:LOCAL_PLANT_MAT:THREAD]
        [GROWTH:LEAVES]
            [GROWTH_NAME:cotton leaf:cotton leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:cotton flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
