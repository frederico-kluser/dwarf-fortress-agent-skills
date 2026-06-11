# Termite

> Fonte: [Termite](https://dwarffortresswiki.org/index.php/Termite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes termites for their ability to devour wood.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny insect capable of destroying large wooden structures when in large numbers.*

**Termites** are a species of above ground vermin who may be found in any non-freezing biome. They live in mounds (  ) which can be spotted in the surface, and they can't be captured in animal traps. Despite what their description indicates, they pose no danger to logs or wooden structures.

Some dwarves like termites for their *industrious nature* and their *ability to devour wood*.

Admired for its *industrious nature*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Research is underway on the easiest way to weaponize these wood-eating fiends as an assault force against elven forest retreats.

    1 kph

    Termites were sponsored by the generous contributions of the Bay 12 community.

        RiceMunk

    [CREATURE:TERMITE]
        [DESCRIPTION:A tiny insect capable of destroying large wooden structures when in large numbers.]
        [NAME:termite:termites:termite]
        [CREATURE_TILE:250][COLOR:7:0:1]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_SOIL_COLONY][FREQUENCY:100]
        [UBIQUITOUS]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [CLUSTER_NUMBER:100:200]
        [SMALL_REMAINS]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [PREFSTRING:industrious nature]
        [PREFSTRING:ability to devour wood]
        [DIURNAL]
        [NO_SLEEP]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [CANNOT_JUMP]
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
        [NOBONES]
        [CASTE:WORKER]
            [CASTE_NAME:worker termite:worker termites:worker termite]
            [POP_RATIO:10000]
        [CASTE:SOLDIER]
            [CASTE_NAME:soldier termite:soldier termites:soldier termite]
            [POP_RATIO:1000]
        [CASTE:KING]
            [MALE]
            [CASTE_NAME:king termite:king termites:king termite]
            [POP_RATIO:1]
        [CASTE:QUEEN]
            [FEMALE]
            [CASTE_NAME:queen termite:queen termites:queen termite]
            [POP_RATIO:1]
        [SELECT_CASTE:ALL]
            [BODY:INSECT:2EYES:HEART:GUTS:BRAIN:MOUTH]
            [BODYGLOSS:INSECT_UPPERBODY:INSECT_LOWERBODY]
            [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
            [BODY_DETAIL_PLAN:CHITIN_TISSUES]
            [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
            [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
