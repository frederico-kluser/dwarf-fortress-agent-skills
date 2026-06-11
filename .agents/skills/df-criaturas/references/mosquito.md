# Mosquito

> Fonte: [Mosquito](https://dwarffortresswiki.org/index.php/Mosquito) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mosquitos for their ability to feast on blood.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra Any Pool**
- **Variations**
- **Mosquito - Mosquito man - Giant mosquito**
- **Attributes**
- **Flying · Hateable**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny pest insect. It uses its long nose to suck blood from its host.*

**Mosquitos** are hateable vermin found in all non-freezing biomes. They will give unhappy thoughts to dwarves who absolutely detest mosquitos when they encounter them. While the female caste can suck blood, this does not currently affect dwarves in any way. All mosquitos possess Legendary skill in climbing.

Some dwarves like mosquitos for their *high-pitched buzz* and their *ability to feast on blood*.

Admired for its *high-pitched buzz*.

    1 kph

    Mosquitos were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:MOSQUITO]
        [DESCRIPTION:A tiny pest insect.  It uses its long nose to suck blood from its host.]
        [NAME:mosquito:mosquitos:mosquito]
        [CASTE_NAME:mosquito:mosquitos:mosquito]
        [CREATURE_TILE:250][COLOR:0:0:1]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [BIOME:ANY_POOL]
        [VERMIN_MICRO][VERMIN_GROUNDER][FREQUENCY:100][VERMIN_HATEABLE]
        [UBIQUITOUS]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:2500:5000]
        [CLUSTER_NUMBER:100:200]
        [SMALL_REMAINS]
        [PREFSTRING:high-pitched buzz]
        [PREFSTRING:ability to feast on blood]
        [FLIER]
        [CREPUSCULAR]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [NOBONES]
        [BODY:INSECT:2EYES:HEART:GUTS:BRAIN:PROBOSCIS:2WINGS]
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
            [APPLY_CREATURE_VARIATION:PROBOSCIS_SUCK_ATTACK]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
