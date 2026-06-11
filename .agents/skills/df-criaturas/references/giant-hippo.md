# Giant hippo

> Fonte: [Giant hippo](https://dwarffortresswiki.org/index.php/Giant_hippo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant hippos for their strength.**
- **Biome**
- **Tropical Saltwater River Tropical Brackish River Tropical Freshwater River Tropical Saltwater Lake Tropical Brackish Lake Tropical Freshwater Lake**
- **Variations**
- **Hippo - Hippo man - Giant hippo**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 401,000 cm 3
- **Mid:** 6,015,000 cm 3
- **Max:** 12,030,000 cm 3
- **Age**
- **Adult at:** 5
- **Max age:** 40-50
- **Butchering returns**
- **Food items**
- **Meat:** 232-343
- **Fat:** 65-93
- **Brain:** 11-17
- **Heart:** 5-8
- **Lungs:** 22-34
- **Intestines:** 34-51
- **Liver:** 11-17
- **Kidneys:** 10-16
- **Tripe:** 11-17
- **Sweetbread:** 5-8
- **Eyes:** 2
- **Spleen:** 5-8
- **Raw materials**
- **Skull:** 1
- **Ivory:** 2
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge hippo-shaped monster.*

Some dwarves like giant hippos for their *strength*.

Not even poachers will go near them.\
*Art by Alexander Deruchenko*

    [CREATURE:GIANT_HIPPO]
        [COPY_TAGS_FROM:HIPPO]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:802]
        [GO_TO_START]
        [NAME:giant hippo:giant hippos:giant hippo]
        [CASTE_NAME:giant hippo:giant hippos:giant hippo]
        [GENERAL_CHILD_NAME:giant hippo calf:giant hippo calves]
        [DESCRIPTION:A huge hippo-shaped monster.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [CREATURE_TILE:'H']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:strength]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:4732:4026:3327:1097:5922:7567] 8 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
