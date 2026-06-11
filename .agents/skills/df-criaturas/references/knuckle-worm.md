# Knuckle worm

> Fonte: [Knuckle worm](https://dwarffortresswiki.org/index.php/Knuckle_worm) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes knuckle worms for their knobs and angles.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Attributes**
- **Alignment:** Evil
- **Exotic pet**
- **Pet value:** 100
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny creature made up of a series of crackling knobs set at strange angles.*

**Knuckle worms** are a species of above ground vermin found in any evil areas that are not freezing, and may cause nearby food to rot. They are tied with the fox squirrel as the most valuable of all vermin. They can be captured by trappers and turned into pets.

Some dwarves like knuckle worms for their *knobs and angles* and their *crackles and pops*.\
\

Looks even *more* disgusting when shedding.\
*Art by Zippy*

    [CREATURE:WORM_KNUCKLE]
        [DESCRIPTION:A tiny creature made up of a series of crackling knobs set at strange angles.]
        [NAME:knuckle worm:knuckle worms:knuckle worm]
        [CASTE_NAME:knuckle worm:knuckle worms:knuckle worm]
        [CREATURE_TILE:'~'][COLOR:0:0:1]
        [PETVALUE:100]
        [FREQUENCY:25][VERMIN_ROTTER]
        [SMALL_REMAINS][NATURAL][PET_EXOTIC][EVIL]
        [NOT_BUTCHERABLE]
        [BIOME:NOT_FREEZING]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:knobs and angles]
        [PREFSTRING:crackles and pops]
        [NOBONES]
        [BODY:BODY_WITH_HEAD_FLAG:HEART:GUTS:BRAIN:MOUTH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [HAS_NERVES]
        [CANNOT_JUMP]  or should it crack and pop?
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:1000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
        [NOCTURNAL]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:BLACK:1]
                [TLCM_NOUN:skin:SINGULAR]
