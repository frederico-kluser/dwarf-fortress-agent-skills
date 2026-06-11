# Gigantic squid

> Fonte: [Gigantic squid](https://dwarffortresswiki.org/index.php/Gigantic_squid) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gigantic squids for their ability to spray ink.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Squid - Squid man - Gigantic squid**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Horn**
- **Tamed Attributes**
- **Pet value:** 2,000
- **Not hunting/war trainable**
- **Size**
- **Max:** 201,400 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 15
- **Fat:** 10
- **Brain:** 1
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge sea monster the shape of a squid.*

**Gigantic squids** are huge versions of normal squids. Unexpectedly, they are able to move on land for a brief time before air-drowning, so they could surprise fisherdwarves. Along with the gigantic panda and gigantic tortoise, they are the only giant animals that are "gigantic", instead of merely "giant", to avoid confusion with their real-life relatives.

Some dwarves like gigantic squids for their *ability to spray ink*.

Drawing of a beached giant squid.\
*Art by A. L. Clément and E. A. Tilly*

    [CREATURE:GIGANTIC SQUID]
        [COPY_TAGS_FROM:SQUID]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:squid]
            [CVCT_REPLACEMENT:giant squid]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:squid]
            [CVCT_REPLACEMENT:giant squid]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:100700] using the typical formula makes this around the same size or a little smaller than the real life ones
                                so it could be changed when those go in
        [GO_TO_START]
        [NAME:gigantic squid:gigantic squids:gigantic squid]
        [CASTE_NAME:gigantic squid:gigantic squids:gigantic squid]
        [DESCRIPTION:A huge sea monster the shape of a squid.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:2000]
        [GO_TO_END]
        [PREFSTRING:ability to spray ink]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
