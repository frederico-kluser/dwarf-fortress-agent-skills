# Monarch butterfly

> Fonte: [Monarch butterfly](https://dwarffortresswiki.org/index.php/Monarch_butterfly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes monarch butterflies for their coloration.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Monarch butterfly - Monarch butterfly man - Giant monarch butterfly**
- **Attributes**
- **Flying**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small insect with large orange wings. It is admired for its beauty.*

**Monarch butterflies** are a type of above ground vermin found flying around in any area that is warmer than freezing, and will not go out in the winter. They may not be caught in animal traps. All monarch butterflies possess Legendary skill in climbing.

Some dwarves like monarch butterflies for their *coloration.*

Admired for its *coloration*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Be very, very careful of the possibility of a dead monarch butterfly jamming your main entrance open. It can lead to some truly absurd scenarios, as the folks at Boatmurdered can attest to.

    [CREATURE:BUTTERFLY_MONARCH]
        [DESCRIPTION:A small insect with large orange wings.  It is admired for its beauty.]
        [CREATURE_TILE:249][COLOR:4:0:1]
        [NAME:monarch butterfly:monarch butterflies:monarch butterfly]
        [CASTE_NAME:monarch butterfly:monarch butterflies:monarch butterfly]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_GROUNDER][FREQUENCY:100]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS][NO_WINTER]
        [PREFSTRING:coloration]
        [FLIER]
        [DIURNAL]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
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
                [TL_COLOR_MODIFIER:ORANGE:1] *** This obviously needs work.
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
