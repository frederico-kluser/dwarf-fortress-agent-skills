# Giant two-humped camel

> Fonte: [Giant two-humped camel](https://dwarffortresswiki.org/index.php/Giant_two-humped_camel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant two-humped camels for their hump.**
- **Biome**
- **Any Desert**
- **Variations**
- **Two-humped camel - Two-humped camel man - Giant two-humped camel**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Milkable**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 405,500 cm 3
- **Mid:** 2,027,500 cm 3
- **Max:** 4,055,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 82
- **Fat:** 49
- **Brain:** 4
- **Heart:** 2
- **Lungs:** 8
- **Intestines:** 14
- **Liver:** 4
- **Kidneys:** 4
- **Tripe:** 4
- **Sweetbread:** 2
- **Eyes:** 2
- **Spleen:** 2
- **Raw materials**
- **Bones:** 46
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster the shape of a two-humped camel.*

**Giant two-humped camels** are massive counterparts of the common two-humped camel who inhabit savage deserts, spawning in groups of 3-7 individuals. They are 8 times bigger than their normal versions and about 67 times heavier than a dwarf, making them one of the largest herbivores in savage environments. Despite this great size, however, they are benign and will normally flee from dwarves rather than fight them. Watch out for the rare case of them being enraged in combat, however, as it may lead to your hunters being quickly trampled to death, and particularly make sure not to agitate your embark's giant camels.

Giant two-humped camels can be captured in cage traps and trained into pets, possessing identical pet value to a normal camel. Because of their immense size, they require a very large pasture to survive, but also grant a spectacular amount of returns if butchered, and like normal two-humped camels, their females can be milked, which can be used for cooking or to produce cheese. Note, however, that giant camel milk is identical to normal-sized camel milk in every aspect. They are exotic mounts, and so may be used by elves during sieges.

Some dwarves like giant two-humped camels for their *humps*.

    [CREATURE:GIANT_CAMEL_2_HUMP]
        [COPY_TAGS_FROM:CAMEL_2_HUMP]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:two-humped camel]
            [CVCT_REPLACEMENT:giant two-humped camel]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:two-humped camel]
            [CVCT_REPLACEMENT:giant two-humped camel]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:811]
        [GO_TO_START]
        [NAME:giant two-humped camel:giant two-humped camels:giant two-humped camel]
        [CASTE_NAME:giant two-humped camel:giant two-humped camels:giant two-humped camel]
        [GENERAL_CHILD_NAME:giant two-humped camel calf:giant two-humped camel calves]
        [DESCRIPTION:A huge monster the shape of a two-humped camel.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [CREATURE_TILE:'C']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:hump]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:405:270:135:1900:2900] 65 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
