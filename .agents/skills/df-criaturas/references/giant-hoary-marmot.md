# Giant hoary marmot

> Fonte: [Giant hoary marmot](https://dwarffortresswiki.org/index.php/Giant_hoary_marmot) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant hoary marmots for their whistles.**
- **Biome**
- **Mountain**
- **Variations**
- **Hoary marmot - Hoary marmot man - Giant hoary marmot**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 27,050 cm 3
- **Mid:** 135,250 cm 3
- **Max:** 270,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
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
- **Teeth:** 0-4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large creature the shape of a hoary marmot.*

    [CREATURE:GIANT_MARMOT_HOARY]
        [COPY_TAGS_FROM:MARMOT_HOARY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2705]
        [GO_TO_START]
        [NAME:giant hoary marmot:giant hoary marmots:giant hoary marmot]
        [CASTE_NAME:giant hoary marmot:giant hoary marmots:giant hoary marmot]
        [GENERAL_CHILD_NAME:giant hoary marmot pup:giant hoary marmot pups]
        [DESCRIPTION:A large creature the shape of a hoary marmot.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [CREATURE_TILE:'M']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:whistles]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
