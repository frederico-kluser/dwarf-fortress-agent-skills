# Giant beetle

> Fonte: [Giant beetle](https://dwarffortresswiki.org/index.php/Giant_beetle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant beetles for their protective shells.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Beetle - Beetle man - Giant beetle**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 1-1
- **Butchering returns**
- **Food items**
- **Meat:** 42
- **Fat:** 17
- **Brain:** 2
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a beetle.*

**Giant beetles** are the giant animal variant of the common beetle, found in most savage biomes where they appear one at a time. Despite its disposition of being a "giant" creature and being about three times the size of a dwarf, they are benign and will be of no threat to your citizens, fighting back only when forced to with pushes and wrestling. All giant beetles possess Legendary skill in climbing.

Giant beetles can be captured in cage traps and trained into exotic pets, possessing the standard giant creature value. They provide a high amount of meat when butchered thanks to their many legs, but due to only living up to 1 year, they cannot feasibly be used in a meat industry. Like other giant animals, giant beetles are exotic mounts, but their tiny lifespan means this generally sees no use.

Some dwarves like giant beetles for their *protective shells*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Contrary to dwarven legend, giant beetles are (unfortunately) not equipped with horns and cannot grow thick, shaggy beards similar to those of a dwarf's.

They don't make newspapers big enough for that...\
*Art by Herckeim*

    [CREATURE:GIANT_BEETLE]
        [COPY_TAGS_FROM:BEETLE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant beetle:giant beetles:giant beetle]
        [CASTE_NAME:giant beetle:giant beetles:giant beetle]
        [DESCRIPTION:A large monster in the shape of a beetle.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'B']
        [COLOR:4:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:protective shells]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
