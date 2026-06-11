# Giant wombat

> Fonte: [Giant wombat](https://dwarffortresswiki.org/index.php/Giant_wombat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant wombats for their waddle.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Mountain**
- **Variations**
- **Wombat - Wombat man - Giant wombat**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 52,885 cm 3
- **Mid:** 188,875 cm 3
- **Max:** 377,750 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 15-19
- **Fat:** 13-16
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
- **Teeth:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a wombat.*

**Giant wombats** are giant animal variants of the wombat, found in savage mountains, temperate forests and temperate shrublands. Like the regular wombat, these animals appear in small groups of up to ten individuals. Being benign creatures they will meander and generally keep to themselves. Giant wombats are roughly the size of an alligator, or roughly 12.5 times larger than a dwarf, and as such they are a force to be reckoned with against a poorly equipped militia if provoked. Children of giant wombats are called *giant wombat joeys'.*

Some dwarves like giant wombats for their *waddle*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
While it may be fun to build brown blocks with Dwarf Fortress, be wary of any brown blocks in the vicinity of a giant wombat, as they may instead be blocks of filth.

    [CREATURE:GIANT_WOMBAT]
        [COPY_TAGS_FROM:WOMBAT]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1511]
        [GO_TO_START]
        [NAME:giant wombat:giant wombats:giant wombat]
        [CASTE_NAME:giant wombat:giant wombats:giant wombat]
        [GENERAL_CHILD_NAME:giant wombat joey:giant wombat joeys]
        [DESCRIPTION:A huge monster in the shape of a wombat.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'W']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:waddle]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
