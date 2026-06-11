# Giant moose

> Fonte: [Giant moose](https://dwarffortresswiki.org/index.php/Giant_moose) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant moose for their great size.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Moose - Moose man - Giant moose**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 1,000
- **Not hunting/war trainable**
- **Size**
- **Birth:** 255,465 cm 3
- **Mid:** 2,128,875 cm 3
- **Max:** 4,257,750 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 60-86
- **Fat:** 20-26
- **Brain:** 4
- **Heart:** 2
- **Lungs:** 8
- **Intestines:** 12
- **Liver:** 4
- **Kidneys:** 4
- **Tripe:** 4
- **Sweetbread:** 2
- **Eyes:** 2
- **Spleen:** 2
- **Raw materials**
- **Bones:** 40-44
- **Skull:** 1
- **Teeth:** 1
- **Hooves:** 4-8
- **Horns:** 2 (males only)
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster the shape of a moose.*

After the elephant and the ogre, the male **giant moose** is the third largest land-based, above ground, non-amphibious, non-megabeast, non-semi-megabeast creature in the game (almost *71* times as large as an average dwarf). This species takes savage giganticism to an extreme: they are fully eight times the size of a regular moose, and giant moose bulls being nearly twice as large as giant moose cows. In addition to their size, giant moose bulls also have two antlers which they use to great effect in combat. Giant moose can often be found roaming savage forests alone, though they may also appear as dreadfully effective mounts during a siege.

Giant moose have a pet value double that of most other "giant" pattern creatures, but when tamed they require an extremely large pasture to survive. While giant moose cows are barely tenable, giant bull mooses are almost impossible to keep alive, and can barely manage to feed themselves given ideal pastureland. Their butchery meat products are understandably large in number; of course ambushers have a hard time taking one down alone, so if you see one in the wild send your best crossbow squad to pincushion it and then bring the corpse home for butchering.

Some dwarves like giant moose for their *great size* and their *broad antlers*.

    [CREATURE:MOOSE, GIANT]
        [COPY_TAGS_FROM:MOOSE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:811]
        [GO_TO_START]
        [NAME:giant moose:giant moose:giant moose]
        [GENERAL_CHILD_NAME:giant moose calf:giant moose calves]
        [DESCRIPTION:A huge monster the shape of a moose.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'M']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:1000]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:giant moose cow:giant moose cows:giant moose cow]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:giant moose bull:giant moose bulls:giant moose bull]
        [SELECT_CASTE:ALL]
        [PREFSTRING:great size]
        [PREFSTRING:broad antlers]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
