# Giant cuttlefish

> Fonte: [Giant cuttlefish](https://dwarffortresswiki.org/index.php/Giant_cuttlefish) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant cuttlefish for their ability to change color.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Cuttlefish - Cuttlefish man - Giant cuttlefish**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Exotic mount · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 207,010 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 1-2
- **Butchering returns**
- **Food items**
- **Meat:** 15
- **Fat:** 10
- **Raw materials**
- **Skin:** Raw hide & Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge sea monster in the shape of a cuttlefish.*

**Giant cuttlefish** are the giant animal counterparts of the standard cuttlefish, over four times heavier than the average dwarf. They are aquatic creatures that will rarely interact with land-dwelling dwarves, however they may squirt ink if threatened.

Despite their size, they apparently retain the ability to be cooked live, assuming your dwarves can find a pot large enough. This may, however, produce significantly less food than a properly-butchered specimen. Because of their internal shell-like structure, giant cuttlefish produce both chitin and raw hide when butchered.

Some dwarves enjoy giant cuttlefish for their *ability to change color* and their *distinctive pupils*.

They have enough ink to flood a factory.\
*Art by Chris Fewster*

    [CREATURE:GIANT_CUTTLEFISH]
        [COPY_TAGS_FROM:CUTTLEFISH]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:cuttlefish]
            [CVCT_REPLACEMENT:giant cuttlefish]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:cuttlefish]
            [CVCT_REPLACEMENT:giant cuttlefish]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20701]
        [GO_TO_START]
        [NAME:giant cuttlefish:giant cuttlefish:giant cuttlefish]
        [CASTE_NAME:giant cuttlefish:giant cuttlefish:giant cuttlefish]
        [DESCRIPTION:A huge sea monster in the shape of a cuttlefish.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'C']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ability to change color]
        [PREFSTRING:distinctive pupils]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
