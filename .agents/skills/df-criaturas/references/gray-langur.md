# Gray langur

> Fonte: [Gray langur](https://dwarffortresswiki.org/index.php/Gray_langur) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gray langurs for their vocalizations.**
- **Biome**
- **Any Desert Any Grassland Any Savanna Any Shrubland Any Forest**
- **Variations**
- **Gray langur - Gray langur man - Giant gray langur**
- **Attributes**
- **Steals food · Steals items**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,500 cm 3
- **Mid:** 7,500 cm 3
- **Max:** 15,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 30-40
- **Butchering returns**
- **Food items**
- **Meat:** 7-12
- **Fat:** 11
- **Brain:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Tripe:** 1
- **Raw materials**
- **Bones:** 10
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small monkey that can be found in forests and the streets of towns.*

**Gray langurs** are small, thieving creatures that can be found in almost any biome, spawning in loose groups of 5-10 individuals. They will attempt to steal food and items from your fortress, and if confronted, they may attack dwarves to defend themselves, but generally stand no chance against a hunter or even an unarmed peasant in a one-on one fight. Dwarves react violently to the presence of gray langurs, generally leading to your civilians going on wild chases after them whenever they pop up in your map, so they can punch the monkeys to death. All gray langurs are born with Legendary skill in climbing.

Gray langurs may be captured in cage traps and trained into exotic pets. They give a low quantity of returns when butchered, making them poor choices for livestock, but are fairly long-lived animals. Unlike most creatures, gray langurs reach adulthood at 3 years of age, though they're fully grown by the age of 2.

Some dwarves like gray langurs for their *social nature* and their *vocalizations*.

Admired for its *vocalizations*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Although Dwarven ethics frowns upon the human habit of hunting for trophy animals, Dwarves have realized that there is nothing more merciful than dropping their current task to cave in the nearest langur's skull with their bare hands. Dwarves don't do this for fun, it's for the good of the fortress as a whole. Please don't miss the next lecture on Dwarven Ethics 101!

    1 kph

    Gray langurs were sponsored by the generous contributions of the Bay 12 community.

        Rose

    [CREATURE:GRAY_LANGUR]
        [DESCRIPTION:A small monkey that can be found in forests and the streets of towns.]
        [NAME:gray langur:gray langurs:gray langur]
        [CASTE_NAME:gray langur:gray langurs:gray langur]
        [CREATURE_TILE:'l'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [NATURAL]
        [PETVALUE:50]
        [PET_EXOTIC]
        [CURIOUSBEAST_EATER]
        [CURIOUSBEAST_ITEM]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING][FREQUENCY:10]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:5:10][LOOSE_CLUSTERS]
        [BIOME:ANY_DESERT]
        [BIOME:ANY_GRASSLAND]
        [BIOME:ANY_SAVANNA]
        [BIOME:ANY_SHRUBLAND]
        [BIOME:ANY_FOREST]
        [PREFSTRING:social nature]
        [PREFSTRING:vocalizations]
        [BODY:QUADRUPED_NECK_FRONT_GRASP:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:5TOES_FQ_FINGERS:5TOES_RQ_ANON:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE:FACIAL_FEATURES]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
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
        [BODY_SIZE:0:0:1500]
        [BODY_SIZE:1:0:7500]
        [BODY_SIZE:2:0:15000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:30:40] 30+ years
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
        [CHILD:3]
        [DIURNAL]
        [HOMEOTHERM:10069]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:711:521:293:1900:2900] 30 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2206:1692:1178:585:3400:4900] 15 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph, NO DATA
        [NATURAL_SKILL:CLIMBING:15]
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
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
