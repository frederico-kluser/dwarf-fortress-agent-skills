# Kingsnake

> Fonte: [Kingsnake](https://dwarffortresswiki.org/index.php/Kingsnake) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kingsnakes for their coloration.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Mountain Any Desert**
- **Variations**
- **Kingsnake - Kingsnake man - Giant kingsnake**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20 cm 3
- **Mid:** 750 cm 3
- **Max:** 1,500 cm 3
- **Food products**
- **Eggs:** 5-12
- **Age**
- **Adult at:** Birth
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 1
- **Fat:** 1
- **Raw materials**
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, brightly-colored snake. It is known for eating other snakes and being mistaken for its venomous cousins.*

**Kingsnakes** are small, solitary animals found in a variety of different biomes. As their description implies, they carry no syndrome unlike some other snakes, making them entirely harmless to the average dwarf. Like other snakes, they continuously grow through their entire lives, though notably never reach their full size; they require 60 years to reach 1,500 cm³ (which's only about as big as a guineafowl), but only live up to 30 years.

Kingsnakes can be captured in cage traps and trained into exotic pets. They are born adults and as such can't be fully tamed. While virtually useless for a meat industry, they can be placed in a nest box to lay eggs, being roughly equivalent to ducks in egg-laying prowess.

Some dwarves like kingsnakes for their *coloration* and their *habit of eating other snakes*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some humans may write music about how these creatures crawl. It is sometimes thought that they slither, but these humans have shown much foresight in looking at the raws- Without legs, these creatures could only be able to crawl. Good job, humans.

|  |
|----|
| "Kingsnake" in other / Languages / Dwarven / : / etar therleth / Elven / : / afedo imaza / Goblin / : / zozlo slorust / Human / : / deng rosha |

Admired for its *habit of eating other snakes*.

    1 kph

    Kingsnakes were sponsored by the generous contributions of the Bay 12 community.

        I'm a crawlin' kingsnake, baby.
        Ouroboros

    [CREATURE:KINGSNAKE]
        [DESCRIPTION:A small, brightly-colored snake.  It is known for eating other snakes and being mistaken for its venomous cousins.]
        [NAME:kingsnake:kingsnakes:kingsnake]
        [CASTE_NAME:kingsnake:kingsnakes:kingsnake]
        [CREATURE_TILE:'k'][COLOR:7:0:1]
        [PETVALUE:50]
        [PET_EXOTIC]
        [FREQUENCY:40]
        [NATURAL]
        [CARNIVORE]
        [LARGE_ROAMING]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:MOUNTAIN]
        [BIOME:ANY_DESERT]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:habit of eating other snakes]
        [PREFSTRING:coloration]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH_WITH_FANGS:RIBCAGE]
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
        [BODY_SIZE:0:0:20]
        [BODY_SIZE:2:0:750]
        [BODY_SIZE:60:0:1500]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [MUNDANE]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:20] no info
                [CLUTCH_SIZE:5:12]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:STRIPES_BLACK_WHITE:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
