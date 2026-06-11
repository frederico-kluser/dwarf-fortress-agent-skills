# Giant deer

> Fonte: [Giant deer](https://dwarffortresswiki.org/index.php/Giant_deer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant deer for their grace.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Deer - Deer man - Giant deer**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 123,760 cm 3
- **Mid:** 618,800 cm 3
- **Max:** 1,237,600 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 25
- **Fat:** 9
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 4
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 22-24
- **Skull:** 1
- **Hooves:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a deer.*

Despite their large size, **giant deer** are usually rather harmless unless cornered or agitated. They are roughly 8 times bigger than standard deer, thus they need a large pasture to survive. They can be tamed, having a decent pet value of 500 like most giant animals, but not trained, so they won't be much use for fortress defense.

Most likely bigger in the game.

    >[CREATURE:GIANT_DEER]
        [COPY_TAGS_FROM:DEER]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:884]
        [GO_TO_START]
        [NAME:giant deer:giant deer:giant deer]
        [CASTE_NAME:giant deer:giant deer:giant deer]
        [GENERAL_CHILD_NAME:giant deer fawn:giant deer fawns]
        [DESCRIPTION:A huge monster in the form of a deer.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [CREATURE_TILE:'D']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:grace]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:411:274:137:1900:2900] 64 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
