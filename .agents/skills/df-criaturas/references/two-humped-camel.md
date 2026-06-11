# Two-humped camel

> Fonte: [Two-humped camel](https://dwarffortresswiki.org/index.php/Two-humped_camel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes two-humped camels for their humps.**
- **Biome**
- **Any Desert**
- **Variations**
- **Two-humped camel - Two-humped camel man - Giant two-humped camel**
- **Attributes**
- **Grazer · Mount · Milkable**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50,000 cm 3
- **Mid:** 250,000 cm 3
- **Max:** 500,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 16
- **Fat:** 15
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 17
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large, long-necked creature with two fleshy humps on its back. It is domesticated to carry passengers and cargo.*

**Two-humped camels** are creatures who can be found in deserts, where they appear in groups of 3-7 individuals. They are notable for being eligible to be pack animals for dwarf and human merchants, while not technically being full domestic animals; this means that, during world generation, civilizations may domesticate them, but are not guaranteed to. Wild camels are benign meanderers and will generally provide no threat to even the clumsiest of dwarves.

Two-humped camels may be butchered for a good amount of returns, or assigned as fairly valuable pets. Female two-humped camels produce milk, which can be cooked or processed into cheese. Like other herbivorous livestock, they require a sizeable pasture to survive. Two-humped camel calves need two years to grow to their full adult size, and they only live for a maximum of 10-20 years.

They are not to be confused with the one-humped camel, which is a completely different species, also meaning that they cannot interbreed. In real life, two-humped camels are most popularly known as Bactrian camels, though the name is not used in *Dwarf Fortress*.

Some dwarves like two-humped camels for their *humps*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Legend says that an untamed two-humped camel laden with fire clay is an omen of great destruction.

Admired for its *humps*.

    1 kph

    [CREATURE:CAMEL_2_HUMP]
        [DESCRIPTION:A large, long-necked creature with two fleshy humps on its back.  It is domesticated to carry passengers and cargo.]
        [NAME:two-humped camel:two-humped camels:two-humped camel]
        [CASTE_NAME:two-humped camel:two-humped camels:two-humped camel]
        [CHILD:1][GENERAL_CHILD_NAME:two-humped camel calf:two-humped camel calves]
        [CREATURE_TILE:'C'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:500]
        [PET]
        [VISION_ARC:50:310]
        [STANDARD_GRAZER]
        [PACK_ANIMAL]
        [MOUNT]
        [PREFSTRING:humps]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING][FREQUENCY:100]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [BIOME:ANY_DESERT]
        [TRADE_CAPACITY:3000]
        [BENIGN][MEANDERER][NATURAL]
        [BODY:QUADRUPED_NECK:TAIL:2HUMPS:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
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
        [BODY_SIZE:0:0:50000]
        [BODY_SIZE:1:0:250000]
        [BODY_SIZE:2:0:500000]
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
        [HOMEOTHERM:10070]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:405:270:135:1900:2900] 65 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
                [STATE_NAME:ALL_SOLID:frozen two-humped camel's milk]
                [STATE_ADJ:ALL_SOLID:frozen two-humped camel's milk]
                [STATE_NAME:LIQUID:two-humped camel's milk]
                [STATE_ADJ:LIQUID:two-humped camel's milk]
                [STATE_NAME:GAS:boiling two-humped camel's milk]
                [STATE_ADJ:GAS:boiling two-humped camel's milk]
                [PREFIX:NONE]
            [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
            [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
                [STATE_NAME:SOLID:two-humped camel cheese]
                [STATE_ADJ:SOLID:two-humped camel cheese]
                [STATE_NAME:SOLID_POWDER:two-humped camel cheese powder]
                [STATE_ADJ:SOLID_POWDER:two-humped camel cheese powder]
                [STATE_NAME:LIQUID:melted two-humped camel cheese]
                [STATE_ADJ:LIQUID:melted two-humped camel cheese]
                [STATE_NAME:GAS:boiling two-humped camel cheese]
                [STATE_ADJ:GAS:boiling two-humped camel cheese]
                [PREFIX:NONE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:TAN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
