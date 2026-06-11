# Giant crow

> Fonte: [Giant crow](https://dwarffortresswiki.org/index.php/Giant_crow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant crows for their intelligence.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Taiga Any Temperate Forest Any Temperate Wetland**
- **Variations**
- **Crow - Crow man - Giant crow**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 8,140 cm 3
- **Max:** 203,500 cm 3
- **Food products**
- **Eggs:** 4-6
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
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

**Giant crows** are monstrously large cousins of the standard crow who can be found in a wide range of savage biomes. They appear in groups of 5-10, where they are very common (due to having a local population of 30-50), and spend the majority of their time flying around a particular area of the map. Unlike some other aerial pests, giant crows are uninterested in carrying away your hard-won food and items, making them much less likely to migrate towards your fortress intentionally, though their presence may lead to constant job cancellations from dwarves who see them.

Giant crows are generally non-aggressive, though due to their size and numbers they can prove dangerous to civilians and livestock when roused. A moderately-skilled marksdwarf should have little difficulty shooting them out of the sky, and the resultant impact with the ground will leave them incapacitated long enough to finish the job.

Slightly larger than your standard llama, giant crows have a respectable pet value and can provide reasonable butchering returns, though there is little to recommend them over many similar animals. They are perhaps best left to roam free for your hunters to harvest and your military marksdwarves to practice upon.

Some dwarves take a fancy to giant crows for their *intelligence*.

Only eats giant earthworms.

    [CREATURE:GIANT_CROW]
        [COPY_TAGS_FROM:BIRD_CROW]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:40700]
        [GO_TO_START]
        [NAME:giant crow:giant crows:giant crow]
        [CASTE_NAME:giant crow:giant crows:giant crow]
        [GENERAL_CHILD_NAME:giant crow hatchling:giant crow hatchlings]
        [DESCRIPTION:A large bird-like monster, even more deadly when found in groups.]
        [POPULATION_NUMBER:30:50]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'C']
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
