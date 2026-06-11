# Ant

> Fonte: [Ant](https://dwarffortresswiki.org/index.php/Ant) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ants for their propensity to dig.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Attributes**
- **Flying**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*This tiny insect can be found in huge colonies in the dirt. They overwhelm their enemies with swarms. Some have poison bites.*

**Ants** are a type of unremarkable above ground vermin found in large numbers in any area that isn't freezing. The color of their wild colonies reflects the material underneath it. Their anthills () can be seen in random locations on the surface.

Some dwarves like ants for their *propensity to dig*.

Admired for its *propensity to dig*.

    1 kph

    [CREATURE:ANT]
        [DESCRIPTION:This tiny insect can be found in huge colonies in the dirt.  They overwhelm their enemies with swarms.  Some have poison bites.]
        [NAME:ant:ants:ant]
        [CREATURE_TILE:250][COLOR:7:0:0]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_SOIL_COLONY][FREQUENCY:100]
        [UBIQUITOUS]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [CLUSTER_NUMBER:100:200]
        [SMALL_REMAINS]
        [PREFSTRING:propensity to dig]
        [DIURNAL]
        [NO_SLEEP]
        [CREATURE_CLASS:EDIBLE_GROUND_BUG]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [CANNOT_JUMP]
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
            [CASTE_NAME:worker ant:worker ants:worker ant]
            Female, but non-breeding (most of the time).
            [POP_RATIO:10000]
        [CASTE:SOLDIER]
            [CASTE_NAME:soldier ant:soldier ants:soldier ant]
            Female, but non-breeding (most of the time).
            [POP_RATIO:1000]
        [CASTE:DRONE]
            [MALE]
            [CASTE_NAME:drone ant:drone ants:drone ant]
            [POP_RATIO:5]
        [CASTE:QUEEN]
            [FEMALE]
            [CASTE_NAME:queen ant:queen ants:queen ant]
            [POP_RATIO:1]
        [SELECT_CASTE:WORKER]
         [SELECT_ADDITIONAL_CASTE:SOLDIER]
         [SELECT_ADDITIONAL_CASTE:QUEEN]
            [BODY:INSECT:2EYES:HEART:GUTS:BRAIN:MOUTH]
            [BODYGLOSS:INSECT_UPPERBODY:INSECT_LOWERBODY]
            [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
            [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
            [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
            [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SELECT_CASTE:DRONE]
            [BODY:INSECT:2EYES:HEART:GUTS:BRAIN:MOUTH:2WINGS]
            [BODYGLOSS:INSECT_UPPERBODY:INSECT_LOWERBODY]
            [FLIER]
            [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph, NO DATA
            [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
            [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
            [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
            [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SELECT_CASTE:ALL]
            [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
            [BODY_DETAIL_PLAN:CHITIN_TISSUES]
            [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
            [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
