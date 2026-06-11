# Skunk man

> Fonte: [Skunk man](https://dwarffortresswiki.org/index.php/Skunk_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes skunk men for their distinctive striping.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Skunk - Skunk man - Giant skunk**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,700 cm 3
- **Mid:** 18,500 cm 3
- **Max:** 37,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A striped person with the head and tail of a skunk.*

**Skunk men** are animal people versions of the common skunk, who can be found in savage temperate flatlands and forests. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like skunk men for their *foul smell* and their *distinctive striping*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite popular belief, skunk men do not speak in a French accent while playing the role of a passive-aggressive and tenacious romantic. They also do not forcefully try to make cats or cat humanoids their wives or girlfriends.

Still smells terrible.

|  |
|----|
| "Skunk man" in other / Languages / Dwarven / : / rungak udos / Elven / : / dipane onino / Goblin / : / masnäm ngorûg / Human / : / slenshi abo |

    [CREATURE:SKUNK_MAN]
        [COPY_TAGS_FROM:SKUNK]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:skunk man:skunk men:skunk man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:skunk woman:skunk women:skunk woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:skunk man:skunk men:skunk man]
        [DESCRIPTION:A striped person with the head and tail of a skunk.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:0:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
