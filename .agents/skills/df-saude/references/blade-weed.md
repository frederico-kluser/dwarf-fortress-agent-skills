# Blade weed

> Fonte: [Blade weed](https://dwarffortresswiki.org/index.php/Blade_weed) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes blade weed for their stiff, triangular leaves.**
- **Seed**
- **/ Blade weed seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Powder:** Emerald dye
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Dye**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Blade weed** is a plant used only to make emerald dye at a mill or quern. They can be planted outdoors any time of year and can be collected by gathering plants in any dry, non-freezing biome.

- Grow time: 300
- Plant value: 2
- Mill value: 20
- Dye color: Emerald
- Seasons: All

Some dwarves like blade weed for their *stiff, triangular leaves*.

## See Also

- List of crops
- Textile industry

|  |
|----|
| "Blade weed" in other / Languages / Dwarven / : / tarmid koshmot / Elven / : / eli mibi / Goblin / : / roz spålu / Human / : / ushav thish |

    [PLANT:WEED_BLADE]
        [NAME:blade weed][NAME_PLURAL:blade weed][ADJ:blade weed]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:231][PICKED_COLOR:2:0:0]
        [DRY][BIOME:NOT_FREEZING]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:emerald dye]
            [STATE_COLOR:ALL_SOLID:EMERALD]
            [DISPLAY_COLOR:2:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:EMERALD]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:25]
        [CLUSTERSIZE:5]
        [PREFSTRING:stiff, triangular leaves]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:blade weed seed:blade weed seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
