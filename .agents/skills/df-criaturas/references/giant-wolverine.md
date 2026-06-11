# Giant wolverine

> Fonte: [Giant wolverine](https://dwarffortresswiki.org/index.php/Giant_wolverine) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant wolverines for their tenacity.**
- **Biome**
- **Taiga Mountain**
- **Variations**
- **Wolverine - Wolverine man - Giant wolverine**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 34,180 cm 3
- **Mid:** 170,900 cm 3
- **Max:** 341,800 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 5-15
- **Butchering returns**
- **Food items**
- **Meat:** 17
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
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large, terrifying monster the shape of a wolverine.*

**Giant wolverines** are a force to be reckoned with. While they are solitary, a single giant wolverine is more than a match for a single dwarf or any livestock. If left unchecked, they will move randomly around the map until they find a target. When they do, they will become enraged, beeline for the target, and likely immediately try to kill it upon catching up to it.

Luckily, a giant wolverine can't use attacks much more powerful than simple bites and scratches, so a military equipped with decent metal armor should be able to deal with them easily, as natural weapons are not the most deadly against dwarf-made armor.

Some dwarves like giant wolverines for their *tenacity*.

    [CREATURE:GIANT_WOLVERINE]
        [COPY_TAGS_FROM:WOLVERINE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1709]
        [GO_TO_START]
        [NAME:giant wolverine:giant wolverines:giant wolverine]
        [CASTE_NAME:giant wolverine:giant wolverines:giant wolverine]
        [GENERAL_CHILD_NAME:giant wolverine kit:giant wolverine kits]
        [DESCRIPTION:A large, terrifying monster the shape of a wolverine.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'W']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:tenacity]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
