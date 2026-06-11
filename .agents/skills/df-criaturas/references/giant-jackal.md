# Giant jackal

> Fonte: [Giant jackal](https://dwarffortresswiki.org/index.php/Giant_jackal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant jackals for their resourceful nature.**
- **Biome**
- **Tropical Shrubland Tropical Savanna Tropical Grassland**
- **Variations**
- **Jackal - Jackal man - Giant jackal**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 30,600 cm 3
- **Mid:** 153,000 cm 3
- **Max:** 306,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-15
- **Butchering returns ( Value multiplier ×2)**
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

*A large monster in the form of a jackal.*

**Giant jackals** are the giant cousin of the jackal, appearing very rarely in savage tropical shrublands, grasslands and savannas, in packs of 1-5 individuals. Giant jackals are more than 20 times the size of normal ones, the size of an elk or a donkey, and thus a minor threat to your dwarves. Armored militia should be able to take them down with relative ease, though. If you've ever dealt with giant dingos, giant jackals are both slightly smaller than these, and come in smaller packs.

Products made from giant jackal parts are worth twice more than those made from common animals.

Giant jackals are exotic mounts, and may as such appear in elven sieges.

Some dwarves like giant jackals for their *resourceful nature*.

Its bark is just as deadly as its bite.

    [CREATURE:GIANT_JACKAL]
        [COPY_TAGS_FROM:JACKAL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2040]
        [GO_TO_START]
        [NAME:giant jackal:giant jackals:giant jackal]
        [CASTE_NAME:giant jackal:giant jackals:giant jackal]
        [GENERAL_CHILD_NAME:giant jackal pup:giant jackal pups]
        [DESCRIPTION:A large monster in the form of a jackal.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:5]
        [CREATURE_TILE:'J']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:resourceful nature]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
