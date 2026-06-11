# Giant louse

> Fonte: [Giant louse](https://dwarffortresswiki.org/index.php/Giant_louse) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant lice for their ability to infest.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Louse - Louse man - Giant louse**
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
- **Meat:** 17-85
- **Fat:** 15-20
- **Brain:** 3
- **Heart:** 1
- **Intestines:** 10
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a louse.*

Just like normal lice, **giant lice** are not bloodsucking parasites, for now. Giant lice are regular giant ground insects, although they lack an attack other than pushing and wrestling. Like all other insects, their max age is very short. They are lacking \[LARGE_PREDATOR\] token and will mostly leave your dwarves alone.

Found in a giant's hair.\
*Art by Britt Martin*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Considering the size of the normal louse and the size of the giant louse (200,000 times bigger), and, furthermore, that an external parasite must be much, much smaller than its host, one wonders what manner of abnormally colossal, yet unknown beasts this insect sucks the blood of. If the proportionality is still valid, these beasts should be at least ten times the size of an adult dragon.

Giant Lice should not be confused with bankers, which wear suits.

    [CREATURE:GIANT_LOUSE]
        [COPY_TAGS_FROM:LOUSE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant louse:giant lice:giant louse]
        [CASTE_NAME:giant louse:giant lice:giant louse]
        [DESCRIPTION:A huge monster in the shape of a louse.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'L']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ability to infest]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
