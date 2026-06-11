# Giant bark scorpion

> Fonte: [Giant bark scorpion](https://dwarffortresswiki.org/index.php/Giant_bark_scorpion) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant bark scorpions for their pincers.**
- **Biome**
- **Any Desert Tropical Grassland Tropical Savanna Tropical Shrubland Tropical Coniferous Forest**
- **Variations**
- **Bark scorpion - Bark scorpion man - Giant bark scorpion**
- **Attributes**
- **Alignment:** Savage
- **No Stun · No Pain · Exotic mount · Syndrome**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,021.01 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-10
- **Butchering returns**
- **Food items**
- **Meat:** 23
- **Fat:** 21
- **Brain:** 1
- **Heart:** 1
- **Intestines:** 2
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a bark scorpion.*

**Giant bark scorpions** are super-sized versions of the common bark scorpion who inhabit savage deserts and some tropical areas. While the original critters are some of the smallest in the game, their giant cousins are 3 times the size of a dwarf, weigh about as much as a troll. While they don't go out of their way to hunt dwarves, they are carnivorous and will attack when provoked by snatching with their pincers and stinging enemies with their stinger tails, injecting a venom which causes pain to the victim. Giant bark scorpions are large enough for this venom to quickly knock dwarves out cold, leaving them vulnerable to a finishing blow to the head. Additionally, the creatures are immune to pain themselves, as well as unaffected by stunning, fear or paralysis effects. All giant bark scorpions possess Legendary skill in climbing.

Giant bark scorpions may be captured in cage traps and trained into pets, possessing the standard high value of savage animals. They are born adults, fully-sized right at birth, and can't be fully tamed. Their many limbs translate to a fairly high amount of returns when butchered, and while the idea of breeding them for the purpose of fortress defense is attractive, the creatures may die of old age at anywhere from 10 to just 2 years of age, making them unpredictable in reliability. They are exotic mounts and may be witnessed being ridden by elves during sieges.

Some dwarves like giant bark scorpions for their *pincers* and their *stinging tail*.

It has enough venom to sting and kill itself by accident.

    [CREATURE:GIANT_BARK_SCORPION]
        [COPY_TAGS_FROM:BARK_SCORPION]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:bark scorpion]
            [CVCT_REPLACEMENT:giant bark scorpion]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:bark scorpion]
            [CVCT_REPLACEMENT:giant bark scorpion]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:bark scorpion]
            [CVCT_REPLACEMENT:giant bark scorpion]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:BARK_SCORPION]
            [CVCT_REPLACEMENT:GIANT_BARK_SCORPION]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:6667367]
        [GO_TO_START]
        [NAME:giant bark scorpion:giant bark scorpions:giant bark scorpion]
        [CASTE_NAME:giant bark scorpion:giant bark scorpions:giant bark scorpion]
        [DESCRIPTION:A huge monster in the form of a bark scorpion.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:pincers]
        [PREFSTRING:stinging tail]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
