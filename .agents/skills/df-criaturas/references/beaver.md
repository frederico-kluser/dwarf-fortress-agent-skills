# Beaver

> Fonte: [Beaver](https://dwarffortresswiki.org/index.php/Beaver) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes beavers for their dams.**
- **Biome**
- **Any Temperate Lake Any Temperate River**
- **Variations**
- **Beaver - Beaver man - Giant beaver**
- **Tamed Attributes**
- **Pet value:** 25
- **Not hunting/war trainable**
- **Size**
- **Birth:** 2,000 cm 3
- **Mid:** 10,000 cm 3
- **Max:** 20,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-20
- **Butchering returns**
- **Food items**
- **Meat:** 12-13
- **Fat:** 12-13
- **Brain:** 1
- **Heart:** 0-1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 0-2
- **Tripe:** 1
- **Sweetbread:** 0-1
- **Spleen:** 0-1
- **Raw materials**
- **Bones:** 10-12
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small river mammal with a flat tail, known for building wooden dams.*

**Beavers** are creatures found in temperate lakes and rivers, where they appear in groups of 3-10 individuals. Comparable in size to kobolds, beavers are benign meanderers who are more likely to flee from dwarves than provoke them. They possess thick fur which provides them with increased insulation compared to most other animals. A newborn beaver is called a *kit*.

Beavers can be captured in cage traps and trained into cheap exotic pets. They provide a fair amount of returns when butchered and live for up to two decades, making a beaver farm a potential proposition for your meat industry. Fortunately or unfortunately, beavers in *Dwarf Fortress* do not actually build dams.

Some dwarves like beavers for their *dams* and their *tree-felling habits*.

Admired for their *dams*.

    12 kph

    Beavers were sponsored by the generous contributions of the Bay 12 community.

        Lord Darkstar

    [CREATURE:BEAVER]
        [DESCRIPTION:A small river mammal with a flat tail, known for building wooden dams.]
        [NAME:beaver:beavers:beaver]
        [CASTE_NAME:beaver:beavers:beaver]
        [GENERAL_CHILD_NAME:beaver kit:beaver kits]
        [CREATURE_TILE:'b'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:25]
        [PET_EXOTIC]
        [NATURAL]
        [BIOME:ANY_TEMPERATE_LAKE]
        [BIOME:ANY_TEMPERATE_RIVER]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:10]
        [BENIGN][MEANDERER]
        [PREFSTRING:dams]
        [PREFSTRING:tree-felling habits]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:RODENT_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [GRASSTRAMPLE:0]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:200]
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
        [BODY_SIZE:0:0:2000]
        [BODY_SIZE:1:0:10000]
        [BODY_SIZE:2:0:20000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:20]
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
        [CHILD:1]
        [NOCTURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:1422:1127:831:488:2500:3700] 18 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:5341:4723:4112:1254:6433:7900] 7 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
