# Giant honey badger

> Fonte: [Giant honey badger](https://dwarffortresswiki.org/index.php/Giant_honey_badger) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant honey badgers for their striped faces.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland Tropical Savanna Tropical Grassland Any Tropical Wetland Any Desert**
- **Variations**
- **Honey badger - Honey badger man - Giant honey badger**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 19,215 cm 3
- **Mid:** 149,450 cm 3
- **Max:** 298,900 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 15
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
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster the shape of a honey badger. It is ferocious in combat.*

Despite their status as giants, reputation for being ferocious in combat, and propensity for becoming enraged, **giant honey badgers** aren't all that dangerous to anything more than a couple lone civilians, being easily beaten by any military dwarf or small group of dogs.

Some dwarves like giant honey badgers for their *great size*, *underground communities* and *stripes faces*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Especially because this thing is a giant, the giant honey badger ***still*** don't care.

Admired for its *unholy nightmare fuel*.

    [CREATURE:HONEY BADGER, GIANT]
        [COPY_TAGS_FROM:HONEY BADGER]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2135]
        [GO_TO_START]
        [NAME:giant honey badger:giant honey badgers:giant honey badger]
        [CASTE_NAME:giant honey badger:giant honey badgers:giant honey badger]
        [GENERAL_CHILD_NAME:giant honey badger cub:giant honey badger cubs]
        [DESCRIPTION:A huge monster the shape of a honey badger.  It is ferocious in combat.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'B']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [PREFSTRING:great size]
        [PREFSTRING:underground communities]
        [PREFSTRING:striped faces]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
