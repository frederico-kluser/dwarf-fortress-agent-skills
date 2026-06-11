# Giant sloth bear

> Fonte: [Giant sloth bear](https://dwarffortresswiki.org/index.php/Giant_sloth_bear) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant sloth bears for their large floppy ears.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Sloth bear - Sloth bear man - Giant sloth bear**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals drink · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 93,300 cm 3
- **Mid:** 466,500 cm 3
- **Max:** 933,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-40
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 35-45
- **Fat:** 28-32
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2-3
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 34-42
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a sloth bear.*

*Not to be confused with giant sloths*

    [CREATURE:GIANT_SLOTH_BEAR]
        [COPY_TAGS_FROM:BEAR_SLOTH]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:933]
        [GO_TO_START]
        [NAME:giant sloth bear:giant sloth bears:giant sloth bear]
        [CASTE_NAME:giant sloth bear:giant sloth bears:giant sloth bear]
        [GENERAL_CHILD_NAME:giant sloth bear cub:giant sloth bear cubs]
        [DESCRIPTION:A huge monster in the form of a sloth bear.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'B']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:large floppy ears]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
