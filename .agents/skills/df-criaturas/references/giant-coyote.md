# Giant coyote

> Fonte: [Giant coyote](https://dwarffortresswiki.org/index.php/Giant_coyote) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant coyotes for their howling.**
- **Biome**
- **Mountain Tundra Taiga Any Temperate Forest Temperate Savanna Temperate Grassland Temperate Shrubland Any Temperate Wetland Any Desert**
- **Variations**
- **Coyote - Coyote man - Giant coyote**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 30,600 cm 3
- **Mid:** 153,000 cm 3
- **Max:** 306,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 13-17
- **Fat:** 12-16
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 0-2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 18-22
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large dog-like monster with a haunting howl.*

**Giant coyotes** are large dog-like monsters with a haunting howl. They appear in groups of 2-10 in most savage biomes, and are pack hunters that are bigger than elks. Lacking the [`[LARGE_PREDATOR]`](/index.php/Creature_token#LARGE_PREDATOR "Creature token") token, they aren't very aggressive towards dwarves, though they butcher into a medium-sized amount of food returns, and so may help a struggling fortress to get by.

*Dwarves like giant coyotes for their howling*.

    [CREATURE:GIANT_COYOTE]
        [COPY_TAGS_FROM:COYOTE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2040]
        [GO_TO_START]
        [NAME:giant coyote:giant coyotes:giant coyote]
        [CASTE_NAME:giant coyote:giant coyotes:giant coyote]
        [GENERAL_CHILD_NAME:giant coyote pup:giant coyote pups]
        [DESCRIPTION:A large dog-like monster with a haunting howl.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:2:10]
        [CREATURE_TILE:'C']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:howling]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:411:274:137:1900:2900] 64 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
