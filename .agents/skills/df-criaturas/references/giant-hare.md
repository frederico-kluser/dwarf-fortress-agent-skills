# Giant hare

> Fonte: [Giant hare](https://dwarffortresswiki.org/index.php/Giant_hare) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant hares for their fluffy tails.**
- **Biome**
- **Temperate Savanna Temperate Grassland**
- **Variations**
- **Hare - Hare man - Giant hare**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 22,456 cm 3
- **Mid:** 112,280 cm 3
- **Max:** 224,560 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 8-12
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
- **Teeth:** 0-2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a hare.*

Every hop causes an earthquake.

    [CREATURE:GIANT_HARE]
        [COPY_TAGS_FROM:HARE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:6416]
        [GO_TO_START]
        [NAME:giant hare:giant hares:giant hare]
        [CASTE_NAME:giant hare:giant hares:giant hare]
        [GENERAL_CHILD_NAME:giant leveret:giant leverets]
        [DESCRIPTION:A large monster in the shape of a hare.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'H']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:long ears]
        [PREFSTRING:fluffy tails]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:438:292:146:1900:2900] 60 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
