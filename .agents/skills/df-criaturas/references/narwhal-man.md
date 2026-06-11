# Narwhal man

> Fonte: [Narwhal man](https://dwarffortresswiki.org/index.php/Narwhal_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes narwhal men for their horns.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Narwhal - Narwhal man - Giant narwhal**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 63,500 cm 3
- **Mid:** 317,500 cm 3
- **Max:** 635,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized creature with the arms and torso on a man, but with the head and tail of a narwhal.*

**Narwhal men** are animal people variants of the common narwhal who can be found in savage arctic oceans. They spawn in groups of 5-10 individuals and are generally content to keep to themselves. In terms of size, they are over ten times heavier than the average dwarf.

While they can learn and are able to join civilizations, they never do so, as they are completely aquatic and cannot survive on the surface.

Some dwarves like narwhal men for their *horns*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite rumors, narwhal women are incapable of generating forcefields.

    [CREATURE:NARWHAL MAN]
        [COPY_TAGS_FROM:NARWHAL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:narwhal man:narwhal men:narwhal man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:narwhal woman:narwhal women:narwhal woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TAIL_ATTACK]
        [APPLY_CREATURE_VARIATION:TUSK_STAB_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:narwhal man:narwhal men:narwhal man]
        [DESCRIPTION:A medium-sized creature with the arms and torso on a man, but with the head and tail of a narwhal.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'N']
        [COLOR:7:0:0]
