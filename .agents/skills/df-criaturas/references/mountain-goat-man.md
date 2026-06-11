# Mountain goat man

> Fonte: [Mountain goat man](https://dwarffortresswiki.org/index.php/Mountain_goat_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mountain goat men for their beards.**
- **Biome**
- **Mountain**
- **Variations**
- **Mountain goat - Mountain goat man - Giant mountain goat**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Horn · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,000 cm 3
- **Mid:** 12,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A horned person with the head of a mountain goat.*

**Mountain goat men** are humanoid versions of the common mountain goat and a species of unremarkable animal people, found in savage mountains. They are as heavy as dwarves when adults and spawn in groups of 1-5 individuals, who should pose no threat to dwarves unless provoked.

Like other savage animal people, mountain goat men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode. Mountain goat men are able to wear dwarf-sized armor and clothing, making it a good choice for then to start in a dwarven civilization.

Some dwarves like mountain goat men for their *beards*, their *long horns* and their *surefootedness*.

Can stomach anything.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

The most remarkable thing about a mountain goat man standing in the doorway, is that it's a mountain goat man, and that it's standing in the doorway.

|  |
|----|
| "Mountain goat man" in other / Languages / Dwarven / : / onol belbez udos / Elven / : / thele efafi onino / Goblin / : / ngosla orang ngorûg / Human / : / thakom apsong abo |

    [CREATURE:GOAT_MOUNTAIN_MAN]
        [COPY_TAGS_FROM:GOAT_MOUNTAIN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:mountain goat man:mountain goat men:mountain goat man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:mountain goat woman:mountain goat women:mountain goat woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:HOOF_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:mountain goat man:mountain goat men:mountain goat man]
        [DESCRIPTION:A horned person with the head of a mountain goat.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'g']
        [COLOR:7:0:1]
