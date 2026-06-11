# Large roach

> Fonte: [Large roach](https://dwarffortresswiki.org/index.php/Large_roach) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes large roaches for their ability to disgust.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **- Roach man - Large roach - Giant roach**
- **Attributes**
- **Devours food · Flying · Hateable · Pet**
- **Pet value:** 5
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small insect that seeks out unwatched food and garbage. They fear light.*

**Large roaches** are a type of hateable above-ground vermin found in any area that is not freezing, can eat stockpiled food, and will cause dwarves that see them to experience an unhappy thought, so make sure to bring some cats to deal with them. All large roaches possess Legendary skill in climbing.

Large roaches possess a pet value of 5, but can't be captured in animal traps. Like certain types of real-life roaches, they can fly, and so you may sometimes see them flying through open space.

Some dwarves like large roaches for their *ability to disgust*.

\

Admired for its *ability to disgust*.

    1 kph

    [CREATURE:ROACH_LARGE]
        [DESCRIPTION:A small insect that seeks out unwatched food and garbage.  They fear light.]
        [NAME:large roach:large roaches:large roach]
        [CASTE_NAME:large roach:large roaches:large roach]
        [CREATURE_TILE:249][COLOR:6:0:0]
        [NATURAL][PET]
        [PETVALUE:5]
        [BIOME:NOT_FREEZING]
        [VERMIN_EATER][PENETRATEPOWER:2][VERMIN_HATEABLE][VERMIN_GROUNDER]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [TRIGGERABLE_GROUP:5:50]
        [SMALL_REMAINS]
        [PREFSTRING:ability to disgust]
        [FLIER]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph, NO DATA
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
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
