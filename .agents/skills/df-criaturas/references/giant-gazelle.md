# Giant gazelle

> Fonte: [Giant gazelle](https://dwarffortresswiki.org/index.php/Giant_gazelle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant gazelles for their grace.**
- **Biome**
- **Tropical Savanna Tropical Grassland**
- **Variations**
- **Gazelle - Gazelle man - Giant gazelle**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 34,180 cm 3
- **Mid:** 170,900 cm 3
- **Max:** 341,800 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 11-13
- **Fat:** 9
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
- **Bones:** 14
- **Skull:** 1
- **Hooves:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a gazelle.*

\

    [CREATURE:GIANT_GAZELLE]
        [COPY_TAGS_FROM:GAZELLE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1709]
        [GO_TO_START]
        [NAME:giant gazelle:giant gazelles:giant gazelle]
        [CASTE_NAME:giant gazelle:giant gazelles:giant gazelle]
        [GENERAL_CHILD_NAME:giant gazelle fawn:giant gazelle fawns]
        [DESCRIPTION:A huge monster in the form of a gazelle.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'G']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:grace]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:327:218:109:1900:2900] 80 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
