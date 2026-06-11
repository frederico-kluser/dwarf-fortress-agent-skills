# Giant raven

> Fonte: [Giant raven](https://dwarffortresswiki.org/index.php/Giant_raven) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant ravens for their intelligence.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Taiga Any Temperate Forest Any Temperate Wetland Tundra Any Desert**
- **Variations**
- **Raven - Raven man - Giant raven**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 8,683.5 cm 3
- **Max:** 208,404 cm 3
- **Food products**
- **Eggs:** 3-7
- **Age**
- **Adult at:** 1
- **Max age:** 20-40
- **Butchering returns**
- **Food items**
- **Meat:** 17
- **Fat:** 11
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 24
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large bird-like monster, even more deadly when found in groups.*

The **giant raven** is the giant variety of the raven. It is much bigger than a regular raven, nearly 174× as big, in fact.

It may be a good idea to capture one of these creatures, as they can be butchered, or kept alive for egg production.

Some dwarves like giant ravens for their *intelligence*.

Only protects one sleeping human at a time.\
*Art by Valonia-Feline*

    [CREATURE:GIANT_RAVEN]
        [COPY_TAGS_FROM:BIRD_RAVEN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:17367]
        [GO_TO_START]
        [NAME:giant raven:giant ravens:giant raven]
        [CASTE_NAME:giant raven:giant ravens:giant raven]
        [GENERAL_CHILD_NAME:giant raven hatchling:giant raven hatchlings]
        [DESCRIPTION:A large bird-like monster, even more deadly when found in groups.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:3:5]
        [CREATURE_TILE:'R']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:intelligence]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
