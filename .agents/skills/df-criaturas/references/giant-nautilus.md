# Giant nautilus

> Fonte: [Giant nautilus](https://dwarffortresswiki.org/index.php/Giant_nautilus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant nautiluses for their shells.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Nautilus - Nautilus man - Giant nautilus**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Exotic mount · Shell · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 203,500 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 15-20
- **Butchering returns**
- **Food items**
- **Meat:** 4-5
- **Fat:** 2
- **Eyes:** 2
- **Raw materials**
- **Shell:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a nautilus.*

**Giant nautiluses** are roughly 400 times the size of a common vermin nautilus, making them slightly larger than an adult llama. Giant nautiluses are aquatic creatures; they will rarely interact with land-dwelling dwarves. While they could theoretically appear as mounts during a siege, no ocean-inhabiting civilization currently exists to ride them into battle.

*Some dwarves prefer giant nautiluses for their shells, or for their many tentacles*.

## Notes

According to the raws, nautiluses have 90 tentacles, copper-based blood, and a shell (though the tentacles are not yet implemented as part of their body structure).

    [CREATURE:GIANT_NAUTILUS]
        [COPY_TAGS_FROM:NAUTILUS]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:40700]
        [GO_TO_START]
        [NAME:giant nautilus:giant nautiluses:giant nautilus]
        [CASTE_NAME:giant nautilus:giant nautiluses:giant nautilus]
        [DESCRIPTION:A huge monster in the shape of a nautilus.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'N']
        [COLOR:4:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:shells]
        [PREFSTRING:many tentacles]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900]
