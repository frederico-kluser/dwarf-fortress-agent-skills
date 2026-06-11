# Gabbro man

> Fonte: [Gabbro man](https://dwarffortresswiki.org/index.php/Gabbro_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gabbro men for their rockiness.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Building destroyer : Level 2**
- **Genderless · No Stun · No Pain · No Exert · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Becomes after death**
- **Gabbro boulder**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Living gabbro in the shape of a man. These strange creatures are found deep underground.*

**Gabbro men** are extremely rare construct creatures made of solid gabbro, found exclusively at the third layer of the caverns. Like other construct creatures, they are non-sentient, feel no pain or fear, cannot be stunned and don't need to breathe. They are as large as humans and are level 2 building destroyers. Gabbro men are immortal and only die to violence.

Gabbro men are deadly to the average dwarf and will usually kill unarmed civilians. Punches and kicks will glance away from their stone hide, but some may deliver lucky bites which can fracture them. Gabbro men should nonetheless be engaged with an equipped military before they can wreak havoc among dwarves and buildings. When killed, gabbro men turn into a rough gabbro boulder which can be used by your masons or stone crafters. They can't be spawned in the object testing arena.

Some dwarves like gabbro men for their *rockiness*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite many rumored sightings and artistic depictions, there is no human that has become an orange gabbro man through a teleportation experiment. It has also been stated that this particular gabbro man has allied himself with three other humans with supernatural abilities.\

I think we know what his favorite genre of music is...\
*Art by Tomáš Hanzík*

    [CREATURE:ELEMENTMAN_GABBRO]
        [ARENA_RESTRICTED]
        [DESCRIPTION:Living gabbro in the shape of a man.  These strange creatures are found deep underground.]
        [NAME:gabbro man:gabbro men:gabbro man]
        [CASTE_NAME:gabbro man:gabbro men:gabbro man]
        [CREATURE_TILE:'M'][COLOR:0:0:1]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:3:3]
        [FREQUENCY:1]
        [POPULATION_NUMBER:15:30]
        [NOPAIN][EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
            [NOTHOUGHT][NOEXERT]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [BUILDINGDESTROYER:2]
        [LARGE_PREDATOR]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [NOT_LIVING]
        [CANOPENDOORS]
        [NOT_BUTCHERABLE]
        [NOFEAR]
        [PREFSTRING:rockiness]
        [ODOR_LEVEL:0] no smell
        [SMELL_TRIGGER:10000] cannot smell
        [NOBONES]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [BODY:HUMANOID_SIMPLE]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [TISSUE:ROCK]
            [TISSUE_NAME:gabbro:NP]
            [TISSUE_MATERIAL:INORGANIC:GABBRO]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:ROCK]
        [BODY_SIZE:0:0:70000]
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
        [ITEMCORPSE:BOULDER:NO_SUBTYPE:INORGANIC:GABBRO]
        [ALL_ACTIVE]
