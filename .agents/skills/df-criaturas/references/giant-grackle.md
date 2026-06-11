# Giant grackle

> Fonte: [Giant grackle](https://dwarffortresswiki.org/index.php/Giant_grackle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant grackles for their raucous calls.**
- **Biome**
- **Temperate Grassland Temperate Savanna**
- **Variations**
- **Grackle - Grackle man - Giant grackle**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 18,410.37 cm 3
- **Max:** 200,840.4 cm 3
- **Food products**
- **Eggs:** 1-7
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

*A huge monster in the form of a grackle.*

In its point of view, dwarves and elves are berries and worms.\
*Art by Carly Weaver*

    [CREATURE:GIANT_GRACKLE]
        [COPY_TAGS_FROM:BIRD_GRACKLE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:167367]
        [GO_TO_START]
        [NAME:giant grackle:giant grackles:giant grackle]
        [CASTE_NAME:giant grackle:giant grackles:giant grackle]
        [GENERAL_CHILD_NAME:giant grackle hatchling:giant grackle hatchlings]
        [DESCRIPTION:A huge monster in the form of a grackle.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'G']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:raucous calls]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
