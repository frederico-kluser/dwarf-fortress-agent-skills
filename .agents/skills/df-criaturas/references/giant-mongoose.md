# Giant mongoose

> Fonte: [Giant mongoose](https://dwarffortresswiki.org/index.php/Giant_mongoose) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant mongooses for their cunning.**
- **Biome**
- **Tropical Savanna Tropical Shrubland**
- **Variations**
- **Mongoose - Mongoose man - Giant mongoose**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 22,104 cm 3
- **Mid:** 110,520 cm 3
- **Max:** 221,040 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 13
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
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large mongoose-like monster known for hunting people amongst other things.*

    [CREATURE:GIANT_MONGOOSE]
        [COPY_TAGS_FROM:MONGOOSE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:7368]
        [GO_TO_START]
        [NAME:giant mongoose:giant mongooses:giant mongoose]
        [CASTE_NAME:giant mongoose:giant mongooses:giant mongoose]
        [GENERAL_CHILD_NAME:giant mongoose pup:giant mongoose pups]
        [DESCRIPTION:A large mongoose-like monster known for hunting people amongst other things.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'M']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:agility]
        [PREFSTRING:cunning]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:453:302:151:1900:2900] 58 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
