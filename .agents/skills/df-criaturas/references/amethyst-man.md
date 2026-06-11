# Amethyst man

> Fonte: [Amethyst man](https://dwarffortresswiki.org/index.php/Amethyst_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes amethyst men for their rockiness.**
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
- **Rough amethysts**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A strange crystalline creature the shape of a man. It is found deep underground.*

**Amethyst men** are an extremely rare type of anthropomorphic creature made of solid amethyst, essentially gemstone golems, found only in the deepest caverns. They are non-sentient, aggressive construct creatures that are not alive, feel no pain, feel no fear, cannot be stunned, never get tired, do not need to breathe, have no thought center, and are type two building destroyers. They are as large as humans.

Amethyst men are decent fighters and will almost certainly kill unarmed civilians, as normal punches and kicks will merely glance away from their rocky hides. However, an equipped military will make short work of them, with bladed weapons like short swords and battle axes being preferable over war hammers; while a hammerdwarf can bash an amethyst man until its body is fractured and crushed, an axedwarf will be able to sever their limbs much faster. If a player is feeling creative, amethyst men can also suffer from a long fall, a cave-in, or magma. Upon death, they leave a rough amethyst gem usable by your jewelers. They can't be spawned in the object testing arena.

Some dwarves like amethyst men for their *rockiness*.

|  |
|----|
| "Amethyst man" in other / Languages / Dwarven / : / alron udos / Elven / : / fece onino / Goblin / : / exost ngorûg / Human / : / zebna abo |

Admired for its *rockiness*.\
*Art by Fault*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Amethyst men are known to be created in vast caverns stripped of all life, and may be found near garnet, pearl, and rose quartz. They wield amethyst-studded whips in battle.

    [CREATURE:ELEMENTMAN_AMETHYST]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A strange crystalline creature the shape of a man.  It is found deep underground.]
        [NAME:amethyst man:amethyst men:amethyst man]
        [CASTE_NAME:amethyst man:amethyst men:amethyst man]
        [CREATURE_TILE:'M'][COLOR:5:0:1]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:3:3]
        [FREQUENCY:1]
        [POPULATION_NUMBER:15:30]
        [NOBONES]
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
        [ODOR_LEVEL:0] no smell
        [SMELL_TRIGGER:10000] cannot smell
        [PREFSTRING:rockiness]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:730:561:351:1900:2900] 25 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [BODY:HUMANOID_SIMPLE]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [TISSUE:ROCK]
            [TISSUE_NAME:amethyst:NP]
            [TISSUE_MATERIAL:INORGANIC:AMETHYST]
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
        [ITEMCORPSE:ROUGH:NO_SUBTYPE:INORGANIC:AMETHYST]
        [ALL_ACTIVE]
