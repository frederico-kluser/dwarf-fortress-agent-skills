# Giant kingsnake

> Fonte: [Giant kingsnake](https://dwarffortresswiki.org/index.php/Giant_kingsnake) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant kingsnakes for their habit of eating other snakes.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Mountain Any Desert**
- **Variations**
- **Kingsnake - Kingsnake man - Giant kingsnake**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 2,806.8 cm 3
- **Mid:** 105,255 cm 3
- **Max:** 210,510 cm 3
- **Food products**
- **Eggs:** 5-12
- **Age**
- **Adult at:** Birth
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 3
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
- **Bones:** 10
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a kingsnake.*

    [CREATURE:GIANT_KINGSNAKE]
        [COPY_TAGS_FROM:KINGSNAKE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:14034]
        [GO_TO_START]
        [NAME:giant kingsnake:giant kingsnakes:giant kingsnake]
        [CASTE_NAME:giant kingsnake:giant kingsnakes:giant kingsnake]
        [DESCRIPTION:A large monster in the form of a kingsnake.]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'K']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:habit of eating other snakes]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
