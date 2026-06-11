# Giant lizard

> Fonte: [Giant lizard](https://dwarffortresswiki.org/index.php/Giant_lizard) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant lizards for their beauty.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Lizard - Lizard man - Giant lizard**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 201,400 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 15
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
- **Bones:** 18
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a lizard.*

**Giant lizards** are super-sized versions of the common lizard who inhabit most savage biomes. While their original counterparts are just vermin, these creatures are over 3 times bigger than a dwarf. They are not particularly aggressive, but are not benign and will attack other creatures (including dwarves) who provoke them, potentially killing them. All giant lizards are born with Legendary skill in climbing.

Giant lizards can be captured in cage traps and trained into pets, possessing the standard giant creature pet value. They are born adults and cannot be permanently tamed. They produce an adequate amount of products when butchered, making them a potential food source. Unlike most reptiles, giant lizards give live birth instead of laying eggs and their offspring are born fully-sized right off the bat. Because they're very short-lived, only living 2 or 3 years at most, giant lizards bred for food should be butchered quickly before they die of old age, while the actual breeding pair will require a certain amount of micromanagement to ensure they're both alive long enough to have children. They are exotic mounts and may be witnessed being ridden by elves during sieges.

Some dwarves like giant lizards for their *beauty*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

In one ancient dwarven story a Giant Lizard rider is found fighting a four armed bio mechanical golem in a hamster wheel. The story and it's previous entries are not looked upon fondly by sane people.

    [CREATURE:GIANT_LIZARD]
        [COPY_TAGS_FROM:LIZARD]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:100700]
        [GO_TO_START]
        [NAME:giant lizard:giant lizards:giant lizard]
        [CASTE_NAME:giant lizard:giant lizards:giant lizard]
        [GENERAL_CHILD_NAME:giant lizard hatchling:giant lizard hatchlings]
        [DESCRIPTION:A huge monster in the shape of a lizard.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'L']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:beauty]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567]
