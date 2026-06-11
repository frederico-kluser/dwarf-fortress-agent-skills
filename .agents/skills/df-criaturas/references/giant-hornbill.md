# Giant hornbill

> Fonte: [Giant hornbill](https://dwarffortresswiki.org/index.php/Giant_hornbill) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant hornbills for their great bills.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Hornbill - Hornbill man - Giant hornbill**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 4,176.48 cm 3
- **Mid:** 108,762.5 cm 3
- **Max:** 217,525 cm 3
- **Food products**
- **Eggs:** 1-4
- **Age**
- **Adult at:** 1
- **Max age:** 35-40
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

*A huge monster in the shape of a hornbill.*

    [CREATURE:GIANT_HORNBILL]
        [COPY_TAGS_FROM:BIRD_HORNBILL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:8701]
        [GO_TO_START]
        [NAME:giant hornbill:giant hornbills:giant hornbill]
        [CASTE_NAME:giant hornbill:giant hornbills:giant hornbill]
        [GENERAL_CHILD_NAME:giant hornbill chick:giant hornbill chicks]
        [DESCRIPTION:A huge monster in the shape of a hornbill.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'H']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:great bills]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
