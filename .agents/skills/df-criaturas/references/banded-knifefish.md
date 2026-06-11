# Banded knifefish

> Fonte: [Banded knifefish](https://dwarffortresswiki.org/index.php/Banded_knifefish) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes banded knifefish for their rippling fin.**
- **Biome**
- **Tropical Freshwater River Tropical Freshwater Lake**
- **Attributes**
- **Aquatic · Fishable**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small spotted fish found in tropical rivers and lakes.*

**Banded knifefish** are aquatic vermin that can be found in tropical freshwater rivers and lakes year-round, and are a ready source of food when cleaned at a fishery.

Some dwarves like banded knifefish for their *rippling fin*.

\

Admired for its *rippling fin*.

|  |
|----|
| "Banded knifefish" in other / Languages / Dwarven / : / emäth zasit-tatlosh / Elven / : / isi ceta-thaci / Goblin / : / dozo ngesosp-otu / Human / : / mones hok-amsir |

    [CREATURE:FISH_KNIFEFISH_BANDED]
        [DESCRIPTION:A small spotted fish found in tropical rivers and lakes.]
        [NAME:banded knifefish:banded knifefish:banded knifefish]
        [CASTE_NAME:banded knifefish:banded knifefish:banded knifefish]
        [CREATURE_TILE:224][COLOR:6:0:0]
        [VERMIN_GROUNDER]
        [AQUATIC][SMALL_REMAINS][FISHITEM][IMMOBILE_LAND][UNDERSWIM][VERMIN_NOTRAP]
        [NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:RIVER_TROPICAL_FRESHWATER]
        [BIOME:LAKE_TROPICAL_FRESHWATER]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:rippling fin]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:SIDE_FINS:DORSAL_FIN:TAIL:2EYES:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:200]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [NO_DRINK]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
