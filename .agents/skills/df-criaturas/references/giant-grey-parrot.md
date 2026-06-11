# Giant grey parrot

> Fonte: [Giant grey parrot](https://dwarffortresswiki.org/index.php/Giant_grey_parrot) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant grey parrots for their social nature.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Grey parrot - Grey parrot man - Giant grey parrot**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,280 cm 3
- **Mid:** 101,400 cm 3
- **Max:** 202,800 cm 3
- **Food products**
- **Eggs:** 1-5
- **Age**
- **Adult at:** 1
- **Max age:** 40-60
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

*A huge monster in the shape of a grey parrot.*

**Giant grey parrots** are 507 times larger than grey parrots, and, like most giant creatures, produce more food.

Some dwarves like giant grey parrots for their *intelligence* and their *social nature*.

## Technical

The raw name for these creatures is, rather logically, `GIANT_GREY_PARROT`, compared to `PARROT_GREY`, the name of grey parrots.

Is insanely much louder when mimicking something.\
*Art by Bianka Hudson*

    [CREATURE:GIANT_GREY_PARROT]
        [COPY_TAGS_FROM:BIRD_PARROT_GREY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:50700]
        [GO_TO_START]
        [NAME:giant grey parrot:giant grey parrots:giant grey parrot]
        [CASTE_NAME:giant grey parrot:giant grey parrots:giant grey parrot]
        [GENERAL_CHILD_NAME:giant grey parrot chick:giant grey parrot chicks]
        [DESCRIPTION:A huge monster in the shape of a grey parrot.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:5]
        [CREATURE_TILE:'P']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:intelligence]
        [PREFSTRING:social nature]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
