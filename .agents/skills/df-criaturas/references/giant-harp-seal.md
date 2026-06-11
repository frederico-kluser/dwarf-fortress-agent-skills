# Giant harp seal

> Fonte: [Giant harp seal](https://dwarffortresswiki.org/index.php/Giant_harp_seal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant harp seals for their adorable pups.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Harp seal - Harp seal man - Giant harp seal**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 14,289 cm 3
- **Mid:** 714,450 cm 3
- **Max:** 1,428,900 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 73
- **Fat:** 7
- **Brain:** 3
- **Heart:** 1
- **Lungs:** 6
- **Intestines:** 11
- **Liver:** 3
- **Kidneys:** 2
- **Tripe:** 3
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 13
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a harp seal.*

No size can reduce its cuteness.

    [CREATURE:GIANT_HARP_SEAL]
        [COPY_TAGS_FROM:HARP_SEAL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:866]
        [GO_TO_START]
        [NAME:giant harp seal:giant harp seals:giant harp seal]
        [CASTE_NAME:giant harp seal:giant harp seals:giant harp seal]
        [GENERAL_CHILD_NAME:giant harp seal pup:giant harp seal pups]
        [DESCRIPTION:A huge monster in the shape of a harp seal.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [CREATURE_TILE:'H']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:adorable pups]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:703:505:274:1900:2900]
