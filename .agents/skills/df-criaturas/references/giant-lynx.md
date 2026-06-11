# Giant lynx

> Fonte: [Giant lynx](https://dwarffortresswiki.org/index.php/Giant_lynx) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant lynx for their ear tufts.**
- **Biome**
- **Taiga**
- **Variations**
- **Lynx - Lynx man - Giant lynx**
- **Attributes**
- **Alignment:** Savage
- **War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 37,775 cm 3
- **Mid:** 188,875 cm 3
- **Max:** 377,750 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 13-19
- **Fat:** 12-16
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
- **Bones:** 18-22
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a lynx.*

    [CREATURE:GIANT_LYNX]
        [COPY_TAGS_FROM:LYNX]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1511]
        [GO_TO_START]
        [NAME:giant lynx:giant lynx:giant lynx]
        [CASTE_NAME:giant lynx:giant lynx:giant lynx]
        [GENERAL_CHILD_NAME:giant lynx cub:giant lynx cubs]
        [DESCRIPTION:A huge monster in the shape of a lynx.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'L']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ear tufts]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
