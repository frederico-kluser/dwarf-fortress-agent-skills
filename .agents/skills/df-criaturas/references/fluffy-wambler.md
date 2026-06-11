# Fluffy wambler

> Fonte: [Fluffy wambler](https://dwarffortresswiki.org/index.php/Fluffy_wambler) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes fluffy wamblers for their warm heart.**
- **Biome**
- **Any Land**
- **Attributes**
- **Alignment:** Good
- **Devours food · Exotic pet**
- **Pet value:** 20
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A fluffy, pudge-filled being, known for its warm heart and stumble bumblings.*

**Fluffy wamblers** are humanoid vermin that can be found the world over in good regions. They can be captured by trappers and turned into low-value pets. They are tied with the fox squirrel as the largest of all vermin, being only a little smaller than a dwarf baby.

They possess a few unusual characteristics; their entire bodies are covered in white fur known as "fluff", while their equivalent of fat is called "pudge". Fluffy wamblers have no organs, bones or blood, with the entirety of their interior being composed of purple pudge. Despite this, they will sometimes attempt to eat food out of stockpiles, similarly to other vermin like rats, and like them, it only takes a cat to solve the problem. Their raws note an immunity to fevers, which vermin aren't known to be affected by to begin with. In adventurer mode, fluffy wamblers can only be found during the day.

Some dwarves like fluffy wamblers for their *warm heart*, their *gentle nature* and their *stumble bumbling*.

A fluffy wambler being ambushed by a nightwing, drawn in crayon by Bay 12 Games.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Fluffy wamblers are surprisingly dense when traveling at high velocities. There was at least one reported slaying of a bronze colossus using a thrown fluffy wambler as a weapon. News of this incident has served to increase the wambler's popular appeal. Despite their status as agricultural pests, it's rare to find a being that actually finds them offensive. They are widely held to be "adorable", and many dwarves consider them to be a delicacy.

Wamblers are not wholly benign and may in fact display aggression when threatened, an act which is almost always futile, as they have power to harm only the feeblest of creatures. Civilizations that use "good" animals and animal materials (and have no qualms about killing animals) can make clothes out of wambler fluff, a prized, yet inexpensive, insulating fabric.

Wamblers maintain a body temperature slightly higher than that of dwarves. They appear to be immune to sickness and are not known to suffer infection of any kind. There is no specific term for any hypothetical wambler offspring; a live wambler birthing has never been seen. One case exists of a wambler possibly resurrecting itself deep underground. The corpse was carried many levels underground by a cat into an active mining area well away from any sort of entrance, then later the corpse was missing and a live wambler was wandering around down in the mining area 13 floors down underground. Up to that point, no other live wamblers had been seen anywhere within the tunnels.

    [CREATURE:WAMBLER_FLUFFY]
        [DESCRIPTION:A fluffy, pudge-filled being, known for its warm heart and stumble bumblings.]
        [NAME:fluffy wambler:fluffy wamblers:fluffy wambler]
        [CASTE_NAME:fluffy wambler:fluffy wamblers:fluffy wambler]
        [CREATURE_TILE:249][COLOR:7:0:1]
        [PETVALUE:20]
        [VERMIN_EATER][PENETRATEPOWER:1][FREQUENCY:100][VERMIN_GROUNDER]
        [SMALL_REMAINS][GOOD][PET_EXOTIC][NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:ANY_LAND]
        [POPULATION_NUMBER:250:500]
        [TRIGGERABLE_GROUP:5:50]
        [PREFSTRING:warm heart]
        [PREFSTRING:gentle nature]
        [PREFSTRING:stumble bumbling]
        [BODY:HUMANOID_SIMPLE:2EYES:NOSE]
        [USE_MATERIAL_TEMPLATE:HAIR:HAIR_TEMPLATE]
            [STATE_NAME:ALL_SOLID:fluff]
            [STATE_ADJ:ALL_SOLID:fluff]
        [USE_TISSUE_TEMPLATE:HAIR:HAIR_TEMPLATE]
            [TISSUE_NAME:fluff:NP]
            [RELATIVE_THICKNESS:3]
            [INSULATION:200]
        [USE_MATERIAL_TEMPLATE:SKIN:SKIN_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:LEATHER:LEATHER_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:PARCHMENT:PARCHMENT_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:TALLOW:TALLOW_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:SOAP:SOAP_TEMPLATE]
        [USE_TISSUE_TEMPLATE:SKIN:SKIN_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:FAT:FAT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:pudge]
            [STATE_ADJ:ALL_SOLID:pudge]
            [STATE_COLOR:ALL:PURPLE]
        [USE_TISSUE_TEMPLATE:FAT:FAT_TEMPLATE]
            [TISSUE_NAME:pudge:NP]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:EYE:EYE_TEMPLATE]
        [USE_TISSUE_TEMPLATE:EYE:EYE_TEMPLATE]
        [NOBONES]
        [CANNOT_JUMP]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:NONE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [GAIT:WALK:Stumble Bumble:1600:NO_BUILD_UP:0:STEALTH_SLOWS:25]
        [GAIT:WALK:Wamble:2900:NO_BUILD_UP:0:STEALTH_SLOWS:25]
        [GAIT:CRAWL:Crawl:5900:NO_BUILD_UP:0]
        [GAIT:CLIMB:Climb:5900:NO_BUILD_UP:0]
        [BODY_SIZE:0:0:2000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [DIURNAL]
        [NO_FEVERS]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [HOMEOTHERM:10070]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:fluff:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:PINK:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
