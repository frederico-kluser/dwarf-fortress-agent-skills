# Giant impala

> Fonte: [Giant impala](https://dwarffortresswiki.org/index.php/Giant_impala) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant impalas for their mighty leaps.**
- **Biome**
- **Tropical Savanna Tropical Grassland**
- **Variations**
- **Impala - Impala man - Giant impala**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 56,000 cm 3
- **Mid:** 280,000 cm 3
- **Max:** 560,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 11-21
- **Fat:** 8
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1-2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 14
- **Skull:** 1
- **Hooves:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of an impala.*

**Giant impalas** are slightly larger than an average horse, and roughly as threatening. They normally appear in savage tropical grasslands and savanna, though elven caravans and sieges may bring them to fortresses located in other biomes.

Tame giant impalas have a moderately-high pet value (the same as most other giant creatures), and require grass to graze. Some dwarves like giant impalas for their "mighty leaps".

    [CREATURE:GIANT_IMPALA]
        [COPY_TAGS_FROM:IMPALA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1120]
        [GO_TO_START]
        [NAME:giant impala:giant impalas:giant impala]
        [CASTE_NAME:giant impala:giant impalas:giant impala]
        [GENERAL_CHILD_NAME:giant impala fawn:giant impala fawns]
        [DESCRIPTION:A huge monster in the form of an impala.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'I']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:mighty leaps]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:438:292:146:1900:2900] 60 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
