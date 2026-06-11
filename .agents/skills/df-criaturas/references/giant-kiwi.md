# Giant kiwi

> Fonte: [Giant kiwi](https://dwarffortresswiki.org/index.php/Giant_kiwi) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant kiwis for their long beaks.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland**
- **Variations**
- **Kiwi - Kiwi man - Giant kiwi**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 1,000
- **Not hunting/war trainable**
- **Size**
- **Birth:** 37,414.3 cm 3
- **Mid:** 108,762.5 cm 3
- **Max:** 217,525 cm 3
- **Food products**
- **Eggs:** 1-2
- **Age**
- **Adult at:** 1
- **Max age:** 20-50
- **Butchering returns**
- **Food items**
- **Meat:** 18-22
- **Fat:** 11-15
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
- **Bones:** 24-28
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster with a long nose and brown feathers.*

**Giant kiwi** are over-sized flightless birds. While they are not generally threatening, their large size allows them to cause significant damage, particularly to unarmored dwarves.

Interestingly, the giant kiwi's pet value is nearly double that of almost all other giant creatures. This can make them lucrative live trade goods, but their butchering returns are no more valuable than common domestic livestock. Some dwarves admire them for their *great size* and *long beaks*.

    [CREATURE:BIRD_KIWI_GIANT]
        [COPY_TAGS_FROM:BIRD_KIWI]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:8701]
        [GO_TO_START]
        [NAME:giant kiwi:giant kiwis:giant kiwi]
        [GENERAL_CHILD_NAME:giant kiwi chick:giant kiwi chicks]
        [DESCRIPTION:A large monster with a long nose and brown feathers.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'K']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [PETVALUE:1000]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:giant kiwi cock:giant kiwi cocks:giant kiwi cock]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:giant kiwi hen:giant kiwi hens:giant kiwi hen]
        [SELECT_CASTE:ALL]
        [PREFSTRING:great size]
        [PREFSTRING:long beaks]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
