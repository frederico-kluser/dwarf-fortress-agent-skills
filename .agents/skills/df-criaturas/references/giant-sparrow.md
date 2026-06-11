# Giant sparrow

> Fonte: [Giant sparrow](https://dwarffortresswiki.org/index.php/Giant_sparrow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant sparrows for their lovely songs.**
- **Biome**
- **Any Grassland Any Savanna Any Shrubland Any Temperate Forest Any Tropical Forest Any Desert Any Wetland**
- **Variations**
- **Sparrow - Sparrow man - Giant sparrow**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 13,347.34 cm 3
- **Max:** 200,210.1 cm 3
- **Food products**
- **Eggs:** 2-7
- **Age**
- **Adult at:** 1
- **Max age:** 5-10
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

*A large bird-like monster in the shape of a sparrow.*

A usually harmless, larger version of a sparrow. Tend to fly around in flocks in line formation. May attack in flocks if provoked.

    [CREATURE:GIANT_SPARROW]
        [COPY_TAGS_FROM:SPARROW]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:667367]
        [GO_TO_START]
        [NAME:giant sparrow:giant sparrows:giant sparrow]
        [CASTE_NAME:giant sparrow:giant sparrows:giant sparrow]
        [GENERAL_CHILD_NAME:giant sparrow hatchling:giant sparrow hatchlings]
        [DESCRIPTION:A large bird-like monster in the shape of a sparrow.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:lovely songs]
        [PREFSTRING:dust baths]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
