# Giant octopus

> Fonte: [Giant octopus](https://dwarffortresswiki.org/index.php/Giant_octopus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant octopuses for their many arms.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Octopus - Octopus man - Giant octopus**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Exotic mount · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 940.4 cm 3
- **Max:** 235,100 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 12-13
- **Fat:** 10
- **Brain:** 1
- **Eyes:** 2
- **Raw materials**
- **Skin:** Raw hide and chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A dangerous water monster known for attacking ships at sea.*

**Giant octopuses** inherit the abilities of octopuses, including their ability to squirt ink.

Giant octopuses can act as a replacement shark in moats. They have the advantage of having multiple arms, and are therefore less likely to be hit in a vital area.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Recipe for moat: 1 or more octopus/shark/crocodile/alligator added into a bowl (moat). Fill with water (7/7 for optimal conditions). Add goblins or another topping (victim) of your choice and whisk (mutilate).

## In real life

This sea monster is also known as the kraken. It regularly attacks ships (possibly one reason why dwarves never build ships). In some legends, sailors evade this terrifying monster by digging deep underground to an island rather than face the perils of the sea.

    [CREATURE:GIANT_OCTOPUS]
        [COPY_TAGS_FROM:OCTOPUS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:octopus]
            [CVCT_REPLACEMENT:giant octopus]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:octopus]
            [CVCT_REPLACEMENT:giant octopus]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:4702]
        [GO_TO_START]
        [NAME:giant octopus:giant octopuses:giant octopus]
        [CASTE_NAME:giant octopus:giant octopuses:giant octopus]
        [DESCRIPTION:A dangerous water monster known for attacking ships at sea.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'O']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:intelligence]
        [PREFSTRING:many arms]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:657:438:219:1900:2900]
