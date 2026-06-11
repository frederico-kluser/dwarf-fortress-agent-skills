# Giant pangolin

> Fonte: [Giant pangolin](https://dwarffortresswiki.org/index.php/Giant_pangolin) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant pangolins for their overlapping scales.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Pangolin - Pangolin man - Giant pangolin**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 23,510 cm 3
- **Mid:** 117,550 cm 3
- **Max:** 235,100 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
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
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a pangolin.*

**Giant pangolins** are enlarged cousins of the common pangolin, found in savage tropical plains and forests. Despite being nearly four times the size of a dwarf, they are just as benign as their original counterparts, doing little more than rooting around the grass and eating bugs along the way. The difference is, they are more capable of fighting back when cornered than a normal pangolin, though they should still not pose a threat to a hunter.

Giant pangolins can be captured in cage traps and trained into pets, possessing the standard high value of a giant creature. They produce an average amount of meat, bones and fat when butchered, making them a choice for a meat industry if a breeding pair is obtained. Like normal pangolins, they possess scales rather than skin, and are therefore unusable for creating leather.

Some dwarves like giant pangolins for their *overlapping scales*.

Feels strange when petting.

    [CREATURE:GIANT_PANGOLIN]
        [COPY_TAGS_FROM:PANGOLIN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:4702]
        [GO_TO_START]
        [NAME:giant pangolin:giant pangolins:giant pangolin]
        [CASTE_NAME:giant pangolin:giant pangolins:giant pangolin]
        [GENERAL_CHILD_NAME:baby giant pangolin:baby giant pangolins]
        [DESCRIPTION:A huge monster in the form of a pangolin.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'P']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:overlapping scales]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
