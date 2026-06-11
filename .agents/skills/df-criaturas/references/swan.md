# Swan

> Fonte: [Swan](https://dwarffortresswiki.org/index.php/Swan) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes swans for their beauty.**
- **Biome**
- **Any Temperate Lake Any Temperate Marsh**
- **Variations**
- **Swan - Swan man - Giant swan**
- **Attributes**
- **Flying · Egglaying**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 300 cm 3
- **Mid:** 5,000 cm 3
- **Max:** 10,000 cm 3
- **Food products**
- **Eggs:** 5-7
- **Age**
- **Adult at:** 1
- **Max age:** 10-25
- **Butchering returns**
- **Food items**
- **Meat:** 9
- **Fat:** 9
- **Brain:** 1
- **Gizzard:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Tripe:** 1
- **Raw materials**
- **Bones:** 6-8
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small aquatic bird, prized for its beauty.*

**Swans** are creatures who can be found in temperate lakes and marshes. These birds are benign and harmless to dwarves due to their small size, though pastured animals in the surface will flee from them when they fly near the ground, leading to your dwarves to constantly have to bring them back to their pasture. Males of the species are called *cob swans*, while females are called *pen swans* and hatchlings are called *cygnets*.

Swans can be captured in cage traps and trained into low-value pets. They're twice the size of a turkey, give prepared organs when butchered and lay a nice amount of eggs, making them a viable target for an exotic farm.

Some dwarves like swans for their *beauty*.

\

Admired for its *beauty*.

    1 kph

    Swans were sponsored by the generous contributions of the Bay 12 community.

        IL

    [CREATURE:BIRD_SWAN]
        [DESCRIPTION:A small aquatic bird, prized for its beauty.]
        [NAME:swan:swans:swan]
        [CHILD:1][GENERAL_CHILD_NAME:cygnet:cygnets]
        [CREATURE_TILE:'s'][COLOR:7:0:1]
        [NATURAL]
        [LARGE_ROAMING]
        [BIOME:ANY_TEMPERATE_LAKE]
        [BIOME:ANY_TEMPERATE_MARSH]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:2]
        [PETVALUE:10]
        [BENIGN][MEANDERER][PET_EXOTIC]
        [FLIER]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [PREFSTRING:beauty]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BILL:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS:FEATHER]
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
        [BODY_SIZE:0:0:300]
        [BODY_SIZE:1:0:5000]
        [BODY_SIZE:2:0:10000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:25]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:pen swan:pen swans:pen swan]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:340]
                [CLUTCH_SIZE:5:7]
        [CASTE:MALE]
            [CASTE_NAME:cob swan:cob swans:cob swan]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
