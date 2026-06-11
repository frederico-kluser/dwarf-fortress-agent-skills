# Giant white stork

> Fonte: [Giant white stork](https://dwarffortresswiki.org/index.php/Giant_white_stork) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant white storks for their long legs.**
- **Biome**
- **Any Grassland Any Wetland**
- **Variations**
- **White stork - White stork man - Giant white stork**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 7,368 cm 3
- **Mid:** 110,520 cm 3
- **Max:** 221,040 cm 3
- **Food products**
- **Eggs:** 1-7
- **Age**
- **Adult at:** 1
- **Max age:** 20-40
- **Butchering returns**
- **Food items**
- **Meat:** 17-19
- **Fat:** 11-13
- **Brain:** 1
- **Gizzard:** 1
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

*A large monster in the form of a stork.*

Some dwarves like giant white storks for their *long necks*, their *long legs* and their *long bills*.

    [CREATURE:GIANT_WHITE_STORK]
        [COPY_TAGS_FROM:BIRD_STORK_WHITE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:7368]
        [GO_TO_START]
        [NAME:giant white stork:giant white storks:giant white stork]
        [CASTE_NAME:giant white stork:giant white storks:giant white stork]
        [GENERAL_CHILD_NAME:giant white stork hatchling:giant white stork hatchlings]
        [DESCRIPTION:A large monster in the form of a stork.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'S']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:long necks]
        [PREFSTRING:long legs]
        [PREFSTRING:long bills]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
