# Plump helmet man

> Fonte: [Plump helmet man](https://dwarffortresswiki.org/index.php/Plump_helmet_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes plump helmet men for their similarity with food.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,500 cm 3
- **Mid:** 10,000 cm 3
- **Max:** 50,000 cm 3
- **Age**
- **Child at:** 1
- **Adult at:** 12
- **Max age:** 60-80
- **Becomes after death**
- **Plump helmet man plump helmet man tissue**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small humanoid resembling a walking mushroom with arms and legs. It lives far underground near water and soil.*

**Plump helmet men** are humanoid, intelligent versions of plump helmets who can be found at the second and third layers of the caverns. These construct creatures are nearly as heavy as dwarves and spawn in groups of 3-5 individuals who meander about aimlessly. They are non-hostile and generally harmless, and if confronted in combat, are easily dispatched by the average dwarf, as their boneless mushroom composition is very fragile to damage. However, uncivilized plump helmet men can easily get into fights with both cats and dogs, so be careful if your fortress has a lot of pets.

Plump helmet men are featureless - they have no mouth, nose, ears or eyes, though they can still see through [`[EXTRAVISION]`](/index.php/Creature_token#EXTRAVISION "Creature token"). They are composed of fungal material called 'plump helmet man tissue' which is, according to the raws, edible, though plump helmet men cannot be butchered or eaten due to being intelligent beings. Due to *Dwarf Fortress'* item naming system, they turn into "Plump helmet man plump helmet man tissue" when they die. While generally fragile, they are also remarkably resistant to fire and magma - Dwarven Science Experiments have shown that they can live for several seasons while submerged in 7/7 magma (while on fire). Additionally, they possess the [`[NO_THOUGHT_CENTER_FOR_MOVEMENT]`](/index.php/Creature_token#NO_THOUGHT_CENTER_FOR_MOVEMENT "Creature token") token, meaning that their limbs do not need to be connected to a brain in order to function (they do not have brains), and possess the [`[SWIMS_INNATE]`](/index.php/Creature_token#SWIMS_INNATE "Creature token") token, which means that they can swim perfectly without needing the swimmer skill.

Plump helmet men are similar to savage animal people in that they can join civilizations, normally being found in dwarven factions where they'll become full-fledged citizens. Plump helmet men are playable in adventurer mode, but come with one major disadvantage compared to other races; they cannot speak (they lack the [`[CAN_SPEAK]`](/index.php/Creature_token#CAN_SPEAK "Creature token") token, evident by them having no mouths), meaning they can't receive quests, trade or hire companions, among other things, which severely limits their ability to interact with others. Going on a murderous rampage as a purple mushroom man is still fair game, though, provided you keep their relative fragility in mind.

Unlike most creatures, plump helmet men can't be spawned in the object testing arena, as they possess the [`[ARENA_RESTRICTED]`](/index.php/Creature_token#ARENA_RESTRICTED "Creature token") token.

Some dwarves like plump helmet men for their *similarity with food*.

Sometimes get made fun of because they're purple.\
*Art by kruggsmash*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Plump helmet men are known for their clever jokes and games, as well as their innocent, almost childlike nature. This has led to them being universally beloved by all sentient creatures of the world, as well as dwarves, who find them both sweeter and more succulent than the farm-grown variety. For years, dwarves have been trying to find a way to brew these majestic creatures alive, but the scientific effort has been frustrated by the tendency of dwarven brewers to pounce on any plump helmet man they see and eat their way through the still-living myconid in an orgy of mushroom juice and drool.

However, beneath the dumb exterior, they have a darker side. They are secretly geniuses, who strive constantly to escape.

(Source: The Littlest Cheesemaker)

Intelligent undead warrior from far away land often tells story about plump helmet men. Said group of plump helmet men usually lives in surface forest or underground, near a lake surrounded by ash. They are known to be legendary strikers.

    [CREATURE:PLUMP_HELMET_MAN]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A small humanoid resembling a walking mushroom with arms and legs.  It lives far underground near water and soil.]
        [NAME:plump helmet man:plump helmet men:plump helmet man]
        [CASTE_NAME:plump helmet man:plump helmet men:plump helmet man]
        [CREATURE_TILE:'m'][COLOR:5:0:0]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:2:3]
        [FREQUENCY:20]
        [BENIGN]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:5]
        [CAN_LEARN]
        [LOCAL_POPS_CONTROLLABLE]
        [LOCAL_POPS_PRODUCE_HEROES]
        [CANOPENDOORS]
        [PREFSTRING:similarity with food]
        [ODOR_LEVEL:0] no smell
        [SMELL_TRIGGER:10000] cannot smell
        [NOBONES]
        [EXTRAVISION]
        [BODY:HUMANOID_SIMPLE]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [USE_MATERIAL_TEMPLATE:PH_TISSUE:STRUCTURAL_PLANT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:plump helmet man tissue]
            [STATE_ADJ:ALL_SOLID:plump helmet man tissue]
            [STATE_NAME:LIQUID:melted plump helmet man tissue]
            [STATE_ADJ:LIQUID:melted plump helmet man tissue]
            [STATE_NAME:GAS:boiling plump helmet man tissue]
            [STATE_ADJ:GAS:boiling plump helmet man tissue]
            [PREFIX:NONE]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [TISSUE:MUSHROOM]
            [TISSUE_NAME:plump helmet man tissue:NP]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:PH_TISSUE]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:MUSHROOM]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
        [BODY_SIZE:0:0:1500]
        [BODY_SIZE:1:168:10000]
        [BODY_SIZE:12:0:50000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:60:80]
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
        [BABY:1]
        [CHILD:12]
        [EQUIPS]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [HOMEOTHERM:10040]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:MUSHROOM]
                [TL_COLOR_MODIFIER:PURPLE:1]
                    [TLCM_NOUN:exterior:SINGULAR]
