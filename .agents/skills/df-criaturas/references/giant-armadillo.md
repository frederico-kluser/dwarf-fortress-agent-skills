# Giant armadillo

> Fonte: [Giant armadillo](https://dwarffortresswiki.org/index.php/Giant_armadillo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant armadillos for their thick, bony armor plates.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Armadillo - Armadillo man - Giant armadillo**
- **Attributes**
- **Alignment:** Savage
- **Shell**
- **Tamed Attributes**
- **Pet value:** 1,000
- **Not hunting/war trainable**
- **Size**
- **Birth:** 25,275 cm 3
- **Mid:** 126,375 cm 3
- **Max:** 252,750 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 14
- **Fat:** 12
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
- **Shell:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster the shape of an armadillo. It has thick armor for skin.*

**Giant armadillos** are the giant animal variant of the common armadillo, found in savage tropical biomes. While the common critter is roughly cat-sized, these giants are over four times the size of a dwarf, though they are generally timid and will not fight back if attacked, preferring to curl up into a ball instead.

Giant armadillos can be captured in cage traps and trained into exotic pets, possessing the default giant animal value. They provide a good amount of food and bones when butchered, on top of serving as a source of shells. Also like other giant animals, they are considered exotic mounts.

Some dwarves like giant armadillos for their *thick, bony armor plates*.

## Arena tests

|       |         |                  |                       |
|-------|---------|------------------|-----------------------|
| Trial | Dwarves | Giant armadillos | Winner                |
| 1     | 9       | 9                | giant armadillos (9)  |
| 2     | 15      | 10               | giant armadillos (10) |

    [CREATURE:ARMADILLO, GIANT]
        [COPY_TAGS_FROM:ARMADILLO]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:3370]
        [GO_TO_START]
        [NAME:giant armadillo:giant armadillos:giant armadillo]
        [GENERAL_CHILD_NAME:giant armadillo pup:giant armadillo pups]
        [DESCRIPTION:A large monster the shape of an armadillo.  It has thick armor for skin.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'A']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:1000]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:giant armadillo boar:giant armadillo boars:giant armadillo boar]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:giant armadillo sow:giant armadillo sows:giant armadillo sow]
        [SELECT_CASTE:ALL]
        [PREFSTRING:thick, bony armor plates]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
