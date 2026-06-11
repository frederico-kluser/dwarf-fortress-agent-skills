# Armadillo man

> Fonte: [Armadillo man](https://dwarffortresswiki.org/index.php/Armadillo_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes armadillo men for their thick, bony armor plates.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Armadillo - Armadillo man - Giant armadillo**
- **Attributes**
- **Alignment:** Savage
- **Learns · Shell · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,875 cm 3
- **Mid:** 19,375 cm 3
- **Max:** 38,750 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the hide and head of an armadillo.*

**Armadillo men** are animal people variants of the common armadillo who can be found in savage tropical regions. They spawn in groups of 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, armadillo men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like armadillo men for their *thick, bony armor plates*.

Doesn't need to wear as much armor.\
*Art by silveranswer*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Armadillo men do not, in fact, have accents. Nor do they wear 37,854 cm3 hats.

    [CREATURE:ARMADILLO MAN]
        [COPY_TAGS_FROM:ARMADILLO]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:armadillo man:armadillo men:armadillo man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:armadillo woman:armadillo women:armadillo woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:armadillo man:armadillo men:armadillo man]
        [DESCRIPTION:A person with the hide and head of an armadillo.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'a']
        [COLOR:7:0:0]
