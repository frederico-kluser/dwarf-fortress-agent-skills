# Giant rhinoceros

> Fonte: [Giant rhinoceros](https://dwarffortresswiki.org/index.php/Giant_rhinoceros) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant rhinoceroses for their horns.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland**
- **Variations**
- **Rhinoceros - Rhinoceros man - Giant rhinoceros**
- **Attributes**
- **Alignment:** Savage
- **War animals · Grazer · Exotic mount · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : War**
- **Size**
- **Birth:** 2,400,000 cm 3
- **Mid:** 12,000,000 cm 3
- **Max:** 24,000,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 40-50
- **Butchering returns ( Value multiplier ×5)**
- **Food items**
- **Meat:** 443-694
- **Fat:** 122-196
- **Brain:** 22-34
- **Heart:** 11-17
- **Lungs:** 44-68
- **Intestines:** 66-102
- **Liver:** 22-34
- **Kidneys:** 22-34
- **Tripe:** 22-34
- **Sweetbread:** 11-17
- **Eyes:** 2
- **Spleen:** 11-17
- **Raw materials**
- **Bones:** 247-389
- **Skull:** 1
- **Teeth:** 1
- **Horns:** 10-16
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster the shape of a rhinoceros.*

Essentially a double-height rhinoceros. Since regular rhinoceroses are already fearsome, needless to say the giant one is a serious foe, being the seventh largest creature in the game, nearly the size of a fully-grown (thousand-year-old) dragon. They come in groups of 3-7 individuals, and their children are called *giant rhinoceros calves*. If these beasts reside in your dwarves' surroundings, the possibility of having giant rhinoceroses agitated should make you think carefully about the number of trees you cut.

Should you catch one with a cage trap it can be war trained to fight for you. Note, however, that they are grazers that need immense pastures to fill their bellies once they are trained. They can also be butchered for great returns. Being exotic mounts, they can sometimes appear in elven sieges. This is a sign of great !fun! to come.

Some dwarves like giant rhinoceroses for their *horns*.

You can even paint their horns. They're okay with that!

    [CREATURE:GIANT_RHINOCEROS]
        [COPY_TAGS_FROM:RHINOCEROS]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:800]
        [GO_TO_START]
        [NAME:giant rhinoceros:giant rhinoceroses:giant rhinoceros]
        [CASTE_NAME:giant rhinoceros:giant rhinoceroses:giant rhinoceros]
        [GENERAL_CHILD_NAME:giant rhinoceros calf:giant rhinoceros calves]
        [DESCRIPTION:A huge monster the shape of a rhinoceros.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [CREATURE_TILE:'R']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:horns]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
