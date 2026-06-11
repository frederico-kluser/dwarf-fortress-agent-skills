# Hagfish

> Fonte: [Hagfish](https://dwarffortresswiki.org/index.php/Hagfish) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hagfish for their ability to tie themselves in knots.**
- **Biome**
- **Arctic Ocean Temperate Ocean**
- **Attributes**
- **Aquatic · Fishable**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, spineless, eel-like fish that lives on the bottom of the ocean. It can turn the water around its body into a cloud of slime to escape predators.*

**Hagfish** are a type of aquatic vermin found year-round, only in arctic and temperate oceans, and are a ready source of food when cleaned at a fishery.

Some dwarves like hagfish for their *slime* and their *ability to tie themselves in knots*.

Admired for its *slime*.

|  |
|----|
| "Hagfish" in other / Languages / Dwarven / : / ulthush tatlosh / Elven / : / ciriko thaci / Goblin / : / zastrur otu / Human / : / agwa amsir |

    [CREATURE:FISH_HAGFISH]
        [DESCRIPTION:A small, spineless, eel-like fish that lives on the bottom of the ocean.  It can turn the water around its body into a cloud of slime to escape predators.]
        [NAME:hagfish:hagfish:hagfish]
        [CASTE_NAME:hagfish:hagfish:hagfish]
        [CREATURE_TILE:'~'][COLOR:6:0:0]
        [AQUATIC][SMALL_REMAINS][UNDERSWIM]
        [VERMIN_FISH][VERMIN_GROUNDER][FISHITEM][IMMOBILE_LAND][VERMIN_NOTRAP]
        [NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:OCEAN_ARCTIC]
        [BIOME:OCEAN_TEMPERATE]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:slime]
        [PREFSTRING:ability to tie themselves in knots]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:TAIL:2EYES:HEART:GUTS:ORGANS:BRAIN:SKULL:MOUTH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:CARTILAGE:CARTILAGE]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
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
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
