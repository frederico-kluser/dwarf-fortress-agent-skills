# Giant stoat

> Fonte: [Giant stoat](https://dwarffortresswiki.org/index.php/Giant_stoat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant stoats for their ability to take down large prey.**
- **Biome**
- **Taiga Tundra**
- **Variations**
- **Stoat - Stoat man - Giant stoat**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,245.05 cm 3
- **Mid:** 101,225.25 cm 3
- **Max:** 202,450.5 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 2-7
- **Butchering returns**
- **Food items**
- **Meat:** 12-13
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
- **Bones:** 12-18
- **Skull:** 1
- **Teeth:** 0-2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a stoat.*

**Giant stoats** are enlarged versions of the common stoat who can be found in savage taigas and tundras. While the regular animal is tiny, their giant cousins are about three times larger than a dwarf, though they possess the same benign disposition which makes them harmless in most cases. Unlike normal stoats, male and female are named the same thing, but the young are still known as *giant stoat kits*.

Giant stoats may be captured in cage traps and trained into pets, possessing the standard value of a savage giant creature. They are large enough to grant food when butchered, giving about the same amount of meat and bones as an alpaca. They're as short-lived as normal stoats, making them poor long-term companions for dwarves.

Some dwarves like giant stoats for their *ability to take down large prey*.

Stoatally different from weasels.\
*Art by Damie_m*

    [CREATURE:GIANT_STOAT]
        [COPY_TAGS_FROM:STOAT]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:57843]
        [GO_TO_START]
        [NAME:giant stoat:giant stoats:giant stoat]
        [CASTE_NAME:giant stoat:giant stoats:giant stoat]
        [GENERAL_CHILD_NAME:giant stoat kit:giant stoat kits]
        [DESCRIPTION:A large monster in the shape of a stoat.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ability to take down large prey]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
