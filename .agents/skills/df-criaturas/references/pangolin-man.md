# Pangolin man

> Fonte: [Pangolin man](https://dwarffortresswiki.org/index.php/Pangolin_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes pangolin men for their overlapping scales.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Pangolin - Pangolin man - Giant pangolin**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,750 cm 3
- **Mid:** 18,750 cm 3
- **Max:** 37,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and scales of a pangolin.*

**Pangolin men** are humanoid versions of the common pangolin and a species of unremarkable animal people, found in savage tropical plains and forests. They are only a little over half the size of an adult dwarf, making them unlikely to pose a threat to civilians and even less to military squads.

Like other savage animal people, pangolin men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like pangolin men for their *overlapping scales*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
There's been rumors of pangolin men with glowing white scales scouring ancient ruins for technology to commune with. However whether or not these may be true: after a lengthy interview with one of *eir* "watchers," even without hierarchy: it has became clear *ey* follow a faith that drives *em* to discovery.

Constantly has to deal with pandemic-related questions\
*Art by caturchandra\
Commissioned by aammton*

    [CREATURE:PANGOLIN_MAN]
        [COPY_TAGS_FROM:PANGOLIN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:pangolin man:pangolin men:pangolin man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:pangolin woman:pangolin women:pangolin woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:pangolin man:pangolin men:pangolin man]
        [DESCRIPTION:A person with the head and scales of a pangolin.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'p']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
