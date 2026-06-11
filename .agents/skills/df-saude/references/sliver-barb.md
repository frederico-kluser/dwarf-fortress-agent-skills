# Sliver barb

> Fonte: [Sliver barb](https://dwarffortresswiki.org/index.php/Sliver_barb) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sliver barbs for their wicked thorns.**
- **Seed**
- **/ Sliver barb seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Alignment**
- **Evil**
- **Products**
- **Alcohol:** Gutter cruor
- **Powder:** Sliver dye
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Dye Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Sliver barb** is an aboveground crop that can be brewed into **gutter cruor**, a low-value alcohol, or milled into black sliver dye, a high-value dye. It only grows in evil areas - since human and elven civilizations never live in these areas, your trading partners won't have seeds for it. To get this plant, your dwarves will need to brave the evil weather and pull it from the earth themselves.

Some dwarves like sliver barbs for their *wicked thorns*.

Sliver barb found in the wild (Steam version).

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Dwarves tend to be surprised at the fact that they appear more gray than silver. This may be due to misreading the name while drunk. The plant is thorny and rhymes with "liver".

There have been reports of dungeon masters mandating export bans on sliver barbs due to them apparently being "way too strong for a 1st-level plant", whatever that means. However, these stories are obviously false because dungeon masters can't make mandates.

|  |
|----|
| "Sliver barb" in other / Languages / Dwarven / : / rasuk robek / Elven / : / rili úpe / Goblin / : / uz tuxxu / Human / : / ápiv zomuth |

    [PLANT:SLIVER_BARB]
        [NAME:sliver barb][NAME_PLURAL:sliver barbs][ADJ:sliver barb]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:1]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:231][PICKED_COLOR:0:0:1]
        [DRY][EVIL][BIOME:NOT_FREEZING]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen gutter cruor]
            [STATE_NAME_ADJ:LIQUID:gutter cruor]
            [STATE_NAME_ADJ:GAS:boiling gutter cruor]
            [STATE_COLOR:ALL:MAROON]
            [MATERIAL_VALUE:1]
            [DISPLAY_COLOR:4:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:sliver dye]
            [STATE_COLOR:ALL_SOLID:BLACK]
            [DISPLAY_COLOR:0:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:BLACK]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:wicked thorns]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:sliver barb seed:sliver barb seeds:4:0:1:LOCAL_PLANT_MAT:SEED]
