# Giant damselfly

> Fonte: [Giant damselfly](https://dwarffortresswiki.org/index.php/Giant_damselfly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant damselflies for their coloration.**
- **Biome**
- **Any Lake**
- **Variations**
- **Damselfly - Damselfly man - Giant damselfly**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 1-1
- **Butchering returns**
- **Food items**
- **Meat:** 42
- **Fat:** 17
- **Brain:** 1
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a damselfly.*

**Giant damselflies** are much larger versions of the standard damselfly vermin. They can be encountered in savage lakes, however they won't be useful for anything other than immediate butchering, as they have a maximum lifespan of one year, like other giant insects. As they are not actually [`[BENIGN]`](/index.php/Creature_token#BENIGN "Creature token"), wild ones might often annoyingly interrupt your dwarves when spotted.

Some dwarves like giant damselflies for their *coloration*.

"'Sup, you dwarves want me to attack your entire fortress or am I gonna be an exotic mount?\
*Art James W Johnson*

    [CREATURE:GIANT_DAMSELFLY]
        [COPY_TAGS_FROM:DAMSELFLY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant damselfly:giant damselflies:giant damselfly]
        [CASTE_NAME:giant damselfly:giant damselflies:giant damselfly]
        [DESCRIPTION:A large monster in the shape of a damselfly.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:5]
        [CREATURE_TILE:'D']
        [COLOR:3:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
