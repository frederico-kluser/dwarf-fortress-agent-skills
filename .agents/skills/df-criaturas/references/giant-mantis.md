# Giant mantis

> Fonte: [Giant mantis](https://dwarffortresswiki.org/index.php/Giant_mantis) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant mantises for their grasping legs.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Mantis - Mantis man - Giant mantis**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 1-1
- **Butchering returns**
- **Food items**
- **Meat:** 40
- **Fat:** 19
- **Brain:** 2
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a mantis.*

**Giant mantises** are large (size 200000, like most giant arthropods) fliers that enter your map alone, and spend most of the time flying all around the map. They are not aggressive if left alone, but they have the unique ability of being able to latch on flesh with their forearms, making them quite good fighters if pressed.

Giant mantises can be tamed, but live only one year, making having a breeding population very difficult, as most of your adults will die on the first of the year, and lack the characteristics of a good attack creature, despite how cool it would be to have giant mantises as fortress defense.

Some dwarves like giant mantises for their *predatory nature* and their *grasping legs*.

Bites other giant creatures' heads off when aroused.\
*Art by Jiri Kus*

    [CREATURE:GIANT_MANTIS]
        [COPY_TAGS_FROM:MANTIS]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant mantis:giant mantises:giant mantis]
        [CASTE_NAME:giant mantis:giant mantises:giant mantis]
        [DESCRIPTION:A large monster in the shape of a mantis.]
        [POPULATION_NUMBER:25:50]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'M']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:predatory nature]
        [PREFSTRING:grasping legs]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
