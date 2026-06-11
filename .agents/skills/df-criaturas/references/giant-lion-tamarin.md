# Giant lion tamarin

> Fonte: [Giant lion tamarin](https://dwarffortresswiki.org/index.php/Giant_lion_tamarin) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant lion tamarins for their small size.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Lion tamarin - Lion tamarin man - Giant lion tamarin**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 204,302.4 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-3
- **Butchering returns**
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
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a lion tamarin.*

**Giant lion tamarins** are much larger cousins of the normal lion tamarin found in savage tropical moist broadleaf forests. They are solitary and only spawn one at a time. Being 3 times larger than a dwarf, giant lion tamarins are more than a match for a peasant in combat, but they are benign and will only fight if cornered. All giant lion tamarins possess Legendary skill in climbing and are born adults.

Giant lion tamarins possess the standard high pet value of giant creatures, making them valuable pets if trained. Additionally, they can be used for the meat industry through hunting or if the player manages to capture a breeding pair, though they are noticeably short-lived animals, only living up to 3 years at most - because they're born fully sized, they should be butchered immediately. They are considered exotic mounts, so you may encounter elves riding them into battle in the event of a siege.

Some dwarves like giant lion tamarins for their *small size* and their *manes*.

    [CREATURE:GIANT_LION_TAMARIN]
        [COPY_TAGS_FROM:LION_TAMARIN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:32952]
        [GO_TO_START]
        [NAME:giant lion tamarin:giant lion tamarins:giant lion tamarin]
        [CASTE_NAME:giant lion tamarin:giant lion tamarins:giant lion tamarin]
        [DESCRIPTION:A huge monster in the form of a lion tamarin.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'L']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:small size]
        [PREFSTRING:manes]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
