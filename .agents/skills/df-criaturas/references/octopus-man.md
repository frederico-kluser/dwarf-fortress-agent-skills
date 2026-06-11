# Octopus man

> Fonte: [Octopus man](https://dwarffortresswiki.org/index.php/Octopus_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes octopus men for their many arms.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Octopus - Octopus man - Giant octopus**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Learns · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 150 cm 3
- **Max:** 37,500 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with an octopus in place of a head.*

**Octopus men** are animal people variants of the common octopus who can be found in savage oceans. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

While they can learn and are able to join civilizations, they never do so, as they are completely aquatic and cannot survive on the surface.

Some dwarves like octopus men for their *many arms* and their *intelligence*.

You don't wanna know where the beak is.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
**Octopus men** have been known to take over the bodies of Spider-men, deeming themselves to have superior intellect compared to the Spider-men.

Octopus men are a surprisingly unscrupulous race; they often feud with squid men over territory and are known to steal precious materials from them. In rare instances, squid man singers have even been kidnapped from their undersea homes and forced to perform for octopus men. Despite this, there is evidence that octopus men and squid men were on equal terms in the distant past.

Octopus men occasionally will don a shirt, coat, and trousers and marry a human, usually living together in the suburbs with children. Despite their obvious differences, members of the civilization rarely suspect anything, with the notable exceptions of chefs. Such chefs will form a grudge against the octopus man and frequently seek vengeance armed with a meat cleaver.

For over 14 years there have been rumors of some octopus men actually being deer men whose bodies have been taken over by a parasitic type of octopus, dubbed "oktigi". This is just silly, and the rumors have stopped by the end of 2020.

    [CREATURE:OCTOPUS_MAN]
        [COPY_TAGS_FROM:OCTOPUS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:octopus]
            [CVCT_REPLACEMENT:octopus man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:octopus]
            [CVCT_REPLACEMENT:octopus man]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:octopus man:octopus men:octopus man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:octopus woman:octopus women:octopus woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:octopus man:octopus men:octopus man]
        [DESCRIPTION:A person with an octopus in place of a head.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'o']
        [COLOR:7:0:0]
