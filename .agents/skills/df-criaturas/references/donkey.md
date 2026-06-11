# Donkey

> Fonte: [Donkey](https://dwarffortresswiki.org/index.php/Donkey) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes donkeys for their stubborness.**
- **Biome**
- **Domesticated**
- **Attributes**
- **Grazer · Milkable · Horn**
- **Tamed Attributes**
- **Pet value:** 200
- **Not hunting/war trainable**
- **Size**
- **Birth:** 40,000 cm 3
- **Mid:** 100,000 cm 3
- **Max:** 300,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 10
- **Fat:** 9
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
- **Bones:** 13
- **Skull:** 1
- **Hooves:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized, hooved herbivore. Some are domesticated as beasts of burden.*

**Donkeys** are a domestic animal that provide a source of milk and cheese in addition to meat. They are slightly smaller than horses and cows, but a single donkey can still feed two dwarves for about a year. They can be obtained on embark or through trading, and can't be found in the wild. Like other domestic herbivores, they require a pasture to survive.

Despite their similarities to horses, donkeys are not ridable mounts in adventure mode. (Mules are also not ridable mounts.)

Some dwarves like donkeys for their *stubborness*.

\

Admired for its *stubborness*.

|  |
|----|
| "Donkey" in other / Languages / Dwarven / : / nuggad / Elven / : / ceriva / Goblin / : / usnog / Human / : / tham |

    [CREATURE:DONKEY]
        [DESCRIPTION:A medium-sized, hooved herbivore.  Some are domesticated as beasts of burden.]
        [NAME:donkey:donkeys:asinine]
        [CASTE_NAME:donkey:donkeys:asinine]
        [CHILD:1][GENERAL_CHILD_NAME:donkey foal:donkey foals]
        [CREATURE_TILE:'D'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:200]
        [PREFSTRING:stubborness]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC][PACK_ANIMAL]
        [BENIGN][MEANDERER][PET]
        [STANDARD_GRAZER]
        [VISION_ARC:50:310]
        [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        [NATURAL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
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
        [BODY_SIZE:0:0:40000]
        [BODY_SIZE:1:0:100000]
        [BODY_SIZE:2:0:300000]
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
        [DIURNAL]
        [HOMEOTHERM:10068]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [TRADE_CAPACITY:1500]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
                [STATE_NAME:ALL_SOLID:frozen donkey's milk]
                [STATE_ADJ:ALL_SOLID:frozen donkey's milk]
                [STATE_NAME:LIQUID:donkey's milk]
                [STATE_ADJ:LIQUID:donkey's milk]
                [STATE_NAME:GAS:boiling donkey's milk]
                [STATE_ADJ:GAS:boiling donkey's milk]
                [PREFIX:NONE]
            [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
            [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
                [STATE_NAME:SOLID:donkey cheese]
                [STATE_ADJ:SOLID:donkey cheese]
                [STATE_NAME:SOLID_POWDER:donkey cheese powder]
                [STATE_ADJ:SOLID_POWDER:donkey cheese powder]
                [STATE_NAME:LIQUID:melted donkey cheese]
                [STATE_ADJ:LIQUID:melted donkey cheese]
                [STATE_NAME:GAS:boiling donkey cheese]
                [STATE_ADJ:GAS:boiling donkey cheese]
                [PREFIX:NONE]
        [CASTE:MALE]
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
