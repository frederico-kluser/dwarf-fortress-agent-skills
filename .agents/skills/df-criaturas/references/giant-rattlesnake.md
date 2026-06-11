# Giant rattlesnake

> Fonte: [Giant rattlesnake](https://dwarffortresswiki.org/index.php/Giant_rattlesnake) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant rattlesnakes for their warning rattle.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Rattlesnake - Rattlesnake man - Giant rattlesnake**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Syndrome**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,424.4 cm 3
- **Mid:** 124,635 cm 3
- **Max:** 249,270 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 6-7
- **Fat:** 3
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 0-2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 10
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster taking the shape of a rattlesnake.*

**Giant Rattlesnakes** are the giant animal variant of rattlesnakes. They are found in any non-freezing, savage biome. While regularly sized rattlesnakes can pose a threat due to their venom, giant rattlesnakes' large size (nearly twice the size of a dwarf) compounds their risk factor.

    [CREATURE:GIANT_RATTLESNAKE]
        [COPY_TAGS_FROM:RATTLESNAKE]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:rattlesnake]
            [CVCT_REPLACEMENT:giant rattlesnake]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:rattlesnake]
            [CVCT_REPLACEMENT:giant rattlesnake]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:rattlesnake]
            [CVCT_REPLACEMENT:giant rattlesnake]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:RATTLESNAKE]
            [CVCT_REPLACEMENT:GIANT_RATTLESNAKE]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:3561]
        [GO_TO_START]
        [NAME:giant rattlesnake:giant rattlesnakes:giant rattlesnake]
        [CASTE_NAME:giant rattlesnake:giant rattlesnakes:giant rattlesnake]
        [DESCRIPTION:A huge monster taking the shape of a rattlesnake.]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:warning rattle]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
