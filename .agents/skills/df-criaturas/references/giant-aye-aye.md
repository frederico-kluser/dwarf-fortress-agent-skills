# Giant aye-aye

> Fonte: [Giant aye-aye](https://dwarffortresswiki.org/index.php/Giant_aye-aye) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant aye-ayes for their interesting fingers.**
- **Biome**
- **Tropical Dry Broadleaf Forest Tropical Moist Broadleaf Forest**
- **Variations**
- **Aye-aye - Aye-aye man - Giant aye-aye**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 21,752.5 cm 3
- **Mid:** 108,762.5 cm 3
- **Max:** 217,525 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
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
- **Bones:** 18
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster shaped like an aye-aye.*

**Giant aye-ayes** are the super-sized counterpart to the common aye-aye found in tropical broadleaf forests. Giant aye-ayes are a little larger than grizzly bears, but not as aggressive as those, instead fleeing any conflict. Only appearing rarely in a small subset of biomes, giant aye-ayes are among the more elusive animals in *Dwarf Fortress*.

Due to their size, they yield a decent amount of returns when butchered, but the aforementioned rarity can make it difficult to obtain a breeding pair for a sustainable meat production. Giant aye-ayes are exotic mounts, and can rarely be ridden by elves in a siege.

Some dwarves like giant aye-ayes for their *interesting fingers*.

"Their fingers are like tree trunks!" - A dwarf's final words after encountering this very creature.\
*Art by Science Photo Library*

    [CREATURE:GIANT_AYE-AYE]
        [COPY_TAGS_FROM:AYE-AYE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:8701]
        [GO_TO_START]
        [NAME:giant aye-aye:giant aye-ayes:giant aye-aye]
        [CASTE_NAME:giant aye-aye:giant aye-ayes:giant aye-aye]
        [DESCRIPTION:A huge monster shaped like an aye-aye.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'A']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:interesting fingers]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:703:505:274:1900:2900] 32 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
