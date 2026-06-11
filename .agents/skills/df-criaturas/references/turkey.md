# Turkey

> Fonte: [Turkey](https://dwarffortresswiki.org/index.php/Turkey) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes turkeys for their wattle.**
- **Biome**
- **Temperate Shrubland Any Temperate Forest Any Temperate Swamp Domesticated**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 85 cm 3
- **Mid:** 2,500 cm 3
- **Max:** 5,000 cm 3
- **Food products**
- **Eggs:** 10-14
- **Age**
- **Adult at:** 1
- **Max age:** 7-10
- **Butchering returns**
- **Food items**
- **Meat:** 9
- **Fat:** 9
- **Intestines:** 1
- **Raw materials**
- **Bones:** 6
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small forest bird known for the distinctive flaps of skin hanging from its face. It is prized for its meat.*

**Turkeys** are a species of domesticated creature who can be brought on embark or found in the wild, inhabiting temperate wetlands. Males are called *turkey gobblers*, females are called *turkey hens* and hatchlings are called *poults*.

Compared to other domestic poultry, turkeys are the largest in size, being a better food source than the likes of chickens. Turkeys take two years to reach their full weight, while the slightly smaller blue peafowl and geese take only one year. They lay the most eggs in average out of all domestic birds (12, compared to the average 10 eggs of the duck and 9 of the guineafowl), making them the best domestic birds for egg production. Having both genders of turkey around allows one to breed them fairly quickly, though framerate can be negatively impacted by plentifully-peeping poults. As with other tame animals, if many turkeys are confined in a small area, they can become overcrowded and start fights. Since poults need no food, and have no practical utility until mature, they are generally best caged, where they cannot eat FPS by doing line-of-sight checks until they are ready for egg laying or slaughter. Putting a couple in a cage in the dining hall gives dwarves who like turkeys happy thoughts, as well.

Wild turkeys can be captured with cage traps. Training them will render them completely tame.

Some dwarves like turkeys for their *wattle*, their *snood* and their *gobble*.

\

Admired for its *gobble*.

    [CREATURE:BIRD_TURKEY]
        [DESCRIPTION:A small forest bird known for the distinctive flaps of skin hanging from its face.  It is prized for its meat.]
        [NAME:turkey:turkeys:turkey]
        [CHILD:1][GENERAL_CHILD_NAME:poult:poults]
        [CREATURE_TILE:'t'][COLOR:4:0:1]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:ANY_TEMPERATE_SWAMP]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [NATURAL]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC]
        [PETVALUE:10]
        [VISION_ARC:50:310]
        [BENIGN][MEANDERER][PET]
        [GOBBLE_VERMIN_CLASS:EDIBLE_GROUND_BUG]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [PREFSTRING:wattle]
        [PREFSTRING:snood]
        [PREFSTRING:gobble]
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
        [BODY_SIZE:0:0:85]
        [BODY_SIZE:1:0:2500]
        [BODY_SIZE:2:0:5000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:7:10]
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
            [CASTE_NAME:turkey hen:turkey hens:turkey hen]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:87]
                [CLUTCH_SIZE:10:14]
        [CASTE:MALE]
            [CASTE_NAME:turkey gobbler:turkey gobblers:turkey gobbler]
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
