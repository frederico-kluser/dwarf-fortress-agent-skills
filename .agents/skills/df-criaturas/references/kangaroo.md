# Kangaroo

> Fonte: [Kangaroo](https://dwarffortresswiki.org/index.php/Kangaroo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kangaroos for their pouches.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Any Desert**
- **Variations**
- **Kangaroo - Kangaroo man - Giant kangaroo**
- **Attributes**
- **Grazer · Milkable · Humanoid**
- **Tamed Attributes**
- **Pet value:** 100
- **Not hunting/war trainable**
- **Size**
- **Birth:** 9,000 cm 3
- **Mid:** 45,000 cm 3
- **Max:** 90,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 14-17
- **Fat:** 11-16
- **Brain:** 1
- **Heart:** 0-1
- **Lungs:** 2
- **Intestines:** 0-1
- **Liver:** 1
- **Kidneys:** 0-2
- **Tripe:** 1
- **Sweetbread:** 0-1
- **Spleen:** 0-1
- **Raw materials**
- **Bones:** 10-22
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized creature that can be found hopping through the grassland.*

**Kangaroos** are a species of creature found in temperate and desert biomes, spawning in groups of 2–4 individuals. While bigger than a dwarf, these animals are benign and do little but meander around aimlessly, fleeing from dwarves who provoke them, and only rarely defending themselves with punches, potent kicks and bites. Males of the species are called *kangaroo bucks*, females are called *kangaroo does* and babies are called *kangaroo joeys*.

Kangaroos can be captured in cage traps and trained into pets. They are grazers; and therefore require a pasture to survive after being trained, but are distinct for being one of the only exotic sources of milk and cheese (the other being the tapir). They provide a good amount of returns when butchered, being large enough to produce prepared organs when adults. They reach their full size at 2 years of age, and therefore should be butchered at that point, if so wished, for maximum returns.

Some dwarves like kangaroos for their *pouches* and their *great leaps*.

\

Admired for its *great leaps*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Contrary to claims by human scholars, newborn kangaroos are not born without legs, nor are they smaller than rats.

    1 kph

    Kangaroos were sponsored by the generous contributions of the Bay 12 community.

        Whittacker: "I just want to see a dwarf get their bowels ripped out by one of these."
        Sponsored by Duncan Burke

    [CREATURE:KANGAROO]
        [DESCRIPTION:A medium-sized creature that can be found hopping through the grassland.]
        [NAME:kangaroo:kangaroos:kangaroo]
        [CHILD:1][GENERAL_CHILD_NAME:kangaroo joey:kangaroo joeys]
        [CREATURE_TILE:'K'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:100]
        [BIOME:GRASSLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:ANY_DESERT]
        [VISION_ARC:50:310]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:2:4]
        [PREFSTRING:pouches]
        [PREFSTRING:great leaps]
        [LARGE_ROAMING]
        [BENIGN][MEANDERER][PET_EXOTIC]
        [STANDARD_GRAZER]
        [BODY:HUMANOID_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH:RIBCAGE]
        [NATURAL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
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
        [BODY_SIZE:0:0:9000] not counting the small birth weight
        [BODY_SIZE:1:0:45000]
        [BODY_SIZE:2:0:90000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:KICK:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_VELOCITY_MODIFIER:3000]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_CANLATCH]
        [NOCTURNAL]
        [CREPUSCULAR]
        [HOMEOTHERM:10070]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:kangaroo doe:kangaroo does:kangaroo doe]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
                [STATE_NAME:ALL_SOLID:frozen kangaroo's milk]
                [STATE_ADJ:ALL_SOLID:frozen kangaroo's milk]
                [STATE_NAME:LIQUID:kangaroo's milk]
                [STATE_ADJ:LIQUID:kangaroo's milk]
                [STATE_NAME:GAS:boiling kangaroo's milk]
                [STATE_ADJ:GAS:boiling kangaroo's milk]
                [PREFIX:NONE]
            [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
            [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
                [STATE_NAME:SOLID:kangaroo cheese]
                [STATE_ADJ:SOLID:kangaroo cheese]
                [STATE_NAME:SOLID_POWDER:kangaroo cheese powder]
                [STATE_ADJ:SOLID_POWDER:kangaroo cheese powder]
                [STATE_NAME:LIQUID:melted kangaroo cheese]
                [STATE_ADJ:LIQUID:melted kangaroo cheese]
                [STATE_NAME:GAS:boiling kangaroo cheese]
                [STATE_ADJ:GAS:boiling kangaroo cheese]
                [PREFIX:NONE]
        [CASTE:MALE]
            [CASTE_NAME:kangaroo buck:kangaroo bucks:kangaroo buck]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BROWN:1] could be better
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
