# Sheep

> Fonte: [Sheep](https://dwarffortresswiki.org/index.php/Sheep) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sheep for their tendency to flock.**
- **Biome**
- **Domesticated**
- **Attributes**
- **Grazer · Milkable · Shearable · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 100
- **Not hunting/war trainable**
- **Size**
- **Birth:** 5,000 cm 3
- **Mid:** 25,000 cm 3
- **Max:** 50,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 8
- **Fat:** 8
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 8/10
- **Skull:** 1
- **Hooves:** 4
- **Horns:** 0/2
- **Skin:** Raw hide
- **Wool:** 7

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized herding animal. It is prized for its thick wool coat.*

**Sheep** are common domestic livestock available to dwarf and human civilizations. Sheep can be sheared once every 300 days to yield wool, which can be used to make low-value cloth. In addition to the standard meat industry products, sheep also supply wool when butchered. *Rams* (male sheep) have two horns which they use for defense (and which your dwarves can use for crafting); *ewes* (female sheep) can be milked, and that milk can then be cooked or made into cheese. Until grown up, their offspring of both sexes are called *lambs*.

Sheep are grazers, and require a moderately-sized pasture to survive. However, sheep eat far less grass than cattle, making them an excellent base animal for combined meat, cheese, and cloth industries.

Notably, sheep are the smallest creature capable of producing wool, and their wool is equivalent in value to that of all other shearable creatures.

Because ewes and rams have the same total body size, the added horns on rams actually make the rest of their body slightly smaller than an ewe's.

Some dwarves like sheep for their *wool* and their *tendency to flock*.

\

Admired for its *wool*.

    [CREATURE:SHEEP]
        [DESCRIPTION:A medium-sized herding animal.  It is prized for its thick wool coat.]
        [NAME:sheep:sheep:ovine]
        [CHILD:1][GENERAL_CHILD_NAME:lamb:lambs]
        [CREATURE_TILE:'s'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:100]
        [PREFSTRING:tendency to flock]
        [PREFSTRING:wool]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC]
        [BENIGN][MEANDERER][PET]
        [STANDARD_GRAZER]
        [VISION_ARC:50:310]
        [CASTE:FEMALE]
            [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        [CASTE:MALE]
            [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE:2HEAD_HORN]
        [SELECT_CASTE:ALL]
        [NATURAL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
            [SELECT_MATERIAL:HAIR]
                [STATE_NAME:ALL_SOLID:wool]
                [STATE_ADJ:ALL_SOLID:wool]
                [YARN]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
            [SELECT_TISSUE:HAIR]
            [TISSUE_NAME:wool:NP]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [SELECT_TISSUE_LAYER:HAIR:BY_CATEGORY:ALL]
            [TL_RELATIVE_THICKNESS:10]
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
        [BODY_SIZE:0:0:5000]
        [BODY_SIZE:1:0:25000]
        [BODY_SIZE:2:0:50000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_REAR]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_CANLATCH]
        [SELECT_CASTE:MALE]
        [ATTACK:HGORE:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [SELECT_CASTE:ALL]
        [DIURNAL]
        [HOMEOTHERM:10070]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:730:561:351:1900:2900] 25 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:ewe:ewes:ewe]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
                [STATE_NAME:ALL_SOLID:frozen sheep's milk]
                [STATE_ADJ:ALL_SOLID:frozen sheep's milk]
                [STATE_NAME:LIQUID:sheep's milk]
                [STATE_ADJ:LIQUID:sheep's milk]
                [STATE_NAME:GAS:boiling sheep's milk]
                [STATE_ADJ:GAS:boiling sheep's milk]
                [PREFIX:NONE]
            [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
            [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
                [STATE_NAME:SOLID:sheep cheese]
                [STATE_ADJ:SOLID:sheep cheese]
                [STATE_NAME:SOLID_POWDER:sheep cheese powder]
                [STATE_ADJ:SOLID_POWDER:sheep cheese powder]
                [STATE_NAME:LIQUID:melted sheep cheese]
                [STATE_ADJ:LIQUID:melted sheep cheese]
                [STATE_NAME:GAS:boiling sheep cheese]
                [STATE_ADJ:GAS:boiling sheep cheese]
                [PREFIX:NONE]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:ram:rams:ram]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:wool:SINGULAR]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:LENGTH:0:0:0:0:0:0:0]
                    [APP_MOD_NOUN:wool:SINGULAR]
                    [APP_MOD_RATE:1:DAILY:0:300:0:0:NO_END]
                    [APP_MOD_DESC_RANGE:10:50:100:150:200:300]
                [SHEARABLE_TISSUE_LAYER:LENGTH:300]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:PINK:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:PUPIL_EYE_AMBER:1]
                    [TLCM_NOUN:eyes:PLURAL]
