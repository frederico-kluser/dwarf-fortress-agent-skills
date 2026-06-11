# Alpaca

> Fonte: [Alpaca](https://dwarffortresswiki.org/index.php/Alpaca) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes alpacas for their jutting teeth.**
- **Biome**
- **Domesticated**
- **Attributes**
- **Grazer · Milkable · Shearable**
- **Tamed Attributes**
- **Pet value:** 200
- **Not hunting/war trainable**
- **Size**
- **Birth:** 7,000 cm 3
- **Mid:** 35,000 cm 3
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 12
- **Fat:** 12
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
- **Bones:** 16
- **Skull:** 1
- **Skin:** Raw hide
- **Wool:** 7

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large domestic animal with a long neck. It has been bred for its valuable hair.*

**Alpacas** are common domestic livestock available to dwarf and human civilizations. They can be sheared once every 300 days to yield wool, which can be used to make low-value cloth. In addition to the standard meat industry products, alpacas also supply wool when butchered. Alpaca wool is equivalent in value to the wool of all other shearable creatures.

As grazers, alpacas require a moderately-sized pasture to survive; however they eat far less grass than cattle, and make an excellent base animal for combined meat, cheese, and cloth industries. Female alpacas can be milked, and that milk can then be cooked or made into cheese.

Some dwarves like alpacas for their *long necks*, their *jutting teeth*, their *wool*, and their *resemblance to a miniature llama*.

\

Admired for their *long necks*.

## In real life

In real life, alpacas are bred and kept for their highly valuable wool, which is prized for its softness and color. It is commonly referred to as "The fiber of the Gods" due to its silk-like feeling.

    [CREATURE:ALPACA]
        [DESCRIPTION:A large domestic animal with a long neck.  It has been bred for its valuable hair.]
        [NAME:alpaca:alpacas:alpaca]
        [CASTE_NAME:alpaca:alpacas:alpaca]
        [CHILD:1][GENERAL_CHILD_NAME:baby alpaca:baby alpacas]
        [CREATURE_TILE:'a'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:200]
        [PREFSTRING:long necks]
        [PREFSTRING:jutting teeth]
        [PREFSTRING:wool]
        [PREFSTRING:resemblance to a miniature llama]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC]
        [BENIGN][MEANDERER][PET]
        [VISION_ARC:50:310]
        [STANDARD_GRAZER]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        [NATURAL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [SELECT_MATERIAL:HAIR]
                [STATE_NAME:ALL_SOLID:wool]
                [STATE_ADJ:ALL_SOLID:wool]
                [YARN]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
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
        [BODY_SIZE:0:0:7000]
        [BODY_SIZE:1:0:35000]
        [BODY_SIZE:2:0:70000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_REAR]
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
        [DIURNAL]
        [HOMEOTHERM:10068]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
                [STATE_NAME:ALL_SOLID:frozen alpaca's milk]
                [STATE_ADJ:ALL_SOLID:frozen alpaca's milk]
                [STATE_NAME:LIQUID:alpaca's milk]
                [STATE_ADJ:LIQUID:alpaca's milk]
                [STATE_NAME:GAS:boiling alpaca's milk]
                [STATE_ADJ:GAS:boiling alpaca's milk]
                [PREFIX:NONE]
            [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
            [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
                [STATE_NAME:SOLID:alpaca cheese]
                [STATE_ADJ:SOLID:alpaca cheese]
                [STATE_NAME:SOLID_POWDER:alpaca cheese powder]
                [STATE_ADJ:SOLID_POWDER:alpaca cheese powder]
                [STATE_NAME:LIQUID:melted alpaca cheese]
                [STATE_ADJ:LIQUID:melted alpaca cheese]
                [STATE_NAME:GAS:boiling alpaca cheese]
                [STATE_ADJ:GAS:boiling alpaca cheese]
                [PREFIX:NONE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:wool:SINGULAR]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:LENGTH:0:0:0:0:0:0:0]
                    [APP_MOD_NOUN:wool:SINGULAR]
                    [APP_MOD_RATE:1:DAILY:0:300:0:0:NO_END]
                    [APP_MOD_DESC_RANGE:10:50:100:150:200:300]
                [SHEARABLE_TISSUE_LAYER:LENGTH:300]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
