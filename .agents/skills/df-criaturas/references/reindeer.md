# Reindeer

> Fonte: [Reindeer](https://dwarffortresswiki.org/index.php/Reindeer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes reindeer for their large herds.**
- **Biome**
- **Tundra Taiga Domesticated**
- **Attributes**
- **Grazer · Milkable · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 200
- **Not hunting/war trainable**
- **Size**
- **Birth:** 13,000 cm 3
- **Mid:** 65,000 cm 3
- **Max:** 130,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 9-11
- **Fat:** 8-9
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
- **Hooves:** 4
- **Horns:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large mammalian herbivore living in cold climates. It has large antlers and sought-after fur.*

**Reindeer** are very versatile domestic animals, providing not only a respectable amount of meat, but also horns and hooves that can be used for crafting. They also produce milk, which can be cooked directly or used to make cheese. While reindeer require a pasture to survive, they need less grass than most other large herbivores, making them a great choice for the food industry. They may be brought on embark or found in wild populations in taigas and tundras.

Some dwarves like reindeer for their *large herds*.

\

Admired for its *large herds*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

It has been rumored that some reindeer are generated with red noses. It has yet to be tested if this is somehow related to Goblin Christmas. It has also been rumoured that due to the relation of these rare specimens to fat humans and elves, the red-nosed sub-species has been systematically killed off by the dwarves.

|  |
|----|
| "Reindeer" in other / Languages / Dwarven / : / memad-kizbiz / Elven / : / reli-liyìÿi / Goblin / : / nusnost-unes / Human / : / gisla-keth |

    [CREATURE:REINDEER]
        [DESCRIPTION:A large mammalian herbivore living in cold climates.  It has large antlers and sought-after fur.]
        [NAME:reindeer:reindeer:reindeer]
        [CHILD:1][GENERAL_CHILD_NAME:reindeer calf:reindeer calves]
        [CREATURE_TILE:'R'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [BIOME:TUNDRA]
        [BIOME:TAIGA]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [PETVALUE:200]
        [PREFSTRING:large herds]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC]
        [BENIGN][MEANDERER][PET]
        [VISION_ARC:50:310]
        [STANDARD_GRAZER]
        [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE:2HEAD_ANTLER]
        [NATURAL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
                [STATE_NAME:ALL_SOLID:antler]
                [STATE_ADJ:ALL_SOLID:antler]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
                [TISSUE_NAME:antler:NP]
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
        [BODY_SIZE:0:0:13000]
        [BODY_SIZE:1:0:65000]
        [BODY_SIZE:2:0:130000]
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
        [ATTACK:HGORE:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [DIURNAL]
        [HOMEOTHERM:10068]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:375:250:125:1900:2900] 70 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [TRADE_CAPACITY:1500]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:reindeer cow:reindeer cows:reindeer cow]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
                [STATE_NAME:ALL_SOLID:frozen reindeer's milk]
                [STATE_ADJ:ALL_SOLID:frozen reindeer's milk]
                [STATE_NAME:LIQUID:reindeer's milk]
                [STATE_ADJ:LIQUID:reindeer's milk]
                [STATE_NAME:GAS:boiling reindeer's milk]
                [STATE_ADJ:GAS:boiling reindeer's milk]
                [PREFIX:NONE]
            [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
            [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
                [STATE_NAME:SOLID:reindeer cheese]
                [STATE_ADJ:SOLID:reindeer cheese]
                [STATE_NAME:SOLID_POWDER:reindeer cheese powder]
                [STATE_ADJ:SOLID_POWDER:reindeer cheese powder]
                [STATE_NAME:LIQUID:melted reindeer cheese]
                [STATE_ADJ:LIQUID:melted reindeer cheese]
                [STATE_NAME:GAS:boiling reindeer cheese]
                [STATE_ADJ:GAS:boiling reindeer cheese]
                [PREFIX:NONE]
        [CASTE:MALE]
            [CASTE_NAME:reindeer bull:reindeer bulls:reindeer bull]
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
