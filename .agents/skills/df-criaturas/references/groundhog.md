# Groundhog

> Fonte: [Groundhog](https://dwarffortresswiki.org/index.php/Groundhog) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes groundhogs for their ability to burrow.**
- **Biome**
- **Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Groundhog - Groundhog man - Giant groundhog**
- **Attributes**
- **Grazer**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 300 cm 3
- **Mid:** 1,500 cm 3
- **Max:** 3,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 6
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large, round, lowland rodent. It lives in burrows in the ground and ventures out to eat.*

**Groundhogs** are small animals found in temperate plains, in groups of 1-4 individuals. Smaller than cats, they're benign meanderers who do little but wander around aimlessly, being easy prey for your hunters. They possess thick fur which provides them with increased insulation compared to most other animals, and their newborns are referred to as *pups*. They won't appear during the winter, mimicking real-life hibernation.

Groundhogs can be captured in cage traps and trained into exotic pets. They give few products when butchered, making them poor targets for a meat industry. Trained groundhogs are grazers and as such need a pasture in order to not starve.

Some dwarves like groundhogs for their *ability to burrow*.

Admired for its *ability to burrow*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
In certain northern temperate lands, some humans think these little fuzzy creatures can predict the arrival of spring by the sight of their shadow. Most dwarves discredit this, but with almost 100% predictability, some humans, and a few dwarves will worship them, especially if the object of worship is named Phil.

    5 kph

    [CREATURE:GROUNDHOG]
        [DESCRIPTION:A large, round, lowland rodent.  It lives in burrows in the ground and ventures out to eat.]
        [NAME:groundhog:groundhogs:groundhog]
        [CASTE_NAME:groundhog:groundhogs:groundhog]
        [GENERAL_CHILD_NAME:groundhog pup:groundhog pups]
        [CREATURE_TILE:'g'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:50]
        [PET_EXOTIC]
        [STANDARD_GRAZER]
        [NATURAL]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:GRASSLAND_TEMPERATE]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [NO_WINTER][BENIGN][MEANDERER]
        [VISION_ARC:50:310]
        [PREFSTRING:ability to burrow]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:RODENT_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [GRASSTRAMPLE:0]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:200]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
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
        [BODY_SIZE:0:0:300]
        [BODY_SIZE:1:0:1500]
        [BODY_SIZE:2:0:3000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:15]
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
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:1945:1504:1062:548:3100:4500] 16 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
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
