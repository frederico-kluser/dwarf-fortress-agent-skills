# Giant oriole

> Fonte: [Giant oriole](https://dwarffortresswiki.org/index.php/Giant_oriole) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant orioles for their coloration.**
- **Biome**
- **Temperate Broadleaf Forest**
- **Variations**
- **Oriole - Oriole man - Giant oriole**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 35,049 cm 3
- **Max:** 200,280 cm 3
- **Food products**
- **Eggs:** 3-7
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 19-21
- **Fat:** 12-14
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
- **Bones:** 24-26
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of an oriole.*

    [CREATURE:GIANT_ORIOLE]
        [COPY_TAGS_FROM:BIRD_ORIOLE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:500700]
        [GO_TO_START]
        [NAME:giant oriole:giant orioles:giant oriole]
        [CASTE_NAME:giant oriole:giant orioles:giant oriole]
        [GENERAL_CHILD_NAME:giant oriole hatchling:giant oriole hatchlings]
        [DESCRIPTION:A huge monster in the form of an oriole.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'O']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
