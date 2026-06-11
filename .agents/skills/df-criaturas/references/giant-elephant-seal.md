# Giant elephant seal

> Fonte: [Giant elephant seal](https://dwarffortresswiki.org/index.php/Giant_elephant_seal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant elephant seals for their great size.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Elephant seal - Elephant seal man - Giant elephant seal**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 2,412,000 cm 3
- **Mid:** 12,060,000 cm 3
- **Max:** 24,120,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 181-870
- **Fat:** 36-195
- **Brain:** 14-68
- **Heart:** 7-34
- **Lungs:** 28-136
- **Intestines:** 43-204
- **Liver:** 14-68
- **Kidneys:** 14-68
- **Tripe:** 14-68
- **Sweetbread:** 7-34
- **Eyes:** 2
- **Spleen:** 7-34
- **Raw materials**
- **Bones:** 47-239
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of an elephant seal.*

**Giant elephant seals** are larger than young dragons and mature much more quickly. Because of their size they will brutally murder anything that provokes them, making them a great addition to your fort's defense. Giant elephant seals can be tamed and kept as pets, but their real value lies in their butchering returns. By breeding giant elephant seals, your meat industry can sustain your entire fortress with food to spare. Note, however, that it takes five years for giant elephant seal pups to reach full adult size.

Unlike most animals, there is a significant size difference between the sexes of giant elephant seals. Males grow to more than three times the size of females, resulting in large variances in butchering returns.

Some dwarves admire giant elephant seals for their *large floppy noses* and their *great size*.

The fact that they can get bigger...

    [CREATURE:GIANT_ELEPHANT_SEAL]
        [COPY_TAGS_FROM:ELEPHANT_SEAL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:804]
        [GO_TO_START]
        [NAME:giant elephant seal:giant elephant seals:giant elephant seal]
        [CASTE_NAME:giant elephant seal:giant elephant seals:giant elephant seal]
        [GENERAL_CHILD_NAME:giant elephant seal pup:giant elephant seal pups]
        [DESCRIPTION:A huge monster in the shape of an elephant seal.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:large floppy noses]
        [PREFSTRING:great size]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:1945:1504:1062:548:3100:4500]
