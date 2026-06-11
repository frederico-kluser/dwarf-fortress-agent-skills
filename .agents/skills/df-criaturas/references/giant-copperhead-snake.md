# Giant copperhead snake

> Fonte: [Giant copperhead snake](https://dwarffortresswiki.org/index.php/Giant_copperhead_snake) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant copperhead snakes for their attractive scale patterns.**
- **Biome**
- **Temperate Broadleaf Forest Any Temperate Swamp**
- **Variations**
- **Copperhead snake - Copperhead snake man - Giant copperhead snake**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Syndrome**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,350 cm 3
- **Mid:** 122,100 cm 3
- **Max:** 203,500 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 6-7
- **Fat:** 3
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 10
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a copperhead snake.*

**Giant copperhead snakes** are the oversized version their smaller cousins. Like most other poisonous snakes, their bites cause a syndrome which lead to short term pain, swelling, and nausea. This significantly increases the snake's effectiveness in combat, but this snake type's bites are not generally fatal.

They produce an underwhelming amount of meat for a creature of their size, and avoid contact with your dwarves unless pressed, so hunters should focus on more profitable or threatening targets first.

Some dwarves enjoy their *attractive scale patterns*.

Each scale pattern is the size of a town.

    [CREATURE:GIANT_COPPERHEAD_SNAKE]
        [COPY_TAGS_FROM:COPPERHEAD_SNAKE]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:copperhead snake]
            [CVCT_REPLACEMENT:giant copperhead snake]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:copperhead snake]
            [CVCT_REPLACEMENT:giant copperhead snake]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:copperhead snake]
            [CVCT_REPLACEMENT:giant copperhead snake]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:COPPERHEAD_SNAKE]
            [CVCT_REPLACEMENT:GIANT_COPPERHEAD_SNAKE]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:40700]
        [GO_TO_START]
        [NAME:giant copperhead snake:giant copperhead snakes:giant copperhead snake]
        [CASTE_NAME:giant copperhead snake:giant copperhead snakes:giant copperhead snake]
        [DESCRIPTION:A huge monster in the form of a copperhead snake.]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:attractive scale patterns]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
