# Stoat man

> Fonte: [Stoat man](https://dwarffortresswiki.org/index.php/Stoat_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes stoat men for their ability to take down large prey.**
- **Biome**
- **Taiga Tundra**
- **Variations**
- **Stoat - Stoat man - Giant stoat**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,517.5 cm 3
- **Mid:** 17,587.5 cm 3
- **Max:** 35,175 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A long-bodied person with the head of a stoat.*

**Stoat men** are humanoid versions of the common stoat and a species of unremarkable animal people, found in savage taigas and tundras. They are a little over half the size of dwarves when adults and spawn in groups of 1-5 individuals. They should pose no threat unless provoked.

Like other savage animal people, stoat men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like stoat men for their *ability to take down large prey*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Known to prey on unassuming hare men with mind control techniques, robbing them of their boots.

Hates when people call them weasels.\
*Art by Snawpee*

    [CREATURE:STOAT_MAN]
        [COPY_TAGS_FROM:STOAT]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:stoat man:stoat men:stoat man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:stoat woman:stoat women:stoat woman]
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
        [NAME:stoat man:stoat men:stoat man]
        [DESCRIPTION:A long-bodied person with the head of a stoat.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
