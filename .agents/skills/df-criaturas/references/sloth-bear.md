# Sloth bear

> Fonte: [Sloth bear](https://dwarffortresswiki.org/index.php/Sloth_bear) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sloth bears for their large floppy ears.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Sloth bear - Sloth bear man - Giant sloth bear**
- **Attributes**
- **Steals food · Steals drink**
- **Tamed Attributes**
- **Pet value:** 250
- **Not hunting/war trainable**
- **Size**
- **Birth:** 10,000 cm 3
- **Mid:** 50,000 cm 3
- **Max:** 100,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-40
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 13
- **Fat:** 12
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
- **Bones:** 18
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Not to be confused with sloths.*

*A medium-sized mammal that lives in the trees. It is known for its easy-going nature.*

**Sloth bears** are rare solitary creatures that raid your food and drink stockpiles who may be found in tropical forests. They are the smallest species of bear in the game, though they're still nearly twice the weight of a dwarf and can make quick work of an unarmed civilian. No more than three sloth bears will inhabit a given surrounding before they become extinct. Unlike other species of bear, sloth bears do appear during the winter season. An infant sloth bear is called a *cub*.

Sloth bears can be captured in cage traps and trained into fairly valuable exotic pets. This makes them a fairly decent option for a highly-rewarding breeding program: sloth bear parts are worth twice as much as those of more domestic animals. However, unlike grizzly bears, sloth bears cannot be trained for hunting or war.

Some dwarves like sloth bears for their *large floppy ears*.

|  |
|----|
| "Sloth bear" in other / Languages / Dwarven / : / gäzot uvel / Elven / : / timeba atha / Goblin / : / ongo ron / Human / : / thruque rorec |

Admired for its *large floppy ears*.

    1 kph, NO DATA

    Sloth bears were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:BEAR_SLOTH]
        [DESCRIPTION:A medium-sized mammal that lives in the trees.  It is known for its easy-going nature.]
        [NAME:sloth bear:sloth bears:sloth bear]
        [CASTE_NAME:sloth bear:sloth bears:sloth bear]
        [CHILD:1][GENERAL_CHILD_NAME:sloth bear cub:sloth bear cubs]
        [CREATURE_TILE:'B'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:250]
        [PET]
        [NATURAL]
        [LARGE_ROAMING][FREQUENCY:5]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [BIOME:ANY_TROPICAL_FOREST]
        [CURIOUSBEAST_EATER]
        [CURIOUSBEAST_GUZZLER]
        [GRASSTRAMPLE:0]
        [MEANDERER]
        [PREFSTRING:large floppy ears]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
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
        [BODY_SIZE:0:0:10000]
        [BODY_SIZE:1:0:50000]
        [BODY_SIZE:2:0:100000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:40]
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
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph, NO DATA
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
