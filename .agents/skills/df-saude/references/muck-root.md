# Muck root

> Fonte: [Muck root](https://dwarffortresswiki.org/index.php/Muck_root) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes muck roots for their twisting shape.**
- **Seed**
- **/ Muck root seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Wetland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Swamp whiskey
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Muck root** is an aboveground crop. It can be eaten raw, cooked, or brewed into swamp whiskey. However, it is not as delicious as any of the underground crops. Muck root has seeds and can be farmed, and it takes about 25 days to grow.

Some dwarves like muck roots for their *twisting shape*.

|  |
|----|
| "Muck root" in other / Languages / Dwarven / : / zagstok odur / Elven / : / corowa nemo / Goblin / : / nokast lobok / Human / : / juwog tegism |

    [PLANT:ROOT_MUCK]
        [NAME:muck root][NAME_PLURAL:muck roots][ADJ:muck root]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:231][PICKED_COLOR:0:0:1]
        [WET][BIOME:ANY_WETLAND]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen swamp whiskey]
            [STATE_NAME_ADJ:LIQUID:swamp whiskey]
            [STATE_NAME_ADJ:GAS:boiling swamp whiskey]
            [STATE_COLOR:ALL:RUSSET]
            [MATERIAL_VALUE:1]
            [DISPLAY_COLOR:0:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:muck root seed:muck root seeds:6:0:0:LOCAL_PLANT_MAT:SEED]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:twisting shape]
