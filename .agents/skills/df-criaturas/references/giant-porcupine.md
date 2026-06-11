# Giant porcupine

> Fonte: [Giant porcupine](https://dwarffortresswiki.org/index.php/Giant_porcupine) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant porcupines for their quills.**
- **Biome**
- **Temperate Shrubland Temperate Savanna Temperate Grassland Temperate Coniferous Forest Taiga Any Desert Tundra**
- **Variations**
- **Porcupine - Porcupine man - Giant porcupine**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 26,343 cm 3
- **Mid:** 131,715 cm 3
- **Max:** 263,430 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 13
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
- **Bones:** 18
- **Skull:** 1
- **Teeth:** 2-4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a porcupine.*

    [CREATURE:GIANT_PORCUPINE]
        [COPY_TAGS_FROM:PORCUPINE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2927]
        [GO_TO_START]
        [NAME:giant porcupine:giant porcupines:giant porcupine]
        [CASTE_NAME:giant porcupine:giant porcupines:giant porcupine]
        [GENERAL_CHILD_NAME:giant porcupine pup:giant porcupine pups]
        [DESCRIPTION:A large monster in the form of a porcupine.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'P']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:quills]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
