# Grasshopper man

> Fonte: [Grasshopper man](https://dwarffortresswiki.org/index.php/Grasshopper_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes grasshopper men for their chirping.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Grasshopper - Grasshopper man - Giant grasshopper**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and legs of a grasshopper.*

**Grasshopper men** are animal people variants of the common grasshopper, who can inhabit most savage biomes. They spawn in groups of 1-3 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, grasshopper men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like grasshopper men for their *great leaps*.

|  |
|----|
| "Grasshopper man" in other / Languages / Dwarven / : / isin-ikus udos / Elven / : / enena-ayefi onino / Goblin / : / struxe-angnu ngorûg / Human / : / kege-buh abo |

Admired for their *great leaps*.

    [CREATURE:GRASSHOPPER_MAN]
        [COPY_TAGS_FROM:GRASSHOPPER]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:grasshopper man:grasshopper men:grasshopper man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:grasshopper woman:grasshopper women:grasshopper woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:grasshopper man:grasshopper men:grasshopper man]
        [DESCRIPTION:A person with the head and legs of a grasshopper.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'g']
        [COLOR:2:0:1]
