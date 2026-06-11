# Lizard man

> Fonte: [Lizard man](https://dwarffortresswiki.org/index.php/Lizard_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes lizard men for their beauty.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Lizard - Lizard man - Giant lizard**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,100 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a lizard.*

**Lizard men** are humanoid versions of the common lizard and a species of unremarkable animal people, found in many savage biomes. They are a little over half the size of dwarves when adults and spawn in groups of 1-3 individuals. They should pose no threat unless provoked. All lizard men are born with Legendary skill in climbing.

Like other savage animal people, lizard men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like lizard men for their *beauty*.

Cold-blooded killers.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some lizard women admire cave fish women for their sheer awesomeness, although they are unable to express it because of their natural timidness. They are also rumored to be connected to the origin of forgotten beasts, which puts even further strain on their fragile psyche.

Human peasants have been occasionally witnessed accusing their local lords of being lizard men, but all such allegations have been proven to be false.

Some lizard women tavern keepers are rumored to be master bakers and can even repair xxsteel spearxx.

|  |
|----|
| "Lizard man" in other / Languages / Dwarven / : / bungek udos / Elven / : / cimathi onino / Goblin / : / asp ngorûg / Human / : / ramac abo |

    [CREATURE:LIZARD_MAN]
        [COPY_TAGS_FROM:LIZARD]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:lizard man:lizard men:lizard man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:lizard woman:lizard women:lizard woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:CLAW_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:lizard man:lizard men:lizard man]
        [DESCRIPTION:A person with the head and tail of a lizard.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'l']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
