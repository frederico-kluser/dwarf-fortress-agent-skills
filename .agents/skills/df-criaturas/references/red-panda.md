# Red panda

> Fonte: [Red panda](https://dwarffortresswiki.org/index.php/Red_panda) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes red pandas for their large striped tails.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Red panda - Red panda man - Giant red panda**
- **Attributes**
- **Grazer**
- **Tamed Attributes**
- **Pet value:** 25
- **Not hunting/war trainable**
- **Size**
- **Birth:** 500 cm 3
- **Mid:** 2,500 cm 3
- **Max:** 5,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 8-15
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 6
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small tree-dwelling mammal with distinctive color. It rears up on its hind legs when cornered. It uses its front paws like hands.*

**Red pandas** are small tree-dwelling mammals, about the size of a ~~rapidly reproducing malevolent demon~~ cat. Like regular and gigantic pandas, trained red pandas must consume bamboo to survive, however their reduced grazer value at least makes survival a possibility when placed in a large pasture. While they can be bred as livestock, their diet and meager butchering returns make them marginally useful, at best. As of 42.06, males are labeled red panda boars and females as red panda sows.

Some dwarves like red pandas for their *large striped tails*.

Admired for their *large striped tails*

    5 kph

    Red pandas were sponsored by the generous contributions of the Bay 12 community.

        Cute, but don't be fooled. They can kill you.
        Sentynel
        Daniel Rasmussen
        m0nster

    [CREATURE:RED PANDA]
        [DESCRIPTION:A small tree-dwelling mammal with distinctive color.  It rears up on its hind legs when cornered.  It uses its front paws like hands.]
        [NAME:red panda:red pandas:red panda]
        [CHILD:1][GENERAL_CHILD_NAME:red panda cub:red panda cubs]
        [CREATURE_TILE:'p'][COLOR:4:0:0]
        [CREATURE_CLASS:MAMMAL]
        [NATURAL]
        [PETVALUE:25]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [BIOME:ANY_TEMPERATE_FOREST]
        [STANDARD_GRAZER]
        [SPECIFIC_FOOD:PLANT:BAMBOO, ARROW]
        [SPECIFIC_FOOD:PLANT:BAMBOO, GOLDEN]
        [SPECIFIC_FOOD:PLANT:BAMBOO, HEDGE]
        [BENIGN]
        [GRASSTRAMPLE:0]
        [PREFSTRING:large striped tails]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:200]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
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
        [BODY_SIZE:0:0:500]
        [BODY_SIZE:1:0:2500]
        [BODY_SIZE:2:0:5000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:8:15]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [CAN_DO_INTERACTION:CLEANING]
            [CDI:ADV_NAME:Clean]
            [CDI:USAGE_HINT:CLEAN_SELF]
            [CDI:USAGE_HINT:CLEAN_FRIEND]
            [CDI:BP_REQUIRED:BY_CATEGORY:TONGUE]
            [CDI:VERB:lick:licks:lick each other]
            [CDI:CAN_BE_MUTUAL]
            [CDI:TARGET:A:SELF_ALLOWED:TOUCHABLE]
            [CDI:TARGET_RANGE:A:1]
            [CDI:MAX_TARGET_NUMBER:A:1]
            [CDI:WAIT_PERIOD:10]
        [CAN_DO_INTERACTION:BP_BUMP]
            [CDI:ADV_NAME:Head bump]
            [CDI:USAGE_HINT:GREETING]
            [CDI:BP_REQUIRED:BY_CATEGORY:HEAD]
            [CDI:VERB:head-bump:head-bumps:bump heads]
            [CDI:CAN_BE_MUTUAL]
            [CDI:TARGET:A:SELF_ONLY]
            [CDI:TARGET:B:TOUCHABLE]
            [CDI:TARGET_RANGE:B:1]
            [CDI:MAX_TARGET_NUMBER:B:1]
            [CDI:WAIT_PERIOD:20]
        [NOCTURNAL]
        [CREPUSCULAR]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:679:458:231:1900:2900] 38 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [CASTE_NAME:red panda sow:red panda sows:red panda sow]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
            [CASTE_NAME:red panda boar:red panda boars:red panda boar]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:HAIR]
                [TL_COLOR_MODIFIER:ORANGE:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_REAR:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:FOOT_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:FOOT_REAR:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:TOE:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:legs:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:EAR:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:TAIL:HAIR]
                [TL_COLOR_MODIFIER:STRIPES_ORANGE_WHITE:1]
                    [TLCM_NOUN:head and tail:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
