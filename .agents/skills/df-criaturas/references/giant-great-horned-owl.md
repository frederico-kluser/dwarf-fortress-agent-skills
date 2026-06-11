# Giant great horned owl

> Fonte: [Giant great horned owl](https://dwarffortresswiki.org/index.php/Giant_great_horned_owl) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant great horned owls for their piercing yellow eyes.**
- **Biome**
- **Any Forest Any Shrubland Any Savanna Any Grassland Any Desert Mangrove Swamp Mountain Tundra**
- **Variations**
- **Great horned owl - Great horned owl man - Giant great horned owl**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 5,350.5 cm 3
- **Mid:** 107,010 cm 3
- **Max:** 214,020 cm 3
- **Food products**
- **Eggs:** 1-5
- **Age**
- **Adult at:** 1
- **Max age:** 15-20
- **Butchering returns**
- **Food items**
- **Meat:** 18-19
- **Fat:** 11-12
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 24
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a great horned owl.*

**Giant great horned owls** are the giant animal version of the standard great horned owl. They are roughly ten times the size of their smaller counterparts. Despite being giant, they do not produce substantial amounts of meat when butchered. Much like their smaller cousins, they are not a particularly large threat to dwarves, and are born with Legendary skill in climbing, can be in cage traps, can be trained to be cheap exotic pets and (if female) can lay a meager amount of eggs. Due to their massive size, they can be exotic mounts.

Some dwarves like giant great horned owls for their *ear tufts* and *piercing yellow eyes*.

Favorite food: Giant rats\
Favorite band: The Who\
*Art by Michele Sommers*

    [CREATURE:GIANT_GREAT_HORNED_OWL]
        [COPY_TAGS_FROM:BIRD_OWL_GREAT_HORNED]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:10701]
        [GO_TO_START]
        [NAME:giant great horned owl:giant great horned owls:giant great horned owl]
        [CASTE_NAME:giant great horned owl:giant great horned owls:giant great horned owl]
        [GENERAL_CHILD_NAME:giant great horned owl chick:giant great horned owl chicks]
        [DESCRIPTION:A huge monster in the shape of a great horned owl.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'O']
        [COLOR:7:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:piercing yellow eyes]
        [PREFSTRING:ear tufts]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
