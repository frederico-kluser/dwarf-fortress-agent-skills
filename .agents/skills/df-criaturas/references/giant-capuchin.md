# Giant capuchin

> Fonte: [Giant capuchin](https://dwarffortresswiki.org/index.php/Giant_capuchin) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant capuchins for their social nature.**
- **Biome**
- **Any Tropical Forest Mangrove Swamp**
- **Variations**
- **Capuchin - Capuchin man - Giant capuchin**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 22,456 cm 3
- **Mid:** 112,280 cm 3
- **Max:** 224,560 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 40-55
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
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a capuchin.*

**Giant capuchins** are giant animal versions of the common capuchin who can be found in savage tropical forests and mangrove swamps. These monkeys enjoy raiding your fortress for food and valuables in groups of 5-10, whilst menacing off any dwarves foolish enough to think of stopping them due to being almost four times heavier than them. Regular capuchins are annoying, but giant ones manage to be annoying *and* dangerous, and can ruin the game for you early in your fortress's life, before you can get all of your things underground.

Giant capuchins do have a pretty high pet value of 500, however, so if you manage to capture one, you're probably better off keeping it. Young giant capuchins require two years to grow to full size, and three years to reach adulthood, making them viable livestock for a meat industry. Like other giant animals, giant capuchins are exotic mounts.

Some dwarves prefer giant capuchins for their *intelligence* and *social nature*.

    [CREATURE:GIANT_CAPUCHIN]
        [COPY_TAGS_FROM:CAPUCHIN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:6416]
        [GO_TO_START]
        [NAME:giant capuchin:giant capuchins:giant capuchin]
        [CASTE_NAME:giant capuchin:giant capuchins:giant capuchin]
        [DESCRIPTION:A large monster in the form of a capuchin.]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'C']
        [COLOR:7:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:intelligence]
        [PREFSTRING:social nature]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
