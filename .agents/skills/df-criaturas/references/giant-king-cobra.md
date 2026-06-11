# Giant king cobra

> Fonte: [Giant king cobra](https://dwarffortresswiki.org/index.php/Giant_king_cobra) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant king cobras for their charming hood.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **King cobra - King cobra man - Giant king cobra**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 161.44 cm 3
- **Mid:** 121,080 cm 3
- **Max:** 242,160 cm 3
- **Food products**
- **Eggs:** 10-30
- **Age**
- **Adult at:** Birth
- **Max age:** 15-25
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 10
- **Fat:** 3
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2
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
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a king cobra.*

This is one brutal cobra. It will dismember your dwarves, beware!

While almost 1/4 larger than the formidable grizzly bear, **giant king cobras** provide only slightly more meat than a pig; however, this doesn't affect their viability for a meat industry as their products are still worth 2x value, they have a considerable clutch size of 10-30, and they are mature at birth, meaning that despite low returns per butcher, after just a couple of generations you could potentially have a cobra-splosion.

Their true value, though, lies more in their use as guard animals, thanks to their incredibly powerful syndrome, which causes complete full body paralysis. Despite being considerably less sturdy than bears, due to both their long, slender bodies and their inability to be trained for war, the giant cobra's viability as a war animal far exceeds many mammals, as they are also incredibly expendable due to maturing instantly and laying large amounts of eggs, while their lack of other limbs means they rely almost entirely on biting, increasing the chance of inflicting their syndrome.

Some dwarves like giant king cobras for their *charming hoods*.

    [CREATURE:GIANT_KING_COBRA]
        [COPY_TAGS_FROM:KING_COBRA]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:king cobra]
            [CVCT_REPLACEMENT:giant king cobra]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:king cobra]
            [CVCT_REPLACEMENT:giant king cobra]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:king cobra]
            [CVCT_REPLACEMENT:giant king cobra]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:KING_COBRA]
            [CVCT_REPLACEMENT:GIANT_KING_COBRA]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:4036]
        [GO_TO_START]
        [NAME:giant king cobra:giant king cobras:giant king cobra]
        [CASTE_NAME:giant king cobra:giant king cobras:giant king cobra]
        [DESCRIPTION:A large monster in the shape of a king cobra.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'K']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:charming hood]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
