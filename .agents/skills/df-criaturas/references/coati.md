# Coati

> Fonte: [Coati](https://dwarffortresswiki.org/index.php/Coati) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes coatis for their curiosity.**
- **Biome**
- **Any Temperate Forest Any Tropical Forest**
- **Variations**
- **Coati - Coati man - Giant coati**
- **Attributes**
- **Steals food · Steals items**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 600 cm 3
- **Mid:** 3,000 cm 3
- **Max:** 6,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 2-6
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, long-nosed raccoon-like creature.*

**Coatis** are small solitary creatures who inhabit both tropical and temperate forests. Slightly larger than the average cat, coatis will attempt to steal unguarded food and items from your fortress, and as such should be kept clear of your stockpiles. Dwarves will react aggressively to their presence and you may see your peasants attack and beat them to death without any input on your part, and their small size means they are generally harmless. Newborn coatis are called *babies*.

Coatis can be captured in cage traps and trained into exotic pets. Their small size means they'll give low returns when butchered, making them subpar as livestock. Consider looking for larger, meatier animals to produce food for your dwarves.

Some dwarves like coatis for their *curiosity*.

Admired for its *curiosity*.

    1 kph

    Coatis were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:COATI]
        [DESCRIPTION:A small, long-nosed raccoon-like creature.]
        [NAME:coati:coatis:coati]
        [CASTE_NAME:coati:coatis:coati]
        [GENERAL_CHILD_NAME:baby coati:baby coatis]
        [CREATURE_TILE:'c'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:50]
        [PET_EXOTIC]
        [CARNIVORE]
        [NATURAL]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:ANY_TROPICAL_FOREST]
        [CURIOUSBEAST_EATER]
        [CURIOUSBEAST_ITEM]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:curiosity]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:RODENT_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [GRASSTRAMPLE:0]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:100]
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
        [BODY_SIZE:0:0:600]
        [BODY_SIZE:1:0:3000]
        [BODY_SIZE:2:0:6000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:15]
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
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:722:545:325:1900:2900] 27 kph
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
                [TL_COLOR_MODIFIER:CHESTNUT:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
