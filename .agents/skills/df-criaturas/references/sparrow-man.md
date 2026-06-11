# Sparrow man

> Fonte: [Sparrow man](https://dwarffortresswiki.org/index.php/Sparrow_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sparrow men for their lovely songs.**
- **Biome**
- **Any Grassland Any Savanna Any Shrubland Any Temperate Forest Any Tropical Forest Any Desert Any Wetland**
- **Variations**
- **Sparrow - Sparrow man - Giant sparrow**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 2,334.3333333333 cm 3
- **Max:** 35,015 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a sparrow.*

**Sparrow men** are animal people variants of the common sparrow who inhabit many savage biomes. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All sparrow men are born with Legendary skill in climbing.

Like other savage animal people, sparrow men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like sparrow men for their *dust baths* and their *lovely songs*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Sparrow men are known for their habit of endeavors in piracy. Beware, if you let young female nobles stay near fun coasts, reanimated skeletons of humans may take her, prompting a sparrow man to drag along your smith to rescue her.

Rumours of sparrow women making prepared meals using sea lamprey late at night have yet to be verified.

    [CREATURE:SPARROW_MAN]
        [COPY_TAGS_FROM:SPARROW]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:sparrow man:sparrow men:sparrow man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:sparrow woman:sparrow women:sparrow woman]
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
        [NAME:sparrow man:sparrow men:sparrow man]
        [DESCRIPTION:A person with the head and wings of a sparrow.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:6:0:0]
