# Louse man

> Fonte: [Louse man](https://dwarffortresswiki.org/index.php/Louse_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes louse men for their ability to infest.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Louse - Louse man - Giant louse**
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

*A person with the head and legs of a louse.*

**Louse men** are animal people variants of the common louse, who can inhabit most savage biomes. They spawn in groups of 1-3 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf. All louse men are born with Legendary skill in climbing.

Like other savage animal people, louse men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like louse men for their *ability to infest*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
So far we failed to locate the louse man called Roger Smith. A shame, considering how valuable the constructs he is said to possess would be for dwarfkind.

|  |
|----|
| "Louse man" in other / Languages / Dwarven / : / sosmil udos / Elven / : / lenipe onino / Goblin / : / baru ngorûg / Human / : / slupi abo |

    [CREATURE:LOUSE_MAN]
        [COPY_TAGS_FROM:LOUSE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:louse man:louse men:louse man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:louse woman:louse women:louse woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:louse man:louse men:louse man]
        [DESCRIPTION:A person with the head and legs of a louse.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'l']
        [COLOR:6:0:0]
