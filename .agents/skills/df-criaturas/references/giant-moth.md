# Giant moth

> Fonte: [Giant moth](https://dwarffortresswiki.org/index.php/Giant_moth) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant moths for their coloration.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Moth - Moth man - Giant moth**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount**
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
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a moth.*

Despite differences in real life, in *Dwarf Fortress*, the **giant moth** is physically exactly like a giant thrips. It, too, lacks any attacks besides pushing. It has the same size, same bodyparts, same wrestling ability, same flying tag and same wings. These giant variations are even more similar to each other than their normal-sized types are; normal moths are significantly faster than normal thrips, but the giant varieties have the same speed. Even though it is quite fast, it is still not much of a threat. It is good for food and marksdwarf training, but not much else. They are also very short-lived, like all the other giant insects.

Some dwarves like giant moths for their *coloration*.

Still not the worst thing those two humans have seen.\
*Art by Josh Guglielmo*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Rumours of intelligent, Megabeast-sized giant moths with a hatred for 3-headed Hydras and a tendancy to team up with giant saltwater crocodiles remain, to this day, uncomfirmed.

    [CREATURE:GIANT_MOTH]
        [COPY_TAGS_FROM:MOTH]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant moth:giant moths:giant moth]
        [CASTE_NAME:giant moth:giant moths:giant moth]
        [DESCRIPTION:A large monster in the form of a moth.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'M']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
