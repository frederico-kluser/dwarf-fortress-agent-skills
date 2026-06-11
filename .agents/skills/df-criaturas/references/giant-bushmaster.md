# Giant bushmaster

> Fonte: [Giant bushmaster](https://dwarffortresswiki.org/index.php/Giant_bushmaster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant bushmasters for their deadly bite.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Bushmaster - Bushmaster man - Giant bushmaster**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 611.4 cm 3
- **Mid:** 129,922.5 cm 3
- **Max:** 259,845 cm 3
- **Food products**
- **Eggs:** 10-20
- **Age**
- **Adult at:** Birth
- **Max age:** 12-24
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 6-8
- **Fat:** 3
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 9-10
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a bushmaster.*

**Giant bushmasters** are giant animal counterparts of the common bushmaster who can be found in savage tropical moist broadleaf forests. Like their smaller relatives, they have a venomous bite that can kill a dwarf in one go. Of course, they're also large enough to just tear limbs off completely without bothering with poison; after all, massive blood loss causes death even quicker than paralytic suffocation. Luckily, they're not aggressive, and will flee contact with your dwarves, despite being more than four times as large.

Excellent pit creatures, if you can capture and tame them. Strangely they are considered exotic mounts, so if giant bushmasters are arriving onto your map as part of an elven siege, be warned - they are extremely dangerous. Luckily, like all other species of snake they take the extent of their lives to reach their maximum size, but because of their bite, giant bushmaster juveniles are still extremely dangerous.

Some dwarves admire giant bushmasters for their *deadly bite*.

Good news: The giant fangs will kill you faster than the venom.\
*Art by Zoë van Dijk*

    [CREATURE:GIANT_BUSHMASTER]
        [COPY_TAGS_FROM:BUSHMASTER]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:bushmaster]
            [CVCT_REPLACEMENT:giant bushmaster]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:bushmaster]
            [CVCT_REPLACEMENT:giant bushmaster]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:bushmaster]
            [CVCT_REPLACEMENT:giant bushmaster]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:BUSHMASTER]
            [CVCT_REPLACEMENT:GIANT_BUSHMASTER]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:3057]
        [GO_TO_START]
        [NAME:giant bushmaster:giant bushmasters:giant bushmaster]
        [CASTE_NAME:giant bushmaster:giant bushmasters:giant bushmaster]
        [DESCRIPTION:A huge monster in the form of a bushmaster.]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:deadly bite]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
