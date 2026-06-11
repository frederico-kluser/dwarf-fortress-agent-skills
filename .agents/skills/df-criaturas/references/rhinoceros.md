# Rhinoceros

> Fonte: [Rhinoceros](https://dwarffortresswiki.org/index.php/Rhinoceros) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rhinoceroses for their horns.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland**
- **Variations**
- **Rhinoceros - Rhinoceros man - Giant rhinoceros**
- **Attributes**
- **War animals · Grazer · Exotic mount · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : War**
- **Size**
- **Birth:** 300,000 cm 3
- **Mid:** 1,500,000 cm 3
- **Max:** 3,000,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 40-50
- **Butchering returns ( Value multiplier ×5)**
- **Food items**
- **Meat:** 45-82
- **Fat:** 12-32
- **Brain:** 2-4
- **Heart:** 1-2
- **Lungs:** 4-8
- **Intestines:** 7-13
- **Liver:** 2-4
- **Kidneys:** 2-4
- **Tripe:** 2-4
- **Sweetbread:** 1-2
- **Eyes:** 2
- **Spleen:** 1-2
- **Raw materials**
- **Bones:** 36-48
- **Skull:** 1
- **Teeth:** 1
- **Horns:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge herbivore with thick plated skin and powerful build. It is known for the thick horns on the end of its nose.*

**Rhinoceroses** are creatures found in tropical plains, where they appear in herds of 3 to 7 individuals. These massive animals are among the largest mundane land creatures in the game, essentially being smaller elephants, though they're benign meanderers, more prone to fleeing from dwarves than attacking them. If pushed over the edge, however, a rhinoceros will quickly turn a dwarf into paste under its weight. A newborn rhinoceros is called a *calf*.

Rhinoceroses can be captured in cage traps and trained into valuable exotic pets. They become grazers after being trained and, as such, require a pasture, and due to their great size, they require a significant patch of grass. They can receive additional war training as well, which will remove their benign demeanor and turn them into one of the strongest war beasts you could possibly have, though their [`[MEANDERER]`](/index.php/Creature_token#MEANDERER "Creature token") tag will cause them to move around very slowly. They also make excellent livestock, as a butchered rhinoceros will provide plentiful returns which are worth *five* times more than those made from common animals. Rhinoceroses take 10 years to reach maturity, although they're fully grown by the age of 5. Additionally, they are exotic mounts and, as such, may appear ridden by surface races during sieges, providing much fun to an unprepared fortress.

Some dwarves like rhinoceroses for their *horns*.

Admired for their *horns*.

Estimated Rhinoceros Size Comparison.

    5 kph

    [CREATURE:RHINOCEROS]
        [DESCRIPTION:A huge herbivore with thick plated skin and powerful build.  It is known for the thick horns on the end of its nose.]
        [NAME:rhinoceros:rhinoceroses:rhinoceros]
        [CASTE_NAME:rhinoceros:rhinoceroses:rhinoceros]
        [CHILD:10][GENERAL_CHILD_NAME:rhinoceros calf:rhinoceros calves]
        [CREATURE_TILE:'R'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:500]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [STANDARD_GRAZER]
        [VISION_ARC:50:310]
        [TRAINABLE_WAR]
        [LARGE_ROAMING]
        [BIOME:GRASSLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [BENIGN][MEANDERER][NATURAL]
        [PREFSTRING:horns]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE:2HEAD_HORN_NUMBERED]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
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
        [BODY_SIZE:0:0:300000]
        [BODY_SIZE:2:0:1500000]
        [BODY_SIZE:5:0:3000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:40:50]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:GORE:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
        [DIURNAL]
        [HOMEOTHERM:10066]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1:IRIS_EYE_GOLD:1:IRIS_EYE_YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:5]
