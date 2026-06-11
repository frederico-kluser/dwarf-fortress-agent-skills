# Giant black mamba

> Fonte: [Giant black mamba](https://dwarffortresswiki.org/index.php/Giant_black_mamba) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant black mambas for their aggression.**
- **Biome**
- **Tropical Savanna Tropical Shrubland Any Tropical Forest Any Tropical Swamp**
- **Variations**
- **Black mamba - Black mamba man - Giant black mamba**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,880.8 cm 3
- **Mid:** 117,550 cm 3
- **Max:** 235,100 cm 3
- **Food products**
- **Eggs:** 10-30
- **Age**
- **Adult at:** Birth
- **Max age:** 10-15
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
- **Bones:** 10
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster taking the shape of a black mamba.*

Black mambas are an extremely deadly but small species of venomous snake whose bites to your dwarves cause short term syndromic symptoms including dizziness, drowsiness, strong pain, fever, unconsciousness, complete paralysis, and death by suffocation soon after. **Giant black mambas** keep their basal creature's deadliness, but beef up their size to that of a full-grown tiger. Not only do they have no problem piercing through your dwarves' clothes, they have no problem piercing through most armor either, and may just as well end a bitten goblin spearman's life by crushing his skull as by stopping his lungs. Luckily giant black mambas require 20 years of growth to reach full size, but only live 10 to 20 years, meaning they rarely reach their most imposing size.

In the wild giant black mambas are solitary creatures that normally flee contact, but have a `[PRONE_TO_RAGE:1]` tag in their creature definitions, which means that about 1% of the time they will flip out on anyone they see. Unless that dwarf happens to be a great axedwarf in full steel armor, they probably won't survive the ensuing encounter. Excellent pit creatures, if not one of the most durable creatures of their size - better to not approach them in the wild.

Some dwarves like giant black mambas for their *deadly bite* and their *aggression*.

Has enough venom to kill two giant sperm whales.

    [CREATURE:GIANT_BLACK_MAMBA]
        [COPY_TAGS_FROM:BLACK_MAMBA]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:black mamba]
            [CVCT_REPLACEMENT:giant black mamba]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:black mamba]
            [CVCT_REPLACEMENT:giant black mamba]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:black mamba]
            [CVCT_REPLACEMENT:giant black mamba]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:BLACK_MAMBA]
            [CVCT_REPLACEMENT:GIANT_BLACK_MAMBA]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:4702]
        [GO_TO_START]
        [NAME:giant black mamba:giant black mambas:giant black mamba]
        [CASTE_NAME:giant black mamba:giant black mambas:giant black mamba]
        [DESCRIPTION:A large monster taking the shape of a black mamba.]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:aggression]
        [PREFSTRING:deadly bite]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
