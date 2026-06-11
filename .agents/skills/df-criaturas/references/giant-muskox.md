# Giant muskox

> Fonte: [Giant muskox](https://dwarffortresswiki.org/index.php/Giant_muskox) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant muskoxen for their strength.**
- **Biome**
- **Tundra Temperate Grassland**
- **Variations**
- **Muskox - Muskox man - Giant muskox**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 248,700 cm 3
- **Mid:** 994,800 cm 3
- **Max:** 2,362,650 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 40-59
- **Fat:** 9-15
- **Brain:** 2-3
- **Heart:** 1
- **Lungs:** 4-6
- **Intestines:** 6-9
- **Liver:** 2-3
- **Kidneys:** 2
- **Tripe:** 2-3
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 28-36
- **Skull:** 1
- **Teeth:** 1
- **Hooves:** 4
- **Horns:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a muskox.*

\

    >[CREATURE:GIANT_MUSKOX]
        [COPY_TAGS_FROM:MUSKOX]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:829]
        [GO_TO_START]
        [NAME:giant muskox:giant muskoxen:giant muskox]
        [CASTE_NAME:giant muskox:giant muskoxen:giant muskox]
        [GENERAL_CHILD_NAME:giant muskox calf:giant muskox calves]
        [DESCRIPTION:A huge monster in the form of a muskox.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [CREATURE_TILE:'M']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:strength]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:438:292:146:1900:2900] 60 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
