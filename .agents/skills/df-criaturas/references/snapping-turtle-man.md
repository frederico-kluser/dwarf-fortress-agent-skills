# Snapping turtle man

> Fonte: [Snapping turtle man](https://dwarffortresswiki.org/index.php/Snapping_turtle_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes snapping turtle men for their powerful bites.**
- **Biome**
- **Temperate Freshwater River Temperate Brackish River Temperate Freshwater Lake Temperate Brackish Lake Temperate Freshwater Pool Temperate Brackish Pool**
- **Variations**
- **Common snapping turtle - Snapping turtle man - Giant snapping turtle**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Shell · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 66.666666666667 cm 3
- **Max:** 50,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the shell and head of a snapping turtle.*

**Snapping turtle men** are animal people variants of the common snapping turtle, who can be found in savage temperate lakes and rivers. They spawn in groups of 1-5 individuals and are possibly aggressive, attacking dwarves who attempt to provoke them. In terms of size, they are only a little smaller than a dwarf, which makes them potentially dangerous if confronted by unarmed civilians.

Like other savage animal people, snapping turtle men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like snapping turtle men for their *powerful bites* and their *long necks.*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
They are well known for their skill as ambushers. They will often congregate under the leadership of a giant rat with a stick in the sewers of human cities.

\

Its bark is much less worse than its snap.\
*Art by Salasti*

    [CREATURE:SNAPPING_TURTLE_MAN]
        [COPY_TAGS_FROM:SNAPPING TURTLE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:snapping turtle man:snapping turtle men:snapping turtle man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:snapping turtle woman:snapping turtle women:snapping turtle woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:snapping turtle man:snapping turtle men:snapping turtle man]
        [DESCRIPTION:A person with the shell and head of a snapping turtle.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'t']
        [COLOR:2:0:0]
