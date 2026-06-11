# Rhubarb

> Fonte: [Rhubarb](https://dwarffortresswiki.org/index.php/Rhubarb) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rhubarbs for their taste.**
- **Seed**
- **/ Rhubarb seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Leaf:** Rhubarb leaf
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Leaf Properties**
- **Edible:** No
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Rhubarb** is an aboveground garden plant. They can be planted in all seasons and is edible raw or cooked. Leaves can be processed in a dyer's shop into tan dye.

**Don't try this at home!** In real life, rhubarb leaves are toxic. The edible parts of the rhubarb are actually its *petioles*, or leaf stalks.

Some dwarves like rhubarbs for their *taste*.

\

Admired for its *taste*.

    [PLANT:RHUBARB] rheum rhabarbarum
        [NAME:rhubarb][NAME_PLURAL:rhubarbs][ADJ:rhubarb]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE] leaf stalk
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        *** root should give brown dye
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:0]
        [DRY][BIOME:ANY_TEMPERATE]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:ROSE]
            [DISPLAY_COLOR:4:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:rhubarb seed:rhubarb seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:taste]
        [GROWTH:LEAVES]
            [GROWTH_NAME:rhubarb leaf:rhubarb leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:rhubarb inflorescence:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:4:0:1:60000:119999:2]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:rhubarb leaf dye]
            [STATE_COLOR:ALL_SOLID:TAN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:TAN]
            [PREFIX:NONE]
