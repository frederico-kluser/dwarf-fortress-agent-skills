# Troll

> Fonte: [Troll](https://dwarffortresswiki.org/index.php/Troll) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes trolls for their terrifying features.**
- **Biome**
- **Underground Depth: 1-3**
- **Attributes**
- **Alignment:** Evil
- **Building destroyer : Level 2**
- **Learns · Shearable · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 10,000 cm 3
- **Mid:** 50,000 cm 3
- **Max:** 250,000 cm 3
- **Age**
- **Child at:** 1
- **Adult at:** 10
- **Max age:** 800-1000
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge humanoid monster with coarse fur, large tusks and horns.*

**Trolls** are large, predatory, dangerous subterranean evil creatures who inhabit all layers of the caverns and often appear under the command of goblins during sieges, and have any number of features which make them creatures to be taken seriously. Over four times larger than a dwarf, they are building destroyers, and will path to your buildings simply for the joy of sheer destruction. During sieges, they act as battering rams, so design your defenses accordingly. They are not related to night trolls, despite the similar names.

Wild trolls meander the underground and attack dwarves who approach or provoke them. Many of them are enslaved/absorbed by goblins during world generation and become their servants, inhabiting their dark pits in truly huge numbers (sometimes enough to cause overwhelming lag Bug:7526) and aiding their smaller masters in their battles against other races. Goblins shear trolls for their fur, making them the evil race's equivalent of sheep. As they are intelligent (although incapable of speech), civilized trolls may gain non-military professions among goblin society. In a modded game, they may be usable in the dwarven textile industry, but you can't change their labors, due to a bug.

Trolls will almost certainly appear accompanying goblins when they siege your fortress. They are quite tough and have a variety of different ways to cause injury to your dwarves due to their humanoid bodies and large tusks. Since they only rarely wear armor (when appearing as helpers of Goblin Claus), they will be easy targets for a decently-skilled squad of axedwarves, though silk-wearing trolls can complicate things, if copper and silver are the only weapons-grade metals your fortress has available. Trolls can and will wrestle your dwarves, which can lead to some broken bones in your military. Unlike goblins, trolls are natural swimmers, which could be a problem for a fortress relying on a moat for defense, or using a drowning chamber or underground lake as a means of administering dwarven justice. Trolls can climb, so it is possible for them to get to level one of a cavern through deep pits and access your fortress to ~~crush the heads of~~ play with your dwarves.

Trolls notably possess cyan-colored blood (possibly hemocyanin-based). Their behavior as a servant race of goblins is done via the combination of the [`[EVIL]`](/index.php/Creature_token#EVIL "Creature token") and [`[SLOW_LEARNER]`](/index.php/Creature_token#SLOW_LEARNER "Creature token") creature tokens and the fact they live underground; through modding, players can create their own subterranean goblin servants who will accompany trolls in battle by giving their race these two tokens. Unlike gremlins, they cannot become pets of citizens.

Some dwarves like trolls for their *terrifying features*.

-

  A dwarf battling a troll, drawn in crayon by Bay 12 Games.

-

  One holding a weapon.\
  *Art by Arne*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

They also enjoy vandalizing wiki pages and causing mass annoyance. Though they do not speak, they would provoke others into angry responses with their wild claims if they could. Once a troll would successfully cause an argument between many individuals, the troll would sit back and laugh, taking an immature enjoyment out of the scenario. Sometimes, the best course of action in defeating a troll is to ignore it.

    [CREATURE:TROLL]
        [DESCRIPTION:A huge humanoid monster with coarse fur, large tusks and horns.]
        [NAME:troll:trolls:troll]
        [CASTE_NAME:troll:trolls:troll]
        [CREATURE_TILE:'T'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [CHILD:10][BABY:1][MULTIPLE_LITTER_RARE]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:3]
        [LARGE_ROAMING][DIFFICULTY:2]
        [POPULATION_NUMBER:5:10]
        [BUILDINGDESTROYER:2]
        [LARGE_PREDATOR]
        [CAN_LEARN][SLOW_LEARNER]
        [EVIL]
        [GRASSTRAMPLE:20]
        [BONECARN]
        [PREFSTRING:terrifying features]
        [BODY:HUMANOID_NECK:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:5FINGERS:5TOES:MOUTH:TONGUE:FACIAL_FEATURES:TEETH:RIBCAGE:2HEAD_HORN:2TUSKS]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:IVORY:TOOTH_TEMPLATE]
                [STATE_NAME:ALL_SOLID:ivory]
                [STATE_ADJ:ALL_SOLID:ivory]
            [SELECT_MATERIAL:HAIR]
                [STATE_NAME:ALL_SOLID:fur]
                [STATE_ADJ:ALL_SOLID:fur]
                [YARN]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
            [USE_TISSUE_TEMPLATE:IVORY:IVORY_TEMPLATE]
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
            [STATE_COLOR:ALL:AQUA]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:10000]
        [BODY_SIZE:1:168:50000]
        [BODY_SIZE:20:0:250000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:75:95:98:100:102:105:125]
            [APP_MOD_IMPORTANCE:500]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:75:95:98:100:102:105:125]
            [APP_MOD_IMPORTANCE:500]
        [SET_BP_GROUP:BY_CATEGORY:EYE]
            [BP_APPEARANCE_MODIFIER:CLOSE_SET:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
            [BP_APPEARANCE_MODIFIER:DEEP_SET:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
            [BP_APPEARANCE_MODIFIER:ROUND_VS_NARROW:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
            [BP_APPEARANCE_MODIFIER:LARGE_IRIS:25:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
                [APP_MOD_DESC_RANGE:30:60:90:110:150:190]
        [SET_BP_GROUP:BY_CATEGORY:LIP]
            [BP_APPEARANCE_MODIFIER:THICKNESS:50:70:90:100:110:130:200]
                [APP_MOD_NOUN:lips:PLURAL]
                [APP_MOD_DESC_RANGE:55:70:90:110:150:190]
        [SET_BP_GROUP:BY_CATEGORY:NOSE]
            [BP_APPEARANCE_MODIFIER:BROADNESS:25:70:90:100:110:130:200]
                [APP_MOD_DESC_RANGE:30:60:90:110:150:190]
            [BP_APPEARANCE_MODIFIER:LENGTH:25:70:90:100:110:130:200]
                [APP_MOD_DESC_RANGE:30:60:90:110:150:190]
            [BP_APPEARANCE_MODIFIER:UPTURNED:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:CONVEX:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:nose bridge:SINGULAR]
        [SET_BP_GROUP:BY_CATEGORY:EAR]
            [BP_APPEARANCE_MODIFIER:SPLAYED_OUT:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:ears:PLURAL]
            [BP_APPEARANCE_MODIFIER:HANGING_LOBES:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:ears:PLURAL]
            [BP_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
                [APP_MOD_IMPORTANCE:700]
                [APP_MOD_NOUN:ears:PLURAL]
                [APP_MOD_DESC_RANGE:91:94:98:102:106:109]
            [BP_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
                [APP_MOD_IMPORTANCE:700]
                [APP_MOD_NOUN:ears:PLURAL]
                [APP_MOD_DESC_RANGE:91:94:98:102:106:109]
        [SET_BP_GROUP:BY_CATEGORY:TOOTH]
            [BP_APPEARANCE_MODIFIER:GAPS:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:teeth:PLURAL]
            [BP_APPEARANCE_MODIFIER:LENGTH:100:100:100:100:100:100:100] for vampires
                [APP_MOD_IMPORTANCE:1000]
                [APP_MOD_NOUN:teeth:PLURAL]
                [APP_MOD_DESC_RANGE:30:60:90:110:150:190]
        [SET_BP_GROUP:BY_CATEGORY:SKULL]
            [BP_APPEARANCE_MODIFIER:HIGH_CHEEKBONES:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:BROAD_CHIN:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:JUTTING_CHIN:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:SQUARE_CHIN:0:70:90:100:110:130:200]
        [SET_BP_GROUP:BY_CATEGORY:THROAT]
            [BP_APPEARANCE_MODIFIER:DEEP_VOICE:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:RASPY_VOICE:0:70:90:100:110:130:200]
        [SET_BP_GROUP:BY_CATEGORY:HEAD]
            [BP_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
                [APP_MOD_IMPORTANCE:700]
                [APP_MOD_DESC_RANGE:91:94:98:102:106:109]
            [BP_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
                [APP_MOD_IMPORTANCE:700]
                [APP_MOD_DESC_RANGE:91:94:98:102:106:109]
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
        [ATTACK:TGORE:BODYPART:BY_CATEGORY:TUSK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
        [ATTACK:HGORE:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [EQUIPS]
        [CANOPENDOORS]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:fur:SINGULAR]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:fur:SINGULAR]
                    [TLCM_TIMING:ROOT:700:0:900:0]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:LENGTH:0:0:0:0:0:0:0]
                    [APP_MOD_NOUN:fur:SINGULAR]
                    [APP_MOD_RATE:1:DAILY:0:300:0:0:NO_END]
                    [APP_MOD_DESC_RANGE:10:50:100:150:200:300]
                [SHEARABLE_TISSUE_LAYER:LENGTH:300]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
