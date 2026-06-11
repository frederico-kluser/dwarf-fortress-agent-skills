# Chameleon man

> Fonte: [Chameleon man](https://dwarffortresswiki.org/index.php/Chameleon_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes chameleon men for their ability to change color.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland Tropical Savanna Any Desert**
- **Variations**
- **Chameleon - Chameleon man - Giant chameleon**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,075 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A colorful person with the head and tail of a chameleon.*

**Chameleon men** are animal people variants of the common chameleon who can be found in savage tropical and desert regions, spawning in groups of 1-5 individuals, and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like chameleon men for their *ability to change color* and their *eyes*.

Can blend into any environment.\
*Art by Dean Spencer*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

In adventure mode, chameleon men will occasionally set up shops inside dungeons "Dungeon (zone)"), and will go berserk if their trade goods get stolen. Despite their harmless appearance, said chameleon men will always be legendary fighters when provoked.

Reports have surfaced of chameleon men with expertise in fire spontaneously turning and remaining blue.

Instances were reported when a chameleon woman would join a fort as a monster slayer, eventually claim a nest box, and lay up to 50 eggs at a time, that dwarves would cook and eat.

    [CREATURE:CHAMELEON_MAN]
        [COPY_TAGS_FROM:CHAMELEON]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:chameleon man:chameleon men:chameleon man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:chameleon woman:chameleon women:chameleon woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:chameleon man:chameleon men:chameleon man]
        [DESCRIPTION:A colorful person with the head and tail of a chameleon.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:2:0:1]
