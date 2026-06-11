# Giant wren

> Fonte: [Giant wren](https://dwarffortresswiki.org/index.php/Giant_wren) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant wrens for their intricate songs.**
- **Biome**
- **Any Forest Any Grassland Any Savanna Any Shrubland Any Wetland Any Desert**
- **Variations**
- **Wren - Wren man - Giant wren**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 25,035 cm 3
- **Max:** 200,280 cm 3
- **Food products**
- **Eggs:** 3-10
- **Age**
- **Adult at:** 1
- **Max age:** 5-7
- **Butchering returns**
- **Food items**
- **Meat:** 17
- **Fat:** 11
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 24
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a wren.*

**Giant wrens** are massive flying creatures that appear in most savage biomes rather frequently. Much larger than a normal wren and nearly four times the size of the average dwarf, they will scare livestock and cause constant job cancellation spam whenever they appear in the surface, but unlike other more aggressive flying giants, they are benign and will avoid actually harming your civilians. They are considered exotic mounts, so you may see elves riding them into battle in the event of a siege.

They are handy for the production of meat, bones and tallow thanks to their great size. Being birds, they can be tamed and will lay delicious eggs if a nest box is provided. Both of these make them a colossal boon for a highly populated fortress.

Some dwarves like giant wrens for their *intricate songs*.

    [CREATURE:GIANT_WREN]
        [COPY_TAGS_FROM:BIRD_WREN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:500700]
        [GO_TO_START]
        [NAME:giant wren:giant wrens:giant wren]
        [CASTE_NAME:giant wren:giant wrens:giant wren]
        [GENERAL_CHILD_NAME:giant wren hatchling:giant wren hatchlings]
        [DESCRIPTION:A huge monster in the form of a wren.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'W']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:intricate songs]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
