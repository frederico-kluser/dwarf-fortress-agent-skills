# Cuttlefish man

> Fonte: [Cuttlefish man](https://dwarffortresswiki.org/index.php/Cuttlefish_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cuttlefish men for their distinctive pupils.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Cuttlefish - Cuttlefish man - Giant cuttlefish**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Learns · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,500 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with a cuttlefish in place of a head.*

**Cutteflish men** are animal people variants of the common cuttlefish who can be found in savage oceans. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

While they can learn and are able to join civilizations, they never do so, as they are completely aquatic and cannot survive on the surface.

Some dwarves like cuttlefish men for their *ability to change color* and their *distinctive pupils*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Legends tell of an ancient **cuttlefish man**, a terrifying sea creature that surpassed all other forgotten beasts in both size and strength. This cuttlefish man was known to incite random fits of madness in nearby fortresses and to inspire dark cults to worship it. It is widely believed by these cults that this ancient cuttlefish man will rise from the ocean at the end of time, only to destroy all of civilization. Only time will tell if this is true, and whether any weapons of mortal man will be able to destroy such a creature. However, this dreaded creature is known to have one weakness, with which to drive it back to its home in the depths: the humble steam boat. Pray to Armok that boats are added to the game before this nightmare becomes a reality. This monstrosity lives in a legendary place, constructed with alien geometry, named R'lyeh.

Some elderly cuttlefish men have been observed aiding trainee squid men soldiers in their war against the octopus men.

You don't want to know where the ink comes out.\
*Art by hobbaloo*

    [CREATURE:CUTTLEFISH_MAN]
        [COPY_TAGS_FROM:CUTTLEFISH]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:cuttlefish]
            [CVCT_REPLACEMENT:cuttlefish man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:cuttlefish]
            [CVCT_REPLACEMENT:cuttlefish man]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:cuttlefish man:cuttlefish men:cuttlefish man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:cuttlefish woman:cuttlefish women:cuttlefish woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:cuttlefish man:cuttlefish men:cuttlefish man]
        [DESCRIPTION:A person with a cuttlefish in place of a head.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:6:0:0]
