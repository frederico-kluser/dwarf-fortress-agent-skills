# Giant koala

> Fonte: [Giant koala](https://dwarffortresswiki.org/index.php/Giant_koala) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant koalas for their adorable appearance.**
- **Biome**
- **Temperate Broadleaf Forest**
- **Variations**
- **Koala - Koala man - Giant koala**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 27,050 cm 3
- **Mid:** 135,250 cm 3
- **Max:** 270,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 13
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
- **Bones:** 18
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large koala-shaped monster.*

    [CREATURE:GIANT_KOALA]
        [COPY_TAGS_FROM:KOALA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2705]
        [GO_TO_START]
        [NAME:giant koala:giant koalas:giant koala]
        [CASTE_NAME:giant koala:giant koalas:giant koala]
        GENERAL_CHILD_NAME:giant koala joey:giant koala joeys]
        [DESCRIPTION:A large koala-shaped monster.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'K']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:adorable appearance]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:1945:1504:1062:548:3100:4500] 16 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
