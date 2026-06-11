# Giant monarch butterfly

> Fonte: [Giant monarch butterfly](https://dwarffortresswiki.org/index.php/Giant_monarch_butterfly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant monarch butterflies for their coloration.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Monarch butterfly - Monarch butterfly man - Giant monarch butterfly**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 1-1
- **Butchering returns**
- **Food items**
- **Meat:** 42
- **Fat:** 17
- **Brain:** 2
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

*A large monster in the shape of a monarch butterfly.*

**Giant monarch butterflies** are giant versions of the monarch butterflies - roughly the size of a lion. Since they are born adults, giant monarch butterflies cannot be fully tamed, though tame versions can be procured from elven sites. They do not lay eggs and give live birth instead. They have a measly one-year lifespan, which makes them inappropriate for breeding. They can be butchered for decent returns. Giant monarch butterflies are an exotic mount, and may be seen during elven sieges.

Some dwarves like giant monarch butterflies for their *coloration*.

    [CREATURE:GIANT_BUTTERFLY_MONARCH]
        [COPY_TAGS_FROM:BUTTERFLY_MONARCH]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant monarch butterfly:giant monarch butterflies:giant monarch butterfly]
        [CASTE_NAME:giant monarch butterfly:giant monarch butterflies:giant monarch butterfly]
        [DESCRIPTION:A large monster in the shape of a monarch butterfly.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:5]
        [CREATURE_TILE:'B']
        [COLOR:4:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
