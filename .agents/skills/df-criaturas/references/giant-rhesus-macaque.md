# Giant rhesus macaque

> Fonte: [Giant rhesus macaque](https://dwarffortresswiki.org/index.php/Giant_rhesus_macaque) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant rhesus macaques for their mischief.**
- **Biome**
- **Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Rhesus macaque - Rhesus macaque man - Giant rhesus macaque**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 23,510 cm 3
- **Mid:** 117,550 cm 3
- **Max:** 235,100 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 30-40
- **Butchering returns**
- **Food items**
- **Meat:** 15
- **Fat:** 13
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

*A large monster in the form of a rhesus macaque.*

**Giant rhesus macaques** are much larger, much more fun versions of the normal rhesus macaque; they're as big as a grizzly bear. They have a willingness to steal items, and are much more dangerous in combat. They can be dispatched with a decent military.

Some dwarves like giant rhesus macaques for their *mischief*.

    >[CREATURE:GIANT_MACAQUE_RHESUS]
        [COPY_TAGS_FROM:MACAQUE_RHESUS]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:4702]
        [GO_TO_START]
        [NAME:giant rhesus macaque:giant rhesus macaques:giant rhesus macaque]
        [CASTE_NAME:giant rhesus macaque:giant rhesus macaques:giant rhesus macaque]
        [DESCRIPTION:A large monster in the form of a rhesus macaque.]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'M']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:mischief]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
