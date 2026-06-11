# Giant adder

> Fonte: [Giant adder](https://dwarffortresswiki.org/index.php/Giant_adder) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant adders for their warning hisses.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Any Temperate Forest Any Temperate Wetland**
- **Variations**
- **Adder - Adder man - Giant adder**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,104.95 cm 3
- **Mid:** 100,524.75 cm 3
- **Max:** 201,049.5 cm 3
- **Food products**
- **Eggs:** 3-10
- **Age**
- **Adult at:** Birth
- **Max age:** 15-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 8-9
- **Fat:** 3
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1-2
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

*A large monster in the form of an adder.*

**Giant adders** are the giant animal variants of the common adder, found in savage temperate regions. While the regular creature is the smallest non-vermin in the game, giant adders are roughly the size of a grizzly bear when fully grown, and are exponentially more threatening as a result. Giant adders retain the syndrome of their counterparts, causing immediate strong pain followed by long-term nausea, blisters, and swelling, which, when combined with the larger size of the monster, may result in a bitten dwarf going unconscious in a matter of seconds if they do not just die outright.

Giant adders can be captured in cage traps and trained into pets, possessing the default giant animal value. They are born adults and as such cannot be permanently tamed. Thanks to their great size, they provide a good amount of returns when butchered, and make decent egg-layers for egg production. Like all giant animals, they are considered exotic mounts.

Some dwarves like giant adders for their *warning hisses*.

Once coiled around an entire castle - that already had another snake around it.\
*Art by Aloys Zötl, 1860*

    [CREATURE:GIANT_ADDER]
        [COPY_TAGS_FROM:ADDER]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:adder]
            [CVCT_REPLACEMENT:giant adder]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:adder]
            [CVCT_REPLACEMENT:giant adder]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:adder]
            [CVCT_REPLACEMENT:giant adder]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:ADDER]
            [CVCT_REPLACEMENT:GIANT_ADDER]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:134033]
        [GO_TO_START]
        [NAME:giant adder:giant adders:giant adder]
        [CASTE_NAME:giant adder:giant adders:giant adder]
        [DESCRIPTION:A large monster in the form of an adder.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'A']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:warning hisses]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
