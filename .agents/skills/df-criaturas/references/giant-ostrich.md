# Giant ostrich

> Fonte: [Giant ostrich](https://dwarffortresswiki.org/index.php/Giant_ostrich) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant ostriches for their long necks.**
- **Biome**
- **Tropical Savanna Tropical Grassland Any Desert**
- **Variations**
- **Ostrich - Ostrich man - Giant ostrich**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 1,000
- **Not hunting/war trainable**
- **Size**
- **Birth:** 17,154 cm 3
- **Mid:** 428,850 cm 3
- **Max:** 857,700 cm 3
- **Food products**
- **Eggs:** 10-15
- **Age**
- **Adult at:** 1
- **Max age:** 35-45
- **Butchering returns**
- **Food items**
- **Meat:** 30-34
- **Fat:** 17
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 3-4
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 29
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge bird monster with extremely long legs and neck.*

**Giant ostriches** are giant animal variants of the ostrich, found in savage deserts, tropical savannas and tropical grasslands. Like the regular ostrich, these animals appear in small groups of up to ten individuals. Being benign creatures they will meander and generally keep to themselves. Giant ostriches are roughly the size of a water buffalo, or 14 times larger than a dwarf, and as such they are a force to be reckoned with against a poorly equipped militia if provoked. Males are called *giant ostrich cocks* and females are called *giant ostrich hens*.

Giant ostriches can be captured in cage traps and trained into exotic pets, possessing the unusually high value of 1000. Their large size translates into a good amount of products if they are butchered, and they lay a fairly high amount of eggs if placed in a nest box. Like all giant animals, they are considered exotic mounts.

Some dwarves like giant ostriches for their *long necks* and their *giant eggs*.

    [CREATURE:BIRD_OSTRICH_GIANT]
        [COPY_TAGS_FROM:BIRD_OSTRICH]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:953]
        [GO_TO_START]
        [NAME:giant ostrich:giant ostriches:giant ostrich]
        [GENERAL_CHILD_NAME:giant ostrich chick:giant ostrich chicks]
        [DESCRIPTION:A huge bird monster with extremely long legs and neck.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:10] should be seasonal
        [CREATURE_TILE:'O']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:1000]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:giant ostrich cock:giant ostrich cocks:giant ostrich cock]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:giant ostrich hen:giant ostrich hens:giant ostrich hen]
        [SELECT_CASTE:ALL]
        [PREFSTRING:long necks]
        [PREFSTRING:giant eggs]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
