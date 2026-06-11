# Giant monitor lizard

> Fonte: [Giant monitor lizard](https://dwarffortresswiki.org/index.php/Giant_monitor_lizard) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant monitor lizards for their intelligence.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Monitor lizard - Monitor lizard man - Giant monitor lizard**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 559.8 cm 3
- **Mid:** 466,500 cm 3
- **Max:** 933,000 cm 3
- **Food products**
- **Eggs:** 15-25
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 35-41
- **Fat:** 28
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2-3
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 34-38
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a monitor lizard.*

**Giant monitor lizards** are massive cousins of the common monitor lizard who can be found in savage tropical plains and forests. They spawn individually and meander through the map, often paying little mind to dwarves in their vicinity. While over 15 times the size of the average dwarf, these reptiles are not particularly aggressive and don't go out of their way to kill people who approach them, but they will prove a challenge if provoked. Giant monitor lizards share their smaller cousins' rarity, and no more than 10 of them will spawn in the area before they are considered extinct. They are considered exotic mounts, so you may see elves riding them into battle during sieges.

Giant monitor lizards can be captured with cage traps and trained into valuable pets, being as worthy as other giant animals. Like their original counterparts, they are prolific egg-layers and a great candidate to be part of a fortress' egg production. Breeding them will quickly fill the fortress with giant lizards, who can be butchered into a very attractive amount of food and bones when they reach their maximum size. Products made from giant monitor lizard parts are worth twice more than those of standard animals.

Some dwarves like giant monitor lizards for their *intelligence*.

    [CREATURE:GIANT_MONITOR_LIZARD]
        [COPY_TAGS_FROM:MONITOR_LIZARD]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:933]
        [GO_TO_START]
        [NAME:giant monitor lizard:giant monitor lizards:giant monitor lizard]
        [CASTE_NAME:giant monitor lizard:giant monitor lizards:giant monitor lizard]
        [GENERAL_CHILD_NAME:giant monitor lizard hatchling:giant monitor lizard hatchlings]
        [DESCRIPTION:A huge monster in the shape of a monitor lizard.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'M']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:intelligence]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
