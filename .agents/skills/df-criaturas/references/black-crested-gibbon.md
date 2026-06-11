# Black-crested gibbon

> Fonte: [Black-crested gibbon](https://dwarffortresswiki.org/index.php/Black-crested_gibbon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes black-crested gibbons for their ability to swing through the trees.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 600 cm 3
- **Mid:** 3,000 cm 3
- **Max:** 6,000 cm 3
- **Age**
- **Adult at:** 8
- **Max age:** 20-40
- **Butchering returns**
- **Food items**
- **Meat:** 6-7
- **Fat:** 6-7
- **Heart:** 1
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small ape from the tropical forest. It can be found in the trees eating fruit.*

**Black-crested gibbons** are a very rare species of gibbon found exclusively in tropical moist broadleaf forests, where they always appear in pairs. Marginally heavier than the average cat, these apes are little more than a distraction for a passing dwarf, being benign and overall harmless. All black-crested gibbons are born with Legendary skill in climbing.

Black-crested gibbons can be captured in cage traps and trained into valuable exotic pets. Due to their rarity and small size, they make poor targets for a meat industry. Black-crested gibbons take 8 years to reach adulthood, but reach their maximum size by the age of 2.

Some dwarves like black-crested gibbons for their *coloration* and their *ability to swing through the trees*.

Admired for its *ability to swing through the trees*.

    [CREATURE:GIBBON_BLACK_CRESTED]
        [DESCRIPTION:A small ape from the tropical forest.  It can be found in the trees eating fruit.]
        [NAME:black-crested gibbon:black-crested gibbons:black-crested gibbon]
        [CASTE_NAME:black-crested gibbon:black-crested gibbons:black-crested gibbon]
        [CREATURE_TILE:'g'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [CREATURE_CLASS:HUMANOID_TRACKING_SYMBOL]
        [PETVALUE:500]
        [PET_EXOTIC]
        [NATURAL]
        [BENIGN][MEANDERER]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING][FREQUENCY:5]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:2:2]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [PREFSTRING:coloration]
        [PREFSTRING:ability to swing through the trees]
        [BODY:QUADRUPED_NECK_FRONT_GRASP:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:5TOES_FQ_FINGERS:5TOES_RQ_ANON:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE:FACIAL_FEATURES]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
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
        [BODY_SIZE:0:0:600]
        [BODY_SIZE:1:0:3000]
        [BODY_SIZE:2:0:6000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:40]
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
        [CHILD:8]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_LEARNED]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
