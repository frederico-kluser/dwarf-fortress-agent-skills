# Sun berry

> Fonte: [Sun berry](https://dwarffortresswiki.org/index.php/Sun_berry) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sun berries for their inner light.**
- **Seed**
- **/ Sun berry seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Alignment**
- **Good**
- **Products**
- **Alcohol:** Sunshine
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Sun berries** are an aboveground plant found naturally growing only in good areas, and only next to natural water sources. They are most numerous upon an embark start in good wetlands of any salinity. Sun berries have a high value and can be brewed into sunshine, the highest-value alcohol in *Dwarf Fortress*. While high value does not increase the chance of a dwarf having a happy thought, it may increase the effect of such a thought. Caravans that travel to your fortress from good areas may bring stacks of sun berries or bags of seeds for trade; this can allow you to set up a sun berry farm anywhere outdoor crops will grow, as long as you are in an adequate biome. Note that despite being described as a "berry," sun berries are considered plants and not fruits, and must be brewed from the "Brew Drink from Plant" task, rather than "Brew Drink from Fruit."

Some dwarves like sun berries for their *inner light*.

Better in liquid form.

|  |
|----|
| "Sun berry" in other / Languages / Dwarven / : / ad lisig / Elven / : / amiÿa ada / Goblin / : / xogak smug / Human / : / sáthra tikbo |

    [PLANT:BERRY_SUN]
        [NAME:sun berry][NAME_PLURAL:sun berries][ADJ:sun berry]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:3]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:6:0:1]
        [WET][GOOD][BIOME:NOT_FREEZING]
        [VALUE:3]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen sunshine]
            [STATE_NAME_ADJ:LIQUID:sunshine]
            [STATE_NAME_ADJ:GAS:boiling sunshine]
            [STATE_COLOR:ALL:YELLOW]
            [MATERIAL_VALUE:5]
            [DISPLAY_COLOR:6:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:inner light]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:sun berry seed:sun berry seeds:4:0:1:LOCAL_PLANT_MAT:SEED]
