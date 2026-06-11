# Desert tortoise

> Fonte: [Desert tortoise](https://dwarffortresswiki.org/index.php/Desert_tortoise) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes desert tortoises for their shells.**
- **Biome**
- **Any Desert**
- **Variations**
- **Desert tortoise - Desert tortoise man - Giant desert tortoise**
- **Attributes**
- **Shell · Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 40 cm 3
- **Mid:** 2,750 cm 3
- **Max:** 5,500 cm 3
- **Food products**
- **Eggs:** 3-5
- **Age**
- **Adult at:** 1
- **Max age:** 80-100
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 6
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Shell:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny shelled reptile that lives in the desert.*

**Desert tortoises** are small creatures found in desert biomes. They spawn individually and do little but wander around aimlessly. They are only slightly bigger than the average cat and will run away when threatened, making them harmless to all but the most unlucky of dwarves. They are one of the few sources of shells in deserts, and the only one when there's no water available.

Desert tortoises can be captured in cage traps and trained into low-value pets. They produce a meager amount of food and bones when butchered, and lay a low number of eggs compared to most domestic poultry. As expected from tortoises, they are quite long-lived, making them long lasting companions for dwarves who adopt them.

Some dwarves like desert tortoises for their *shells* and their *longevity*.

\

Admired for its *longevity*.

\

    12 kph

    Desert tortoises were sponsored by the generous contributions of the Bay 12 community.

        Zari

    [CREATURE:DESERT TORTOISE]
        [DESCRIPTION:A tiny shelled reptile that lives in the desert.]
        [NAME:desert tortoise:desert tortoises:desert tortoise]
        [CASTE_NAME:desert tortoise:desert tortoises:desert tortoise]
        [CHILD:1][GENERAL_CHILD_NAME:desert tortoise hatchling:desert tortoise hatchlings]
        [CREATURE_TILE:'t'][COLOR:6:0:0]
        [PETVALUE:50]
        [BENIGN][NATURAL][PET_EXOTIC]
        [BIOME:ANY_DESERT]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:10:30]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:shells]
        [PREFSTRING:longevity]
        [CANNOT_JUMP]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:RIBCAGE:SHELL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:SHELL:SHELL_TEMPLATE]
                [STATE_COLOR:ALL:BROWN]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_TISSUE_TEMPLATE:SHELL:SHELL_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:SHELL_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:80:100]
        [BODY_SIZE:0:0:40]
        [BODY_SIZE:2:0:2750]
        [BODY_SIZE:5:0:5500]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [DIURNAL]
        [CREPUSCULAR]
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:40] no data
                [CLUTCH_SIZE:3:5]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
