# Giant beaver

> Fonte: [Giant beaver](https://dwarffortresswiki.org/index.php/Giant_beaver) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant beavers for their dams.**
- **Biome**
- **Any Temperate Lake Any Temperate River**
- **Variations**
- **Beaver - Beaver man - Giant beaver**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 34,180 cm 3
- **Mid:** 170,900 cm 3
- **Max:** 341,800 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-20
- **Butchering returns**
- **Food items**
- **Meat:** 14-20
- **Fat:** 13-17
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 0-2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 18-22
- **Skull:** 1
- **Teeth:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large river monster, known for building huge wooden fortresses.*

**Giant beavers** are the giant animal variant of the common beaver, found in savage temperate lakes and rivers where they appear in groups of 3-10 individuals. They are roughly five times the size of a dwarf, but are generally benign and content to simply meander their territory. If confronted, however, they may fight back and make quick work out of inexperienced warriors.

Giant beavers can be captured in cage traps and trained into exotic pets, possessing the standard giant creature value. They provide plenty of meat and bones when butchered, making them useful as potential livestock. Like other giant animals, giant beavers are exotic mounts.

Some dwarves like beavers for their *dams* and their *tree-felling habits*.

## In real life

An animal often called a 'Giant Beaver' lived in Ice Age North America. Castoroides was the size of a black bear. However, the DF Giant Beaver is much bigger than Castoroides.

Dams it all.

    [CREATURE:GIANT_BEAVER]
        [COPY_TAGS_FROM:BEAVER]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1709]
        [GO_TO_START]
        [NAME:giant beaver:giant beavers:giant beaver]
        [CASTE_NAME:giant beaver:giant beavers:giant beaver]
        [GENERAL_CHILD_NAME:giant beaver kit:giant beaver kits]
        [DESCRIPTION:A large river monster, known for building huge wooden fortresses.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:10]
        [CREATURE_TILE:'B']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:dams]
        [PREFSTRING:tree-felling habits]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
