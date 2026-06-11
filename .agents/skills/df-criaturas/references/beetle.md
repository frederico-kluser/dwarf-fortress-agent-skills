# Beetle

> Fonte: [Beetle](https://dwarffortresswiki.org/index.php/Beetle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes beetles for their protective shells.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Beetle - Beetle man - Giant beetle**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny insect that can be found almost anywhere outside.*

**Beetles** are a type of unremarkable above ground vermin found anywhere that isn't freezing, and may not be caught in animal traps. Despite having wings, they are flightless (a comment on their raws says it's to allow them to crawl around instead). All beetles possess Legendary skill in climbing.

Some dwarves like beetles for their *protective shells*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some other dwarves like beetles for their *music* and their *cheapness*.

Admired for its *protective shells*.

|  |
|----|
| "Beetle" in other / Languages / Dwarven / : / ngárak / Elven / : / pama / Goblin / : / strog / Human / : / agthreb |

    1 kph

    [CREATURE:BEETLE]
        [DESCRIPTION:A tiny insect that can be found almost anywhere outside.]
        [NAME:beetle:beetles:beetle]
        [CASTE_NAME:beetle:beetles:beetle]
        [CREATURE_TILE:250][COLOR:4:0:0]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_SOIL][FREQUENCY:100]
        [UBIQUITOUS]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [PREFSTRING:protective shells]
        Could be FLIER but leaving it off so they crawl around.
        [ALL_ACTIVE]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [NOBONES]
        [CREATURE_CLASS:EDIBLE_GROUND_BUG]
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
                [TL_COLOR_MODIFIER:RED:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
