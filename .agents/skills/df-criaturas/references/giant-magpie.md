# Giant magpie

> Fonte: [Giant magpie](https://dwarffortresswiki.org/index.php/Giant_magpie) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant magpies for their fondness of shiny objects.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland**
- **Variations**
- **Magpie - Magpie man - Giant magpie**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 10,070 cm 3
- **Max:** 201,400 cm 3
- **Food products**
- **Eggs:** 2-5
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
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

*A huge monster in the shape of a magpie.*

It is a very big bird. It is relatively harmless and runs away if approached.

    [CREATURE:GIANT_MAGPIE]
        [COPY_TAGS_FROM:BIRD_MAGPIE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:100700]
        [GO_TO_START]
        [NAME:giant magpie:giant magpies:giant magpie]
        [CASTE_NAME:giant magpie:giant magpies:giant magpie]
        [GENERAL_CHILD_NAME:giant magpie hatchling:giant magpie hatchlings]
        [DESCRIPTION:A huge monster in the shape of a magpie.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:10]
        [CREATURE_TILE:'M']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:intelligence]
        [PREFSTRING:fondness of shiny objects]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
