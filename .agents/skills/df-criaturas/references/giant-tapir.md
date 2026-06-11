# Giant tapir

> Fonte: [Giant tapir](https://dwarffortresswiki.org/index.php/Giant_tapir) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant tapirs for their floppy noses.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Tapir - Tapir man - Giant tapir**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Milkable**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 170,000 cm 3
- **Mid:** 850,000 cm 3
- **Max:** 1,700,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 25-30
- **Butchering returns**
- **Food items**
- **Meat:** 49-60
- **Fat:** 27-29
- **Brain:** 1-2
- **Heart:** 1
- **Lungs:** 2-4
- **Intestines:** 4-7
- **Liver:** 1-2
- **Kidneys:** 2
- **Tripe:** 1-2
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 40-44
- **Skull:** 1
- **Teeth:** 0-1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a tapir.*

**Giant tapirs** are creatures found in savage tropical moist broadleaf forests; the much larger cousin of the common tapir. They are considerably larger than both dwarves and normal tapirs, weighting nearly 2 tons - about 28 times heavier than the average Urist - though despite their great size, they are as benign as their common cousins and will react to attackers by trying to run away from them. Note, however, that they can deal massive damage to dwarves in the event they do fight back, so it's good to keep an eye open. Like normal tapirs, a baby giant tapir is named a *giant tapir calf*.

Giant tapirs can be captured in cage traps and trained into pets, possessing the standard value of giant creatures. Their huge size means they give a very good amount of returns when butchered, and like normal tapirs, they also serve as a source of milk and later cheese. Note, however, that giant tapir milk and normal-sized tapir milk are completely identical in every aspect. They are exotic mounts, and so may be used by elves during sieges.

Some dwarves like giant tapirs for their *floppy noses*.

    [CREATURE:GIANT_TAPIR]
        [COPY_TAGS_FROM:TAPIR]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:tapir]
            [CVCT_REPLACEMENT:giant tapir]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:tapir]
            [CVCT_REPLACEMENT:giant tapir]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:850]
        [GO_TO_START]
        [NAME:giant tapir:giant tapirs:giant tapir]
        [CASTE_NAME:giant tapir:giant tapirs:giant tapir]
        [GENERAL_CHILD_NAME:giant tapir calf:giant tapir calves]
        [DESCRIPTION:A huge monster in the form of a tapir.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'T']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:floppy noses]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:703:505:274:1900:2900] 32 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
