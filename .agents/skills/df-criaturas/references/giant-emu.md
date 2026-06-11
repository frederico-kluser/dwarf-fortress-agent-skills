# Giant emu

> Fonte: [Giant emu](https://dwarffortresswiki.org/index.php/Giant_emu) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant emus for their inquisitive nature.**
- **Biome**
- **Temperate Shrubland Any Temperate Forest**
- **Variations**
- **Emu - Emu man - Giant emu**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 10,288 cm 3
- **Mid:** 225,050 cm 3
- **Max:** 450,100 cm 3
- **Food products**
- **Eggs:** 5-15
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 25
- **Fat:** 16
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
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

*A huge monster in the form of an emu.*

**Giant emus** are very large creatures - between an alligator and a bull moose in size. They'll wander around your fortress surroundings in groups of 2-10, and produce a very sizeable amount of meat when butchered. If you manage to capture a breeding pair, you can make use of a trifecta of properties of the species: excellent butchery returns, excellent egg production, and excellent pet value. Capturing and breeding giant emus is a win-win-win situation, leading to a very profitable birdsplosion.

Some dwarves like giant emus for their *size* and their *inquisitive nature*.

    [CREATURE:GIANT_EMU]
        [COPY_TAGS_FROM:BIRD_EMU]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1286]
        [GO_TO_START]
        [NAME:giant emu:giant emus:giant emu]
        [CASTE_NAME:giant emu:giant emus:giant emu]
        [GENERAL_CHILD_NAME:giant emu chick:giant emu chicks]
        [DESCRIPTION:A huge monster in the form of an emu.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:2:10]
        [CREATURE_TILE:'E']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:size]
        [PREFSTRING:inquisitive nature]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
