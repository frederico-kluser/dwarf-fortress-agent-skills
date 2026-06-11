# Giant cardinal

> Fonte: [Giant cardinal](https://dwarffortresswiki.org/index.php/Giant_cardinal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant cardinals for their coloration.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Temperate Broadleaf Forest Temperate Coniferous Forest**
- **Variations**
- **Cardinal - Cardinal man - Giant cardinal**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 32,056 cm 3
- **Max:** 200,350 cm 3
- **Food products**
- **Eggs:** 2-5
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 19-21
- **Fat:** 12-14
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 24-26
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a cardinal.*

**Giant cardinals** are giant animal variants of the common cardinal, found in a number of savage temperate biomes. They spawn in flocks of anywhere between 5 and 10 individuals. Being three times the size of the average dwarf, these birds may pose a threat if provoked, but will generally leave a fortress alone save for potential job cancellations or scaring livestock out of pastures.

Giant cardinals can be captured in cage traps and trained into exotic pets, possessing the default giant animal value. They give a decent amount of returns when butchered, and can be placed in a nest box for a meager amount of eggs, though they fail to produce as much as your common poultry. Like all giant animals, they are considered exotic mounts.

Some dwarves like giant cardinals for their *coloration*.

Also admired for their ability to *bend trees by perching on them for too long*.

    [CREATURE:GIANT_CARDINAL]
        [COPY_TAGS_FROM:BIRD_CARDINAL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:400700]
        [GO_TO_START]
        [NAME:giant cardinal:giant cardinals:giant cardinal]
        [CASTE_NAME:giant cardinal:giant cardinals:giant cardinal]
        [GENERAL_CHILD_NAME:giant cardinal hatchling:giant cardinal hatchlings]
        [DESCRIPTION:A huge monster in the form of a cardinal.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'C']
        [COLOR:4:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
