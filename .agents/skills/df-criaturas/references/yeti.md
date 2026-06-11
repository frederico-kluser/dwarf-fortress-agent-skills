# Yeti

> Fonte: [Yeti](https://dwarffortresswiki.org/index.php/Yeti) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes yetis for their white fur.**
- **Biome**
- **Mountain Glacier Tundra**
- **Attributes**
- **Alignment:** Savage
- **Building destroyer : Level 2**
- **Fanciful · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 20,000 cm 3
- **Mid:** 100,000 cm 3
- **Max:** 300,000 cm 3
- **Age**
- **Child at:** 1
- **Adult at:** 10
- **Max age:** 800-1000
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 31-34
- **Fat:** 18
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 32-33
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large ape-like creature with white fur, found in the snowy wilds.*

**Yetis** are large, fanciful, dangerous creatures found only in savage mountains, tundras and glaciers. They are fully capable of massacring dozens of unarmed dwarves due to their large size, and their disposition to destroy buildings will draw them into contact with fortresses, where they will topple furniture and wreck workshops in their path. Yetis can equip items and open unlocked doors, though the former is not typically seen in normal play and the latter is normally ignored, as the yeti will simply destroy the whole door instead of opening it.

When players embark on a savage glacier, they should expect to encounter yetis. Due to a glacier's general lack of other animal life, the map will almost always spawn one yeti right after another, making them a deadly hazard for an early fortress. However, since they have a relatively low population number, no more than 5-10 yetis will spawn before they become extinct in your biome. Despite their humanoid physiology, yetis are not intelligent, and your dwarves will gleefully butcher them into food and bones for crafting. Items made from yeti parts are worth 3 times more than those of your standard domestic animals.

Yetis can be captured with cage traps, but cannot be trained. If the player doesn't want to butcher them for meat, their extremely long lifespan can make them valuable as permanent decorations for your fortress.

Some dwarves like yetis for their *white fur*.

-

  Admired for its *white fur*... From a distance...

-

  He's not evil, just not in the mood.\
  *Art by kruggsmash*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Though many take the yetis to be violent, demented beasts, some have been tamed (with great difficulty) and even integrated into dwarven society. This can be attributed to their joyful and cheery nature; often they can be seen playfully tipping over workshops and 'accidentally' crushing anyone working within. Many dwarves admire this warped sense of humour and the yeti's obvious love of beer, wine and spirits.

When faced with a mighty sasquatch, yetis become immense wimps, despite the Sasquatch being barely any different from them. Dwarven scientists think this is caused by the high contrast between a sasquatch's white skin and brown fur, which makes a simple-minded yeti panic.

    [CREATURE:YETI]
        [DESCRIPTION:A large ape-like creature with white fur, found in the snowy wilds.]
        [NAME:yeti:yetis:yeti]
        [CASTE_NAME:yeti:yetis:yeti]
        [CREATURE_TILE:'Y'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [CREATURE_CLASS:HUMANOID_TRACKING_SYMBOL]
        [CHILD:10][BABY:1][MULTIPLE_LITTER_RARE]
        [BIOME:MOUNTAIN]
        [BIOME:GLACIER]
        [BIOME:TUNDRA]
        [LARGE_ROAMING][SAVAGE][DIFFICULTY:2][FREQUENCY:1]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [BUILDINGDESTROYER:2]
        [LARGE_PREDATOR][MEANDERER]
        [FANCIFUL]
        [GRASSTRAMPLE:0]
        [BONECARN]
        [PREFSTRING:white fur]
        [BODY:HUMANOID_NECK:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:5FINGERS:5TOES:MOUTH:TONGUE:FACIAL_FEATURES:TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:300]
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
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
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
        [BODY_SIZE:0:0:20000]
        [BODY_SIZE:1:168:100000]
        [BODY_SIZE:20:0:300000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:800:1000]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_CANLATCH]
        [EQUIPS]
        [CANOPENDOORS]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_AZURE:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
