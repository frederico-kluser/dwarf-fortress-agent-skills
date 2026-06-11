# Giant giraffe

> Fonte: [Giant giraffe](https://dwarffortresswiki.org/index.php/Giant_giraffe) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant giraffes for their hump.**
- **Biome**
- **Tropical Savanna Tropical Shrubland**
- **Variations**
- **Giraffe - Giraffe man - Giant giraffe**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 803,000 cm 3
- **Mid:** 4,015,000 cm 3
- **Max:** 8,030,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 25-30
- **Butchering returns ( Value multiplier ×5)**
- **Food items**
- **Meat:** 150-223
- **Fat:** 41-58
- **Brain:** 6-10
- **Heart:** 3-5
- **Lungs:** 12-20
- **Intestines:** 20-30
- **Liver:** 6-10
- **Kidneys:** 6-10
- **Tripe:** 6-10
- **Sweetbread:** 3-5
- **Eyes:** 2
- **Spleen:** 3-5
- **Raw materials**
- **Bones:** 70-102
- **Skull:** 1
- **Teeth:** 1
- **Horns:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster the shape of a giraffe.*

**Giant giraffes** are gargantuan versions of the giraffe, a long-necked grazer found roaming savage tropical savannas and shrublands. Being a giant creature, giant giraffes provide an absurd amount of (extremely valuable, being 5x the value of common domestic animals) butchering returns, but also are an animal that you do not want agitated.

Giant giraffes also make decent exotic pets, but their real value lies as a staple of the meat industry.

Due to an error, giant giraffes walk far slower than they can stroll. Their strolling speed is equal to 60 kph, much greater than either their trot or canter speed. As a consequence, giant giraffes are very difficult to chase, as they will never get tired from maintaining this speed. They may also sneak at this speed without suffering penalty to their stealth, but will likely never abuse this in game.

Some dwarves like giant giraffes for their *hump*. They are notable for having a different prefstring than their base animal.

    [CREATURE:GIANT_GIRAFFE]
        [COPY_TAGS_FROM:GIRAFFE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:803]
        [GO_TO_START]
        [NAME:giant giraffe:giant giraffes:giant giraffe]
        [CASTE_NAME:giant giraffe:giant giraffes:giant giraffe]
        [GENERAL_CHILD_NAME:giant giraffe calf:giant giraffe calves]
        [DESCRIPTION:A huge monster the shape of a giraffe.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [CREATURE_TILE:'G']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:hump]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:438:292:146:1900:2900] 60 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
