# Giant black bear

> Fonte: [Giant black bear](https://dwarffortresswiki.org/index.php/Giant_black_bear) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant black bears for their strength.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Black bear - Black bear man - Giant black bear**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals drink · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 108,480 cm 3
- **Mid:** 542,400 cm 3
- **Max:** 1,084,800 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 47-49
- **Fat:** 33
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 3-4
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 42
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a black bear.*

**Giant black bears** are the giant animal variant of the common black bear, found in savage taigas and temperate forests. They are solitary creatures, and only three may spawn on a given map. With a [`[LARGE_PREDATOR]`](/index.php/Creature_token#LARGE_PREDATOR "Creature token") token and a willingness to steal food and booze from your stockpiles, these creatures can pose a threat even to well-prepared fortresses, as they are 18 times the size of the average dwarf (roughly the size of a water buffalo).

The best way to prevent them from stealing your food and drink is to use cage traps. Once trapped, these animals can be trained into exotic pets, possessing the default giant animal value. While they can't be trained for war or hunting, they can still make powerful defense animals, especially if they're pastured in the correct area. Like other giant animals, they are considered exotic mounts.

Some dwarves like giant black bears for their *strength*.

"Embarking in this savage biome was *your* idea!"\
*Art by JMKilpatrick*

    >[CREATURE:GIANT_BEAR_BLACK]
        [COPY_TAGS_FROM:BEAR_BLACK]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:904]
        [GO_TO_START]
        [NAME:giant black bear:giant black bears:giant black bear]
        [CASTE_NAME:giant black bear:giant black bears:giant black bear]
        [GENERAL_CHILD_NAME:giant black bear cub:giant black bear cubs]
        [DESCRIPTION:A huge monster in the shape of a black bear.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'B']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:strength]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
