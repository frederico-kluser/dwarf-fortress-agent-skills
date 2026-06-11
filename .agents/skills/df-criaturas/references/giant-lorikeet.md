# Giant lorikeet

> Fonte: [Giant lorikeet](https://dwarffortresswiki.org/index.php/Giant_lorikeet) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant lorikeets for their bright coloration.**
- **Biome**
- **Tropical Moist Broadleaf Forest Mangrove Swamp**
- **Variations**
- **Lorikeet - Lorikeet man - Giant lorikeet**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 10,070 cm 3
- **Max:** 201,400 cm 3
- **Food products**
- **Eggs:** 2
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

*A large monster in the shape of a lorikeet.*

    [CREATURE:GIANT_LORIKEET]
        [COPY_TAGS_FROM:BIRD_LORIKEET]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:100700]
        [GO_TO_START]
        [NAME:giant lorikeet:giant lorikeets:giant lorikeet]
        [CASTE_NAME:giant lorikeet:giant lorikeets:giant lorikeet]
        [GENERAL_CHILD_NAME:giant lorikeet hatchling:giant lorikeet hatchlings]
        [DESCRIPTION:A large monster in the shape of a lorikeet.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'L']
        [COLOR:4:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:bright coloration]
        [PREFSTRING:playful personalities]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
