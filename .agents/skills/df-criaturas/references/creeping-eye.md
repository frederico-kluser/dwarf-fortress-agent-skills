# Creeping eye

> Fonte: [Creeping eye](https://dwarffortresswiki.org/index.php/Creeping_eye) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes creeping eyes for their unnerving stare.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Alignment:** Evil
- **Genderless**
- **Cannot be tamed**
- **Size**
- **Max:** 20,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Butchering returns**
- **Food items**
- **Meat:** 13
- **Fat:** 13
- **Heart:** 1
- **Intestines:** 1
- **Raw materials**
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small underground monster that crawls across the cavern wall with its four clawed hands. It has a single large eye which can shine with its own light, otherwise its stony skin blends in with the rock. It has no mouth and is said to feed on evil alone.*

**Creeping eyes** are small, four-armed evil monsters that can be found in the deepest caverns in large packs. They have no attacks whatsoever, apart from the standard push attack, but they are so small they will rarely ever hurt a dwarf.

Drowning chambers do not work on creeping eyes, as they have [`[NOBREATHE]`](/index.php/Creature_token#NOBREATHE "Creature token"). The same 5 z-level pit trap, capable of killing dozens of blind cave ogres with assembly-line efficiency, doesn't even damage these hardy creatures. Your best bet is your military, even though creeping eyes have a lot of excess targetable body parts and only one weak point: the heart.

Creeping eyes possess a pet value of 50, but lack the necessary tokens to be trainable. All creeping eyes possess Legendary skill in climbing and are biologically immortal, only dying from violence or disease. When encountered in adventurer mode, they will glow in the dark. They can't be spawned in the object testing arena.

Some dwarves like creeping eyes for their *unnerving stare*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Interestingly, despite feeding on evil alone creeping eyes have intestines, implying that evil can be metabolized. Because of this, it is widely believed that bars of soap derived from the evil-saturated fat of creeping eyes is a powerful dwarven aphrodisiac (beard strengthener).

|  |
|----|
| "Creeping eye" in other / Languages / Dwarven / : / shadkik ker / Elven / : / coni evi / Goblin / : / gudo mangdu / Human / : / sagam ape |

## Gallery

-

  *Art by Arne.*

-

  "Scurries on walls. Can blend into stone. Bioluminescence. Feeds on evil emanations from below."\
  *Concept art by Bay 12 Games.*

    [CREATURE:CREEPING_EYE]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A small underground monster that crawls across the cavern wall with its four clawed hands.  It has a single large eye which can shine with its own light, otherwise its stony skin blends in with the rock.  It has no mouth and is said to feed on evil alone.]
        [NAME:creeping eye:creeping eyes:creeping eye]
        [CASTE_NAME:creeping eye:creeping eyes:creeping eye]
        [CREATURE_TILE:'e'][COLOR:7:0:1]
        [PETVALUE:50]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:3:3]
        [LARGE_ROAMING]
        [FREQUENCY:5]
        [NOBREATHE]
        [NOBONES]
        [EVIL]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [NATURAL_SKILL:CLIMBING:15]
        [CLUSTER_NUMBER:10:20]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:unnerving stare]
        [GLOWTILE:9][GLOWCOLOR:4:0:1]
        [BODY:BASIC_1PARTBODY:4ARMS_STANCE:HEART:GUTS:4FINGERS:BODY_EYE:BODY_EYELID]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:20000]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [CANNOT_JUMP]
        [NO_SLEEP]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:GRAY:1]
                [TLCM_NOUN:skin:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:ALL:EYE]
            [TL_COLOR_MODIFIER:IRIS_EYE_RED:1]
                [TLCM_NOUN:eye:SINGULAR]
