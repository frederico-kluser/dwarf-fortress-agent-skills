# Opossum

> Fonte: [Opossum](https://dwarffortresswiki.org/index.php/Opossum) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes opossums for their ability to play dead.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Opossum - Opossum man - Giant opossum**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 300 cm 3
- **Mid:** 1,500 cm 3
- **Max:** 3,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 2-4
- **Butchering returns**
- **Food items**
- **Meat:** 0-6
- **Fat:** 0-6
- **Raw materials**
- **Bones:** 0-4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small mammal resembling a large, white rat.*

**Opossums** are small, solitary animals found in many temperate biomes. Smaller than your average cat, they're benign and do little but meander around cluelessly, being easy prey for any dwarf who attempts to hunt them. They possess thick fur, which provides them with increased insulation compared to most other animals. A newborn opossum is called a *baby*.

Opossums can be captured in cage traps and trained into exotic pets of quite low value. Given their small size, they provide very few returns when butchered, making them poor targets for a meat industry.

Some dwarves like opossums for their *ability to play dead*.

Admired for its *ability to play dead*.

    1 kph

    Opossums were sponsored by the generous contributions of the Bay 12 community.

        The master-plan unfolds, silent sinister / Is there any hope left, Opossum Minister?

    [CREATURE:OPOSSUM]
        [DESCRIPTION:A small mammal resembling a large, white rat.]
        [NAME:opossum:opossums:opossum]
        [CASTE_NAME:opossum:opossums:opossum]
        [GENERAL_CHILD_NAME:baby opossum:baby opossums]
        [CREATURE_TILE:'o'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:10]
        [PET_EXOTIC]
        [NATURAL]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:GRASSLAND_TEMPERATE]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [BENIGN][MEANDERER]
        [PREFSTRING:ability to play dead]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:GENERIC_TEETH:RIBCAGE]
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
        [BODY_SIZE:0:0:300]
        [BODY_SIZE:1:0:1500]
        [BODY_SIZE:2:0:3000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:4]
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
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:3251:2446:1640:798:4600:6500] 11 kph
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
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
