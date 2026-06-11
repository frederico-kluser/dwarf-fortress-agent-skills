# Gigantic panda

> Fonte: [Gigantic panda](https://dwarffortresswiki.org/index.php/Gigantic_panda) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gigantic pandas for their enormous size.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Panda - Panda man - Gigantic panda**
- **Attributes**
- **Alignment:** Savage
- **War animals · Hunting animals · Grazer · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 1,000
- **Trainable : Hunting War**
- **Size**
- **Birth:** 1,339.5 cm 3
- **Mid:** 580,450 cm 3
- **Max:** 1,160,900 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 37
- **Fat:** 32
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 3
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 42
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant bear-like creature found in the wildest parts of the world. It has striking black and white fur.*

Though considerably dangerous, **gigantic pandas** can be a great asset to your fortress. Consider embarking near a temperate forest, on the chance that you might encounter this creature. It can be considered a must-cage creature for its tremendous size, value and train-ability (for hunting or war).

However, like their smaller panda relatives, trained gigantic pandas must graze on bamboo, and given their immense size, they must graze **constantly** to avoid starvation, making them a very poor choice for training and livestock. Their butchering returns are twice as valuable as common creatures, but their dietary requirements make gigantic pandas a better target for hunting than husbandry.

It should be noted that this creature is considered gigantic, *not* merely giant. Like the gigantic squid and gigantic tortoise, this is presumably to avoid confusion since "giant panda" is the formal name of *normal* pandas.

Some dwarves like gigantic pandas for their *enormous size*, their *striking coloration*, their *gigantic fluffy heads and bellies* and their *lazy nature*.

Its hunger can clear out an entire bamboo field.

    [CREATURE:PANDA, GIGANTIC]
        [COPY_TAGS_FROM:PANDA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:893]
        [GO_TO_START]
        [NAME:gigantic panda:gigantic pandas:gigantic panda]
        [CASTE_NAME:gigantic panda:gigantic pandas:gigantic panda]
        [GENERAL_CHILD_NAME:gigantic panda cub:gigantic panda cubs]
        [DESCRIPTION:A giant bear-like creature found in the wildest parts of the world.  It has striking black and white fur.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'P']
        [COLOR:7:0:1]
        [TRAINABLE]
        [PET_EXOTIC]
        [PETVALUE:1000]
        [MOUNT_EXOTIC]
        [PREFSTRING:enormous size]
        [PREFSTRING:striking coloration]
        [PREFSTRING:gigantic fluffy heads and bellies]
        [PREFSTRING:lazy nature]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:2728:2069:1409:675:4000:5700] 13 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
