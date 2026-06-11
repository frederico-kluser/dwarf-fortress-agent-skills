# Giant spider monkey

> Fonte: [Giant spider monkey](https://dwarffortresswiki.org/index.php/Giant_spider_monkey) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant spider monkeys for their prehensile tails.**
- **Biome**
- **Tropical Moist Broadleaf Forest Tropical Dry Broadleaf Forest**
- **Variations**
- **Spider monkey - Spider monkey man - Giant spider monkey**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 25,984.5 cm 3
- **Mid:** 129,922.5 cm 3
- **Max:** 259,845 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 20-30
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

*A large monster in the form of a spider monkey.*

Good thing it doesn't spit webs.\
*Art by Aert Schouman, 1764*

    [CREATURE:GIANT_SPIDER_MONKEY]
        [COPY_TAGS_FROM:SPIDER_MONKEY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:3057]
        [GO_TO_START]
        [NAME:giant spider monkey:giant spider monkeys:giant spider monkey]
        [CASTE_NAME:giant spider monkey:giant spider monkeys:giant spider monkey]
        [DESCRIPTION:A large monster in the form of a spider monkey.]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:1:6]
        [CREATURE_TILE:'M']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:long limbs]
        [PREFSTRING:prehensile tails]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:900:750:600:439:1900:2900] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
