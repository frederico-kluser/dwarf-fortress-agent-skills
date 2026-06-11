# Giant hamster

> Fonte: [Giant hamster](https://dwarffortresswiki.org/index.php/Giant_hamster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant hamsters for their puffy cheeks.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Hamster - Hamster man - Giant hamster**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 201,049.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 3-5
- **Butchering returns**
- **Food items**
- **Meat:** 13-14
- **Fat:** 12-13
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 0-2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 18
- **Skull:** 1
- **Teeth:** 0-2
- **Hooves:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large creature the shape of a hamster.*

**Giant hamsters** are just the giant versions of their vermin counterparts: the hamster. They are fairly uncommon and may appear in a small group within most savage biomes. They are benign and will not attempt to remove the entrails of your bearded slaves even when attacked, this despite being slightly larger than grizzly bears.

They can be caught in cage traps to be turned into pets, live trade goods, meat, bones, and leather. Despite their pet value, their products don't fetch a high price. Giant hamsters are capable of breeding, though have a somewhat short lifespan of 3-5 years. There exists no such thing as a giant hamster pup in *Dwarf Fortress*, as they are born adults. Giant hamsters can, therefore, never be fully domesticated.

Being exotic mounts, they sometimes appear in elven sieges.

Some dwarves like giant hamsters for their *puffy cheeks*.

Not nearly as cute in-game.\
*Art by Panda-With-Oar*

    [CREATURE:GIANT_HAMSTER]
        [COPY_TAGS_FROM:HAMSTER]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:134033]
        [GO_TO_START]
        [NAME:giant hamster:giant hamsters:giant hamster]
        [CASTE_NAME:giant hamster:giant hamsters:giant hamster]
        [DESCRIPTION:A large creature the shape of a hamster.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'H']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:puffy cheeks]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
