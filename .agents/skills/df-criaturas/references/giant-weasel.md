# Giant weasel

> Fonte: [Giant weasel](https://dwarffortresswiki.org/index.php/Giant_weasel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant weasels for their long bodies.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra Tundra**
- **Variations**
- **Weasel - Weasel man - Giant weasel**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,140 cm 3
- **Mid:** 100,700 cm 3
- **Max:** 201,400 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 12-13
- **Fat:** 12
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 12-18
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster taking the shape of a weasel.*

**Giant weasels** are much larger versions of the common weasel, found in most savage biomes. While the common animal is one of the smallest in the game, the giant variant is about three times bigger than a dwarf, but they are generally harmless due to being benign. Like normal weasels, they are solitary, don't spawn during the winter and their young are called *kits*.

Giants weasels may be captured in cage traps and trained into pets. They're large enough to actually produce food when butchered, giving returns equivalent to a mule in quantity. Like their common counterparts, giant weasels are very short-lived, living no more than 2-3 years, making keeping them around for extended periods of time a questionable decision. Giant weasels are exotic mounts and may be witnessed being used by elves during sieges.

Some dwarves like giant weasels for their *long bodies* and their *short legs*.

"Earth-shattering thud" goes the weasel.

    [CREATURE:GIANT_WEASEL]
        [COPY_TAGS_FROM:WEASEL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:100700]
        [GO_TO_START]
        [NAME:giant weasel:giant weasels:giant weasel]
        [CASTE_NAME:giant weasel:giant weasels:giant weasel]
        [GENERAL_CHILD_NAME:giant weasel kit:giant weasel kits]
        [DESCRIPTION:A large monster taking the shape of a weasel.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'W']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:long bodies]
        [PREFSTRING:short legs]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
