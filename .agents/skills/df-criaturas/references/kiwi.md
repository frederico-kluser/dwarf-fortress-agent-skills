# Kiwi

> Fonte: [Kiwi](https://dwarffortresswiki.org/index.php/Kiwi) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kiwis for their long beaks.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland**
- **Variations**
- **Kiwi - Kiwi man - Giant kiwi**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 430 cm 3
- **Mid:** 1,250 cm 3
- **Max:** 2,500 cm 3
- **Food products**
- **Eggs:** 1-2
- **Age**
- **Adult at:** 1
- **Max age:** 20-50
- **Butchering returns**
- **Food items**
- **Meat:** 2
- **Fat:** 2
- **Intestines:** 0-1
- **Raw materials**
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, brown, flightless bird. It eats insects and grubs and is known for its keen sense of smell.*

**Kiwis** are small flightless birds who can be found in temperate forests and shrublands, where they spawn individually. Benign and only half the size of a cat, they do nothing but root around the ground, eating vermin and fleeing from dwarves who try and hunt them. A male kiwi is called a *kiwi cock*, while a female is called a *kiwi hen*.

Kiwis can be captured in cage traps and trained into cheap exotic pets. They produce a tiny amount of returns when butchered and only lay up to 2 eggs at a time, making them poor choices for livestock. However, they are fairly long lived for wild animals, making them potentially long-lasting companions for dwarves who adopt them.

Some dwarves like kiwis for their *long beaks*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some dwarves like to engrave boxes with this bird and put stimulating toys inside for young dwarves to occupy themselves with. Contrary to popular belief, Kiwis do not only appear on small, remote, Islands.

Admired for their *long beaks*

    12 kph

    Kiwis were sponsored by the generous contributions of the Bay 12 community.

        For Tamsyn Muir
        Gregory Kampjes, McLovin

    [CREATURE:BIRD_KIWI]
        [DESCRIPTION:A small, brown, flightless bird.  It eats insects and grubs and is known for its keen sense of smell.]
        [NAME:kiwi:kiwis:kiwi]
        [CHILD:1][GENERAL_CHILD_NAME:kiwi chick:kiwi chicks]
        [CREATURE_TILE:'k'][COLOR:6:0:0]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:SHRUBLAND_TEMPERATE]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [NATURAL]
        [LARGE_ROAMING]
        [PETVALUE:10]
        [BENIGN][MEANDERER]
        [PET_EXOTIC]
        [GOBBLE_VERMIN_CLASS:EDIBLE_GROUND_BUG]
        [NOCTURNAL]
        [CREPUSCULAR]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [PREFSTRING:long beaks]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:2TOES:BEAK:TONGUE:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS:FEATHER]
        [USE_MATERIAL_TEMPLATE:TALON:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:TALON:TALON_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:TALON:FRONT]
        [BODY_DETAIL_PLAN:EGG_MATERIALS]
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
        [BODY_SIZE:0:0:430]
        [BODY_SIZE:1:0:1250]
        [BODY_SIZE:2:0:2500]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:50]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:TALON]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:snatch at:snatches at]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ROOT_AROUND:BY_CATEGORY:BEAK:root around in:roots around in]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:kiwi hen:kiwi hens:kiwi hen]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:450]
                [CLUTCH_SIZE:1:2]
        [CASTE:MALE]
            [CASTE_NAME:kiwi cock:kiwi cocks:kiwi cock]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
