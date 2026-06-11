# Grizzly bear

> Fonte: [Grizzly bear](https://dwarffortresswiki.org/index.php/Grizzly_bear) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes grizzly bears for their strength.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Grizzly bear - Grizzly bear man - Giant grizzly bear**
- **Attributes**
- **Steals food · Steals drink · War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 20,000 cm 3
- **Mid:** 100,000 cm 3
- **Max:** 200,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×3)**
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

*A huge brown creature found in temperate woodland. It is known for its ferocious attack, usually when it or its young are threatened.*

**Grizzly bears** are large, tough mammals that inhabit temperate forests and taigas. They may be drawn to your fortress in search of food; they will locate and consume any food and drink that your dwarves have carelessly left lying around. This can be particularly fun for new fortresses without a seasoned military, as their entire food and alcohol supply is destroyed in moments and discover the hard way that unarmed and unarmored dwarves can't win against a creature that's more than three times their size. Grizzly bears are very rare; such that only two to three of them will exist in a single region before they are considered locally extinct. They do not spawn during the winter, mimicking real-life hibernation.

However, their fondness for food makes them pretty easy to trap in a cage trap. Make a small food/booze stockpile, probably outdoors, and surround it with cage traps (or some walls) on all sides. Grizzly bears will be attracted to the food and booze, and become trapped in the cage trap. They can then be trained into valuable exotic pets. Trained grizzly bears can be further turned into war and hunting beasts, being a popular choice for war animals since they are large and strong enough to do some serious damage. They are also frequently available from elven caravans, as elves tend to live in temperate forests. Should you butcher them, products made from their parts are 3 times more valuable than those made from common domestic animals.

Much larger and stronger than your regular dog, war grizzlies can make fast work of an ambush if they aren't outnumbered. Their powerful jaws can puncture straight through common iron mail, making a nice snack out of unprepared foes. Having a couple of Elite Marksdwarves with 10 bears assigned is a splendid idea, as the bears will act as a biting meat shield, while your crossbowdwarves take care of the tougher enemies the bears can't handle. Grizzly bears are exotic mounts and are sometimes spotted being ridden by humans during sieges.

Some dwarves like grizzly bears for their *strength*.

Admired for its *strength*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

In world gen, a green grizzly bear with mental problems will form a relationship with a porcupine. But this always ends in fun for the porcupine. They choose red porcupines more over regular ones.

## See also

- Black bear

|  |
|----|
| "Grizzly bear" in other / Languages / Dwarven / : / enol uvel / Elven / : / caqui atha / Goblin / : / utux ron / Human / : / damso rorec |

    [CREATURE:BEAR_GRIZZLY]
        [DESCRIPTION:A huge brown creature found in temperate woodland.  It is known for its ferocious attack, usually when it or its young are threatened.]
        [NAME:grizzly bear:grizzly bears:grizzly bear]
        [CASTE_NAME:grizzly bear:grizzly bears:grizzly bear]
        [CHILD:1][GENERAL_CHILD_NAME:grizzly bear cub:grizzly bear cubs]
        [CREATURE_TILE:'B'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [NATURAL]
        [PETVALUE:500]
        [PET]
        [TRAINABLE]
        [MOUNT_EXOTIC]
        [LARGE_ROAMING][FREQUENCY:2]
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
        [BODY_SIZE:0:0:20000]
        [BODY_SIZE:1:0:100000]
        [BODY_SIZE:2:0:200000]
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
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:471:314:157:1900:2900] 56 kph
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
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
