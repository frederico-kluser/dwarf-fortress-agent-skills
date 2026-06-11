# Giant elk

> Fonte: [Giant elk](https://dwarffortresswiki.org/index.php/Giant_elk) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant elk for their grace.**
- **Biome**
- **Tundra Temperate Grassland**
- **Variations**
- **Elk - Elk man - Giant elk**
- **Attributes**
- **Alignment:** Savage
- **Grazer · Exotic mount · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 247,800 cm 3
- **Mid:** 1,239,000 cm 3
- **Max:** 2,478,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 49-59
- **Fat:** 15
- **Brain:** 2-3
- **Heart:** 1
- **Lungs:** 4-6
- **Intestines:** 7-9
- **Liver:** 2-3
- **Kidneys:** 2
- **Tripe:** 2-3
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 30-36
- **Skull:** 1
- **Teeth:** 1
- **Hooves:** 4
- **Horns:** 2 (males only)
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of an elk.*

Elks are large, **giant elks** are larger. At more than twice the size of a giraffe, giant elks are formidable creatures, appearing in groups of 4-7 in temperate grasslands and tundras. Despite this, giant elks are a relatively safe prey for your hunters, being benign creatures that most of the time will simply flee instead of putting up a fight. The males have antlers, but they cannot use these for goring. Their young are called *fawns*.

Elk can be captured in cage traps and trained into exotic pets. Being large grazers, giant elks need large grassy pastures not to starve to death. This makes them difficult to keep, but this is made up for by their large size, still making them very viable targets for a meat industry. While there are larger creatures in the game, giant elks are the biggest game found in their respective biomes, barring the very dangerous giant polar bears in tundras and unbutcherable ogres in terrifying grasslands.

Male giant elks are one of the few creatures in the game that give horns (called antlers) when butchered. However, since several of the other horn-givers are domestic animals, most forts have little need for additional horns. Still, this means more material for making crafts. They also give hooves when butchered. Both horn and hoof crafts are made by a bone carver. Despite being larger than their smaller cousins, giant elks give exactly the same amount of horn and hoof material as those when butchered. Products made from elk parts are worth twice more than those made from other, more common animals.

Giant elks are exotic mounts, and can sometimes arrive with elves in sieges.

Some dwarves like giant elks for their *grace*.

Can sometimes mow down entire forests with those horns.\
*Art by Mark Witton*

    >[CREATURE:GIANT_ELK]
        [COPY_TAGS_FROM:ELK]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:826]
        [GO_TO_START]
        [NAME:giant elk:giant elk:giant elk]
        [CASTE_NAME:giant elk:giant elk:giant elk]
        [GENERAL_CHILD_NAME:giant elk fawn:giant elk fawns]
        [DESCRIPTION:A huge monster in the form of an elk.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [CREATURE_TILE:'E']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:grace]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:366:244:122:1900:2900] 72 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
