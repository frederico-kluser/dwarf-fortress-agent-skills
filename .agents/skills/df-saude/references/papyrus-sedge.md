# Papyrus sedge

> Fonte: [Papyrus sedge](https://dwarffortresswiki.org/index.php/Papyrus_sedge) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes papyrus sedges for their useful stems.**
- **Seed**
- **/ Papyrus seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Tropical Wetland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Papyrus**
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Paper industry**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Papyrus sedge** is an aboveground crop. It can be used to make paper sheets at a farmer's workshop without the need to be milled into a slurry first.v0.42.01 Otherwise, it's useless – it's neither edible, millable, nor cookable.

Some dwarves like papyrus sedges for their *useful stems*.

## Technical information

Papyrus sedge plants use the `[REACTION_CLASS:PAPER_PLANT]` class to allow them to be turned directly from plants to paper.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Despite the insistence of some human children, papyrus sedge plants are not involved in the production of "spaghetti" (whatever that is), nor do they bear any relation to dwarf skeletons or cave fish women.

Admired for its *useful stems*.

    [PLANT:PAPYRUS_SEDGE] Cyperus papyrus
        [NAME:papyrus sedge][NAME_PLURAL:papyrus sedges][ADJ:papyrus sedge]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [STATE_NAME_ADJ:SOLID:papyrus]
            [STATE_NAME_ADJ:SOLID_PRESSED:papyrus]
            [PREFIX:NONE]
            [REACTION_CLASS:PAPER_PLANT]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:ANY_TROPICAL_WETLAND]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL_SOLID:BROWN]
            [DISPLAY_COLOR:6:0:0]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:papyrus seed:papyrus seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:useful stems]
        [GROWTH:LEAVES]
            [GROWTH_NAME:papyrus leaf:papyrus leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:papyrus flower cluster:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:0:60000:119999:2]
