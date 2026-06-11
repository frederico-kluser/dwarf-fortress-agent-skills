# Duck

> Fonte: [Duck](https://dwarffortresswiki.org/index.php/Duck) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ducks for their quacks.**
- **Biome**
- **Any Lake Any Wetland Domesticated**
- **Attributes**
- **Flying · Egglaying**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50 cm 3
- **Mid:** 500 cm 3
- **Max:** 1,000 cm 3
- **Food products**
- **Eggs:** 8-13
- **Age**
- **Adult at:** 1
- **Max age:** 7-9
- **Butchering returns**
- **Food items**
- **Meat:** 0-2
- **Raw materials**
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small water bird. It has a long neck and powerful legs meant for swimming and diving.*

**Ducks** are small domestic birds which can be encountered in the wild, living in lakes and wetlands. Females of the species are called *ducks*, while males are referred to as *drakes* (*not to be confused with dragons!*) and hatchlings are called *ducklings*.

Ducks are the smallest of the common domestic poultry, so small that they only produce a skull when butchered. They take two years to grow to full size, and have a relatively short lifespan. These qualities make raising ducks useless for a meat industry. However, on average, ducks lay the second-most eggs of any domestic bird (8-13, exceeded only by turkeys' 10-14) making them a decent choice for egg production.

Some dwarves like ducks for their *quacks*.

\

Admired for its *quacks*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Many a new player has first seen the drake in their unit list and become excited, imagining it to be some sort of lesser dragon, until they found out it's just a duck. Such scenarios have typically ended with a new duck totem being added to the finished goods stockpile.

    [CREATURE:BIRD_DUCK]
        [DESCRIPTION:A small water bird.  It has a long neck and powerful legs meant for swimming and diving.]
        [NAME:duck:ducks:duck]
        [CHILD:1][GENERAL_CHILD_NAME:duckling:ducklings]
        [CREATURE_TILE:'d'][COLOR:2:0:0]
        [NATURAL]
        [LARGE_ROAMING]
        [BIOME:ANY_LAKE]
        [BIOME:ANY_WETLAND]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [COMMON_DOMESTIC]
        [PETVALUE:10]
        [BENIGN][MEANDERER][PET]
        [GOBBLE_VERMIN_CLASS:EDIBLE_GROUND_BUG]
        [VISION_ARC:50:310]
        [DIURNAL]
        [FLIER]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:4732:4026:3327:1097:5922:7567] 8 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:411:274:137:1900:2900] 64 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [PREFSTRING:quacks]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BILL:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS:FEATHER]
        [BODY_DETAIL_PLAN:EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
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
        [BODY_SIZE:0:0:50]
        [BODY_SIZE:1:0:500]
        [BODY_SIZE:2:0:1000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:7:9]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ROOT_AROUND:BY_CATEGORY:BEAK:root around in:roots around in]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:duck:ducks:duck]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:52]
                [CLUTCH_SIZE:8:13]
        [CASTE:MALE]
            [CASTE_NAME:drake:drakes:drake]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
