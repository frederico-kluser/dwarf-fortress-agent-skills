# Giant horseshoe crab

> Fonte: [Giant horseshoe crab](https://dwarffortresswiki.org/index.php/Giant_horseshoe_crab) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant horseshoe crabs for their ability to hide in sand.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Horseshoe crab - Horseshoe crab man - Giant horseshoe crab**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 214,020 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 20-40
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 2
- **Brain:** 1
- **Heart:** 1
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a horseshoe crab.*

**Giant horseshoe crabs** are 100 times the size of regular horseshoe crabs, making them slightly larger than a llama. Giant horseshoe crabs are amphibious creatures found in ocean biomes, and are normally non-threatening. Theoretically, giant horseshoe crabs could appear as mounts during a siege, however no ocean-inhabiting civilization exists to ride them into battle.

Giant horseshoe crabs can be tamed as exotic pets, though their pet value is the same as most other giant creatures. Some dwarves prefer giant horseshoe crabs for their ability to hide in sand.

Unlike their smaller cousins, giant horseshoe crabs make for poor training partners in adventure mode, being too flimsy to last long as punching bags, too large for an unskilled wrestler to restrain, and massive enough that their pushes will crush limbs and mangle joints if they connect.

You don't want to see the ugliness underneath.\
*Photographed by PBS*

    [CREATURE:GIANT_HORSESHOE_CRAB]
        [COPY_TAGS_FROM:HORSESHOE_CRAB]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:10701]
        [GO_TO_START]
        [NAME:giant horseshoe crab:giant horseshoe crabs:giant horseshoe crab]
        [CASTE_NAME:giant horseshoe crab:giant horseshoe crabs:giant horseshoe crab]
        [DESCRIPTION:A huge monster in the form of a horseshoe crab.]
        [POPULATION_NUMBER:250:500]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'C']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ability to hide in sand]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
