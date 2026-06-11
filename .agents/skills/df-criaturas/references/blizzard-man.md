# Blizzard man

> Fonte: [Blizzard man](https://dwarffortresswiki.org/index.php/Blizzard_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes blizzard men for their icicle teeth.**
- **Biome**
- **Glacier Tundra**
- **Attributes**
- **Alignment:** Evil
- **Genderless · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 300,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large humanoid monster from the wild tundra. It has translucent skin, icicles for teeth, red glowing eyes and pointed ears.*

**Blizzard men** are a species of intelligent and very rare creature found in evil-aligned tundras and glaciers, who spawn one at a time. Weighing more than a troll, these beasts are aggressive and will attack any dwarf who approaches them with punches, kicks, scratches and bites, and should be disposed of with an equipped military squad or traps. Despite being named in a similar fashion, they do not share many characteristics with construct creatures like the subterranean gabbro man or fire man. Fighting a blizzard man in adventurer mode grants more experience than other normal creatures because of their `[``DIFFICULTY``:2]` token.

Despite what their description may imply, blizzard men are not made of ice, instead being made of normal flesh. However, a note on their raw files states Toady One plans to make them be made out of ice in a future update. Blizzard men possess the [`[NO_THOUGHT_CENTER_FOR_MOVEMENT]`](/index.php/Creature_token#NO_THOUGHT_CENTER_FOR_MOVEMENT "Creature token") token, meaning that their limbs do not need to be connected to a brain in order to function (they do not have brains). Due to the aforementioned intelligence, dwarves will not butcher, eat or use products made from blizzard men, limiting their use to occupying space in your refuse stockpile, live training or putting them somewhere of your liking if you capture one in a cage trap.

Some dwarves like blizzard men for their *translucent skin*, their *icicle teeth*, their *glowing red eyes* and their *pointy ears*.

|  |
|----|
| "Blizzard man" in other / Languages / Dwarven / : / zolak udos / Elven / : / ethela onino / Goblin / : / xodu ngorûg / Human / : / rismal abo |

A blizzard man, drawn in crayon by Bay 12 Games.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
It has been posited that the best way to keep blizzard men out of the fortress is with an exceptionally large wall.

Blizzard men are often though to roll into spheres to attack, though this behavior has never been seen before. It is unknown how this idea came to be.

## Trivia

-

  Initially, the premium version had a graphic for a child blizzard man sprite. It was later removed from the game, because blizzard men are adults at birth.

    [CREATURE:BLIZZARD_MAN]
        [DESCRIPTION:A large humanoid monster from the wild tundra.  It has translucent skin, icicles for teeth, red glowing eyes and pointed ears.]
        [NAME:blizzard man:blizzard men:blizzard man]
        [CASTE_NAME:blizzard man:blizzard men:blizzard man]
        [CREATURE_TILE:'M'][COLOR:3:0:1]
        [CREATURE_CLASS:HUMANOID_TRACKING_SYMBOL]
        [GLOWTILE:'"'][GLOWCOLOR:4:0:1]
        [BIOME:GLACIER]
        [BIOME:TUNDRA]
        [LARGE_ROAMING][EVIL][DIFFICULTY:2][FREQUENCY:5]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [LARGE_PREDATOR][MEANDERER]
        [CAN_LEARN][SLOW_LEARNER]
        [GRASSTRAMPLE:0]
        [BONECARN]
        [PREFSTRING:translucent skin]
        [PREFSTRING:icicle teeth]
        [PREFSTRING:glowing red eyes]
        [PREFSTRING:pointy ears]
        [BODY:HUMANOID_NECK:2EYES:2EARS:NOSE:HUMANOID_JOINTS:5FINGERS:5TOES:MOUTH:TONGUE:FACIAL_FEATURES:TEETH]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        *** needs to be made out of ice
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [BODY_SIZE:0:0:300000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
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
        [NO_FEVERS]
        [HOMEOTHERM:10067]
        [ODOR_LEVEL:0] no smell
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
            [TL_COLOR_MODIFIER:RED:1]
                [TLCM_NOUN:eyes:PLURAL]
