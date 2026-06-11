# Giant kestrel

> Fonte: [Giant kestrel](https://dwarffortresswiki.org/index.php/Giant_kestrel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant kestrels for their coloration.**
- **Biome**
- **Tropical Freshwater Marsh Tropical Saltwater Marsh Temperate Freshwater Marsh Temperate Saltwater Marsh Any Shrubland Any Savanna Any Grassland**
- **Variations**
- **Kestrel - Kestrel man - Giant kestrel**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 24,210 cm 3
- **Mid:** 100,875 cm 3
- **Max:** 201,750 cm 3
- **Food products**
- **Eggs:** 3-6
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 20
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

*A huge monster in the shape of a kestrel.*

**Giant kestrels** are simply giant versions of their smaller, more common cousins: kestrels. In a similar manner to normal kestrels, they can be captured in a cage trap and used for egg production. This makes them better assets for your dwarves alive than dead.

Some dwarves like giant kestrels for their *coloration* and their *hunting prowess*.

    [CREATURE:GIANT_KESTREL]
        [COPY_TAGS_FROM:BIRD_KESTREL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:80700]
        [GO_TO_START]
        [NAME:giant kestrel:giant kestrels:giant kestrel]
        [CASTE_NAME:giant kestrel:giant kestrels:giant kestrel]
        [GENERAL_CHILD_NAME:giant kestrel chick:giant kestrel chicks]
        [DESCRIPTION:A huge monster in the shape of a kestrel.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'K']
        [COLOR:4:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [PREFSTRING:hunting prowess]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
