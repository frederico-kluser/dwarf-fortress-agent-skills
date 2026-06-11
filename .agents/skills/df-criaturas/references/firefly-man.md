# Firefly man

> Fonte: [Firefly man](https://dwarffortresswiki.org/index.php/Firefly_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes firefly men for their enchanting glow.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Firefly - Firefly man - Giant firefly**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the wings and head of a firefly.*

**Firefly men** are animal people variants of the common firefly, who can inhabit most savage biomes. They spawn in groups of 2-5 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf. All firefly men are born with Legendary skill in climbing.

Like other savage animal people, firefly men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like firefly men for their *enchanting glow*.

Who needs a flashlight?

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Contrary to some misattributed quotes, they do not prefer to be called captain, and as their torsos are weak, they avoid wearing tight pants at all costs.

|  |
|----|
| "Firefly man" in other / Languages / Dwarven / : / ziril-fenglel udos / Elven / : / inira-yetine onino / Goblin / : / zedan-atu ngorûg / Human / : / usmok-ngáthi abo |

    [CREATURE:FIREFLY_MAN]
        [COPY_TAGS_FROM:FIREFLY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:firefly man:firefly men:firefly man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:firefly woman:firefly women:firefly woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:firefly man:firefly men:firefly man]
        [DESCRIPTION:A person with the wings and head of a firefly.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'f']
        [COLOR:2:0:1]
