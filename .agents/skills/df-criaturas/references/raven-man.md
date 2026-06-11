# Raven man

> Fonte: [Raven man](https://dwarffortresswiki.org/index.php/Raven_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes raven men for their intelligence.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Taiga Any Temperate Forest Any Temperate Wetland Tundra Any Desert**
- **Variations**
- **Raven - Raven man - Giant raven**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,483.3333333333 cm 3
- **Max:** 35,600 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a raven.*

**Raven men** are animal people variants of the common raven, who inhabit most savage biomes. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All raven men are born with Legendary skill in climbing.

Like other savage animal people, raven men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like raven men for their *intelligence*.

Never forgets a face.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Ancient scripts tell of a Raven Woman whose father was a great demon, capable of shadow magic. Text from an unknown language roughly translating to 'Azarath Mentrion Zinthos' accompanies a few recountings, as well as mentions of a robin man, a shapeshifting beast man, an extraterrestrial elf, and a mechanically enhanced human, but as none of these exist, they are discounted as fanciful tales.

|  |
|----|
| "Raven man" in other / Languages / Dwarven / : / toltot udos / Elven / : / ceca onino / Goblin / : / rosp ngorûg / Human / : / tuma abo |

    [CREATURE:RAVEN_MAN]
        [COPY_TAGS_FROM:BIRD_RAVEN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:raven man:raven men:raven man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:raven woman:raven women:raven woman]
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
        [NAME:raven man:raven men:raven man]
        [DESCRIPTION:A person with the head and wings of a raven.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'r']
        [COLOR:0:0:1]
