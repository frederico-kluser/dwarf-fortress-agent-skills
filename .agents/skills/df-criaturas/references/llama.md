# Llama

> Fonte: [Llama](https://dwarffortresswiki.org/index.php/Llama) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes llamas for their jutting teeth.**
- **Biome**
- **Domesticated**
- **Attributes**
- **Grazer · Milkable · Shearable**
- **Tamed Attributes**
- **Pet value:** 200
- **Not hunting/war trainable**
- **Size**
- **Birth:** 18,000 cm 3
- **Mid:** 90,000 cm 3
- **Max:** 180,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-30
- **Butchering returns**
- **Food items**
- **Meat:** 12-13
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
- **Bones:** 12-18
- **Skull:** 1
- **Skin:** Raw hide
- **Wool:** 15

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large domestic pack animal. It has a long neck. It is prized for its hair.*

**Llamas** are common domestic livestock available to most civilizations. Llamas can be sheared once every 300 days to yield wool, which can be used to make low-value cloth. In addition to the standard meat industry products, llamas also supply wool when butchered.

Female llamas can be milked, and that milk can then be cooked or made into cheese.

As grazers, llamas require a moderately-large pasture to survive; however they still eat significantly less grass than cattle, making them an excellent base animal for the player's combined meat, cheese, and cloth industries.

Notably, Llamas are the largest and provide the most meat and wool of all the shearable creatures, though llama wool is equivalent in value to all other wool.

Some dwarves like llamas for their *long necks*, their *jutting teeth*, and their *wool*.

Admired for their *wool*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Instead of Pasture land you may also give your Llamas faces and hands to satisfy their lust for flesh. They seem to also prefer to be pastured next to stockpiles of hats. (more testing needed)

While llamas are a common choice of livestock, be warned. You never know which one might actually be a noble transformed by a syndrome. Said llamas are usually very arrogant and self-centered, and often talk about building a pool upon a hilltop.

    [CREATURE:LLAMA]
        [DESCRIPTION:A large domestic pack animal.  It has a long neck.  It is prized for its hair.]
        [NAME:llama:llamas:llama]
        [CASTE_NAME:llama:llamas:llama]
        [CHILD:1][GENERAL_CHILD_NAME:baby llama:baby llamas]
        [CREATURE_TILE:'L'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:200]
        [PREFSTRING:long necks]
        [PREFSTRING:jutting teeth]
        [PREFSTRING:wool]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC][PACK_ANIMAL]
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
        [BODY_SIZE:0:0:18000]
        [BODY_SIZE:1:0:90000]
        [BODY_SIZE:2:0:180000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:30]
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
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [TRADE_CAPACITY:1500]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:llama:llamas:llama]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
                [STATE_NAME:ALL_SOLID:frozen llama's milk]
                [STATE_ADJ:ALL_SOLID:frozen llama's milk]
                [STATE_NAME:LIQUID:llama's milk]
                [STATE_ADJ:LIQUID:llama's milk]
                [STATE_NAME:GAS:boiling llama's milk]
                [STATE_ADJ:GAS:boiling llama's milk]
                [PREFIX:NONE]
            [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
            [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
                [STATE_NAME:SOLID:llama cheese]
                [STATE_ADJ:SOLID:llama cheese]
                [STATE_NAME:SOLID_POWDER:llama cheese powder]
                [STATE_ADJ:SOLID_POWDER:llama cheese powder]
                [STATE_NAME:LIQUID:melted llama cheese]
                [STATE_ADJ:LIQUID:melted llama cheese]
                [STATE_NAME:GAS:boiling llama cheese]
                [STATE_ADJ:GAS:boiling llama cheese]
                [PREFIX:NONE]
        [CASTE:MALE]
            [CASTE_NAME:llama:llamas:llama]
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
