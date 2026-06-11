# Giant saltwater crocodile

> Fonte: [Giant saltwater crocodile](https://dwarffortresswiki.org/index.php/Giant_saltwater_crocodile) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant saltwater crocodiles for their strength.**
- **Biome**
- **Tropical Freshwater Swamp Tropical Freshwater Marsh Tropical Saltwater Swamp Tropical Saltwater Marsh Mangrove Swamp Tropical Saltwater River Tropical Brackish River Tropical Freshwater River**
- **Variations**
- **Saltwater crocodile - Saltwater crocodile man - Giant saltwater crocodile**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 483 cm 3
- **Mid:** 3,220,000 cm 3
- **Max:** 6,440,000 cm 3
- **Food products**
- **Eggs:** 20-70
- **Age**
- **Adult at:** 3
- **Max age:** 60-100
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 174
- **Fat:** 62
- **Brain:** 7
- **Heart:** 3
- **Lungs:** 14
- **Intestines:** 23
- **Liver:** 7
- **Kidneys:** 6
- **Tripe:** 7
- **Sweetbread:** 3
- **Eyes:** 2
- **Spleen:** 3
- **Raw materials**
- **Bones:** 98
- **Skull:** 1
- **Skin:** Scales
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a saltwater crocodile.*

**Giant saltwater crocodiles** are the much larger giant cousins of the saltwater crocodile who can be found in savage tropical wetlands. At over 6 tons, they are among the largest creatures in savage environments, being only slightly smaller than a cyclops, and they know well how to use their massive size; a dwarf caught by a giant saltwater crocodile has a good chance of being torn to shreds in seconds, and they are eager to scare civilians or inexperienced soldiers into the water for an even quicker death. If you are having trouble with giant saltwater crocs, fight them with the most well equipped and experienced members of your military, or use cage traps.

These monsters may be worth more alive, however. While their pet value is actually lower than that of their normal counterparts (500 vs 700), if the player manages to capture and train them, giant saltwater crocodiles are *the* best egg-layers in the entire game; not only do they lay a staggering amount of eggs for egg production (20 to 70 each time), the crocs may also be hatched and butchered into a colossal source of meat, bones and prepared organs. An adult giant saltwater towers over a jabberer, and if used as a fortress defense force, the goblin rabble will only be able to match your beasts by employing cave dragons.

Some dwarves like giant saltwater crocodiles for their *strength*.

    [CREATURE:GIANT_CROCODILE_SALTWATER]
        [COPY_TAGS_FROM:CROCODILE_SALTWATER]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:805]
        [GO_TO_START]
        [NAME:giant saltwater crocodile:giant saltwater crocodiles:giant saltwater crocodile]
        [CASTE_NAME:giant saltwater crocodile:giant saltwater crocodiles:giant saltwater crocodile]
        [GENERAL_CHILD_NAME:giant saltwater crocodile hatchling:giant saltwater crocodile hatchlings]
        [DESCRIPTION:A huge monster in the shape of a saltwater crocodile.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [CREATURE_TILE:'C']
        [COLOR:2:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:strength]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:1683:1315:947:516:2800:4100] 17 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:714:529:303:1900:2900]
