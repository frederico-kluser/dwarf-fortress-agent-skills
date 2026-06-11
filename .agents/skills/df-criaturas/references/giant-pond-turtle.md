# Giant pond turtle

> Fonte: [Giant pond turtle](https://dwarffortresswiki.org/index.php/Giant_pond_turtle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant pond turtles for their shells.**
- **Biome**
- **Any Lake**
- **Variations**
- **Pond turtle - Pond turtle man - Giant pond turtle**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount · Shell · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 2,035 cm 3
- **Max:** 203,500 cm 3
- **Food products**
- **Eggs:** 1-15
- **Age**
- **Adult at:** Birth
- **Max age:** 40-100
- **Butchering returns**
- **Food items**
- **Meat:** 13
- **Fat:** 12
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 18
- **Skull:** 1
- **Shell:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster shaped like a pond turtle.*

**Giant pond turtles** are much larger versions of pond turtles your fisherdwarves gather in large quantities. Like their smaller cousins, giant pond turtles possess shells, which they can retract into when threatened.

They can be encountered in savage lakes. Giant pond turtles also serve as foreign mounts during a siege.

Giant pond turtles are a decent source of shells and meat.

Some dwarves like giant pond turtles for their *shells*.

    [CREATURE:GIANT_POND_TURTLE]
        [COPY_TAGS_FROM:POND_TURTLE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:40700]
        [GO_TO_START]
        [NAME:giant pond turtle:giant pond turtles:giant pond turtle]
        [CASTE_NAME:giant pond turtle:giant pond turtles:giant pond turtle]
        [DESCRIPTION:A huge monster shaped like a pond turtle.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'T']
        [COLOR:2:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:shells]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
