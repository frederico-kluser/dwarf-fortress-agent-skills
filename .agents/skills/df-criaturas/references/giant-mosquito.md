# Giant mosquito

> Fonte: [Giant mosquito](https://dwarffortresswiki.org/index.php/Giant_mosquito) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant mosquitos for their high-pitched buzz.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra Any Pool**
- **Variations**
- **Mosquito - Mosquito man - Giant mosquito**
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
- **Meat:** 40-64
- **Fat:** 15-17
- **Brain:** 2
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a mosquito.*

**Giant mosquitos** are oversized versions of the common mosquito who can be found in any non-freezing savage biome, where they spawn one at a time. They are not inherently aggressive but will attack dwarves who provoke them with bites and wrestling with their wings, which might be dangerous as they're 3 times bigger than dwarves, though their chitin isn't particularly resistant to damage even from peasant punches. As with standard mosquitos, only the females have the ability to suck blood on a bite. All giant mosquitos possess Legendary skill in climbing.

Giant mosquitos may be captured in cage traps and trained into pets, having the standard value of savage giants. They are born adults and may never be rendered fully tame. They only live one year, making them a bad choice for livestock or display, and as such they should be butchered immediately upon training. Elves may sometimes sell fully tame mosquitos, and the creatures may also appear as mounts during an elven siege, where their maneuverability and numbers may make them a substantial threat.

Some dwarves like giant mosquitoes for their *high-pitched buzz* and their *ability to feast on blood*.

*Art by DevBurmak*.

## History

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Giant mosquitoes may have attempted what was the shortest claim at the throne of king of beasts for v0.34.01. Not only could they fly, but *they appeared by the hundreds* (exactly from 100 to 200 at a time), ensuring a large FPS drop to most forts and just plain being deadly in these numbers.

    [CREATURE:GIANT_MOSQUITO]
        [COPY_TAGS_FROM:MOSQUITO]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant mosquito:giant mosquitos:giant mosquito]
        [CASTE_NAME:giant mosquito:giant mosquitos:giant mosquito]
        [DESCRIPTION:A huge monster in the shape of a mosquito.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'M']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:high-pitched buzz]
        [PREFSTRING:ability to feast on blood]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
