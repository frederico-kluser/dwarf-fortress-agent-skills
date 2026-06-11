# Yak

> Fonte: [Yak](https://dwarffortresswiki.org/index.php/Yak) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes yaks for their shaggy hair.**
- **Biome**
- **Mountain Domesticated**
- **Attributes**
- **Grazer · Milkable · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 200
- **Not hunting/war trainable**
- **Size**
- **Birth:** 70,000 cm 3
- **Mid:** 350,000 cm 3
- **Max:** 700,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-25
- **Butchering returns**
- **Food items**
- **Meat:** 13-21
- **Fat:** 8-9
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 16
- **Skull:** 1
- **Hooves:** 4
- **Horns:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large mammalian herbivore. It has long fur and curving horns. It can be found in the mountains.*

**Yaks** are large, milkable domestic animals. They can serve as pack animals and are a common sight in merchant caravans. They may be either brought on embark or found in wild populations in mountains. The males of the species are known as *yak bulls*, while the females are known as *yak cows*.

Yaks are the second largest of all domestic livestock (losing only to water buffalos), making them one of the best domestic creatures for a food industry. They provide significant food, fat and bones when butchered, and also serve as a source of horns. Yaks eat a lot of grass, so it may be in a player's best interest to give them a separate pasture, so they don't hog all the grass from other animals in a given area.

Some dwarves like yaks for their *shaggy hair*. Whilst the hair is recovered upon butchering the animal, it cannot be shorn.

Admired for its *shaggy hair*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some Yaks are dumber than dwarves, there are rumors about yaks climbing the trees and then starving to death while unable to get down.

    [CREATURE:YAK]
        [DESCRIPTION:A large mammalian herbivore.  It has long fur and curving horns.  It can be found in the mountains.]
        [NAME:yak:yaks:yak]
        [CHILD:1][GENERAL_CHILD_NAME:yak calf:yak calves]
        [CREATURE_TILE:'Y'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [BIOME:MOUNTAIN]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [PETVALUE:200]
        [PREFSTRING:shaggy hair]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC][PACK_ANIMAL][WAGON_PULLER]
        [BENIGN][MEANDERER][PET]
        [VISION_ARC:50:310]
        [STANDARD_GRAZER]
        [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE:2HEAD_HORN]
        [NATURAL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
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
        [BODY_SIZE:0:0:70000]
        [BODY_SIZE:1:0:350000]
        [BODY_SIZE:2:0:700000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:25]
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
        [ATTACK:HGORE:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [DIURNAL]
        [HOMEOTHERM:10068]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [TRADE_CAPACITY:1500]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:yak cow:yak cows:yak cow]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
                [STATE_NAME:ALL_SOLID:frozen yak's milk]
                [STATE_ADJ:ALL_SOLID:frozen yak's milk]
                [STATE_NAME:LIQUID:yak's milk]
                [STATE_ADJ:LIQUID:yak's milk]
                [STATE_NAME:GAS:boiling yak's milk]
                [STATE_ADJ:GAS:boiling yak's milk]
                [PREFIX:NONE]
            [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
            [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
                [STATE_NAME:SOLID:yak cheese]
                [STATE_ADJ:SOLID:yak cheese]
                [STATE_NAME:SOLID_POWDER:yak cheese powder]
                [STATE_ADJ:SOLID_POWDER:yak cheese powder]
                [STATE_NAME:LIQUID:melted yak cheese]
                [STATE_ADJ:LIQUID:melted yak cheese]
                [STATE_NAME:GAS:boiling yak cheese]
                [STATE_ADJ:GAS:boiling yak cheese]
                [PREFIX:NONE]
        [CASTE:MALE]
            [CASTE_NAME:yak bull:yak bulls:yak bull]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
