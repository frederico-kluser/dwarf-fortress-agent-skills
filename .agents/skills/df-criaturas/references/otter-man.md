# Otter man

> Fonte: [Otter man](https://dwarffortresswiki.org/index.php/Otter_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes otter men for their fluffy faces.**
- **Biome**
- **Any Lake Any Lake Any River**
- **Variations**
- **River otter - Otter man - Giant otter**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,000 cm 3
- **Mid:** 20,000 cm 3
- **Max:** 40,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the long body and head of an otter.*

**Otter men** are animal people variants of the common river otter who can be found in savage lakes and rivers. They spawn in groups of 5-10 individuals and are generally content to keep to themselves. In terms of size, they are over half the weight of the average dwarf.

Like other savage animal people, otter men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like otter men for their *playfulness* and their *fluffy faces*.

*Art found at http://monstrumathenaeum.org*

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Otter men are not known to be atheists, and are not at war with other atheists who are human.

    [CREATURE:OTTER_MAN]
        [COPY_TAGS_FROM:RIVER OTTER]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:otter man:otter men:otter man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:otter woman:otter women:otter woman]
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
        [NAME:otter man:otter men:otter man]
        [DESCRIPTION:A person with the long body and head of an otter.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'o']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
