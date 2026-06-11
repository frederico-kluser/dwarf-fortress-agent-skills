# Goose

> Fonte: [Goose](https://dwarffortresswiki.org/index.php/Goose) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes geese for their formation flying.**
- **Biome**
- **Any Temperate Lake Any Temperate Marsh Domesticated**
- **Attributes**
- **Flying · Egglaying**
- **Tamed Attributes**
- **Pet value:** 10
- **Not hunting/war trainable**
- **Size**
- **Birth:** 150 cm 3
- **Mid:** 2,250 cm 3
- **Max:** 4,500 cm 3
- **Food products**
- **Eggs:** 3-8
- **Age**
- **Adult at:** 1
- **Max age:** 10-24
- **Butchering returns**
- **Food items**
- **Meat:** 8-9
- **Fat:** 8-9
- **Intestines:** 1
- **Raw materials**
- **Bones:** 6
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small migratory bird. It has a very long neck and can be found in lakes and other bodies of water.*

**Geese** are domestic waterfowl that can also be found in wild populations. A male goose is called a *gander*, and young geese are called *goslings*. Of the common domestic egg-laying animals, the goose is the second largest; only the turkey is larger. The turkey, however, requires two years to reach full size and provides only a couple more meat, meaning the goose provides similar meat in half the time.

Because of their good size, the fact they reach adulthood and full size in only one year, and low embark cost, geese are, cost-wise, perhaps the best starter animals for the meat industry or as sources of bones. Although they lay eggs, they lay the fewest eggs of all domestic birds, making guineafowl or turkey more attractive for eating eggs, while goose eggs are used to raise geese for slaughter.

Note that geese can fly, even while assigned to pastures. If they get up on a roof you will experience a large amount of spam as dwarves attempt to return them to their pasture. This can be avoided by keeping them away from elevated surfaces that your dwarves cannot access. Alternatively, simply remove them from the pasture to prevent further repasturing jobs.

Some dwarves like geese for their *formation flying*.

\

Admired for their *formation flying*.

\

|  |
|----|
| "Goose" in other / Languages / Dwarven / : / kurig / Elven / : / abime / Goblin / : / us / Human / : / jathbi |

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Geese are prone to inconvenience dwarves by picking up and misplacing important items for no apparent purpose other than annoy them. A single goose can lead to dozens of job canceling reports as every dwarf in the vicinity converges on the dreadful bird to reclaim the stolen goods. They are especially keen on stealing percussion instruments with a bell component.

## See also

- Comparison of domestic poultry

    [CREATURE:BIRD_GOOSE]
        [DESCRIPTION:A small migratory bird.  It has a very long neck and can be found in lakes and other bodies of water.]
        [NAME:goose:geese:goose]
        [CHILD:1][GENERAL_CHILD_NAME:gosling:goslings]
        [CREATURE_TILE:'g'][COLOR:7:0:1]
        [BIOME:ANY_TEMPERATE_LAKE]
        [BIOME:ANY_TEMPERATE_MARSH]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [NATURAL]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC]
        [PETVALUE:10]
        [BENIGN][MEANDERER][PET]
        [GOBBLE_VERMIN_CLASS:EDIBLE_GROUND_BUG]
        [VISION_ARC:50:310]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:4732:4026:3327:1097:5922:7567] 8 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:411:274:137:1900:2900] 64 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [PREFSTRING:formation flying]
        [FLIER]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BILL:RIBCAGE]
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
        [BODY_SIZE:0:0:150]
        [BODY_SIZE:0:168:2250]
        [BODY_SIZE:1:0:4500]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:24]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ROOT_AROUND:BY_CATEGORY:BEAK:root around in:roots around in]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:goose:geese:goose]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:152]
                [CLUTCH_SIZE:3:8]
        [CASTE:MALE]
            [CASTE_NAME:gander:ganders:gander]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
