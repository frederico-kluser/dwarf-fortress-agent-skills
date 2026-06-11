# Giant firefly

> Fonte: [Giant firefly](https://dwarffortresswiki.org/index.php/Giant_firefly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant fireflies for their enchanting glow.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Firefly - Firefly man - Giant firefly**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 1-1
- **Butchering returns**
- **Food items**
- **Meat:** 42-51
- **Fat:** 17
- **Brain:** 2
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a firefly.*

**Giant fireflies** are the giant version of fireflies that appear in savage biomes. They get to about the size of a grizzly bear and stay that size their whole lives. They are generally benign but will cancel work orders and occasionally attack your dwarves if provoked. All giant fireflies are born with legendary skill in climbing and as full sized adults.

Giant fireflies can be caught in cage traps and trained into exotic pets with the standard pet value of 500. However, they don't live that long and are difficult to breed, so they aren't a great choice of pet. They do butcher into a decent amount of meat and fat each, however. Since they are exotic mounts they can spawn as mounts during elf sieges.

Some dwarves like giant fireflies for their *enchanting glow*.

Can light an entire town with ease.\
*Art by Marc Denault*\
*Original sketch artist is unknown...*

    [CREATURE:GIANT_FIREFLY]
        [COPY_TAGS_FROM:FIREFLY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant firefly:giant fireflies:giant firefly]
        [CASTE_NAME:giant firefly:giant fireflies:giant firefly]
        [DESCRIPTION:A large monster in the shape of a firefly.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:10]
        [CREATURE_TILE:'F']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:enchanting glow]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
