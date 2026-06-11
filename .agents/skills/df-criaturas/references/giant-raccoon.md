# Giant raccoon

> Fonte: [Giant raccoon](https://dwarffortresswiki.org/index.php/Giant_raccoon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant raccoons for their cunning.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Raccoon - Raccoon man - Giant raccoon**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 24,927 cm 3
- **Mid:** 124,635 cm 3
- **Max:** 249,270 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 15
- **Fat:** 13
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

*A huge monster in the shape of a raccoon.*

**Giant raccoons** are much bigger, more problematic versions of the regular raccoon. They're the size of a grizzly bear, and enjoy stealing fortresses' food and finished goods.

Some dwarves like giant raccoons for their *cunning*.

## Combat

While an unarmed civilian is likely to be killed by a giant raccoon, a few well-trained dwarves should be able to kill one of these animals. As a result, giant raccoons aren't really much of a threat once a good military and good defenses are set up.

## Trading

Elves will occasionally offer them as exotic pets.

    >[CREATURE:GIANT_RACCOON]
        [COPY_TAGS_FROM:RACCOON]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:3561]
        [GO_TO_START]
        [NAME:giant raccoon:giant raccoons:giant raccoon]
        [CASTE_NAME:giant raccoon:giant raccoons:giant raccoon]
        [GENERAL_CHILD_NAME:giant raccoon pup:giant raccoon pups]
        [DESCRIPTION:A huge monster in the shape of a raccoon.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:3]
        [CREATURE_TILE:'R']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:cunning]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
