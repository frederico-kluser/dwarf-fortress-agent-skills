# Giant chinchilla

> Fonte: [Giant chinchilla](https://dwarffortresswiki.org/index.php/Giant_chinchilla) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant chinchillas for their fur.**
- **Biome**
- **Mountain**
- **Variations**
- **Chinchilla - Chinchilla man - Giant chinchilla**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,350 cm 3
- **Mid:** 101,750 cm 3
- **Max:** 203,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 12
- **Fat:** 11
- **Brain:** 1
- **Heart:** 0-1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 0-1
- **Kidneys:** 0-2
- **Tripe:** 0-1
- **Sweetbread:** 0-1
- **Spleen:** 0-1
- **Raw materials**
- **Bones:** 17
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a chinchilla.*

**Giant chinchillas** are giant animal variants of the common chinchilla who inhabit savage mountains, spawning in groups of 3-5 individuals, and fleeing if confronted by hostiles such as hunters, despite being about three times the size of the average dwarf.

Giant chinchillas can be captured in cage traps and trained into exotic pets, possessing the default giant animal value, and producing a decent amount of returns when butchered. Like all giant animals, they are considered exotic mounts, though their restriction to mountain regions means you are unlikely to ever see one being used as such.

Some dwarves like giant chinchillas for their *fur*.

"They stop being cute when they reach a certain size."\
*Art by Mari-Liis Kirsimägi*

    [CREATURE:GIANT_CHINCHILLA]
        [COPY_TAGS_FROM:CHINCHILLA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:40700]
        [GO_TO_START]
        [NAME:giant chinchilla:giant chinchillas:giant chinchilla]
        [CASTE_NAME:giant chinchilla:giant chinchillas:giant chinchilla]
        [GENERAL_CHILD_NAME:giant chinchilla kit:giant chinchilla kits]
        [DESCRIPTION:A large monster in the shape of a chinchilla.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:5]
        [CREATURE_TILE:'C']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:fur]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
