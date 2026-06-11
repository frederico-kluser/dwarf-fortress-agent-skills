# Crow man

> Fonte: [Crow man](https://dwarffortresswiki.org/index.php/Crow_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes crow men for their intelligence.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Taiga Any Temperate Forest Any Temperate Wetland**
- **Variations**
- **Crow - Crow man - Giant crow**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,410 cm 3
- **Max:** 35,250 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small person with the head and wings of a crow.*

**Crow men** are animal people variants of the common crow who inhabit a variety of savage temperate biomes as well as taigas. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All crow men are born with Legendary skill in climbing.

Like other savage animal people, crow men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like crow men for their *intelligence*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
As the crow man flies is a common expression among some human cultures, as most crow men they see seem to know exactly where they're going after a couple weeks, and won't stop even for inconvenient and negligible annoyances.

Crow men seem to like wandering around ruins and temples, and caw at anyone who gets in their way.

People still associate bad luck with him.\
*Art by Ermine*

|  |
|----|
| "Crow man" in other / Languages / Dwarven / : / ustir udos / Elven / : / minaro onino / Goblin / : / osok ngorûg / Human / : / erthok abo |

    [CREATURE:CROW_MAN]
        [COPY_TAGS_FROM:BIRD_CROW]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:crow man:crow men:crow man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:crow woman:crow women:crow woman]
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
        [NAME:crow man:crow men:crow man]
        [DESCRIPTION:A small person with the head and wings of a crow.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:0:0:1]
