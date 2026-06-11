# Grasshopper

> Fonte: [Grasshopper](https://dwarffortresswiki.org/index.php/Grasshopper) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes grasshoppers for their chirping.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Grasshopper - Grasshopper man - Giant grasshopper**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny insect which uses its powerful legs to leap and make noise.*

**Grasshoppers** are a species of unremarkable above ground vermin who may be found in any non-freezing biome, being caught by using the catch live land animal task.

Some dwarves like grasshoppers for their *chirping* and their *great leaps*.

|  |
|----|
| "Grasshopper" in other / Languages / Dwarven / : / isin-ikus / Elven / : / enena-ayefi / Goblin / : / struxe-angnu / Human / : / kege-buh |

Admired for its *chirping*.

    1 kph

    Grasshoppers were sponsored by the generous contributions of the Bay 12 community.

        Bernard Suits

    [CREATURE:GRASSHOPPER]
        [DESCRIPTION:A tiny insect which uses its powerful legs to leap and make noise.]
        [NAME:grasshopper:grasshoppers:grasshopper]
        [CASTE_NAME:grasshopper:grasshoppers:grasshopper]
        [CREATURE_TILE:250][COLOR:2:0:1]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_GROUNDER][FREQUENCY:100]
        [UBIQUITOUS]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [PREFSTRING:chirping]
        [PREFSTRING:great leaps]
        [BENIGN][ALL_ACTIVE]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [NOBONES]
        [BODY:INSECT:2EYES:HEART:GUTS:BRAIN:MOUTH:2WINGS]
        [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
        [BODY_DETAIL_PLAN:CHITIN_TISSUES]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:1]
        [MAXAGE:1:1]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:GREEN:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
