# Elk

> Fonte: [Elk](https://dwarffortresswiki.org/index.php/Elk) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes elk for their grace.**
- **Biome**
- **Tundra Temperate Grassland**
- **Variations**
- **Elk - Elk man - Giant elk**
- **Attributes**
- **Grazer · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 100
- **Not hunting/war trainable**
- **Size**
- **Birth:** 30,000 cm 3
- **Mid:** 150,000 cm 3
- **Max:** 300,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 10-12
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
- **Bones:** 13-15
- **Skull:** 1
- **Hooves:** 4
- **Horns:** 2 (males only)
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large hooved animal found roaming wild in temperate forests. The males have long antlers.*

**Elk** are animals who inhabit temperate grasslands and tundras, appearing in groups of 3-7 individuals. Five times heavier than a dwarf, they're benign meanderers who do little but wander around aimlessly, being relatively harmless and easy for hunters to take down. They possess some sexual dimorphism, with the males having a pair of antlers, though it doesn't give them the ability to gore enemies. They possess thick fur which provides them with increased insulation compared to most other animals, and their young are called *fawns*.

Elk can be captured in cage traps and trained into exotic pets. Given their large size, they provide a good amount of returns when butchered, making them valid targets for a meat industry. Products made from elk parts are worth twice more than those made from other, more common animals.

Some dwarves like elk for their *grace*.

Admired for its *grace*.

    12 kph

    [CREATURE:ELK]
        [DESCRIPTION:A large hooved animal found roaming wild in temperate forests.  The males have long antlers.]
        [NAME:elk:elk:elk]
        [CASTE_NAME:elk:elk:elk]
        [CREATURE_TILE:'E'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:100]
        [PET_EXOTIC]
        [STANDARD_GRAZER]
        [VISION_ARC:50:310]
        [PREFSTRING:grace]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [GRASSTRAMPLE:0]
        [BIOME:TUNDRA]
        [BIOME:GRASSLAND_TEMPERATE]
        [BENIGN][MEANDERER]
        [NATURAL]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        [CASTE:MALE]
            [MALE]
        [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:2HEAD_ANTLER:RIBCAGE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
                [STATE_NAME:ALL_SOLID:antler]
                [STATE_ADJ:ALL_SOLID:antler]
                [ANTLER]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:200]
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
        [BODY_SIZE:0:0:30000]
        [BODY_SIZE:1:0:150000]
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
        [CHILD:1][GENERAL_CHILD_NAME:elk fawn:elk fawns]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:366:244:122:1900:2900] 72 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
            [TL_COLOR_MODIFIER:BROWN:1]
                [TLCM_NOUN:hair:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                [TLCM_NOUN:skin:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
            [TL_COLOR_MODIFIER:BLACK:1]
                [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
