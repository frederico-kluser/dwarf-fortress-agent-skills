# Giant mountain goat

> Fonte: [Giant mountain goat](https://dwarffortresswiki.org/index.php/Giant_mountain_goat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant mountain goats for their beards.**
- **Biome**
- **Mountain**
- **Variations**
- **Mountain goat - Mountain goat man - Giant mountain goat**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 56,000 cm 3
- **Mid:** 112,000 cm 3
- **Max:** 560,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 13-15
- **Fat:** 9
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1-2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 16
- **Skull:** 1
- **Hooves:** 4
- **Horns:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a mountain goat.*

**Giant mountain goats** are much larger counterparts of the mountain goat who can be found inhabiting savage mountains. They behave much like their normal cousins, appearing in groups of 1 to 4 individuals who meander aimlessly around the landscape, with the difference being that they rival the weight of an adult moose. Despite the size, however, they are benign and will normally flee from danger. A baby giant mountain goat is called a *giant mountain goat kid*.

Giant mountain goats may be captured in cage traps and trained into pets. Due to the larger size, they produce more food when butchered than a normal goat, though they are among the smaller (and less productive) giant creatures. Like a common goat, a trained giant mountain goat will require a pasture to survive. They are considered exotic mounts and may be witnessed being ridden by elves during sieges.

Some dwarves like giant mountain goats for their *beards*, their *long horns* and their *surefootedness*.

Still one of the smaller giants.

    [CREATURE:GIANT_GOAT_MOUNTAIN]
        [COPY_TAGS_FROM:GOAT_MOUNTAIN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1120]
        [GO_TO_START]
        [NAME:giant mountain goat:giant mountain goats:giant mountain goat]
        [CASTE_NAME:giant mountain goat:giant mountain goats:giant mountain goat]
        [GENERAL_CHILD_NAME:giant mountain goat kid:giant mountain goat kids]
        [DESCRIPTION:A huge monster in the form of a mountain goat.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [CREATURE_TILE:'G']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:beards]
        [PREFSTRING:long horns]
        [PREFSTRING:surefootedness]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
