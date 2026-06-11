# Giant cockatiel

> Fonte: [Giant cockatiel](https://dwarffortresswiki.org/index.php/Giant_cockatiel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant cockatiels for their crests.**
- **Biome**
- **Any Desert Temperate Grassland**
- **Variations**
- **Cockatiel - Cockatiel man - Giant cockatiel**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 22,292.2 cm 3
- **Max:** 200,629.8 cm 3
- **Food products**
- **Eggs:** 2-8
- **Age**
- **Adult at:** 1
- **Max age:** 15-30
- **Butchering returns**
- **Food items**
- **Meat:** 17
- **Fat:** 11
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
- **Bones:** 24
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a cockatiel.*

**Giant cockatiels** are giant animal counterparts of regular cockatiels, who spawn in savage deserts and temperate grassland. Unlike their basal equivalents, giant cockatiels are larger than a grizzly bear. They appear in clusters of 5-10 individuals, and may cause annoyances to a fortress, primarily through job cancelations.

Giant cockatiels are difficult to capture and difficult to hunt, but they can be used to start an exotic egg farm, if you manage to nab a breeding pair. Because they are flying savage birds, they may cause problems on the sliver of a chance that they appear in an elven siege. Unlike their brethren, they lay eggs two to eight a clutch.

Some dwarves like giant cockatiels for their *crests*.

    [CREATURE:GIANT_COCKATIEL]
        [COPY_TAGS_FROM:BIRD_COCKATIEL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:222922]
        [GO_TO_START]
        [NAME:giant cockatiel:giant cockatiels:giant cockatiel]
        [CASTE_NAME:giant cockatiel:giant cockatiels:giant cockatiel]
        [GENERAL_CHILD_NAME:giant cockatiel hatchling:giant cockatiel hatchlings]
        [DESCRIPTION:A large monster in the form of a cockatiel.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'C']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:crests]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
