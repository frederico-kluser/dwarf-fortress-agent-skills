# Giant aardvark

> Fonte: [Giant aardvark](https://dwarffortresswiki.org/index.php/Giant_aardvark) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant aardvarks for their snout.**
- **Biome**
- **Tropical Shrubland Tropical Savanna Tropical Grassland**
- **Variations**
- **Aardvark - Aardvark man - Giant aardvark**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 5,600 cm 3
- **Mid:** 280,000 cm 3
- **Max:** 560,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 19
- **Fat:** 16
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
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of an aardvark.*

**Giant aardvarks** are the giant cousins of the common aardvark, found in savage tropical plains. Like their regular-sized brethren, they spawn individually and meander through the map, generally minding their own business. Despite being over 9 times the size of a dwarf, giant aardvarks are just as benign as their smaller cousins and will flee if confronted, making them unlikely to pose a threat unless cornered by your hunters.

Giant aardvarks can be captured with cage traps and trained into pets, possessing the standard value of a giant creature. A breeding pair can be used for a fortress's meat industry somewhat more efficiently than normal aardvarks, as their larger size makes them drop a larger quantity of meat, fat and bones. Giant aardvarks are exotic mounts, so you may see elves riding them into battle in the event of a siege.

Some dwarves like giant aardvarks for their *snout* and their *long ears*.

\

    [CREATURE:GIANT_AARDVARK]
        [COPY_TAGS_FROM:AARDVARK]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1120]
        [GO_TO_START]
        [NAME:giant aardvark:giant aardvarks:giant aardvark]
        [CASTE_NAME:giant aardvark:giant aardvarks:giant aardvark]
        [GENERAL_CHILD_NAME:giant aardvark cub:giant aardvark cubs]
        [DESCRIPTION:A huge monster in the form of an aardvark.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'A']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:long ears]
        [PREFSTRING:snout]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
