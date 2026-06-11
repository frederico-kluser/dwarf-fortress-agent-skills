# Hyena

> Fonte: [Hyena](https://dwarffortresswiki.org/index.php/Hyena) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hyenas for their coordinated hunting.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland**
- **Variations**
- **Hyena - Hyena man - Giant hyena**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 6,000 cm 3
- **Mid:** 30,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-25
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 12-13
- **Fat:** 12-13
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
- **Bones:** 12-16
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized pack predator found in the savanna.*

**Hyenas** are rare carnivorous animals who inhabit tropical flatlands, where they appear in packs of 5-15 individuals. As heavy as a dwarf, these predators' high numbers make them a threat to a lone individual if they're unlucky enough to be caught in their path, especially in adventurer mode, though their very low frequency rate means they may not even be encountered at all. They possess thick fur which provides them with increased insulation compared to most other animals. A newborn hyena is called a *cub*.

Hyenas can be captured in cage traps and trained into low-value exotic pets, and fully tame individuals may be brought in elven caravans. They give a decent amount of returns if butchered, but their rarity makes them poor targets for a meat industry. Products made from hyena parts are worth twice more than those made from more common animals.

Some dwarves like hyenas for their *distinctive laugh* and their *coordinated hunting*.

Admired for its *distinctive laugh*.

    1 kph

    Hyenas were sponsored by the generous contributions of the Bay 12 community.
        xnrad likes hyenas for their distinctive laugh
        Cruxador

    [CREATURE:HYENA]
        [DESCRIPTION:A medium-sized pack predator found in the savanna.]
        [NAME:hyena:hyenas:hyena]
        [CASTE_NAME:hyena:hyenas:hyena]
        [CHILD:1][GENERAL_CHILD_NAME:hyena cub:hyena cubs]
        [CREATURE_TILE:'h'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [LARGE_PREDATOR][MEANDERER]
        [LARGE_ROAMING][FREQUENCY:5]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:GRASSLAND_TROPICAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:5:15]
        [GRASSTRAMPLE:0][NATURAL]
        [PETVALUE:50]
        [PET_EXOTIC]
        [BONECARN]
        [PREFSTRING:distinctive laugh]
        [PREFSTRING:coordinated hunting]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:4TOES_RQ_REG:MOUTH:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
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
        [BODY_SIZE:0:0:6000]
        [BODY_SIZE:1:0:30000]
        [BODY_SIZE:2:0:60000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:25]
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
        [NOCTURNAL]
        [CREPUSCULAR]
        [HOMEOTHERM:10070]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
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
                [TL_COLOR_MODIFIER:SPOTS_TAN_BLACK:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_ORANGE:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
