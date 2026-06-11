# Giant flying squirrel

> Fonte: [Giant flying squirrel](https://dwarffortresswiki.org/index.php/Giant_flying_squirrel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant flying squirrels for their large eyes.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Flying squirrel - Flying squirrel man - Giant flying squirrel**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 201,400 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 5-6
- **Butchering returns**
- **Food items**
- **Meat:** 13-14
- **Fat:** 12-13
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
- **Teeth:** 0-2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster taking the shape of a flying squirrel.*

A fairly boring upscaled vermin creature that mostly makes a good target for your hunters. Like the cat, it is a legendary climber. Although it has the word "flying" in its name, it (just like real life flying squirrels) can't actually fly, nor even glide from tree to tree as these animals do in real life.

    [CREATURE:GIANT_FLYING_SQUIRREL]
        [COPY_TAGS_FROM:SQUIRREL_FLYING]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:100700]
        [GO_TO_START]
        [NAME:giant flying squirrel:giant flying squirrels:giant flying squirrel]
        [CASTE_NAME:giant flying squirrel:giant flying squirrels:giant flying squirrel]
        [DESCRIPTION:A large monster taking the shape of a flying squirrel.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:3:5]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:gliding]
        [PREFSTRING:large eyes]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
