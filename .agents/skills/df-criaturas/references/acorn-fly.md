# Acorn fly

> Fonte: [Acorn fly](https://dwarffortresswiki.org/index.php/Acorn_fly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes acorn flies for their deafening buzz.**
- **Biome**
- **Any Pool**
- **Attributes**
- **Alignment:** Savage
- **Flying**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*An insect many times the size of its peers. It is known for its deafening buzz.*

**Acorn flies** are a type of vermin which spawn around murky pools in savage areas. It may be observed in swarms around rotting corpses. Unlike regular flies, dwarves do not ever detest acorn flies, though they can be mildly annoyed by them. Can be caught with "Capture Live Land Animal" job, but can not be trapped in built animal traps. All acorn flies possess Legendary skill in climbing.

Some dwarves like acorn flies for their *deafening buzz*.

You would think this could be more than mildly annoying. *Photo by Judy Gallagher*

    [CREATURE:FLY_ACORN]
        [DESCRIPTION:An insect many times the size of its peers.  It is known for its deafening buzz.]
        [NAME:acorn fly:acorn flies:acorn fly]
        [CASTE_NAME:acorn fly:acorn flies:acorn fly]
        [CREATURE_TILE:250][COLOR:6:0:0]
        [NATURAL]
        [BIOME:ANY_POOL]
        [VERMIN_ROTTER][VERMIN_GROUNDER][VERMIN_MICRO][FREQUENCY:100]
        [VERMIN_NOTRAP]
        [SAVAGE]
        [POPULATION_NUMBER:2500:5000]
        [CLUSTER_NUMBER:100:200]
        [SMALL_REMAINS]
        [PREFSTRING:deafening buzz]
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
        [BODY_SIZE:0:0:20]
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
