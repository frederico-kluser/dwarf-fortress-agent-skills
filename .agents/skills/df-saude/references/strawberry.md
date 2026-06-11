# Strawberry

> Fonte: [Strawberry](https://dwarffortresswiki.org/index.php/Strawberry) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes strawberry plants for their vivid red color.**
- **Seed**
- **Strawberry seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Strawberry wine
- **Fruit:** Strawberry
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Strawberries** are an above-ground crop. They can be gathered nearly anywhere, and are common items when trading with non-dwarven caravans. The plant can be eaten raw, cooked, or processed into fruit. The fruit can then be eaten raw, cooked, or brewed into strawberry wine. They are much like an above-ground version of plump helmets, having the same value and uses. Keep in mind that they must be brewed from the Brew Drink From Fruit task, rather than the Brew Drink From Plant task.

Strawberry crops are one of the few crops with multiple usable products: harvesting a strawberry crop will yield *strawberry plant*, a plant used in cooking, and processing a *strawberry plant* will yield *strawberry seeds* as well as *strawberry* fruit, which can be cooked or brewed. As always, cooking a strawberry plant does not yield seeds, and despite this, they are enabled for use in cooking by default. This is a great way to accidentally run out of seeds, although it is easy to obtain more by gathering them in the wild. Brewing with strawberries does yield seeds.

Strawberries can be planted and harvested in farm plots year-round.

Strawberries are stored in spice barrels/pots.

Some dwarves like strawberries for their *vivid red color*.

Admired for its *vivid red color*.

|  |
|----|
| "Strawberry" in other / Languages / Dwarven / : / atith-lisig / Elven / : / aÿife-ada / Goblin / : / slatspu-smug / Human / : / pak-tikbo |

    [PLANT:BERRIES_STRAW]
        [NAME:strawberry plant][NAME_PLURAL:strawberry plants][ADJ:strawberry plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
            [STOCKPILE_PLANT_GROWTH]
        [PICKED_TILE:58][PICKED_COLOR:4:0:0]
        [DRY][BIOME:NOT_FREEZING]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen strawberry wine]
            [STATE_NAME_ADJ:LIQUID:strawberry wine]
            [STATE_NAME_ADJ:GAS:boiling strawberry wine]
            [STATE_COLOR:ALL:PINK]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:5:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:strawberry seed:strawberry seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:vivid red color]
        [GROWTH:FRUIT]
            [GROWTH_NAME:strawberry:strawberries]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':7:4:0:1:120000:200000:3]
