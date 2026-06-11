# Rice

> Fonte: [Rice](https://dwarffortresswiki.org/index.php/Rice) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rice plants for their grain.**
- **Seed**
- **/ Rice**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Rice beer
- **Powder:** Rice flour
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Alcohol Flour**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Rice plants** are an aboveground crop. They can either be milled into rice flour, brewed into rice beer or processed in a dyer's shop into buff dye.

Some dwarves like rice plants for their *grain*.

\

Admired for its *grain*.

    [PLANT:RICE] Oryza sativa
        [NAME:rice plant][NAME_PLURAL:rice plants][ADJ:rice plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][WET][BIOME:ANY_TROPICAL]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen rice beer] wiki: sake is a rice beer, and there are also rice wines
            [STATE_NAME_ADJ:LIQUID:rice beer]
            [STATE_NAME_ADJ:GAS:boiling rice beer]
            [STATE_COLOR:ALL:AMBER]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:5:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:rice flour]
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
        [SEED:rice:rice:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:grain]
        [GROWTH:LEAVES]
            [GROWTH_NAME:rice leaf:rice leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [USE_MATERIAL_TEMPLATE:HUSK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:rice husk dye]
            [STATE_COLOR:ALL_SOLID:BUFF]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:BUFF]
            [PREFIX:NONE]
