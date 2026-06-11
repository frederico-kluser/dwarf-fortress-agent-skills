# Giant chipmunk

> Fonte: [Giant chipmunk](https://dwarffortresswiki.org/index.php/Giant_chipmunk) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant chipmunks for their stripes.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Chipmunk - Chipmunk man - Giant chipmunk**
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

*A large creature the shape of a chipmunk.*

**Giant chipmunks** are giant animal variants of the common chipmunk, found in most savage temperate forests. While these hulking and fluffy critters may look cute, they are also roughly the size of a grizzly bear and are not benign, meaning they make pose a threat to passing dwarves or livestock. It is best to approach them with an armored military.

Giant chipmunks can be captured in cage traps and trained into exotic pets, possessing the default giant animal value. They give a decent amount of returns when butchered. Like all giant animals, they are considered exotic mounts.

Some dwarves like giant chipmunks for their *stripes*.

    [CREATURE:GIANT_CHIPMUNK]
        [COPY_TAGS_FROM:CHIPMUNK]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:67367]
        [GO_TO_START]
        [NAME:giant chipmunk:giant chipmunks:giant chipmunk]
        [CASTE_NAME:giant chipmunk:giant chipmunks:giant chipmunk]
        [GENERAL_CHILD_NAME:giant chipmunk pup:giant chipmunk pups]
        [DESCRIPTION:A large creature the shape of a chipmunk.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [CREATURE_TILE:'C']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:stripes]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
