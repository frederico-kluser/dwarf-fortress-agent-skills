# Giant puffin

> Fonte: [Giant puffin](https://dwarffortresswiki.org/index.php/Giant_puffin) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant puffins for their colorful beaks.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Puffin - Puffin man - Giant puffin**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 8,210.1 cm 3
- **Mid:** 102,626.25 cm 3
- **Max:** 205,252.5 cm 3
- **Food products**
- **Eggs:** 1
- **Age**
- **Adult at:** 1
- **Max age:** 15-20
- **Butchering returns**
- **Food items**
- **Meat:** 17-19
- **Fat:** 11-13
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 1
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 24-26
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a puffin.*

**Giant puffins** are much larger than their smaller relatives (273.67 times larger, in fact), and produce meat and other edible products.

Some dwarves like giant puffins for their *colorful beaks*.

    [CREATURE:GIANT_PUFFIN]
        [COPY_TAGS_FROM:BIRD_PUFFIN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:27367]
        [GO_TO_START]
        [NAME:giant puffin:giant puffins:giant puffin]
        [CASTE_NAME:giant puffin:giant puffins:giant puffin]
        [GENERAL_CHILD_NAME:giant puffin chick:giant puffin chicks]
        [DESCRIPTION:A large monster in the form of a puffin.]
        [POPULATION_NUMBER:30:50]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'P']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:colorful beaks]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
