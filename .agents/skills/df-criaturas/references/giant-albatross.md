# Giant albatross

> Fonte: [Giant albatross](https://dwarffortresswiki.org/index.php/Giant_albatross) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant albatrosses for their large wings.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Albatross - Albatross man - Giant albatross**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 9,612 cm 3
- **Mid:** 128,160 cm 3
- **Max:** 256,320 cm 3
- **Food products**
- **Eggs:** 1
- **Age**
- **Adult at:** 1
- **Max age:** 40-50
- **Butchering returns**
- **Food items**
- **Meat:** 19
- **Fat:** 13
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
- **Bones:** 26
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of an albatross.*

**Giant albatrosses** are the giant animal variant of the common albatross, found in savage oceans. They spawn in groups of 1-10 individuals, and will fly around aimlessly, fleeing when approached. They are roughly four times larger than a dwarf, but are unlikely to provide a threat to a fortress.

Giant albatrosses can be captured in cage traps and trained into pets. Like all other giant animals, they provide a decent amount of food and bones when butchered, but breeding them is a subpar choice, due to the fact they lay only one egg at a time. Also like other giant animals, they are considered exotic mounts.

Some dwarves like giant albatrosses for their *large wings*.

    [CREATURE:GIANT_ALBATROSS]
        [COPY_TAGS_FROM:BIRD_ALBATROSS]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:3204]
        [GO_TO_START]
        [NAME:giant albatross:giant albatrosses:giant albatross]
        [CASTE_NAME:giant albatross:giant albatrosses:giant albatross]
        [GENERAL_CHILD_NAME:giant albatross hatchling:giant albatross hatchlings]
        [DESCRIPTION:A huge monster in the shape of an albatross.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:10]
        [CREATURE_TILE:'A']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:large wings]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
