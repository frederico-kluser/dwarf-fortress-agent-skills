# Giant leopard

> Fonte: [Giant leopard](https://dwarffortresswiki.org/index.php/Giant_leopard) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant leopards for their spotted coats.**
- **Biome**
- **Any Tropical Badlands Rocky Wasteland Sand Desert**
- **Variations**
- **Leopard - Leopard man - Giant leopard**
- **Attributes**
- **Alignment:** Savage
- **War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 56,000 cm 3
- **Mid:** 280,000 cm 3
- **Max:** 560,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 14
- **Fat:** 13
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
- **Bones:** 17
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A gigantic spotted predator, dwarfing its small cousins. It is found in the wild lands.*

**Giant leopards** are strong carnivorous animals, slightly smaller than a standard cow. They are lonesome hunters, roaming savage tropical and desert areas. Giant leopards may also appear as mounts during a siege.

Giant leopards may be tamed and kept as pets, trained for hunting or war, or used as livestock for a meat industry. While they do not produce as much meat as other "giant" creatures, giant leopard butchering returns are worth four times as much as those of common domestic animals.

Some dwarves like giant leopards for their *spotted coats*.

    [CREATURE:GIANT_LEOPARD]
        [COPY_TAGS_FROM:LEOPARD]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1120]
        [GO_TO_START]
        [NAME:giant leopard:giant leopards:giant leopard]
        [CASTE_NAME:giant leopard:giant leopards:giant leopard]
        [GENERAL_CHILD_NAME:giant leopard cub:giant leopard cubs]
        [DESCRIPTION:A gigantic spotted predator, dwarfing its small cousins.  It is found in the wild lands.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'L']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:spotted coats]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:453:302:151:1900:2900] 58 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
