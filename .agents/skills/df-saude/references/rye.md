# Rye

> Fonte: [Rye](https://dwarffortresswiki.org/index.php/Rye) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rye for their beer.**
- **Seed**
- **/ Rye seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Rye beer
- **Powder:** Rye flour
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Alcohol Flour**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Rye** is an aboveground crop. It can either be milled into rye flour or brewed into rye beer.

Some dwarves like rye for its *beer*.

\

Admired for its *beer*.

    [PLANT:RYE] Secale cereale
        [NAME:rye][NAME_PLURAL:rye][ADJ:rye]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:NOT_FREEZING]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen rye beer]
            [STATE_NAME_ADJ:LIQUID:rye beer]
            [STATE_NAME_ADJ:GAS:boiling rye beer]
            [STATE_COLOR:ALL:AMBER]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:rye flour]
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
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:rye seed:rye seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:beer]
        [GROWTH:LEAVES]
            [GROWTH_NAME:rye leaf:rye leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
