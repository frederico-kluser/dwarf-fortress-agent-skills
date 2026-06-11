# Giant gila monster

> Fonte: [Giant gila monster](https://dwarffortresswiki.org/index.php/Giant_gila_monster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant gila monsters for their venomous bite.**
- **Biome**
- **Any Desert**
- **Variations**
- **Gila monster - Gila monster man - Giant gila monster**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount · Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 3,210.3 cm 3
- **Mid:** 107,010 cm 3
- **Max:** 214,020 cm 3
- **Food products**
- **Eggs:** 2-12
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 13
- **Fat:** 12
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
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge beast in the form of a gila monster.*

**Giant gila monsters** are over one hundred times larger than normal gila monsters and produce more food - sadly, not 100 times as much food. Gila monsters lie between a tiger and a lion in size, and are not aggressive, so can be hunted for food: they do have a *mostly* harmless bite however, causing mild pain and swelling. They only appear one a time, however, and so cannot easily be made into the founding members of an exotic egg farm. Some dwarves prefer them for their "venomous bite" and "coloration".

## In Real Life

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Giant Gila Monsters were thought not to exist until a gripping film of an attack in the American midwest in 1959 revealed that they did exist and that they look an awful lot like regular Gila Monsters crawling on a model train set.

Contrary to stories told by human bards, giant gila monsters cannot be summoned by necromancers, nor can they turn into winged, fire breathing forgotten beasts after consuming enough of them

"The bad movie version was scarier."\
  —Urist Notteimprest\
*Art by Devilingo*

    [CREATURE:GIANT_GILA_MONSTER]
        [COPY_TAGS_FROM:GILA_MONSTER]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:gila monster]
            [CVCT_REPLACEMENT:giant gila monster]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:gila monster]
            [CVCT_REPLACEMENT:giant gila monster]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:gila monster]
            [CVCT_REPLACEMENT:giant gila monster]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:GILA_MONSTER]
            [CVCT_REPLACEMENT:GIANT_GILA_MONSTER]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:10701]
        [GO_TO_START]
        [NAME:giant gila monster:giant gila monsters:giant gila monster]
        [CASTE_NAME:giant gila monster:giant gila monsters:giant gila monster]
        [GENERAL_CHILD_NAME:giant gila monster hatchling:giant gila monster hatchlings]
        [DESCRIPTION:A huge beast in the form of a gila monster.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'G']
        [COLOR:4:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:venomous bite]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
