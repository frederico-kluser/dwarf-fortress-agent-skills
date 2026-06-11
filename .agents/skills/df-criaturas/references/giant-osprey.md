# Giant osprey

> Fonte: [Giant osprey](https://dwarffortresswiki.org/index.php/Giant_osprey) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant ospreys for their fishing ability.**
- **Biome**
- **Any Ocean Any Lake Any River Tropical Freshwater Marsh Tropical Saltwater Marsh Temperate Freshwater Marsh Temperate Saltwater Marsh**
- **Variations**
- **Osprey - Osprey man - Giant osprey**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 5,885.55 cm 3
- **Mid:** 107,010 cm 3
- **Max:** 214,020 cm 3
- **Food products**
- **Eggs:** 2-4
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 18-20
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

*A large monster in the form of an osprey.*

    [CREATURE:GIANT_OSPREY]
        [COPY_TAGS_FROM:BIRD_OSPREY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:10701]
        [GO_TO_START]
        [NAME:giant osprey:giant ospreys:giant osprey]
        [CASTE_NAME:giant osprey:giant ospreys:giant osprey]
        [GENERAL_CHILD_NAME:giant osprey chick:giant osprey chicks]
        [DESCRIPTION:A large monster in the form of an osprey.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'O']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:fishing ability]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
