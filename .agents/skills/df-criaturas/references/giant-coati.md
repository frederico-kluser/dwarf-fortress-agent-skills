# Giant coati

> Fonte: [Giant coati](https://dwarffortresswiki.org/index.php/Giant_coati) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant coatis for their curiosity.**
- **Biome**
- **Any Temperate Forest Any Tropical Forest**
- **Variations**
- **Coati - Coati man - Giant coati**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 24,216 cm 3
- **Mid:** 121,080 cm 3
- **Max:** 242,160 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 11
- **Fat:** 11
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 17
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a coati.*

**Giant coatis** are giant animal counterparts to coatis, who can be found in savage tropical and temperate forests. Like their smaller cousins, they may steal items and foo from the fortress if given an opportunity and will take any item they can get their paws on, and being four times the size of a dwarf means they are more than capable of defending themselves in a fight against unarmed civilians. They are best hunted or baited and killed before they get away with something useful.

Giant coatis can be captured in cage traps and trained into exotic pets, possessing the default giant animal value. They give a decent amount of returns when butchered but are difficult to breed due to their solitary nature. Like all giant animals, they are considered exotic mounts.

Some dwarves like giant coatis for their *curiosity*.

Admired for their *curiosity*.

    [CREATURE:GIANT_COATI]
        [COPY_TAGS_FROM:COATI]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:4036]
        [GO_TO_START]
        [NAME:giant coati:giant coatis:giant coati]
        [CASTE_NAME:giant coati:giant coatis:giant coati]
        [GENERAL_CHILD_NAME:baby giant coati:baby giant coatis]
        [DESCRIPTION:A huge monster in the form of a coati.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'C']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:curiosity]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:722:545:325:1900:2900] 27 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
