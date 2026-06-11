# Giant otter

> Fonte: [Giant otter](https://dwarffortresswiki.org/index.php/Giant_otter) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant otters for their playfulness.**
- **Biome**
- **Any Lake Any Lake Any River**
- **Variations**
- **River otter - Otter man - Giant otter**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 27,050 cm 3
- **Mid:** 135,250 cm 3
- **Max:** 270,500 cm 3
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

*A large monster in the form of an otter.*

**Giant otters** are over-sized cousins of the river otter, growing to the size of a small donkey. Giant otters are typically nonthreatening amphibious creatures, though they may also serve as mounts during a siege.

As exotic pets, giant otters can be tamed with moderate effort, or potentially purchased tame from elven caravans. They have a similar pet value to most other giant variants, and their butchering returns are only common value. Still, a breeding pair of giant otters will provide convenient non-grazing stock for your meat industry.

Some dwarves like giant otters for their *playfulness* and their *fluffy faces*.

    [CREATURE:GIANT_OTTER]
        [COPY_TAGS_FROM:RIVER OTTER]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2705]
        [GO_TO_START]
        [NAME:giant otter:giant otters:giant otter]
        [CASTE_NAME:giant otter:giant otters:giant otter]
        [GENERAL_CHILD_NAME:giant otter pup:giant otter pups]
        [DESCRIPTION:A large monster in the form of an otter.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:4]
        [CREATURE_TILE:'O']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:playfulness]
        [PREFSTRING:big fluffy faces]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
