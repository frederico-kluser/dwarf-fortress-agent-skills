# Giant opossum

> Fonte: [Giant opossum](https://dwarffortresswiki.org/index.php/Giant_opossum) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant opossums for their ability to play dead.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Opossum - Opossum man - Giant opossum**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 22,104 cm 3
- **Mid:** 110,520 cm 3
- **Max:** 221,040 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 2-4
- **Butchering returns**
- **Food items**
- **Meat:** 12-13
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
- **Bones:** 12-18
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of an opossum.*

**Giant opossums** are larger versions of the standard opossum. They can be somewhat dangerous to an unarmed dwarf, though they should pose little threat to even a fledgling military.

Giant opossums can be tamed as pets, or bred as livestock for a meat industry, though their lifespan of 2-4 years significantly limits their usefulness. They provide a medium amount of meat, but other, larger "giant" animals provide better butchering returns. Therefore, giant opossums are little more than pests to most fortresses, but they can be useful as wild hunting targets.

Some dwarves like giant opossums for their *ability to play dead*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some dwarven scholars consider these creatures to be a probable origin of the elven worship of nature, postulating that, due to the peculiar appearance of these animals, they might have mistaken the opossums for moving walls powered by divine will.

    [CREATURE:GIANT_OPOSSUM]
        [COPY_TAGS_FROM:OPOSSUM]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:7368]
        [GO_TO_START]
        [NAME:giant opossum:giant opossums:giant opossum]
        [CASTE_NAME:giant opossum:giant opossums:giant opossum]
        [GENERAL_CHILD_NAME:baby giant opossum:baby giant opossums]
        [DESCRIPTION:A huge monster in the shape of an opossum.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'O']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ability to play dead]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
