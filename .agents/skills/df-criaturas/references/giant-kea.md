# Giant kea

> Fonte: [Giant kea](https://dwarffortresswiki.org/index.php/Giant_kea) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant kea for their intelligence.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Mountain**
- **Variations**
- **Kea - Kea man - Giant kea**
- **Attributes**
- **Alignment:** Savage
- **Flying · Steals food · Steals items · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 12,420.6 cm 3
- **Mid:** 103,505 cm 3
- **Max:** 207,010 cm 3
- **Food products**
- **Eggs:** 2-5
- **Age**
- **Adult at:** 1
- **Max age:** 30-50
- **Butchering returns**
- **Food items**
- **Meat:** 18
- **Fat:** 11
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

*A monster many times the size of an ordinary kea.*

**Giant kea** are airborne infiltrators more than 200 times the size of normal pesky kea. They are incredibly dangerous animals, so much that they are the uncontested aerial king of beasts in the modern versions. Their habit of going into your fort and stealing your stuff will mean these monsters will come right into contact with your dwarves and fight. And do not expect a civilian, unarmored dwarf to win any of these fights. Giant kea will kill your dwarves faster than you can say *"It's just a big parrot, what harm could it do?"*

This animal is capable of stealing artifacts.[1] Additionally, they come in groups of 5-10. As such, they can quickly become your fort's top concern. They tend to fly away when targeted, but that won't stop them from returning to steal again later.

Overall, these things can be a huge threat to a fortress.

When butchered they leave behind useless feathers. Some dwarves admire giant kea for their *curiosity* and *intelligence*.

Ready to attack and steal.

    [CREATURE:GIANT_KEA]
        [COPY_TAGS_FROM:BIRD_KEA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20701]
        [GO_TO_START]
        [NAME:giant kea:giant kea:giant kea]
        [CASTE_NAME:giant kea:giant kea:giant kea]
        [GENERAL_CHILD_NAME:giant kea chick:giant kea chicks]
        [DESCRIPTION:A monster many times the size of an ordinary kea.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'K']
        [COLOR:2:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:curiosity]
        [PREFSTRING:intelligence]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
