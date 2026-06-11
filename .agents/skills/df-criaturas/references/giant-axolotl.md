# Giant axolotl

> Fonte: [Giant axolotl](https://dwarffortresswiki.org/index.php/Giant_axolotl) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant axolotls for their gills.**
- **Biome**
- **Tropical Saltwater Lake Tropical Brackish Lake Tropical Freshwater Lake**
- **Variations**
- **Axolotl - Axolotl man - Giant axolotl**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 201,400 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 10-25
- **Butchering returns**
- **Food items**
- **Meat:** 13-14
- **Fat:** 12-13
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
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of an axolotl.*

**Giant axolotls** are giant animal versions of the common axolotl who inhabit savage tropical lakes. While their original counterparts are just vermin, these creatures are over 3 times bigger than a dwarf. They spawn individually and not particularly aggressive, but are not benign and will attack other creatures (including dwarves) who provoke them, potentially killing them.

Giant axolotls can be captured in cage traps and trained into pets, possessing the standard giant creature pet value. They are born adults and cannot be permanently tamed. They produce an adequate amount of products when butchered (comparable to a cow), and as such may serve as a choice for novelty livestock. They are also fairly long-lived compared to most giant vermin, and since they're born as fully-sized adults, they can start producing more of themselves fairly quickly, provided a breeding pair is obtained. They are exotic mounts and may be witnessed being ridden by elves during sieges.

Some dwarves like giant axolotls for their *gills*.

Too cute to be considered a vermin.\
*Art by Matthieu Papy*

    [CREATURE:GIANT_AXOLOTL]
        [COPY_TAGS_FROM:AXOLOTL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:100700]
        [GO_TO_START]
        [NAME:giant axolotl:giant axolotls:giant axolotl]
        [CASTE_NAME:giant axolotl:giant axolotls:giant axolotl]
        [DESCRIPTION:A large monster in the shape of an axolotl.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'A']
        [COLOR:5:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:gills]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
