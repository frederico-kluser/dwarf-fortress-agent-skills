# Giant cougar

> Fonte: [Giant cougar](https://dwarffortresswiki.org/index.php/Giant_cougar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant cougars for their cunning.**
- **Biome**
- **Any Temperate Forest Any Tropical Forest Temperate Shrubland Tropical Shrubland**
- **Variations**
- **Cougar - Cougar man - Giant cougar**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 63,360 cm 3
- **Mid:** 316,800 cm 3
- **Max:** 633,600 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 21-35
- **Fat:** 17-29
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1-2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 22-34
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a cougar.*

**Giant cougars** are much larger versions of their smaller counterparts. They are roughly 10 times the size of a dwarf and standard cougar. Much like their standard-sized, smaller cousins, they also spawn in shrub- and woodlands, are solitary and rarely attack your dwarves. They can appear as exotic mounts in sieges. Despite being giant, the amount of meat they produce when is only slightly higher than their smaller counterparts when butchered.

Some dwarves like giant cougars for their *cunning*.

The would-be best wallpaper for a dwarf's PC.\
*Art by John Sirey-Leicester*

    >[CREATURE:GIANT_COUGAR]
        [COPY_TAGS_FROM:COUGAR]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1056]
        [GO_TO_START]
        [NAME:giant cougar:giant cougars:giant cougar]
        [CASTE_NAME:giant cougar:giant cougars:giant cougar]
        [GENERAL_CHILD_NAME:giant cougar cub:giant cougar cubs]
        [DESCRIPTION:A huge monster in the form of a cougar.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'C']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:cunning]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:585:390:195:1900:2900] 45 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
