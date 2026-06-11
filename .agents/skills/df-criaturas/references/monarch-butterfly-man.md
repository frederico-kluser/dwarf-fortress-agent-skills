# Monarch butterfly man

> Fonte: [Monarch butterfly man](https://dwarffortresswiki.org/index.php/Monarch_butterfly_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes monarch butterfly men for their coloration.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Monarch butterfly - Monarch butterfly man - Giant monarch butterfly**
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

*A person with the wings and head of a monarch butterfly.*

**Monarch butterfly men** are animal people variants of the common monarch butterfly, who can inhabit most savage biomes. They spawn in groups of 2-5 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf. All monarch butterfly men are born with Legendary skill in climbing.

Like other savage animal people, monarch butterfly men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like monarch butterfly men for their *coloration*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
A monarch butterfly man and his army of butterfly men have been spotted obsessively antagonizing a (self-proclaimed) super-genius scholar dwarf and his two sons, however, he is always stopped by their blond muscular bodyguard. It is said the butterfly man and his minions fly around in a flying giant cocoon that has no obvious means of propulsion.

    [CREATURE:BUTTERFLY_MONARCH_MAN]
        [COPY_TAGS_FROM:BUTTERFLY_MONARCH]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:monarch butterfly man:monarch butterfly men:monarch butterfly man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:monarch butterfly woman:monarch butterfly women:monarch butterfly woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:monarch butterfly man:monarch butterfly men:monarch butterfly man]
        [DESCRIPTION:A person with the wings and head of a monarch butterfly.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:4:0:1]
