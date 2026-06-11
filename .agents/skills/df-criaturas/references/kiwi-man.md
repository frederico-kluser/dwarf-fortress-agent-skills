# Kiwi man

> Fonte: [Kiwi man](https://dwarffortresswiki.org/index.php/Kiwi_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kiwi men for their long beaks.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland**
- **Variations**
- **Kiwi - Kiwi man - Giant kiwi**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,235 cm 3
- **Mid:** 18,125 cm 3
- **Max:** 36,250 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and feathers of a kiwi.*

**Kiwi men** are animal people variants of the common kiwi, who inhabit savage temperate shrublands and forests. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, kiwi men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like kiwi men for their *long beaks*.

A pencil drawing of a Kiwiman armed with a stone axe.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Despite common belief, there appears to be no major connection between the location of kiwi men and their proximity to countries far east of badland continents.

    [CREATURE:KIWI MAN]
        [COPY_TAGS_FROM:BIRD_KIWI]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:kiwi man:kiwi men:kiwi man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:kiwi woman:kiwi women:kiwi woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TALON_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:kiwi man:kiwi men:kiwi man]
        [DESCRIPTION:A person with the head and feathers of a kiwi.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'k']
        [COLOR:6:0:0]
