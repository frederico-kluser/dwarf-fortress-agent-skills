# Giant anaconda

> Fonte: [Giant anaconda](https://dwarffortresswiki.org/index.php/Giant_anaconda) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant anacondas for their great size.**
- **Biome**
- **Any Tropical Wetland**
- **Variations**
- **Anaconda - Anaconda man - Giant anaconda**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 933 cm 3
- **Mid:** 466,500 cm 3
- **Max:** 933,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 6-11
- **Fat:** 3
- **Brain:** 1
- **Intestines:** 1-2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 3
- **Spleen:** 1
- **Raw materials**
- **Bones:** 10
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of an anaconda.*

**Giant anacondas** are the giant animal variant of the common anaconda, who can be found in savage tropical wetlands. Regular anacondas are a particularly large species of snake, but their giant counterparts take this to an extreme: at 933,000 cm3 they are one of the largest above-ground creatures in the game, almost as large as water buffalos and giraffes, and 15.55 times the size of a lowly dwarf: when it comes to snakes, only the even-more-extremely oversized giant python is larger. While not venomous, their bite is strong enough to reliably tear entire limbs off your dwarves, armor and all. Their `[LARGE_PREDATOR]` creature token makes them aggressive towards any dwarves foolish enough to come close. They should only be approached by multiple seasoned military dwarves in full regalia, or better yet, avoided entirely.

Giant anacondas can be captured in cage traps and trained into pets, possessing the default giant animal value. They are born adults and as such cannot be permanently tamed. Giant anacondas require 20 years of growth to reach full size, but only live 10-20 years, meaning they rarely reach their most imposing size. Like all giant animals, they are considered exotic mounts.

Some dwarves admire giant anacondas for their *great size*.

Once swallowed a dwarf, elf and a goblin in one gulp. Without killing them. Right away.

    [CREATURE:GIANT_ANACONDA]
        [COPY_TAGS_FROM:ANACONDA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:933]
        [GO_TO_START]
        [NAME:giant anaconda:giant anacondas:giant anaconda]
        [CASTE_NAME:giant anaconda:giant anacondas:giant anaconda]
        [DESCRIPTION:A huge monster in the form of an anaconda.]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'A']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:great size]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
