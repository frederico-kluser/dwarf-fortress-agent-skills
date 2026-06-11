# Pond turtle man

> Fonte: [Pond turtle man](https://dwarffortresswiki.org/index.php/Pond_turtle_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes pond turtle men for their shells.**
- **Biome**
- **Any Lake**
- **Variations**
- **Pond turtle - Pond turtle man - Giant pond turtle**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Shell · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 352.5 cm 3
- **Max:** 35,250 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and shell of a pond turtle.*

**Pond turtle men** are animal people variants of the common pond turtle who can be encountered in savage lakes. They spawn in groups of 1-3 individuals and are able to retract into their shells when threatened, much like common turtles. In terms of size, they are a little over half the weight of the average dwarf.

Some dwarves like pond turtle men for their *shells*.

Putting on breastplates is difficult.\
*Art by Arne*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Pond turtle men are known for their ability to count by twos and tie their shoes, despite never wearing shoes.

    [CREATURE:POND_TURTLE_MAN]
        [COPY_TAGS_FROM:POND_TURTLE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:pond turtle man:pond turtle men:pond turtle man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:pond turtle woman:pond turtle women:pond turtle woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:pond turtle man:pond turtle men:pond turtle man]
        [DESCRIPTION:A person with the head and shell of a pond turtle.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'t']
        [COLOR:2:0:0]
