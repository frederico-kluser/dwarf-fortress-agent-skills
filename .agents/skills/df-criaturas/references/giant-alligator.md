# Giant alligator

> Fonte: [Giant alligator](https://dwarffortresswiki.org/index.php/Giant_alligator) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant alligators for their strength.**
- **Biome**
- **Temperate Freshwater Swamp Temperate Freshwater Marsh Tropical Freshwater Swamp Tropical Freshwater Marsh Temperate Freshwater River Tropical Freshwater River Temperate Brackish River Tropical Brackish River**
- **Variations**
- **Alligator - Alligator man - Giant alligator**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 490.2 cm 3
- **Mid:** 1,634,000 cm 3
- **Max:** 3,268,000 cm 3
- **Food products**
- **Eggs:** 10-30
- **Age**
- **Adult at:** 1
- **Max age:** 60-100
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 83
- **Fat:** 37
- **Brain:** 3
- **Gizzard:** 3
- **Heart:** 1
- **Lungs:** 6
- **Intestines:** 9
- **Liver:** 3
- **Kidneys:** 2
- **Tripe:** 3
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 53
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Scales
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of an alligator.*

**Giant alligators** are immense counterparts of the common alligator found in many savage rivers and swamps. They are over 8 times bigger than their normal cousins, making them over 54 times more massive than a dwarf; straying too close to these beasts will lead to your civilians being reduced to mincemeat. If confronted by giant alligators, a competent military and traps are a must. Take caution when fighting them near water, however, as they may cause dwarves to fall into it, where death by drowning is all but inevitable, if the alligator doesn't outright murder them.

While dangerous, giant alligators may be more valuable alive than dead. While their pet value is actually lower than that of their normal counterparts (500 vs 650), if the player manages to capture and train them, giant alligators make some of the best egg-layers in the whole game; they possess all the good things about normal alligators combined with being *much* larger, meaning they give many more returns when butchered. A giant alligator farm will provide a fortress with food, valuable crafting materials and a force of big, mean, water-dwelling defenders.

Some dwarves like giant alligators for their *strength*.

What part of "No Swimming!" was not clear on the sign?

    >[CREATURE:GIANT_ALLIGATOR]
        [COPY_TAGS_FROM:ALLIGATOR]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:817]
        [GO_TO_START]
        [NAME:giant alligator:giant alligators:giant alligator]
        [CASTE_NAME:giant alligator:giant alligators:giant alligator]
        [GENERAL_CHILD_NAME:giant alligator hatchling:giant alligator hatchlings]
        [DESCRIPTION:A huge monster in the shape of an alligator.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [CREATURE_TILE:'A']
        [COLOR:2:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:strength]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:1422:1127:831:488:2500:3700] 18 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:3251:2446:1640:798:4600:6500]
