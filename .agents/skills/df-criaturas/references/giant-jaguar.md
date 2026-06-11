# Giant jaguar

> Fonte: [Giant jaguar](https://dwarffortresswiki.org/index.php/Giant_jaguar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant jaguars for their spotted coats.**
- **Biome**
- **Any Tropical Badlands Rocky Wasteland Sand Desert**
- **Variations**
- **Jaguar - Jaguar man - Giant jaguar**
- **Attributes**
- **Alignment:** Savage
- **War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 74,550 cm 3
- **Mid:** 397,600 cm 3
- **Max:** 745,500 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 35-37
- **Fat:** 29
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
- **Bones:** 34
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A gigantic feline predator, similar to its cousins in all but size. It can be found in the savage wilderness.*

**Giant jaguars** are trainable into War/hunting giant jaguars, but are exotic pets. See animal training zone for how this is done.

    [CREATURE:GIANT_JAGUAR]
        [COPY_TAGS_FROM:JAGUAR]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:994]
        [GO_TO_START]
        [NAME:giant jaguar:giant jaguars:giant jaguar]
        [CASTE_NAME:giant jaguar:giant jaguars:giant jaguar]
        [GENERAL_CHILD_NAME:giant jaguar cub:giant jaguar cubs]
        [DESCRIPTION:A gigantic feline predator, similar to its cousins in all but size.  It can be found in the savage wilderness.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'J']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:spotted coats]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:411:274:137:1900:2900] 64 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
