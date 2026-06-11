# Quarry bush

> Fonte: [Quarry bush](https://dwarffortresswiki.org/index.php/Quarry_bush) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes quarry bushes for their gray leaves.**
- **Seed**
- **/ Rock nuts**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Underground Depth: 1-3**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Leaf:** Quarry bush leaf
- **Oil:** Rock nut oil
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Leaf Properties**
- **Edible:** No
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **quarry bush** is one of the six known subterranean crops, and as such, it may only be grown underground, but can be planted in spring, summer and autumn.

Harvesting a grown quarry bush will yield several leaves, and an equal amount of quarry bush *plants*, which may be processed into yet more leaves at a farmer's workshop by selecting the Process plant to bag work order. You will need an empty bag available for this task. This will result in bags of quarry bush leaves, which then must be cooked in the kitchen to be edible. Quarry bushes cannot be brewed into alcohol.

Processing quarry bushes at a farmer's workshop requires one bag, and will produce 5 quarry bush leaves (and one rock nut) for every plant in a given stack of quarry bushes. Unlike, say, flour, quarry bush leaves do not *need* to stay in bags, but your dwarves will not usually take them out without micro-management (exception: leaves will be removed if taken for cooking while still in a farmer's workshop).

It is also possible to use the generic "process plants" job (which does not require a bag) on quarry bushes, but this will only yield **one** leaf per plant; as such, this should be avoided whenever possible.

Cooking quarry bush leaves can result in very large stacks of prepared food, thus saving space and barrels. In a fortress that relies on selling large, expensive stacks of prepared food, quarry bush leaves are great filler: a lavish meal made from whip wine and dwarven cheese with two stacks of quarry bush leaves for filler, is worth almost ten times more than an easy meal made from wine and cheese alone.

Some dwarves like quarry bushes for their *gray leaves*.

## Rock nuts

Quarry bush seeds are known as **rock nuts**. Although their material definition marks them as being edible raw, dwarves will **not** eat them.

Rock nuts can be milled at a millstone or quern into rock nut paste, using the s job to mill seeds/nuts to paste. This paste can then be used in cooking, or pressed at a screw press into a rock nut press cake and a jug of rock nut oil.

Both the rock nut paste and rock nut press cake are cookable and considered a single food category, referred to as "rock nut" in the Kitchen tab in the Labor menu y (not to be confused with "rock nuts", the entry for the seeds), the Stocks screen compacted view, and Prepared meal descriptions.

The rock nut oil can be cooked or used in place of tallow to make soap.

Use moderation when commanding rock nuts to be converted to paste - the nuts are required to re-plant the crop; if you grind up your entire supplies, you can't grow new quarry bushes.

The main attraction of grinding up rock nuts is the production of rock nut oil as a soapmaking ingredient. Both the globs of paste and the press cakes are minimum-value cooking ingredients, at 1☼ each. When looking at cooking ingredients, the quarry bush leaves completely overshadow what can be gained from an oil-pressing operation. However, if you have a surplus of rock nuts such that you could never plant them all at once, it makes sense to use them for something productive.

## Plant Gathering

Like with any plant growth, a wild quarry bush plant growing underground (not planted) will yield exactly *one* leaf when gathered, plus the usual random amount of quarry bushes, which can be processed into more leaves as usual.

## Food Value

Thanks to the increased value of rock nut oil as a by-product of rock nut processing, the highest potential value of products gleaned from one quarry bush plant is 66 (six leaves at a value of 10 each, plus oil and a press cake).

- Grow time: 500
- Plant value: 2
- Spice value: 10(x6)
- Seed value: 1
- Mill value: 1
- Press cake value: 1
- Press oil value: 5

## Trivia

Quarry bush seeds are refered to as rock nuts, despite the fact that nuts are a type of fruit, not seed.

    [PLANT:BUSH_QUARRY]
        [NAME:quarry bush][NAME_PLURAL:quarry bushes][ADJ:quarry bush]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [ITEM_REACTION_PRODUCT:BAG_ITEM:PLANT_GROWTH:LEAVES:LOCAL_PLANT_MAT:LEAF]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:5][PICKED_COLOR:7:0:0]
        [GROWDUR:500][VALUE:2]
        [USE_MATERIAL_TEMPLATE:OIL:PLANT_OIL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen rock nut oil]
            [STATE_NAME_ADJ:LIQUID:rock nut oil]
            [STATE_NAME_ADJ:GAS:boiling rock nut oil]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
            [EDIBLE_COOKED]
        [USE_MATERIAL_TEMPLATE:SOAP:PLANT_SOAP_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:rock nut soap]
            [STATE_NAME_ADJ:LIQUID:melted rock nut soap]
            [STATE_NAME_ADJ:GAS:n/a]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [MATERIAL_VALUE:5]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:rock nut]
            [STATE_NAME_ADJ:SOLID_PASTE:rock nut paste]
            [STATE_NAME_ADJ:SOLID_PRESSED:rock nut press cake]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:PRESS_LIQUID_MAT:LOCAL_PLANT_MAT:OIL]
            [PREFIX:NONE]
            [STOCKPILE_GLOB_PASTE]
            [STOCKPILE_GLOB_PRESSED]
        [SEED:rock nut:rock nuts:7:0:1:LOCAL_PLANT_MAT:SEED]
        [SPRING][SUMMER][AUTUMN]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:gray leaves]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:3]
        [SHRUB_TILE:58]
        [DEAD_SHRUB_TILE:58]
        [SHRUB_COLOR:7:0:0]
        [DEAD_SHRUB_COLOR:0:0:1]
        [GROWTH:LEAVES]
            [GROWTH_NAME:quarry bush leaf:quarry bush leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:7:0:0:NONE]
