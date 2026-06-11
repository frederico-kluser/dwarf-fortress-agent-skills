# Giant walrus

> Fonte: [Giant walrus](https://dwarffortresswiki.org/index.php/Giant_walrus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant walruss for their tusks.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Walrus - Walrus man - Giant walrus**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,203,000 cm 3
- **Mid:** 6,015,000 cm 3
- **Max:** 12,030,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 357
- **Fat:** 74
- **Brain:** 28
- **Heart:** 14
- **Lungs:** 56
- **Intestines:** 84
- **Liver:** 28
- **Kidneys:** 28
- **Tripe:** 28
- **Sweetbread:** 14
- **Eyes:** 2
- **Spleen:** 14
- **Raw materials**
- **Bones:** 95
- **Skull:** 1
- **Ivory:** 6
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant monster in the form of a walrus.*

\
**Giant Walruses** are even larger counterparts to the already large walruses, roughly 8 times as large as them.

Some dwarves like giant walruses for their *tusks* and their *whiskers*.

More tusks for us!\
*Art by StaplesArt*

    >[CREATURE:GIANT_WALRUS]
        [COPY_TAGS_FROM:WALRUS]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:802]
        [GO_TO_START]
        [NAME:giant walrus:giant walruss:giant walrus]
        [CASTE_NAME:giant walrus:giant walruss:giant walrus]
        [GENERAL_CHILD_NAME:giant walrus pup:giant walrus pups]
        [DESCRIPTION:A giant monster in the form of a walrus.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [CREATURE_TILE:'W']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:tusks]
        [PREFSTRING:whiskers]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:691:482:251:1900:2900]
