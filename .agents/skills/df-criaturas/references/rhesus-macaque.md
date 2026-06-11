# Rhesus macaque

> Fonte: [Rhesus macaque](https://dwarffortresswiki.org/index.php/Rhesus_macaque) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rhesus macaques for their mischief.**
- **Biome**
- **Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Rhesus macaque - Rhesus macaque man - Giant rhesus macaque**
- **Attributes**
- **Steals food · Steals items**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 500 cm 3
- **Mid:** 2,500 cm 3
- **Max:** 5,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 30-40
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 6
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized monkey found in woods and grassland. It usually lives on roots and insects but can become a pest in civilized areas, roaming in large groups and begging for scraps.*

**Rhesus macaques** are small creatures found in many temperate biomes, spawning in loose groups of 5 to 10 individuals with the intent to steal your fortress - they are not cute little chimps that wear tiny tuxedos and dance to calypso music. They are larger, meaner, and considerably more likely to leave teeth marks in the neck of any working dwarf foolish enough to get in their way. If they exist on a map, they *will* be trouble at one point or another. They are known for stealing pretty much everything, including food, items, weapons, armor, and artifacts. Weight is no consideration; they'll steal your one and only anvil as quickly as they will your bag of plump helmet seeds. All rhesus macaques are born with Legendary skill in climbing.

Fortunately, they can be dispatched without too much trouble due to their small size, and will often flee when faced with even the most ludicrously underpowered militia. War dogs will also usually make quick work of them, though it is generally recommended to take all important items underground as soon as possible when embarking in a macaque-inhabited area, as a group of them can quickly swarm an undefended wagon "Wagon (embark)"). They are essentially flightless kea and should be treated accordingly.

Rhesus macaques can be captured in cage traps and trained into low-value pets. While they can be bred to supplement a meat industry, they are small and yield few products when butchered. They also take 3 years to reach adulthood, much longer than more accessible sources of food, which may not be worth waiting for.

Some dwarves like rhesus macaques for their *mischief*.

Admired for its *mischief*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
It has been suggested by some that diced rhesus macaque meat cooked with dwarven syrup is used for a tasty dwarven candy, or Rhesus Pieces. [1]

Some insane dwarves find the mammalian features of macaques exceptionally hilarious, laughing hysterically as they run around giggling "Macaques really hairy!" All dwarves who exhibit this symptom defy all laws of insanity by showing no signs that they would become insane; One case even had a dwarf return to normal life before being eaten alive by a group of hungry, hungry hippos.

    12 kph

    [CREATURE:MACAQUE_RHESUS]
        [DESCRIPTION:A medium-sized monkey found in woods and grassland.  It usually lives on roots and insects but can become a pest in civilized areas, roaming in large groups and begging for scraps.]
        [NAME:rhesus macaque:rhesus macaques:rhesus macaque]
        [CASTE_NAME:rhesus macaque:rhesus macaques:rhesus macaque]
        [CREATURE_TILE:'m'][COLOR:7:0:0]
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
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:GRASSLAND_TEMPERATE]
        [PREFSTRING:mischief]
        [BODY:QUADRUPED_NECK_FRONT_GRASP:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:5TOES_FQ_FINGERS:5TOES_RQ_ANON:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE:FACIAL_FEATURES]
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
        [BODY_SIZE:0:0:500]
        [BODY_SIZE:1:0:2500]
        [BODY_SIZE:2:0:5000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:30:40]
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
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
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
