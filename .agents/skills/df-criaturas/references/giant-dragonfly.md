# Giant dragonfly

> Fonte: [Giant dragonfly](https://dwarffortresswiki.org/index.php/Giant_dragonfly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant dragonflies for their faceted eyes.**
- **Biome**
- **Any Lake**
- **Variations**
- **Dragonfly - Dragonfly man - Giant dragonfly**
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

*A large monster in the shape of a dragonfly.*

**Giant dragonflies** are much larger versions of the standard vermin dragonfly, appearing in savage lakes.

They aren't very useful for anything other than immediate butchering, as they have a maximum lifespan of one year like other giant insects. And as they are not [`[BENIGN]`](/index.php/Creature_token#BENIGN "Creature token"), wild ones may annoyingly interrupt your dwarves when spotted.

Some dwarves like giant dragonflies for their *faceted eyes*.

Are they still harmless to humans..?\
*Art by Dead Fox*

    [CREATURE:GIANT_DRAGONFLY]
        [COPY_TAGS_FROM:DRAGONFLY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant dragonfly:giant dragonflies:giant dragonfly]
        [CASTE_NAME:giant dragonfly:giant dragonflies:giant dragonfly]
        [DESCRIPTION:A large monster in the shape of a dragonfly.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'D']
        [COLOR:3:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:faceted eyes]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph    [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
