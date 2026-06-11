# Giant platypus

> Fonte: [Giant platypus](https://dwarffortresswiki.org/index.php/Giant_platypus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant platypuses for their large bills.**
- **Biome**
- **Any River**
- **Variations**
- **Platypus - Platypus man - Giant platypus**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount · Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,070.1 cm 3
- **Mid:** 107,010 cm 3
- **Max:** 214,020 cm 3
- **Food products**
- **Eggs:** 1-3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 13
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
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster, the shape of a platypus.*

The males are armed with a non-lethal venom, that can be injected if they wound someone with their rear paws, causing extreme pain and minor swelling.

Some dwarves admire giant platypuses for their *great size*, their *bizarre appearance*, their *venomous spurs*, their *flat tails* and their *large bills*.

    [CREATURE:PLATYPUS, GIANT]
        [COPY_TAGS_FROM:PLATYPUS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:platypus]
            [CVCT_REPLACEMENT:giant platypus]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:platypus]
            [CVCT_REPLACEMENT:giant platypus]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:platypus]
            [CVCT_REPLACEMENT:giant platypus]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:PLATYPUS]
            [CVCT_REPLACEMENT:PLATYPUS, GIANT]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:10701]
        [GO_TO_START]
        [NAME:giant platypus:giant platypuses:giant platypus]
        [CASTE_NAME:giant platypus:giant platypuses:giant platypus]
        [GENERAL_CHILD_NAME:baby giant platypus:baby giant platypuses]
        [DESCRIPTION:A huge monster, the shape of a platypus.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'P']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [PREFSTRING:great size]
        [PREFSTRING:bizarre appearance]
        [PREFSTRING:venomous spurs]
        [PREFSTRING:flat tails]
        [PREFSTRING:large bills]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
