# Giant desert tortoise

> Fonte: [Giant desert tortoise](https://dwarffortresswiki.org/index.php/Giant_desert_tortoise) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant desert tortoises for their shells.**
- **Biome**
- **Any Desert**
- **Variations**
- **Desert tortoise - Desert tortoise man - Giant desert tortoise**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Shell · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,735.6 cm 3
- **Mid:** 119,322.5 cm 3
- **Max:** 238,645 cm 3
- **Food products**
- **Eggs:** 3-5
- **Age**
- **Adult at:** 1
- **Max age:** 80-100
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
- **Bones:** 19
- **Skull:** 1
- **Shell:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a desert tortoise.*

**Giant desert tortoises** are enlarged cousins of the common desert tortoise, found in savage desert biomes. They are far larger than a dwarf, about as heavy as a tiger, but rarely pose any threat to a fortress; like normal tortoises, they are benign and will flee from attackers. They are one of the few sources of shells in deserts, and the only one when there's no water available.

Giant desert tortoises can be captured in cage traps and trained into pets, possessing the standard value of giant creatures. They produce far more returns when butchered than their normal counterparts, but aren't any better at egg-laying. Like normal tortoises, they are very long-lived and serve as good long-term pets for dwarves who adopt them.

Some dwarves like giant desert tortoises for their *shells* and their *longevity*.

"I got sand in my shell."

    [CREATURE:GIANT_DESERT_TORTOISE]
        [COPY_TAGS_FROM:DESERT TORTOISE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:4339]
        [GO_TO_START]
        [NAME:giant desert tortoise:giant desert tortoises:giant desert tortoise]
        [CASTE_NAME:giant desert tortoise:giant desert tortoises:giant desert tortoise]
        [GENERAL_CHILD_NAME:giant desert tortoise hatchling:giant desert tortoise hatchlings]
        [DESCRIPTION:A large monster in the form of a desert tortoise.]
        [POPULATION_NUMBER:10:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'T']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:shells]
        [PREFSTRING:longevity]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
