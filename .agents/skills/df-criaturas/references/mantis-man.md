# Mantis man

> Fonte: [Mantis man](https://dwarffortresswiki.org/index.php/Mantis_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mantis men for their grasping legs.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Mantis - Mantis man - Giant mantis**
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

*A green person with the head and arms of a mantis.*

**Mantis men** are animal people variants of the common mantis who can inhabit most savage biomes. They spawn in groups of 1-3 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf. All mantis men are born with Legendary skill in climbing.

Like other savage animal people, mantis men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like mantis men for their *grasping legs* and their *predatory nature*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
For the beta testers for mantis men, there was good news and bad news. The bad news is those copies of the beta were postponed indefinitely. The good news is we don't have to deal with an army of mantis men. So take arms and kill any you happen to see on your map.

Known to carry monster condoms for their magnum dongs.

Not telepathic, contrary to popular opinion.

Can fly to fuel nightmares.

You'll always be in a mantis' thoughts and prayers.\
*Art by Tommy Graven*

    [CREATURE:MANTIS_MAN]
        [COPY_TAGS_FROM:MANTIS]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:mantis man:mantis men:mantis man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:mantis woman:mantis women:mantis woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_EDGE_ATTACK]
        [APPLY_CREATURE_VARIATION:ARM_LOWER_SNATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:mantis man:mantis men:mantis man]
        [DESCRIPTION:A green person with the head and arms of a mantis.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'m']
        [COLOR:2:0:1]
