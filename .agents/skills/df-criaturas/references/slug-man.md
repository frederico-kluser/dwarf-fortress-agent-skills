# Slug man

> Fonte: [Slug man](https://dwarffortresswiki.org/index.php/Slug_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes slug men for their slime trails.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Slug - Slug man - Giant slug**
- **Attributes**
- **Alignment:** Savage
- **Genderless · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A great slug with the torso of a man. It pulls itself across the ground with its hands for greater speed.*

**Slug men** are animal people variants of the common slug, who can inhabit most savage biomes. They spawn in groups of 1-3 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, slug men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like slug men for their *slime trails*.

Slippery to the touch.

|  |
|----|
| "Slug man" in other / Languages / Dwarven / : / tozör udos / Elven / : / ralu onino / Goblin / : / omu ngorûg / Human / : / dush abo |

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Slug men have been shown to have a preference for spears over other weapons and are highly fascinated by large dwarven computers.

    [CREATURE:SLUG_MAN]
        [COPY_TAGS_FROM:SLUG]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:slug man:slug men:slug man]
        [CASTE_NAME:slug man:slug men:slug man]
        [DESCRIPTION:A great slug with the torso of a man.  It pulls itself across the ground with its hands for greater speed.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:6:0:0]
