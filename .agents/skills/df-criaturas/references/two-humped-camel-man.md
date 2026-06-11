# Two-humped camel man

> Fonte: [Two-humped camel man](https://dwarffortresswiki.org/index.php/Two-humped_camel_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes two-humped camel men for their humps.**
- **Biome**
- **Any Desert**
- **Variations**
- **Two-humped camel - Two-humped camel man - Giant two-humped camel**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Milkable · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 28,500 cm 3
- **Mid:** 142,500 cm 3
- **Max:** 285,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and humps of a two-humped camel.*

**Two-humped camel men** are humanoid versions of the common two-humped camel and a species of animal people, found in savage deserts. They are nearly 5 times bigger than dwarves when adults and spawn in groups of 5-10 individuals, and as such make potentially dangerous opponents if provoked. Funnily enough, only 5-10 of them may exist in a single area before they're considered extinct, so you might witness your map's entire population of camel men pass by your fort all in one go.

Like other savage animal people, two-humped camel men may occasionally join civilizations, becoming full-fledged citizens, who may appear in your fortress as visitors or be playable in adventurer mode.

As the animal person template does not remove it, two-humped camel women produce milk.

Some dwarves like two-humped camel men for their *humps*.

Has little problems containing water.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite many depictions of camel men, they are not known to promote tobacco related products.

    [CREATURE:CAMEL_2_HUMP_MAN]
        [COPY_TAGS_FROM:CAMEL_2_HUMP]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:two-humped camel]
            [CVCT_REPLACEMENT:two-humped camel man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:two-humped camel]
            [CVCT_REPLACEMENT:two-humped camel man]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:two-humped camel man:two-humped camel men:two-humped camel man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:two-humped camel woman:two-humped camel women:two-humped camel woman]
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
        [NAME:two-humped camel man:two-humped camel men:two-humped camel man]
        [DESCRIPTION:A person with the head and humps of a two-humped camel.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'C']
        [COLOR:6:0:0]
        [GO_TO_TAG:BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [APPLY_CREATURE_VARIATION:NAIL_MATERIALS]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
