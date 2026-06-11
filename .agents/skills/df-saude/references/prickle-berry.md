# Prickle berry

> Fonte: [Prickle berry](https://dwarffortresswiki.org/index.php/Prickle_berry) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes prickle berries for their precise thorns.**
- **Seed**
- **/ Prickle berry seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Prickle berry wine
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Prickle berry** is an inferior aboveground crop, similar in that way to rat weed. It can be eaten, cooked, or brewed into prickle berry wine. However, it is not as prized (or valuable) as any of the underground crops.

Some dwarves like prickle berries for their *precise thorns*.

    [PLANT:BERRIES_PRICKLE]
        [NAME:prickle berry][NAME_PLURAL:prickle berries][ADJ:prickle berry]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:0]
        [DRY][BIOME:NOT_FREEZING]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen prickle berry wine]
            [STATE_NAME_ADJ:LIQUID:prickle berry wine]
            [STATE_NAME_ADJ:GAS:boiling prickle berry wine]
            [STATE_COLOR:ALL:DARK_OLIVE]
            [MATERIAL_VALUE:1]
            [DISPLAY_COLOR:2:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:prickle berry seed:prickle berry seeds:2:0:0:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:precise thorns]
