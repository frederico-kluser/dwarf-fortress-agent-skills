# Giant skink

> Fonte: [Giant skink](https://dwarffortresswiki.org/index.php/Giant_skink) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant skinks for their colorful tongues.**
- **Biome**
- **Any Temperate Any Tropical Any Desert**
- **Variations**
- **Skink - Skink man - Giant skink**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 203,500 cm 3
- **Food products**
- **Eggs:** 10-30
- **Age**
- **Adult at:** Birth
- **Max age:** 15-20
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

*A large monster in the shape of a skink.*

**Giant skinks** are super-sized versions of the common skink who inhabit most savage biomes. While their original counterparts are just vermin, these creatures are over 3 times bigger than a dwarf. They are not particularly aggressive, but are carnivorous and will attack other creatures (including dwarves) who provoke them, potentially killing them. All giant skinks are born with Legendary skill in climbing.

Giant skinks can be captured in cage traps and trained into pets, possessing the standard giant creature pet value. They are born adults, fully-sized right after birth, and cannot be permanently tamed. They produce an adequate amount of products when butchered and lay a fairly high amount of eggs, making them a good choice for food production - being born fully-sized means they can be butchered immediately after birth for maximum returns, meaning a breeding pair of giant skinks can be a huge help for your egg production and meat industry. They are exotic mounts and may be witnessed being ridden by elves during sieges.

Some dwarves like giant skinks for their *colorful tongues*.

    [CREATURE:GIANT_SKINK]
        [COPY_TAGS_FROM:SKINK]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:40700]
        [GO_TO_START]
        [NAME:giant skink:giant skinks:giant skink]
        [CASTE_NAME:giant skink:giant skinks:giant skink]
        [DESCRIPTION:A large monster in the shape of a skink.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:colorful tongues]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
