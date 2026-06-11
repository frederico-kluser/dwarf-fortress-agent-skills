# Bobcat

> Fonte: [Bobcat](https://dwarffortresswiki.org/index.php/Bobcat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bobcats for their short tails.**
- **Biome**
- **Any Forest Any Desert Tropical Freshwater Swamp Tropical Saltwater Swamp Temperate Freshwater Swamp Temperate Saltwater Swamp Mangrove Swamp Mountain**
- **Variations**
- **Bobcat - Bobcat man - Giant bobcat**
- **Attributes**
- **War animals · Hunting animals**
- **Tamed Attributes**
- **Pet value:** 75
- **Trainable : Hunting War**
- **Size**
- **Birth:** 800 cm 3
- **Mid:** 4,000 cm 3
- **Max:** 8,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-35
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 8
- **Fat:** 7
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small feline predator with a shortened tail.*

**Bobcats** are small feline creatures found in a variety of biomes. Extremely uncommon to encounter, they spawn individually, and no more than a measly 3 of them will exist in one map before being considered locally extinct. While carnivorous, they're only a little larger than common cats and will rarely, if ever pose a threat to any adult dwarf. Bobcat kittens take 3 years to reach adulthood, a strange characteristic for an animal so small.

Bobcats can be captured in cage traps and trained into pets. They can be further turned into war or hunting beasts, but the fact they're under half the size of a dog simply makes them too small to be of any effect. Products made from bobcat parts are worth twice as much as those made from common animals, though as noted, unless the player purposely breeds them, they'll run out of bobcats to use extremely quickly.

Some dwarves like bobcats for their *short tails*.

Admired for their *short tails*.

    5 kph

    Bobcats were sponsored by the generous contributions of the Bay 12 community.

        MarineMorton

    [CREATURE:BOBCAT]
        [DESCRIPTION:A small feline predator with a shortened tail.]
        [NAME:bobcat:bobcats:bobcat]
        [CASTE_NAME:bobcat:bobcats:bobcat]
        [CHILD:3][GENERAL_CHILD_NAME:bobcat kitten:bobcat kittens]
        [CREATURE_TILE:'b'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:75]
        [PET_EXOTIC]
        [TRAINABLE]
        [BIOME:ANY_FOREST]
        [BIOME:ANY_DESERT]
        [BIOME:SWAMP_TROPICAL_FRESHWATER]
        [BIOME:SWAMP_TROPICAL_SALTWATER]
        [BIOME:SWAMP_TEMPERATE_FRESHWATER]
        [BIOME:SWAMP_TEMPERATE_SALTWATER]
        [BIOME:SWAMP_MANGROVE]
        [BIOME:MOUNTAIN]
        [LARGE_ROAMING][FREQUENCY:5]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CARNIVORE][NATURAL]
        [MEANDERER]
        [GRASSTRAMPLE:0]
        [PREFSTRING:short tails]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:4TOES_RQ_REG:MOUTH:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
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
        [BODY_SIZE:0:0:800]
        [BODY_SIZE:1:0:4000]
        [BODY_SIZE:2:0:8000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:35]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:CLAW]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
        [CREPUSCULAR]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:699:497:266:1900:2900] 33 kph
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
                [TL_COLOR_MODIFIER:SPOTS_ORANGE_BLACK:990:BLACK:10:WHITE:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_GREEN-YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
