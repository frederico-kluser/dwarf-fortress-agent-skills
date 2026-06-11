# Blood gnat

> Fonte: [Blood gnat](https://dwarffortresswiki.org/index.php/Blood_gnat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes blood gnats for their pulsating lumpy bodies.**
- **Biome**
- **Any Pool**
- **Attributes**
- **Alignment:** Evil
- **Flying · Hateable**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny insect with a pulsating, lumpy body. It is an evil bug that seeks blood.*

**Blood gnats** are a type of hateable above ground vermin that are found in swarms near pools in evil areas. They may spawn near rotting food, and will inspire unhappy thoughts in dwarves who hold a particular antipathy towards them. Despite their description, they don't damage dwarves beyond the aforementioned unhappy thought.

Some dwarves like blood gnats for their *thirst for blood* and their *pulsating lumpy bodies*.

Admired for its *thirst for blood*.

    [CREATURE:GNAT_BLOOD]
        [DESCRIPTION:A tiny insect with a pulsating, lumpy body.  It is an evil bug that seeks blood.]
        [NAME:blood gnat:blood gnats:blood gnat]
        [CASTE_NAME:blood gnat:blood gnats:blood gnat]
        [CREATURE_TILE:250][COLOR:4:0:1]
        [NATURAL]
        [BIOME:ANY_POOL]
        [EVIL]
        [VERMIN_MICRO][VERMIN_ROTTER][VERMIN_GROUNDER][FREQUENCY:100][VERMIN_HATEABLE]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:2500:5000]
        [CLUSTER_NUMBER:100:200]
        [SMALL_REMAINS]
        [PREFSTRING:thirst for blood]
        [PREFSTRING:pulsating lumpy bodies]
        [FLIER]
        [DIURNAL]
        [NO_SLEEP]
        [HOMEOTHERM:10071]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
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
                [TL_COLOR_MODIFIER:RED:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
