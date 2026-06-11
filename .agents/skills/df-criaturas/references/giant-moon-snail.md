# Giant moon snail

> Fonte: [Giant moon snail](https://dwarffortresswiki.org/index.php/Giant_moon_snail) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant moon snails for their predatory nature.**
- **Biome**
- **Temperate Ocean**
- **Variations**
- **Moon snail - Moon snail man - Giant moon snail**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Exotic mount · Shell**
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
- **Meat:** 4-5
- **Fat:** 2
- **Brain:** 1
- **Heart:** 1
- **Intestines:** 1
- **Raw materials**
- **Shell:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a moon snail.*

**Giant moon snails** are much larger than a normal moon snail, roughly the size of an average llama. this can make their push attacks dangerous since they are so much larger than a dwarf. They provide two shells when butchered, which can prove useful during a strange mood.

They dwell in savage temperate ocean biomes. Dwarves can apparently prefer giant moon snails for their predatory nature or their striking coloration.

\

    [CREATURE:GIANT_MOON_SNAIL]
        [COPY_TAGS_FROM:MOON_SNAIL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:100700]
        [GO_TO_START]
        [NAME:giant moon snail:giant moon snails:giant moon snail]
        [CASTE_NAME:giant moon snail:giant moon snails:giant moon snail]
        [DESCRIPTION:A huge monster in the shape of a moon snail.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:4:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:predatory nature]
        [PREFSTRING:striking coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
