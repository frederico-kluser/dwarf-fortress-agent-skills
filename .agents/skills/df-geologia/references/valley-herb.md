# Valley herb

> Fonte: [Valley herb](https://dwarffortresswiki.org/index.php/Valley_herb) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes valley herbs for their soothing fragrance.**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Temperate Grassland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Extract:** Golden salve
- **Plant Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food Golden salve production**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\
The **valley herb** is a somewhat hard-to-gather plant, for it grows only in temperate grasslands in spring. It is edible when cooked, but its main use is in producing golden salve. It has no seeds (*in an unmodded/vanilla game, specifically - see the mod below*). This plant can be collected by plant gathering. Unlike most other gathered plants, only a single valley herb will be gathered from a shrub.

Elven and human caravans may offer valley herbs for trade in stacks of 5, assuming their nations have access to the proper biome; this large stack size makes them ideal for processing into golden salve, as a single stack will yield a trade good worth 2,500☼ (plus vial value).

- Plant value: 10
- Extract value: 100
- Seasons: Spring

Some dwarves like valley herbs for their *tiny leaves* and their *soothing fragrance*.

Pieces of valley herb.

\

## Seed mod

This is a simple mod to add valley herb seeds (**originally produced for ASCII mode, as it were - premium graphics may cause it to not work as intended**) :

            [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
                    [MATERIAL_VALUE:10]
                    [EDIBLE_COOKED]
            [SEED:valley herb seed:valley herb seeds:2:4:1:LOCAL_PLANT_MAT:SEED]
            [SELECT_MATERIAL:STRUCTURAL]
                    [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]

    [PLANT:HERB_VALLEY]
        [NAME:valley herb][NAME_PLURAL:valley herbs][ADJ:valley herb]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:5]
            [EDIBLE_COOKED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:152][PICKED_COLOR:2:0:1]
        [DRY][BIOME:GRASSLAND_TEMPERATE]
        [VALUE:5]
        [USE_MATERIAL_TEMPLATE:EXTRACT:PLANT_EXTRACT_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen golden salve]
            [STATE_NAME_ADJ:LIQUID:golden salve]
            [STATE_NAME_ADJ:GAS:boiling golden salve]
            [MATERIAL_VALUE:100]
            [DISPLAY_COLOR:6:0:1]
            [EXTRACT_STORAGE:FLASK]
            [PREFIX:NONE]
        [EXTRACT_VIAL:LOCAL_PLANT_MAT:EXTRACT]
        [SPRING]
        [FREQUENCY:5]
        [CLUSTERSIZE:1]
        [PREFSTRING:tiny leaves]
        [PREFSTRING:soothing fragrance]
