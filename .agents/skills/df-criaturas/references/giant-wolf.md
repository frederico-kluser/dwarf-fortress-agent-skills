# Giant wolf

> Fonte: [Giant wolf](https://dwarffortresswiki.org/index.php/Giant_wolf) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant wolves for their cunning.**
- **Biome**
- **Tundra Taiga Any Temperate Forest Temperate Shrubland**
- **Variations**
- **Wolf - Wolf man - Giant wolf**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 48,680 cm 3
- **Mid:** 243,400 cm 3
- **Max:** 486,800 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 21
- **Fat:** 17
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 22
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a wolf.*

**Giant wolves** are just what the name implies; bigger, meaner versions of the normal wolf, much larger than a polar bear. They can only appear in the savage biome types of tundra, taiga, temperate forest, or temperate shrubland.

Some dwarves like giant wolves for their *cunning*.

## Adventure mode

These animals aren't nearly as common as giant dingoes, but they almost always come in packs. Be careful with these animals, for a number of them can easily dispatch a poorly equipped adventurer. If a stray tame one is encountered, either at a player fortress or rarely at elven sites, they can be ridden.

## Fortress mode

In fortress mode, these animals can be tamed as a bigger dog replacement, though they cannot be trained for war or hunting. Be careful to not let unarmed civilians too close to wild ones, else they will likely be killed.

    >[CREATURE:GIANT_WOLF]
        [COPY_TAGS_FROM:WOLF]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1217]
        [GO_TO_START]
        [NAME:giant wolf:giant wolves:giant wolf]
        [CASTE_NAME:giant wolf:giant wolves:giant wolf]
        [GENERAL_CHILD_NAME:giant wolf pup:giant wolf pups]
        [DESCRIPTION:A huge monster in the shape of a wolf.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'W']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:cunning]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:447:298:149:1900:2900] 59 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
