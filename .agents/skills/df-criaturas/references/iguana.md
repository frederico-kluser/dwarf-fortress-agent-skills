# Iguana

> Fonte: [Iguana](https://dwarffortresswiki.org/index.php/Iguana) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes iguanas for their dewlaps.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Iguana - Iguana man - Giant iguana**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 400
- **Not hunting/war trainable**
- **Size**
- **Birth:** 15 cm 3
- **Mid:** 500 cm 3
- **Max:** 4,000 cm 3
- **Food products**
- **Eggs:** 40-50
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 6
- **Fat:** 6
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A relatively large arboreal lizard found in the tropical forests. Though it is a vegetarian, and mainly docile, it may whip with its extremely long tail when angered.*

**Iguanas** are small exotic reptiles found in all tropical forests. They are relatively rare and are solitary, only spawning one at a time. Despite their description, they are carnivorous, but due to being roughly the size of cats, they rarely present any danger to a dwarf. Likewise, they cannot actually attack with their tails.

Iguanas possess a respectable pet value for a creature of their size, making them valuable pets. Additionally, they lay between 40 to 50 eggs at a time, being the second most egg-laying non-vermin creature found in the surface after the saltwater crocodile, which makes them excellent for egg production. Elven caravans may bring tame iguanas with them, which serves as an easy way of acquiring the creatures. In case you capture a pair of opposite sexes, be wary that breeding them will inevitably lead to an iguanasplosion which may be harmful to your FPS.

Some dwarves like iguanas for their *dewlaps* and their *head bobs*.

Admired for its *dewlaps*.

    12 kph

    [CREATURE:IGUANA]
        [DESCRIPTION:A relatively large arboreal lizard found in the tropical forests.  Though it is a vegetarian, and mainly docile, it may whip with its extremely long tail when angered.]
        [NAME:iguana:iguanas:iguana]
        [CASTE_NAME:iguana:iguanas:iguana]
        [CHILD:1][GENERAL_CHILD_NAME:iguana hatchling:iguana hatchlings]
        [CREATURE_TILE:'i'][COLOR:2:0:1]
        [BIOME:ANY_TROPICAL_FOREST]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [CARNIVORE][NATURAL]
        [MEANDERER]
        [PETVALUE:400]
        [PET_EXOTIC]
        [GRASSTRAMPLE:20]
        [PREFSTRING:head bobs]
        [PREFSTRING:dewlaps]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
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
        [BODY_SIZE:0:0:15]
        [BODY_SIZE:1:0:500]
        [BODY_SIZE:3:0:4000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:15]
                [CLUTCH_SIZE:40:50]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:GREEN:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
