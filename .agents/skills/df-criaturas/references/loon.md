# Loon

> Fonte: [Loon](https://dwarffortresswiki.org/index.php/Loon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes loons for their coloration.**
- **Biome**
- **Temperate Saltwater Lake Temperate Brackish Lake Temperate Freshwater Lake**
- **Variations**
- **Loon - Loon man - Giant loon**
- **Attributes**
- **Flying · Egglaying**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 150 cm 3
- **Mid:** 3,000 cm 3
- **Max:** 6,000 cm 3
- **Food products**
- **Eggs:** 2-4
- **Age**
- **Adult at:** 1
- **Max age:** 25-30
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

*A small water bird found in remote lakes. It is known for its haunting call.*

**Loons** are a species of bird found inhabiting temperate lakes, appearing in groups of anywhere between 1-4 individuals. They do little but fly through the air and are only slightly bigger than a cat, being benign and harmless to all but the most unlucky of dwarves.

Loons can be captured in cage traps and trained into cheap pets. They produce butchering returns equivalent to a turkey, though being flying wild animals, they are considerably harder to catch. If put in a nest box, they lay an average of 3 eggs at a time, making them a subpar choice for egg production.

Some dwarves like loons for their *coloration* and their *haunting call*.

Admired for its *haunting call*.

    1 kph

    Loons were sponsored by the generous contributions of the Bay 12 community.

        IL
        Usurper
        Sponsored by Klokwurk. You can't get better than awesome!

    [CREATURE:BIRD_LOON]
        [DESCRIPTION:A small water bird found in remote lakes.  It is known for its haunting call.]
        [NAME:loon:loons:loon]
        [CASTE_NAME:loon:loons:loon]
        [CHILD:1][GENERAL_CHILD_NAME:loon chick:loon chicks]
        [CREATURE_TILE:'l'][COLOR:0:0:1]
        [NATURAL]
        [LARGE_ROAMING]
        [BIOME:LAKE_TEMPERATE_SALTWATER]
        [BIOME:LAKE_TEMPERATE_BRACKISHWATER]
        [BIOME:LAKE_TEMPERATE_FRESHWATER]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
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
        [PREFSTRING:haunting call]
        [PREFSTRING:coloration]
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
        [BODY_SIZE:0:0:150]
        [BODY_SIZE:1:0:3000]
        [BODY_SIZE:2:0:6000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:25:30]
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
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:152]
                [CLUTCH_SIZE:2:4]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BLACK:1] more than this
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
