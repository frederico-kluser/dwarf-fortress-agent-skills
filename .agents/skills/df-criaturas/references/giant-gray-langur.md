# Giant gray langur

> Fonte: [Giant gray langur](https://dwarffortresswiki.org/index.php/Giant_gray_langur) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant gray langurs for their vocalizations.**
- **Biome**
- **Any Desert Any Grassland Any Savanna Any Shrubland Any Forest**
- **Variations**
- **Gray langur - Gray langur man - Giant gray langur**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 30,600 cm 3
- **Mid:** 153,000 cm 3
- **Max:** 306,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 30-40
- **Butchering returns**
- **Food items**
- **Meat:** 13-17
- **Fat:** 12-14
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

*A huge monster in the shape of a gray langur.*

**Giant gray langurs** are the giant counterparts of the common gray langur who inhabit most savage biomes, where they appear in loose groups of 5 to 10 individuals. While a normal langur is just a glorified rhesus macaque, a giant langur is 5 times more massive than a dwarf, and their combined size and numbers make them a real threat to unarmed civilians. Much like their normal cousins, giant gray langurs will attempt to steal items and food from your fortress, potentially leading your peasants to be assaulted by a swarm of massive, biting and scratching gray-furred monkeys unless measures are made to defend the fortress. All giant gray langurs are born with Legendary skill in climbing.

Giant gray langurs may be captured in cage traps and trained into valuable pets. They give a respectable amount of returns when butchered and capturing multiple langurs shouldn't be particularly difficult due to them appearing in groups, making them a potential choice for exotic livestock. They are exotic mounts and may be witnessed being ridden by elves during sieges.

Some dwarves like giant gray langurs for their *social nature* and their *vocalizations*.

    [CREATURE:GIANT_GRAY_LANGUR]
        [COPY_TAGS_FROM:GRAY_LANGUR]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2040]
        [GO_TO_START]
        [NAME:giant gray langur:giant gray langurs:giant gray langur]
        [CASTE_NAME:giant gray langur:giant gray langurs:giant gray langur]
        [DESCRIPTION:A huge monster in the shape of a gray langur.]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'L']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:social nature]
        [PREFSTRING:vocalizations]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
