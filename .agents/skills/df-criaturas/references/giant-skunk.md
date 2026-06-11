# Giant skunk

> Fonte: [Giant skunk](https://dwarffortresswiki.org/index.php/Giant_skunk) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant skunks for their distinctive striping.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Skunk - Skunk man - Giant skunk**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 22,804 cm 3
- **Mid:** 114,020 cm 3
- **Max:** 228,040 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
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
- **Teeth:** 0-2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a skunk.*

The **giant skunk** is one of the lesser giant creatures. They're not rare and a totally untrained dwarf can usually kill one with a crossbow and some wooden bolts.

    [CREATURE:GIANT_SKUNK]
        [COPY_TAGS_FROM:SKUNK]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:5701]
        [GO_TO_START]
        [NAME:giant skunk:giant skunks:giant skunk]
        [CASTE_NAME:giant skunk:giant skunks:giant skunk]
        [GENERAL_CHILD_NAME:giant skunk kit:giant skunk kits]
        [DESCRIPTION:A large monster in the form of a skunk.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:distinctive striping]
        [PREFSTRING:foul smell]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
