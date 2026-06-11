# Giant badger

> Fonte: [Giant badger](https://dwarffortresswiki.org/index.php/Giant_badger) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant badgers for their great size.**
- **Biome**
- **Taiga Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Badger - Badger man - Giant badger**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 30,600 cm 3
- **Mid:** 153,000 cm 3
- **Max:** 306,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns**
- **Food items**
- **Meat:** 15
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
- **Teeth:** 2

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster the shape of a badger. It is ferocious in combat.*

**Giant badgers** are giant animal variants of the common badger, found in a wide variety of savage biomes. Like the regular badger, these animals are prone to rage and may randomly flip out in a berserk fury, very much badgering anything unfortunate enough to cross their path. Giant badgers are roughly the size of an elk, or 5 times larger than a dwarf, and as such will make quick work of civilians and a poorly trained, poorly equipped militia. Like their common cousins, they also tend to spawn in large clusters of 4-12 individuals, making them exponentially more dangerous if multiple badgers decide to get peeved together close to your dwarves or especially if the local badger population is agitated.

Giant badgers can be captured in cage traps and trained into exotic pets, possessing the default giant animal value. Their large size translates into a good amount of products if they are butchered, and you may also be inclined to use these huge, angry mustelids in your fortress defense. Like all giant animals, they are considered exotic mounts.

Some dwarves like giant badgers for their *underground communities* and their *striped faces*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Giant badgers used to be the king of beasts of 0.31.25 due to appearing frequently in temperate biomes and ripping apart young fortresses mercilessly. Now they are noticeably less common.

Giant badgers spawn in small groups of 4-12 individuals, apparently harmless - but this is merely a facade. As fury takes them, they will fall unto your fortress in a fury of claws and teeth.

Be warned. They are still here. Lurking.

Humans and their effective mounts.

    [CREATURE:BADGER, GIANT]
        [COPY_TAGS_FROM:BADGER]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2040]
        [GO_TO_START]
        [NAME:giant badger:giant badgers:giant badger]
        [GENERAL_CHILD_NAME:giant badger cub:giant badger cubs]
        [DESCRIPTION:A huge monster the shape of a badger.  It is ferocious in combat.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:4:12]
        [CREATURE_TILE:'B']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:giant badger boar:giant badger boars:giant badger boar]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:giant badger sow:giant badger sows:giant badger sow]
        [SELECT_CASTE:ALL]
        [PREFSTRING:great size]
        [PREFSTRING:underground communities]
        [PREFSTRING:striped faces]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
