# Giant mink

> Fonte: [Giant mink](https://dwarffortresswiki.org/index.php/Giant_mink) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant minks for their long bodies.**
- **Biome**
- **Any Temperate Lake Any Temperate River**
- **Variations**
- **Mink - Mink man - Giant mink**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,560 cm 3
- **Mid:** 102,800 cm 3
- **Max:** 205,600 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 13
- **Fat:** 12
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2
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

*A huge monster in the form of a mink.*

**Giant minks** are *much* larger than minks - 257 times larger, in fact, according to the raws, making them slightly larger than a llama when full-grown. Due to this, they are, unlike normal minks, butcherable, and yield fairly decent amount of products. They also reach their maximum size at the age of two years old, just like most domestic livestock mammals. However, unlike those animals, they always give birth to only one kit. Those characteristics make them a decent meat industry animal if a breeding pair is obtained, but inferior to most other giant animal variants. Giant minks are benign, and therefore pose no threat to dwarves and are mostly useless for fortress defense.

    [CREATURE:GIANT_MINK]
        [COPY_TAGS_FROM:MINK]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:25700]
        [GO_TO_START]
        [NAME:giant mink:giant minks:giant mink]
        [CASTE_NAME:giant mink:giant minks:giant mink]
        [GENERAL_CHILD_NAME:giant mink kit:giant mink kits]
        [DESCRIPTION:A huge monster in the form of a mink.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'M']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:long bodies]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
