# Black bear

> Fonte: [Black bear](https://dwarffortresswiki.org/index.php/Black_bear) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes black bears for their strength.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Black bear - Black bear man - Giant black bear**
- **Attributes**
- **Steals food · Steals drink**
- **Tamed Attributes**
- **Pet value:** 300
- **Not hunting/war trainable**
- **Size**
- **Birth:** 12,000 cm 3
- **Mid:** 60,000 cm 3
- **Max:** 120,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 14
- **Fat:** 13
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
- **Bones:** 17
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large omnivorous predator found in temperate woodlands. Mainly living on berries, it will also steal carcasses from other hunters. Though normally a docile animal, it has been known to kill in a predatory attack.*

**Black bears** are dangerous and rare creatures that raid your food and drink stockpiles who may be found in temperate forests and taigas. They are mainly a threat early in a fort's existence before defenses have been established.

In any given region, up to three black bears may appear before they become extinct. They are always solitary, and hibernate during the winter. This makes winter a decent time to set up a bear trap: surround a small food stockpile with cage traps, and black bears will be yours, assuming it doesn't get overwhelmed by other natural thieves (like raccoons or grizzly bears) first.

Black bears can be trained and have a reasonably high pet value of 300. This makes them a fairly decent option for a highly rewarding breeding program: black bear parts are worth twice as much as those of more domestic animals. However, unlike grizzly bears, black bears cannot be trained for hunting or war without modding.

Some dwarves like black bears for their *strength*.

|  |
|----|
| "Black bear" in other / Languages / Dwarven / : / udir uvel / Elven / : / opa atha / Goblin / : / ogur ron / Human / : / oth rorec |

Admired for its *strength*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Black bears are rumored to extort raccoons who have destroyed their food supply.

    12 kph

    [CREATURE:BEAR_BLACK]
        [DESCRIPTION:A large omnivorous predator found in temperate woodlands.  Mainly living on berries, it will also steal carcasses from other hunters.  Though normally a docile animal, it has been known to kill in a predatory attack.]
        [NAME:black bear:black bears:black bear]
        [CASTE_NAME:black bear:black bears:black bear]
        [CHILD:1][GENERAL_CHILD_NAME:black bear cub:black bear cubs]
        [CREATURE_TILE:'B'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:300]
        [PET]
        [NATURAL]
        [LARGE_ROAMING][FREQUENCY:5]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [BIOME:FOREST_TAIGA]
        [BIOME:ANY_TEMPERATE_FOREST]
        [CURIOUSBEAST_EATER]
        [CURIOUSBEAST_GUZZLER]
        [GRASSTRAMPLE:0]
        [LARGE_PREDATOR]
        [NO_WINTER][MEANDERER]
        [PREFSTRING:strength]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
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
        [BODY_SIZE:0:0:12000]
        [BODY_SIZE:1:0:60000]
        [BODY_SIZE:2:0:120000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
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
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
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
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
