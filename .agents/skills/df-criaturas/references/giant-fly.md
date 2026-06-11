# Giant fly

> Fonte: [Giant fly](https://dwarffortresswiki.org/index.php/Giant_fly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant flies for their ability to annoy.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra Any Pool**
- **Variations**
- **Fly - Fly man - Giant fly**
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
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a fly.*

**Giant flies** are the much larger cousins of the common fly, found in just about every savage biome, but mountains, glacier and tundra. They are also supposed to appear in savage pools, but as non-vermin can't spawn in pools, this never happens. Over three times bigger than a dwarf, these insects aren't benign and will defend themselves if provoked. They lack any sort of offensive attack and rely on pushes for self-defense; however, they are large enough to potentially injure a dwarf with such attacks. Additionally, they also can use their wings for wrestling, potentially leading to the absurd circumstance of a dwarf getting throttled to death by overgrown vermin. All giant flies are born full-sized adults, and with Legendary skill in climbing.

Giant flies can be captured in cage traps and trained into pets, possessing the standard high value of giant creatures. Keeping giant flies as long-term fortress pets isn't a good idea, however, due to their exceptionally short lifespan - they only live for one measly year. Any dwarf who adopts them as pets will find them dying very quickly, and their lifespans are too short for a giant fly farm to be viable. The player should instead consider butchering them for food and fat while they can. Giant flies are exotic mounts and can be ridden by elves during sieges.

Some dwarves like giant flies for their *ability to annoy*.

In restaurants, this fly is in *everyone's* soup.

    [CREATURE:GIANT_FLY]
        [COPY_TAGS_FROM:FLY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant fly:giant flies:giant fly]
        [CASTE_NAME:giant fly:giant flies:giant fly]
        [DESCRIPTION:A large monster in the shape of a fly.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'F']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ability to annoy]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
