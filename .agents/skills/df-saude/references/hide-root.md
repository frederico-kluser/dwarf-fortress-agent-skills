# Hide root

> Fonte: [Hide root](https://dwarffortresswiki.org/index.php/Hide_root) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hide root for their fuzzy projections.**
- **Seed**
- **/ Hide root seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Powder:** Redroot dye
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Dye**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Hide root** is an above ground crop. It can be acquired by harvesting or by trading. It is milled into redroot dye in order to dye cloth and thread.

Actual redroot dye is brown in color; presumably, this is a bug, since there *are* rolls of red cloth in the clothier's shop sprite, and Redroot Dye is the only dye to where its powder state color, Brown, is different from the name of its dye: Red. Unfortunately, this means that when applied, it will make any cloth or silk look identical to undyed leather, and tends to make it difficult to tell what is and isn't dyed at a glance. Depending on how you feel about that, you may want to avoid using redroot dye at all without a mod that changes this.

- Grow time: 300
- Plant value: 1
- Mill value: 10
- Dye color: Red
- Seasons: All

## Gallery

-

  From top to bottom: a leather hood, a redroot dyed sheep wool hood, and a basic sheep wool hood with no dye. Redroot dye's color is literally identical to leather.

Some dwarves like hide root for their *fuzzy projections*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Since redroot dye's value is *half* that of all other dyes, it is rumored that 'hide' is short for 'hideous'.

|  |
|----|
| "Hide root" in other / Languages / Dwarven / : / sebïr odur / Elven / : / cóce nemo / Goblin / : / obruk lobok / Human / : / rakbin tegism |

    [PLANT:ROOT_HIDE]
        [NAME:hide root][NAME_PLURAL:hide root][ADJ:hide root]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:1]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:231][PICKED_COLOR:6:0:0]
        [DRY][BIOME:NOT_FREEZING]
        [VALUE:1]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:redroot dye]
            [STATE_COLOR:ALL_SOLID:BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:10]
            [POWDER_DYE:RED]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:fuzzy projections]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:hide root seed:hide root seeds:4:0:0:LOCAL_PLANT_MAT:SEED]
