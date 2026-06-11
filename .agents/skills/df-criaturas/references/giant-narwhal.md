# Giant narwhal

> Fonte: [Giant narwhal](https://dwarffortresswiki.org/index.php/Giant_narwhal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant narwhals for their horns.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Narwhal - Narwhal man - Giant narwhal**
- **Attributes**
- **Alignment:** Savage
- **Aquatic**
- **Tamed Attributes**
- **Pet value:** 2,000
- **Not hunting/war trainable**
- **Size**
- **Birth:** 962,400 cm 3
- **Mid:** 4,812,000 cm 3
- **Max:** 9,624,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 40-50
- **Butchering returns**
- **Food items**
- **Meat:** 250-320
- **Fat:** 59-65
- **Brain:** 20-30
- **Heart:** 10-15
- **Lungs:** 40-55
- **Intestines:** 60-85
- **Liver:** 20-30
- **Kidneys:** 20-30
- **Tripe:** 20-30
- **Sweetbread:** 10-15
- **Eyes:** 2
- **Spleen:** 10-15
- **Raw materials**
- **Bones:** 55-80
- **Skull:** 1
- **Ivory:** 20-30
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

*A huge sea monster with an enormous horn on its nose.*

A bigger version of its smaller cousin. More dangerous and may gore dwarves with its horn.

    [CREATURE:NARWHAL, GIANT]
        [COPY_TAGS_FROM:NARWHAL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:802]
        [GO_TO_START]
        [NAME:giant narwhal:giant narwhals:giant narwhal]
        [CASTE_NAME:giant narwhal:giant narwhals:giant narwhal]
        [GENERAL_CHILD_NAME:giant narwhal calf:giant narwhal calves]
        [DESCRIPTION:A huge sea monster with an enormous horn on its nose.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'N']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:2000]
        [GO_TO_END]
        [PREFSTRING:horns]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:691:482:251:1900:2900]
