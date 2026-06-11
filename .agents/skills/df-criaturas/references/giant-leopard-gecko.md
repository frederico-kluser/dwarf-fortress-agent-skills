# Giant leopard gecko

> Fonte: [Giant leopard gecko](https://dwarffortresswiki.org/index.php/Giant_leopard_gecko) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant leopard geckos for their coloration.**
- **Biome**
- **Any Desert**
- **Variations**
- **Leopard gecko - Leopard gecko man - Giant leopard gecko**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,350 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 6-20
- **Butchering returns**
- **Food items**
- **Meat:** 13
- **Fat:** 12
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

*A large monster in the shape of a gecko.*

**Giant leopard geckos** are super-sized versions of the common leopard gecko who inhabit savage deserts. While their original counterparts are just vermin, these creatures are over 3 times bigger than a dwarf. They are not particularly aggressive, but are carnivorous and will attack other creatures (including dwarves) who provoke them, potentially killing them. All giant leopard geckos are born with Legendary skill in climbing.

Giant leopard geckos can be captured in cage traps and trained into pets, possessing the standard giant creature pet value. They are born adults, fully-sized right after birth, and cannot be permanently tamed. They produce an adequate amount of products when butchered, but unlike most reptiles, they give live birth instead of laying eggs. They are exotic mounts and may be witnessed being ridden by elves during sieges.

Some dwarves like giant leopard geckos for their *coloration*.

    [CREATURE:GIANT_LEOPARD_GECKO]
        [COPY_TAGS_FROM:GECKO_LEOPARD]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:400700]
        [GO_TO_START]
        [NAME:giant leopard gecko:giant leopard geckos:giant leopard gecko]
        [CASTE_NAME:giant leopard gecko:giant leopard geckos:giant leopard gecko]
        [DESCRIPTION:A large monster in the shape of a gecko.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'G']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
