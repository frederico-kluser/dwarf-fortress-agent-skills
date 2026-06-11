# Giant kangaroo

> Fonte: [Giant kangaroo](https://dwarffortresswiki.org/index.php/Giant_kangaroo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant kangaroos for their pouches.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Any Desert**
- **Variations**
- **Kangaroo - Kangaroo man - Giant kangaroo**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Milkable · Humanoid**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 85,770 cm 3
- **Mid:** 428,850 cm 3
- **Max:** 857,700 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 25-28
- **Fat:** 16
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 3-4
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 22
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a kangaroo.*

**Giant kangaroos** are oversized cousins of the common kangaroo, found in savage temperate and desert biomes. They are 9 times heavier than their normal cousins and about 14 times heavier than a dwarf, but despite their great size, they are benign and will run away from dwarves who attack them. In the event they fight back, they may deal great damage to civilians, though they'll probably not last long against even an unarmored hunter. Unlike normal kangaroos, males and females are both simply named giant kangaroos, though their babies are referred to as *giant kangaroo joeys*.

Giant kangaroos can be captured in cage traps and trained into pets, possessing the standard value of giant creatures. Their large size means they give a good amount of returns when butchered, and like normal kangaroos, they also serve as a source of milk and later cheese. Note, however, that giant kangaroo milk and normal-sized kangaroo milk are completely identical in every aspect. They are exotic mounts, and so may be used by elves during sieges.

Some dwarves like giant kangaroos for their *pouches* and their *great leaps*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
The methods of riding a giant kangaroo are a matter of discussion among dwarves. Do the elves come hiding inside their pouches, or do the kangaroos give them piggy-back rides? Or, Armok forbid, both? More research is required before conclusions are made.

    [CREATURE:GIANT_KANGAROO]
        [COPY_TAGS_FROM:KANGAROO]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:kangaroo]
            [CVCT_REPLACEMENT:giant kangaroo]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:kangaroo]
            [CVCT_REPLACEMENT:giant kangaroo]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:953]
        [GO_TO_START]
        [NAME:giant kangaroo:giant kangaroos:giant kangaroo]
        [CASTE_NAME:giant kangaroo:giant kangaroos:giant kangaroo]
        [GENERAL_CHILD_NAME:giant kangaroo joey:giant kangaroo joeys]
        [DESCRIPTION:A huge monster in the shape of a kangaroo.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:2:4]
        [CREATURE_TILE:'K']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:pouches]
        [PREFSTRING:great leaps]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
