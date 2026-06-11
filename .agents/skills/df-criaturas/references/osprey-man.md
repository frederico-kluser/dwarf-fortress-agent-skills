# Osprey man

> Fonte: [Osprey man](https://dwarffortresswiki.org/index.php/Osprey_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes osprey men for their fishing ability.**
- **Biome**
- **Any Ocean Any Lake Any River Tropical Freshwater Marsh Tropical Saltwater Marsh Temperate Freshwater Marsh Temperate Saltwater Marsh**
- **Variations**
- **Osprey - Osprey man - Giant osprey**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 990 cm 3
- **Mid:** 18,000 cm 3
- **Max:** 36,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of an osprey.*

**Osprey men** are animal people variants of the common osprey, who inhabit savage water-heavy biomes. They spawn in groups of anywhere between 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All osprey men are born with Legendary skill in climbing.

Like other savage animal people, osprey men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Osprey women inside your civilization can lay eggs inside a nest box.

Some dwarves like osprey men for their *fishing ability*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Osprey people are flightless birds, but according to research by a certain ~~bearded bastard~~ dwarf, Osprey people like to hang atop trees and high buildings until they die of dehydration or starvation, perhaps in a ritual to ascend into the ranks of the flying ones high above their flightless plane of existence, in hopes that they might soar the skies freely once again as their ancestors once did, this particular religious ritual is called the ascension, but it's best known as a lack of AI.

They also make decent farmers, just remember to keep them locked indoors.

Bird fighting stance\
*Art by Tim Ziegler*

    [CREATURE:OSPREY_MAN]
        [COPY_TAGS_FROM:BIRD_OSPREY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:osprey man:osprey men:osprey man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:osprey woman:osprey women:osprey woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TALON_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:osprey man:osprey men:osprey man]
        [DESCRIPTION:A person with the head and wings of an osprey.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'o']
        [COLOR:7:0:1]
