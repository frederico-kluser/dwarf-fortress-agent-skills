# Puffin

> Fonte: [Puffin](https://dwarffortresswiki.org/index.php/Puffin) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes puffins for their colorful beaks.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Puffin - Puffin man - Giant puffin**
- **Attributes**
- **Flying · Egglaying**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 30 cm 3
- **Mid:** 375 cm 3
- **Max:** 750 cm 3
- **Food products**
- **Eggs:** 1
- **Age**
- **Adult at:** 1
- **Max age:** 15-20
- **Butchering returns**
- **Food items**
- **Raw materials**
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny diving bird found living on seaside cliffs in the colder climates.*

**Puffins** are a species of bird found in the coast of arctic oceans. They appear individually and are entirely benign, doing little but fly through the air aimlessly. They are one of the smallest animals in the game who aren't outright vermin, making them harmless to all but the most unlucky of dwarves.

Puffins can be captured in cage traps and trained into cheap pets. Hunted puffins are too small to be butchered and slaughtered trained ones will only yield a skull, making them useless for a meat industry. In addition, they only lay a single egg at a time, making them overall terrible animals for livestock.

Some dwarves like puffins for their *colorful beaks*.

Admired for their *colorful beaks*.

    1 kph

    Puffins were sponsored by the generous contributions of the Bay 12 community.

        Sponsored on behalf of Ekaterina Puffini

    [CREATURE:BIRD_PUFFIN]
        [DESCRIPTION:A tiny diving bird found living on seaside cliffs in the colder climates.]
        [NAME:puffin:puffins:puffin]
        [CASTE_NAME:puffin:puffins:puffin]
        [CHILD:1][GENERAL_CHILD_NAME:puffin chick:puffin chicks]
        [CREATURE_TILE:'p'][COLOR:0:0:1]
        [NATURAL]
        [LARGE_ROAMING]
        [BIOME:OCEAN_ARCTIC]
        [POPULATION_NUMBER:30:50]
        [CLUSTER_NUMBER:5:10]
        [PETVALUE:10]
        [BENIGN][PET_EXOTIC]
        [FLIER]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [PREFSTRING:colorful beaks]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:RIBCAGE]
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
        [BODY_SIZE:0:0:30]
        [BODY_SIZE:1:0:375]
        [BODY_SIZE:2:0:750]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:20]
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
                [EGG_SIZE:30] no data
                [CLUTCH_SIZE:1:1]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BLACK:1] white part
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
