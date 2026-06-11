# Giant swan

> Fonte: [Giant swan](https://dwarffortresswiki.org/index.php/Giant_swan) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant swans for their beauty.**
- **Biome**
- **Any Temperate Lake Any Temperate Marsh**
- **Variations**
- **Swan - Swan man - Giant swan**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 8,115 cm 3
- **Mid:** 135,250 cm 3
- **Max:** 270,500 cm 3
- **Food products**
- **Eggs:** 5-7
- **Age**
- **Adult at:** 1
- **Max age:** 10-25
- **Butchering returns**
- **Food items**
- **Meat:** 17-25
- **Fat:** 11-19
- **Brain:** 1
- **Gizzard:** 1
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
- **Bones:** 24-32
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a swan.*

**Giant swans** are enlarged cousins of the common swan, found in savage temperate lakes and marshes. Despite being four and a half times larger than the average dwarf, giant swans are as benign as their normal-sized counterparts and will pose little to no threat to a fortress, though much like normal swans, they'll scare animals out of their pastures every time they fly close to them, leading to many distracted dwarves. Unlike normal swans, both genders of giant ones have the same name, though hatchlings are still referred to as *giant cygnets*.

Giant swans can be captured in cage traps and trained into pets, possessing the standard high value of a giant creature. Their much bigger size compared to normal swans makes them an even better choice for a farm, as they produce much more returns when butchered. Giant swans are exotic mounts and can be used by elves during sieges.

Some dwarves like giant swans for their *beauty*.

    [CREATURE:GIANT_SWAN]
        [COPY_TAGS_FROM:BIRD_SWAN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2705]
        [GO_TO_START]
        [NAME:giant swan:giant swans:giant swan]
        [CASTE_NAME:giant swan:giant swans:giant swan]
        [GENERAL_CHILD_NAME:giant cygnet:giant cygnets]
        [DESCRIPTION:A large monster in the form of a swan.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:2]
        [CREATURE_TILE:'S']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:beauty]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
