# Giant ibex

> Fonte: [Giant ibex](https://dwarffortresswiki.org/index.php/Giant_ibex) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant ibexes for their long horns.**
- **Biome**
- **Any Grassland Any Desert**
- **Variations**
- **Ibex - Ibex man - Giant ibex**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 56,000 cm 3
- **Mid:** 112,000 cm 3
- **Max:** 560,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 11-13
- **Fat:** 8
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
- **Bones:** 16
- **Skull:** 1
- **Hooves:** 4
- **Horns:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of an ibex.*

**Giant ibexes** are not a direct threat to your fortress, as they won't actively seek out targets and are generally skittish. However, these animals can be quite dangerous to any dwarves foolish enough to agitate or otherwise antagonize them. They have hooves, horns, and enough mass to cause considerable damage. They can even pose a threat to your militia with heavy blunt and stabbing damage.

    [CREATURE:GIANT_IBEX]
        [COPY_TAGS_FROM:IBEX]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1120]
        [GO_TO_START]
        [NAME:giant ibex:giant ibexes:giant ibex]
        [CASTE_NAME:giant ibex:giant ibexes:giant ibex]
        [GENERAL_CHILD_NAME:giant ibex kid:giant ibex kids]
        [DESCRIPTION:A huge monster in the form of an ibex.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [CREATURE_TILE:'I']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:long horns]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:585:390:195:1900:2900] 45 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
