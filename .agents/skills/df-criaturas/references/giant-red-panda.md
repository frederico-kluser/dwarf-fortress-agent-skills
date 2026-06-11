# Giant red panda

> Fonte: [Giant red panda](https://dwarffortresswiki.org/index.php/Giant_red_panda) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant red pandas for their large striped tails.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Red panda - Red panda man - Giant red panda**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 23,510 cm 3
- **Mid:** 117,550 cm 3
- **Max:** 235,100 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 8-15
- **Butchering returns**
- **Food items**
- **Meat:** 14
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

*A large monster with the shape of a red panda.*

**Giant red pandas** can be found in savage temperate forests and should not be ignored, even if gigantic pandas are available. They have the same great pet value (500), and suffer the same crippling dependence on bamboo. Wild giant red pandas require no food; however, when trained, they subsist solely on bamboo (which generally doesn't exist in sufficient quantity to prevent starvation). Being giant animals, they provide large amounts of meat, though their butchering products are base value. Even though they aren't trainable like gigantic pandas, a herd of giant red pandas will fetch a very good price from any caravan--assuming you can keep them alive long enough to complete the trade.

Admired for their *large striped tails*

    [CREATURE:RED PANDA, GIANT]
        [COPY_TAGS_FROM:RED PANDA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:4702]
        [GO_TO_START]
        [NAME:giant red panda:giant red pandas:giant red panda]
        [GENERAL_CHILD_NAME:giant red panda cub:giant red panda cubs]
        [DESCRIPTION:A large monster with the shape of a red panda.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'P']
        [COLOR:4:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:giant red panda boar:giant red panda boars:giant red panda boar]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:giant red panda sow:giant red panda sows:giant red panda sow]
        [SELECT_CASTE:ALL]
        [PREFSTRING:large striped tails]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:679:458:231:1900:2900] 38 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
