# Giant lion

> Fonte: [Giant lion](https://dwarffortresswiki.org/index.php/Giant_lion) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant lions for their roars.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland**
- **Variations**
- **Lion - Lion man - Giant lion**
- **Attributes**
- **Alignment:** Savage
- **War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 170,000 cm 3
- **Mid:** 850,000 cm 3
- **Max:** 1,700,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 20
- **Fat:** 17
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
- **Bones:** 21
- **Skull:** 1
- **Teeth:** 2

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A gigantic version of the feline predator. Its giant prides can be found in the wildest, most savage parts of the world.*

**Giant lions** are strong, carnivorous animals found in savage tropical areas. They often appear in small hunting groups of 2-3 animals. Giant lions are much larger than many other "giant" creatures, growing to more than 8 times the size of a regular lion, or slightly more than 1/3 the size of an elephant. Occasionally, giant lions may appear as mounts during a siege. Their chief advantage over the larger giant tiger and giant polar bear is their much greater speed.

Giant lions can be captured and tamed by an animal trainer. Although they have a rather low pet value (*of 500, to be exact*), their butchering products are 4 times as valuable as common animals. Once tamed, they may also be trained for hunting or war. Because of their value, size, and utility, giant lions can prove quite useful to your fortress if you can secure a breeding pair.

Curiously, dwarves only admire giant lions for their *roars*.

Legend has it that your problems are permanently over when encountering these.\
*Art by kruggsmash*

    [CREATURE:GIANT_LION]
        [COPY_TAGS_FROM:LION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:850]
        [GO_TO_START]
        [NAME:giant lion:giant lions:giant lion]
        [CASTE_NAME:giant lion:giant lions:giant lion]
        [GENERAL_CHILD_NAME:giant lion cub:giant lion cubs]
        [DESCRIPTION:A gigantic version of the feline predator.  Its giant prides can be found in the wildest, most savage parts of the world.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [CREATURE_TILE:'L']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:roars]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:327:218:109:1900:2900] 80 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
