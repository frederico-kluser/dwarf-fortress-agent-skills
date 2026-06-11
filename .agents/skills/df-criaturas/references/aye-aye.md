# Aye-aye

> Fonte: [Aye-aye](https://dwarffortresswiki.org/index.php/Aye-aye) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes aye-ayes for their interesting fingers.**
- **Biome**
- **Tropical Dry Broadleaf Forest Tropical Moist Broadleaf Forest**
- **Variations**
- **Aye-aye - Aye-aye man - Giant aye-aye**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 250 cm 3
- **Mid:** 1,250 cm 3
- **Max:** 2,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 6
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, nocturnal, tree-dwelling mammal. It uses its long fingers to fish out grubs from the wood.*

**Aye-ayes** are small solitary animals uncommonly found in tropical broadleaf forests. Half the size of a cat, they are inoffensive and will flee from any dwarf who attempts to approach them, and are easily disposed of by even the most inexperienced of hunters. While described as nocturnal, their raws are set to being diurnal instead, and as such they're mostly active during the day in adventurer mode. All aye-ayes are born with Legendary skill in climbing.

Aye-ayes can be captured in cage traps and trained into cheap exotic pets. Due to their small size and rarity, they make poor targets for a meat industry.

Some dwarves like aye-ayes for their *interesting fingers*.

Admired for its *interesting fingers*.

    1 kph

    Aye-ayes were sponsored by the generous contributions of the Bay 12 community.

        LASD

    [CREATURE:AYE-AYE]
        [DESCRIPTION:A small, nocturnal, tree-dwelling mammal.  It uses its long fingers to fish out grubs from the wood.]
        [NAME:aye-aye:aye-ayes:aye-aye]
        [CASTE_NAME:aye-aye:aye-ayes:aye-aye]
        [CREATURE_TILE:'a'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [NATURAL]
        [PETVALUE:50]
        [BENIGN][PET_EXOTIC]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING][FREQUENCY:10]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [BIOME:FOREST_TROPICAL_DRY_BROADLEAF]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [PREFSTRING:interesting fingers]
        [BODY:QUADRUPED_NECK_FRONT_GRASP:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:5TOES_FQ_FINGERS:5TOES_RQ_ANON:GENERIC_TEETH:RIBCAGE:FACIAL_FEATURES]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
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
        [BODY_SIZE:0:0:250]
        [BODY_SIZE:1:0:1250]
        [BODY_SIZE:2:0:2500]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
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
        [CHILD:1]
        [DIURNAL]
        [HOMEOTHERM:10069]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:703:505:274:1900:2900] 32 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
