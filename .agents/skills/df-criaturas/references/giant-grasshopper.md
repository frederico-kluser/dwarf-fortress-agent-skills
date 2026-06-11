# Giant grasshopper

> Fonte: [Giant grasshopper](https://dwarffortresswiki.org/index.php/Giant_grasshopper) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant grasshoppers for their chirping.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Grasshopper - Grasshopper man - Giant grasshopper**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
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
- **Meat:** 21-42
- **Fat:** 15-17
- **Brain:** 2
- **Heart:** 0-1
- **Intestines:** 8
- **Eyes:** 0-2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge creature in the shape of a grasshopper.*

**Giant grasshoppers** are giant versions of the insect grasshopper. Compared to most other "giant" creatures, they are unimpressive. Usually benign, if forced into combat they have no attacks apart from pushing and wrestling, and unlike their real-world counterparts, they cannot fly or jump. Even with their size maxing out at 200,007 cm3, this makes them little threat; consider using them as combat dummies for your military.

Giant grasshoppers cannot be tamed in fortress mode, as they are born as adults. Tame versions may be obtained from elven caravans or in raids on elven sites, but they cannot be trained for war or hunting. Like most giant insects, they only have a maximum age of one year, making these rare tame specimens very poor choices as pets anyway. If you happen to acquire one, you may as well just butcher it.

Some dwarves like giant grasshoppers for their *chirping* and *great leaps*.

The human should have brought bug spray.

    [CREATURE:GIANT_GRASSHOPPER]
        [COPY_TAGS_FROM:GRASSHOPPER]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant grasshopper:giant grasshoppers:giant grasshopper]
        [CASTE_NAME:giant grasshopper:giant grasshoppers:giant grasshopper]
        [DESCRIPTION:A huge creature in the shape of a grasshopper.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'G']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:chirping]
        [PREFSTRING:great leaps]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
