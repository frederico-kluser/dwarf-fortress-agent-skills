# Giant gray squirrel

> Fonte: [Giant gray squirrel](https://dwarffortresswiki.org/index.php/Giant_gray_squirrel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant gray squirrels for their tails.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Gray squirrel - Gray squirrel man - Giant gray squirrel**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 202,101 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 15
- **Fat:** 13
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

*A large creature the shape of a gray squirrel.*

    [CREATURE:GIANT_SQUIRREL_GRAY]
        [COPY_TAGS_FROM:SQUIRREL_GRAY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:67367]
        [GO_TO_START]
        [NAME:giant gray squirrel:giant gray squirrels:giant gray squirrel]
        [CASTE_NAME:giant gray squirrel:giant gray squirrels:giant gray squirrel]
        [GENERAL_CHILD_NAME:giant gray squirrel pup:giant gray squirrel pups]
        [DESCRIPTION:A large creature the shape of a gray squirrel.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [CREATURE_TILE:'S']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:tails]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
