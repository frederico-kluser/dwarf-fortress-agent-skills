# Leopard gecko man

> Fonte: [Leopard gecko man](https://dwarffortresswiki.org/index.php/Leopard_gecko_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes leopard gecko men for their coloration.**
- **Biome**
- **Any Desert**
- **Variations**
- **Leopard gecko - Leopard gecko man - Giant leopard gecko**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,025 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and fingers of a gecko.*

**Leopard gecko men** are humanoid versions of the common leopard gecko and a species of unremarkable animal people, found in savage deserts. They are a bit over half the size of dwarves and spawn in groups of 1-5 individuals, who should pose no threat to dwarves unless provoked. All leopard gecko men are born with Legendary skill in climbing.

Like other savage animal people, leopard gecko men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like leopard gecko men for their *coloration* and their *amazing sticky feet*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Contrary to popular belief, leopard gecko men will not sell your dwarves wagon insurance.

    [CREATURE:LEOPARD_GECKO_MAN]
        [COPY_TAGS_FROM:GECKO_LEOPARD]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:leopard gecko man:leopard gecko men:leopard gecko man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:leopard gecko woman:leopard gecko women:leopard gecko woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:leopard gecko man:leopard gecko men:leopard gecko man]
        [DESCRIPTION:A person with the head and fingers of a gecko.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'g']
        [COLOR:6:0:1]
