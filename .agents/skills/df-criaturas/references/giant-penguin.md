# Giant penguin

> Fonte: [Giant penguin](https://dwarffortresswiki.org/index.php/Giant_penguin) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant penguins for their enormous size.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Penguin - Penguin man - Giant penguin**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 6,842.4 cm 3
- **Mid:** 114,040 cm 3
- **Max:** 228,080 cm 3
- **Food products**
- **Eggs:** 2
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 29
- **Fat:** 20
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
- **Bones:** 32
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster, shaped like a penguin.*

**Giant penguins** are enlarged counterparts of the common penguin, found in savage arctic oceans. They waddle through the landscape in groups of 5 to 10 individuals, each standing nearly four times the size of a dwarf, though despite their size, they are as benign as their smaller cousins, fleeing from dwarves unless cornered. Hunters and a half-competent military squad should be able to take on these creatures without much difficulty.

Giant penguins can be captured in cage traps and, unlike every other kind of penguin in the game, they can be trained into pets, possessing the standard high value of a giant creature. Because they provide a respectable amount of food and bones when butchered, the idea of breeding them for a meat industry is an attractive one, but they are very poor egg-layers - only laying 2 eggs at a time - and take two years to reach their adult size, meaning the player will require patience to get a functional giant penguin farm running smoothly. Granted, crazier things have been done before.

Some dwarves like giant penguins for their *enormous size*, their *coloration*, their *waddling gait* and their *way of flying through the water*.

## Trivia

- In real life, a genus of extinct penguin named *Palaeeudyptinae* is sometimes known as the giant penguin. However, as the game's giant penguins are enlarged versions of Magellanic penguins, this is most likely a coincidence.

    [CREATURE:BIRD_PENGUIN_GIANT]
        [COPY_TAGS_FROM:BIRD_PENGUIN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:5702] this also resizes the eggs
        [GO_TO_START]
        [NAME:giant penguin:giant penguins:giant penguin]
        [CASTE_NAME:giant penguin:giant penguins:giant penguin]
        [GENERAL_CHILD_NAME:giant penguin chick:giant penguin chicks]
        [DESCRIPTION:A huge monster, shaped like a penguin.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'P']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [PREFSTRING:enormous size]
        [PREFSTRING:coloration]
        [PREFSTRING:waddling gait]
        [PREFSTRING:way of flying through the water]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
