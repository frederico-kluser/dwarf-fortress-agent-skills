# Giant masked lovebird

> Fonte: [Giant masked lovebird](https://dwarffortresswiki.org/index.php/Giant_masked_lovebird) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant masked lovebirds for their loving nature.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Masked lovebird - Masked lovebird man - Giant masked lovebird**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 17,833.76 cm 3
- **Max:** 200,629.8 cm 3
- **Food products**
- **Eggs:** 4-5
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 15
- **Fat:** 11
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
- **Bones:** 24
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a masked lovebird.*

    [CREATURE:GIANT_MASKED_LOVEBIRD]
        [COPY_TAGS_FROM:BIRD_LOVEBIRD_MASKED]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:222922]
        [GO_TO_START]
        [NAME:giant masked lovebird:giant masked lovebirds:giant masked lovebird]
        [CASTE_NAME:giant masked lovebird:giant masked lovebirds:giant masked lovebird]
        [GENERAL_CHILD_NAME:giant masked lovebird hatchling:giant masked lovebird hatchlings]
        [DESCRIPTION:A huge monster in the form of a masked lovebird.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'L']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:loving nature]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
