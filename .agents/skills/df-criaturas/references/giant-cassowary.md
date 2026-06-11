# Giant cassowary

> Fonte: [Giant cassowary](https://dwarffortresswiki.org/index.php/Giant_cassowary) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant cassowaries for their casques.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Cassowary - Cassowary man - Giant cassowary**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 5,600 cm 3
- **Mid:** 280,000 cm 3
- **Max:** 560,000 cm 3
- **Food products**
- **Eggs:** 3-6
- **Age**
- **Adult at:** 1
- **Max age:** 40-50
- **Butchering returns**
- **Food items**
- **Meat:** 27
- **Fat:** 17
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 29
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a cassowary.*

**Giant cassowaries** are the much bigger savage counterpart of the common cassowary, found in a savage tropical moist broaflead forests. The birds are considerably larger than dwarves, being heavier than a moose, though despite this they are still benign and will rarely fight back if provoked. In the event they do, they can deliver formidable kick attacks which might turn your dwarves' heads into sauce, so you may want to confront them with a few armored military dwarves rather than a mere hunter.

Giant cassowaries can be captured with cage traps and trained into pets, possessing the standard value of a giant creature. While they lay a poor amount of eggs compared to most domestic poultry, they give a sizeable amount of returns when butchered, making the idea of a giant cassowary farm an attractive one if a breeding pair is obtained. Like most creatures, they reach their full size at two years of age and should be butchered at that point for maximum return efficiency. Giant cassowaries are exotic mounts and may be seen being ridden by elves during sieges.

Some dwarves like giant cassowaries for their *casques*.

Size = confidence.\
*Art by windfalcon*

    [CREATURE:GIANT_CASSOWARY]
        [COPY_TAGS_FROM:BIRD_CASSOWARY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1120]
        [GO_TO_START]
        [NAME:giant cassowary:giant cassowaries:giant cassowary]
        [CASTE_NAME:giant cassowary:giant cassowaries:giant cassowary]
        [GENERAL_CHILD_NAME:giant cassowary chick:giant cassowary chicks]
        [DESCRIPTION:A huge monster in the shape of a cassowary.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'C']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:casques]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
