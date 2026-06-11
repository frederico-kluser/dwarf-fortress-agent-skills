# Giant anole

> Fonte: [Giant anole](https://dwarffortresswiki.org/index.php/Giant_anole) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant anoles for their dewlaps.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Anole - Anole man - Giant anole**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,629.8 cm 3
- **Food products**
- **Eggs:** 1-2
- **Age**
- **Adult at:** Birth
- **Max age:** 5-7
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
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of an anole.*

**Giant anoles** are the giant animal versions of the common anole who inhabit savage tropical forests. While their original counterparts are just vermin, these creatures are over 3 times bigger than a dwarf. They are not particularly aggressive, but are not benign and will attack other creatures (including dwarves) who provoke them, potentially killing them. All giant anoles are born with Legendary skill in climbing.

Giant anoles can be captured in cage traps and trained into pets, possessing the standard giant creature pet value. They are born adults and cannot be permanently tamed. They produce an adequate amount of products when butchered and may be placed in a nest box to lay eggs, however they only lay 1 to 2 eggs at a time, making them very poor animals for egg production. Additionally, giant anoles are noticeably short-lived, only living up to 7 years at most. They are exotic mounts and may be witnessed being ridden by elves during sieges.

Some dwarves like giant anoles for their *dewlaps* and their *ability to change color*.

    [CREATURE:GIANT_ANOLE]
        [COPY_TAGS_FROM:ANOLE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:222922]
        [GO_TO_START]
        [NAME:giant anole:giant anoles:giant anole]
        [CASTE_NAME:giant anole:giant anoles:giant anole]
        [DESCRIPTION:A large monster in the shape of an anole.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'A']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ability to change color]
        [PREFSTRING:dewlaps]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
