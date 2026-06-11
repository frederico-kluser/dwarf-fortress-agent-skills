# Giant leech

> Fonte: [Giant leech](https://dwarffortresswiki.org/index.php/Giant_leech) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant leeches for their feeding habits.**
- **Biome**
- **Any Lake Any Lake**
- **Variations**
- **Leech - Leech man - Giant leech**
- **Attributes**
- **Alignment:** Savage
- **Genderless · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,700 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 5-10
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 2
- **Brain:** 1
- **Heart:** 1
- **Intestines:** 1-2
- **Raw materials**
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a leech.*

**Giant leeches** are super-sized versions of the common leech, who inhabit savage pools and lakes. While their original counterparts are just vermin, these creatures are over 3 times larger than a dwarf. They spawn individually and are not particularly aggressive, but are not benign and will attack other creatures (including dwarves) who provoke them, potentially killing them. However, due to their lack of bones, they are fairly vulnerable to damage and can be killed rather easily. Being bitten by a giant leech may cause it to suck some blood out of the victim.

Giant leeches can be captured in cage traps and trained into pets, possessing the standard giant creature pet value. They are born adults and cannot be permanently tamed. Due to their lack of limbs, they produce very few products when butchered, making them a subpar choice for a meat industry despite being born instantly fully-sized. They are exotic mounts and may be witnessed being ridden by elves during sieges.

Some dwarves like giant leeches for their *feeding habits*.

**Good news:** It doesn't want blood.\
**Bad news:** It wants more than that...

    [CREATURE:GIANT_LEECH]
        [COPY_TAGS_FROM:LEECH]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:200700]
        [GO_TO_START]
        [NAME:giant leech:giant leeches:giant leech]
        [CASTE_NAME:giant leech:giant leeches:giant leech]
        [DESCRIPTION:A large monster in the shape of a leech.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'L']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:feeding habits]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
