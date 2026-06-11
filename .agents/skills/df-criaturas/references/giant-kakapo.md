# Giant kakapo

> Fonte: [Giant kakapo](https://dwarffortresswiki.org/index.php/Giant_kakapo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant kakapo for their longevity.**
- **Biome**
- **Temperate Shrubland Temperate Savanna Temperate Grassland Any Temperate Forest**
- **Variations**
- **Kakapo - Kakapo man - Giant kakapo**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 3,684 cm 3
- **Mid:** 110,520 cm 3
- **Max:** 221,040 cm 3
- **Food products**
- **Eggs:** 1-4
- **Age**
- **Adult at:** 7
- **Max age:** 60-120
- **Butchering returns**
- **Food items**
- **Meat:** 17-19
- **Fat:** 11-13
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 24-26
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster the shape of a kakapo.*

**Giant kakapo** are enlarged cousins of the common kakapo, found in some savage temperate biomes. Despite being over 3 times bigger than a dwarf, these birds are about as benign as their normal counterparts; a lone giant kakapo will occasionally appear in the map and meander around adorably, fleeing from attackers who threaten it. However, due to their larger size, hunters who try to kill them may meet some resistance.

Giant kakapo can be captured in cage traps and trained into pets, possessing the standard high value of a giant creature. While they aren't any better than normal kakapo when it comes to laying eggs, they actually give a decent amount of returns when butchered, making the idea of a giant parrot farm a viable one. Giant kakapo are exotic mounts and can be used by elves during sieges, which may not be a smart choice for them as they could've picked a bird actually capable of flight instead.

Some dwarves like giant kakapo for their *longevity*, their *flightlessness* and their *booming calls*.

    [CREATURE:GIANT_KAKAPO]
        [COPY_TAGS_FROM:BIRD_KAKAPO]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:7368]
        [GO_TO_START]
        [NAME:giant kakapo:giant kakapo:giant kakapo]
        [CASTE_NAME:giant kakapo:giant kakapo:giant kakapo]
        [GENERAL_CHILD_NAME:giant kakapo chick:giant kakapo chicks]
        [DESCRIPTION:A large monster the shape of a kakapo.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'K']
        [COLOR:2:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:longevity]
        [PREFSTRING:flightlessness]
        [PREFSTRING:booming calls]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
