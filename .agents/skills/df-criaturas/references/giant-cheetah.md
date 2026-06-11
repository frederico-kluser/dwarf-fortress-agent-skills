# Giant cheetah

> Fonte: [Giant cheetah](https://dwarffortresswiki.org/index.php/Giant_cheetah) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant cheetahs for their speed.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland**
- **Variations**
- **Cheetah - Cheetah man - Giant cheetah**
- **Attributes**
- **Alignment:** Savage
- **War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 56,000 cm 3
- **Mid:** 280,000 cm 3
- **Max:** 560,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 14
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
- **Bones:** 17
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A gigantic spotted cat. It is possibly the fastest animal on land and is found in the savage wilds.*

**Giant cheetahs** are massive, strong and carnivorous animals, roaming savage tropical areas. They are roughly 11 times the size of their normal-sized cousins. Baby giant cheetahs are slightly smaller than a standard cow. Giant cheetahs may also appear as mounts during a siege.

Captured giant cheetahs may be tamed and kept as pets, trained for hunting or war, or used as livestock for a meat industry. While they do not produce as much meat as other "giant" creatures, giant cheetah butchering returns are worth four times as much as common domestic animals.

Despite their much greater size, giant cheetahs cannot sprint any faster than normal ones.

Some dwarves like giant cheetahs for their *speed*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
There have been reports of some in the adventurer community vehemently calling night trolls "giant cheetahs" because of how often one that receives a spine-destroying blow from a supposedly prepared and surely winning opponent somehow manages to turn the tide and, soon after, mercilessly beats said adventurer to a pulp or shreds them into ribbons with incredible alacrity, with the fatal injury often ironically being sometimes direct but frequently indirect damage to the spine. Our fortress dwarves have yet to figure out how the label of "giant cheetah" would, at all, make sense in this context.

Like an entire fortress with teeth that can run faster than you.\
*Art by Hillary D Wilson*

    [CREATURE:GIANT_CHEETAH]
        [COPY_TAGS_FROM:CHEETAH]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1120]
        [GO_TO_START]
        [NAME:giant cheetah:giant cheetahs:giant cheetah]
        [CASTE_NAME:giant cheetah:giant cheetahs:giant cheetah]
        [GENERAL_CHILD_NAME:giant cheetah cub:giant cheetah cubs]
        [DESCRIPTION:A gigantic spotted cat.  It is possibly the fastest animal on land and is found in the savage wilds.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'C']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:speed]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:300:200:100:1900:2900] 87+ (120) kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
