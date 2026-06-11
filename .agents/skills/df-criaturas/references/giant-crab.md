# Giant crab

> Fonte: [Giant crab](https://dwarffortresswiki.org/index.php/Giant_crab) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant crabs for their pincers.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Crab - Crab man - Giant crab**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 32.04 cm 3
- **Max:** 256,320 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 19
- **Fat:** 19
- **Brain:** 1
- **Heart:** 1
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a crab.*

As its name suggests, the **giant crab** is an especially large version of the crab, and can be found on savage beaches, where they spawn one at a time. Standing 32 times larger than a normal crab, these creatures are large enough to not be intimidated by the presence of dwarves and will fight if provoked, which may be a fatal encounter for a civilian who just happened to be on its path. However, they should not prove to be a threat to a crossbow-wielding hunter or a half-competent military squad.

Like their smaller counterparts, all giant crabs possess Legendary skill in climbing as well as blue-colored blood. Unlike normal crabs, however, they are tamable creatures with the standard high pet value of giant animals, meaning they can be freely used as valuable pets or in the meat industry. Giant crabs are considered exotic mounts, so you may see elves riding them into battle in the event of a siege.

Some dwarves like giant crabs for their *pincers* and their *sideways walk*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

As with most creatures, the best way to defeat the giant enemy crab is to attack its weak point for massive damage.

Only true players can see its health bar.\
*Art by Luigi Giordano*

    [CREATURE:GIANT_CRAB]
        [COPY_TAGS_FROM:CRAB]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:3204]
        [GO_TO_START]
        [NAME:giant crab:giant crabs:giant crab]
        [CASTE_NAME:giant crab:giant crabs:giant crab]
        [DESCRIPTION:A large monster in the shape of a crab.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'C']
        [COLOR:4:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:pincers]
        [PREFSTRING:sideways walk]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
