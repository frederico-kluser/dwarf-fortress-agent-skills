# Narwhal

> Fonte: [Narwhal](https://dwarffortresswiki.org/index.php/Narwhal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes narwhals for their horns.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Narwhal - Narwhal man - Giant narwhal**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 120,000 cm 3
- **Mid:** 600,000 cm 3
- **Max:** 1,200,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 40-50
- **Butchering returns**
- **Food items**
- **Meat:** 30-37
- **Fat:** 8
- **Brain:** 2-3
- **Heart:** 1
- **Lungs:** 4 or 6
- **Intestines:** 7-9
- **Liver:** 2-3
- **Kidneys:** 2
- **Tripe:** 2-3
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 12
- **Skull:** 1
- **Ivory:** 2-3
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized sea mammal with a long thin horn on its nose. It uses this horn to communicate and break up ice.*

**Narwhals** are marine creatures who inhabit arctic oceans. They spawn one at a time and do little but meander through the water, minding their own business. Narwhals are huge, weighting over a ton, but are benign and will rarely pay attention to dwarves even if they fall into the ocean. If forced to fight for whatever reason, they will attempt to stab the enemy with their tusks or slap them with their tails. Narwhals will occasionally "tusk" one another as a greeting, bumping their tusks together in a similar manner to how cats greet others by head-bumping. An infant narwhal is called a *narwhal calf*.

Being fully-sized creatures rather than vermin, the only way to fish narwhals is to trap them on land, typically with the use of a drowning chamber. Due to their huge size, they provide a great amount of returns when butchered, with their tusks serving as a source of ivory.

Some dwarves like narwhals for their *horns*.

Admired for their *horns*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Humans would tell you unicorn horns are actually the severed tusks of a narwhal. Dwarves know better, however, as they're professionals in extracting horns from actual unicorns as well as narwhals if needed. Both are equally delicious when cooked into biscuits.

Some dwarves like narwhals for their *commotion* or their *awesomeness*.

    Narwhals were sponsored by the generous contributions of the Bay 12 community.

        Stormrage: "Original inventors of the shish kebab."
        Ubuntu X.org Maintainers
        PruneyToes
        Sadpear
        Kete

    [CREATURE:NARWHAL]
        [DESCRIPTION:A medium-sized sea mammal with a long thin horn on its nose.  It uses this horn to communicate and break up ice.]
        [NAME:narwhal:narwhals:narwhal]
        [CASTE_NAME:narwhal:narwhals:narwhal]
        [CHILD:1][GENERAL_CHILD_NAME:narwhal calf:narwhal calves]
        [CREATURE_TILE:'N'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [BENIGN][MEANDERER][NATURAL]
        [PETVALUE:100]
        [BIOME:OCEAN_ARCTIC]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [PREFSTRING:horns]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:SIDE_FLIPPERS:TAIL:2EYES:2LUNGS:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:TONGUE:TUSK:RIBCAGE]
        [RELSIZE:BY_CATEGORY:TUSK:200]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:IVORY:TOOTH_TEMPLATE]
                [STATE_NAME:ALL_SOLID:ivory]
                [STATE_ADJ:ALL_SOLID:ivory]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:IVORY:IVORY_TEMPLATE]
                [TISSUE_NAME:ivory:NP]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
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
        [BODY_SIZE:0:0:120000]
        [BODY_SIZE:3:0:600000]
        [BODY_SIZE:5:0:1200000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:40:50]
        [ATTACK:STAB:BODYPART:BY_CATEGORY:TUSK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:stab:stabs]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
        [ATTACK:SLAP:BODYPART:BY_CATEGORY:TAIL]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:slap:slaps]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [CAN_DO_INTERACTION:BP_BUMP]
            [CDI:USAGE_HINT:GREETING]
            [CDI:BP_REQUIRED:BY_CATEGORY:TUSK]
            [CDI:VERB:tusk:tusks:are tusking]
            [CDI:CAN_BE_MUTUAL]
            [CDI:TARGET:B:TOUCHABLE]
            [CDI:TARGET_RANGE:B:1]
            [CDI:WAIT_PERIOD:20]
        [ALL_ACTIVE]
        [NO_DRINK]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:MOTTLED_BLACK_WHITE:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
