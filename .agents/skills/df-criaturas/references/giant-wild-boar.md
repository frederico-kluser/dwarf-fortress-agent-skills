# Giant wild boar

> Fonte: [Giant wild boar](https://dwarffortresswiki.org/index.php/Giant_wild_boar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant wild boars for their tusks.**
- **Biome**
- **Any Savanna Any Grassland Any Shrubland Any Forest Any Wetland**
- **Variations**
- **Wild boar - Wild boar man - Giant wild boar**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 78,320 cm 3
- **Mid:** 391,600 cm 3
- **Max:** 783,200 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-20
- **Butchering returns**
- **Food items**
- **Meat:** 13-16
- **Fat:** 8
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2-3
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 14-18
- **Skull:** 1
- **Ivory:** 2
- **Hooves:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster boar with jagged tusks.*

**Giant wild boars** are roughly 10 times the size of standard wild boars. They appear in groups of 5-10, wandering through various savage biomes, and may also serve as mounts during a siege.

Despite the ferocity implied by their name, they retain the \[benign\] token of their smaller cousins, and will generally run away instead of engaging in combat. They are large enough to seriously injure unarmored dwarves if cornered.

Captured giant wild boars can be tamed and bred as livestock for a meat industry. Their piglets grow to full size in two years, producing a respectable amount of meat and ivory tusks as a bonus. As non-grazers, they can be conveniently stored in cages and small pastures while they are growing.

Some dwarves admire giant wild boars for their *tusks* and their *ferocious charges*.

    [CREATURE:GIANT_WILD_BOAR]
        [COPY_TAGS_FROM:WILD_BOAR]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:979]
        [GO_TO_START]
        [NAME:giant wild boar:giant wild boars:giant wild boar]
        [CASTE_NAME:giant wild boar:giant wild boars:giant wild boar]
        [GENERAL_CHILD_NAME:giant wild boar piglet:giant wild boar piglets]
        [DESCRIPTION:A huge monster boar with jagged tusks.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'B']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:tusks]
        [PREFSTRING:ferocious charges]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
