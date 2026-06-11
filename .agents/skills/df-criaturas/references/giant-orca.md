# Giant orca

> Fonte: [Giant orca](https://dwarffortresswiki.org/index.php/Giant_orca) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant orcas for their coloration.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Orca - Orca man - Giant orca**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Exotic mount · Beaching**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,440,000 cm 3
- **Mid:** 20,000,000 cm 3
- **Max:** 40,000,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 50-90
- **Butchering returns**
- **Food items**
- **Meat:** 1240-1370
- **Fat:** 260-300
- **Brain:** 100-120
- **Heart:** 50-60
- **Lungs:** 200-230
- **Intestines:** 325-350
- **Liver:** 105-120
- **Kidneys:** 100-120
- **Tripe:** 100-120
- **Sweetbread:** 50-60
- **Eyes:** 4
- **Spleen:** 50-60
- **Raw materials**
- **Bones:** 310-340
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A gigantic monster in the shape of an orca.*

**Giant orcas** are big – really big. Of *all* the creatures in *Dwarf Fortress*, only the giant sperm whale is larger. A single specimen can feed a fortress for years and keep bone carvers very busy, but giant orcas appear in groups of 3-**9**. If that massive bounty isn't enough to motivate your dwarves to leave dry land, you're in luck: giant orcas are also prone to beaching themselves on shore, leaving a corpse ripe for butchering. Giant orcas can prove very valuable to any fort on a savage ocean. Dwarves in a terrifying biome should fear them as well – zombie orcas may crawl up on dry land.

Some dwarves like giant orcas for their *coloration* and *great jumps*, though one imagines that they admire both from quite a distance.

Once accidentally flopped itself onto land and took out three fortresses... in three different biomes... kilometers apart from each other.\
*Art by Chernyakov Aleksandr*

    [CREATURE:GIANT_ORCA]
        [COPY_TAGS_FROM:ORCA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:800]
        [GO_TO_START]
        [NAME:giant orca:giant orcas:giant orca]
        [CASTE_NAME:giant orca:giant orcas:giant orca]
        [GENERAL_CHILD_NAME:giant orca calf:giant orca calves]
        [DESCRIPTION:A gigantic monster in the shape of an orca.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:9]
        [CREATURE_TILE:'O']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [PREFSTRING:great jumps]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:528:352:176:1900:2900]
