# Giant red-winged blackbird

> Fonte: [Giant red-winged blackbird](https://dwarffortresswiki.org/index.php/Giant_red-winged_blackbird) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant red-winged blackbirds for their coloration.**
- **Biome**
- **Temperate Freshwater Marsh Temperate Saltwater Marsh**
- **Variations**
- **Red-winged blackbird - Red-winged blackbird man - Giant red-winged blackbird**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 40,070 cm 3
- **Max:** 200,350 cm 3
- **Food products**
- **Eggs:** 2-4
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

*A huge monster in the form of a red-winged blackbird.*

The **giant red-winged blackbird** is a giant variant of the regular red-winged blackbird. They can be found in savage marshes.

Some dwarves like red-winged blackbirds for their *coloration*.

    [CREATURE:GIANT_RW_BLACKBIRD]
        [COPY_TAGS_FROM:BIRD_RW_BLACKBIRD]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:400700]
        [GO_TO_START]
        [NAME:giant red-winged blackbird:giant red-winged blackbirds:giant red-winged blackbird]
        [CASTE_NAME:giant red-winged blackbird:giant red-winged blackbirds:giant red-winged blackbird]
        [GENERAL_CHILD_NAME:giant red-winged blackbird hatchling:giant red-winged blackbird hatchlings]
        [DESCRIPTION:A huge monster in the form of a red-winged blackbird.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'R']
        [COLOR:0:0:1]
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
