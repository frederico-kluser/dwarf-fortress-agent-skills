# Giant snowy owl

> Fonte: [Giant snowy owl](https://dwarffortresswiki.org/index.php/Giant_snowy_owl) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant snowy owls for their yellow eyes.**
- **Biome**
- **Tundra**
- **Variations**
- **Snowy owl - Snowy owl man - Giant snowy owl**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 6,420.6 cm 3
- **Mid:** 107,010 cm 3
- **Max:** 214,020 cm 3
- **Food products**
- **Eggs:** 5-10
- **Age**
- **Adult at:** 1
- **Max age:** 10-30
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

*A large bird monster in the shape of a snowy owl.*

\
Some dwarves like giant snowy owls for their *coloration* and their *yellow eyes*.

    [CREATURE:GIANT_SNOWY_OWL]
        [COPY_TAGS_FROM:BIRD_OWL_SNOWY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:10701]
        [GO_TO_START]
        [NAME:giant snowy owl:giant snowy owls:giant snowy owl]
        [CASTE_NAME:giant snowy owl:giant snowy owls:giant snowy owl]
        [GENERAL_CHILD_NAME:giant snowy owl chick:giant snowy owl chicks]
        [DESCRIPTION:A large bird monster in the shape of a snowy owl.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'O']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:yellow eyes]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
