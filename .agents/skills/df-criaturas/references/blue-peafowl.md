# Blue peafowl

> Fonte: [Blue peafowl](https://dwarffortresswiki.org/index.php/Blue_peafowl) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes blue peafowls for their coloration.**
- **Biome**
- **Tropical Dry Broadleaf Forest Tropical Moist Broadleaf Forest Domesticated**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 100 cm 3
- **Mid:** 2,000 cm 3
- **Max:** 4,000 cm 3
- **Food products**
- **Eggs:** 6-8
- **Age**
- **Adult at:** 1
- **Max age:** 15-30
- **Butchering returns**
- **Food items**
- **Meat:** 6-9
- **Fat:** 6-8
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4-6
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small forest bird. The male's tail creates an extravagant display for females. At night, they roost in the trees.*

**Blue peafowl** are goose-sized domestic birds found in tropical broadleaf forests. The males (*peacocks*) have bright blue plumage and tail feathers that make large, "eyed" fans. Females (*peahens*) have brown plumage, and lay eggs in a nest box. If a peacock is present and the eggs are not collected, they may eventually hatch into *peachicks*. Peachicks grow into adults 1 year after hatching.

Peafowl can be used as the basis for a poultry industry. They can often be purchased at embark or from traders. Peafowl, ducks, geese, and turkeys are the only common domestic egg-laying animals that can be found in wild populations, and, if your fortress includes the proper biome, can be gathered with cage traps and tamed, instead of purchased from traders or at embark.

On average, peahens lay slightly fewer eggs than chicken hens, but are more consistent (and therefore predictable), laying between 6 and 8 eggs per clutch. Additionally, peafowl produce more meat, fat, and bones than chickens when butchered as part of a meat industry. However, turkeys lay more eggs and produce more meat, fat, and bones than peafowl, although turkeys take twice as long to grow to full size. Peafowl are also the longest-lived of all the domestic birds; this can make them perfect for alternate uses of a domestic animal, such as sealing them in "lookout towers". Since they don't eat or drink, and can stay pastured in a 1×1 area staring through a window and/or fortification for up to 15 years in a row, they make useful watch-birds in preventing goblin ambushes from sneaking through unmolested.

Some dwarves like blue peafowls for their *coloration* and their *enormous fan tails*.

Admired for their *enormous fan tails*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

All of the qualities of the blue peafowl suggest it would be an excellent choice for egg production and the meat industry. However, there is one small problem. At night, blue peafowl enjoy roosting in trees. This Elfish conduct is unbecoming for any creature owned by dwarves (although, there are some that feel that eating "tree roosters" sends the right message to the ~~tree-fondling hippies~~ Elves).

    [CREATURE:BIRD_PEAFOWL_BLUE]
        [DESCRIPTION:A small forest bird.  The male's tail creates an extravagant display for females.  At night, they roost in the trees.]
        [NAME:blue peafowl:blue peafowls:blue peafowl]
        [CHILD:1][GENERAL_CHILD_NAME:blue peachick:blue peachicks]
        [CREATURE_TILE:'p'][COLOR:1:0:1]
        [BIOME:FOREST_TROPICAL_DRY_BROADLEAF]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [NATURAL]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC]
        [PETVALUE:10]
        [BENIGN][MEANDERER][PET]
        [DIURNAL]
        [VISION_ARC:50:310]
        [GOBBLE_VERMIN_CLASS:EDIBLE_GROUND_BUG]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [PREFSTRING:coloration]
        [PREFSTRING:enormous fan tails]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:TONGUE:RIBCAGE]
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
        [BODY_SIZE:0:0:100]
        [BODY_SIZE:0:168:2000]
        [BODY_SIZE:1:0:4000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:30]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:TALON]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:snatch at:snatches at]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ROOT_AROUND:BY_CATEGORY:BEAK:root around in:roots around in]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:blue peahen:blue peahens:blue peahen]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:102]
                [CLUTCH_SIZE:6:8]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [CASTE_COLOR:6:0:0]
        [CASTE:MALE]
            [CASTE_NAME:blue peacock:blue peacocks:blue peacock]
            [MALE]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BLUE:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [CASTE_COLOR:1:0:1]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
