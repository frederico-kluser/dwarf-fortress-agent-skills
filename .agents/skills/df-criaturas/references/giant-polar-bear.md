# Giant polar bear

> Fonte: [Giant polar bear](https://dwarffortresswiki.org/index.php/Giant_polar_bear) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant polar bears for their strength.**
- **Biome**
- **Glacier Tundra**
- **Variations**
- **Polar bear - Polar bear man - Giant polar bear**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals drink · War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 326,800 cm 3
- **Mid:** 1,634,000 cm 3
- **Max:** 3,268,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 83-112
- **Fat:** 39-47
- **Brain:** 3-4
- **Heart:** 1-2
- **Intestines:** 9-13
- **Liver:** 3-4
- **Kidneys:** 2-4
- **Tripe:** 3-4
- **Sweetbread:** 1-2
- **Eyes:** 2
- **Spleen:** 1-2
- **Raw materials**
- **Bones:** 58-70
- **Skull:** 1
- **Teeth:** 3
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a polar bear.*

**Giant polar bears** are colossal predators that can be found in savage tundras and glaciers. Like normal polar bears, they will attempt to steal food and alcohol from stockpiles. A lone dwarf, especially a civilian, stands little chance of stopping a giant polar bear.

Some dwarves like giant polar bears for their *strength*.

Maybe play dead?

    >[CREATURE:GIANT_BEAR_POLAR]
        [COPY_TAGS_FROM:BEAR_POLAR]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:817]
        [GO_TO_START]
        [NAME:giant polar bear:giant polar bears:giant polar bear]
        [CASTE_NAME:giant polar bear:giant polar bears:giant polar bear]
        [GENERAL_CHILD_NAME:giant polar bear cub:giant polar bear cubs]
        [DESCRIPTION:A huge monster in the shape of a polar bear.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'B']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:strength]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
