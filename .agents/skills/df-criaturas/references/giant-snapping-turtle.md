# Giant snapping turtle

> Fonte: [Giant snapping turtle](https://dwarffortresswiki.org/index.php/Giant_snapping_turtle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant snapping turtles for their vicious bites.**
- **Biome**
- **Temperate Freshwater River Temperate Brackish River Temperate Freshwater Lake Temperate Brackish Lake Temperate Freshwater Pool Temperate Brackish Pool**
- **Variations**
- **Common snapping turtle - Snapping turtle man - Giant snapping turtle**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount · Shell · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 552 cm 3
- **Max:** 414,000 cm 3
- **Food products**
- **Eggs:** 5-10
- **Age**
- **Adult at:** Birth
- **Max age:** 30-50
- **Butchering returns**
- **Food items**
- **Brain:** 1
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
- **Bones:** 19
- **Skull:** 1
- **Shell:** 1-2
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster with an enormous shell and immensely powerful jaw.*

While the alligator snapping turtle is named after its ferocity, similarly to an alligator, it is still much smaller than one. This is unlike the **giant snapping turtle**, a carnivorous beast almost 7 times the size of the average dwarf (slightly larger than an alligator). Giant snapping turtles may be found individually in savage, temperate lakes and rivers.

Like most giant animals, giant snapping turtles may be caught using cage traps, and butchered to give a fair amount of returns. However, be aware that as they do not have a child stage, offspring of a caught breeding pair won't be possible to domesticate, meaning they will revert to a wild state if their training is not maintained. Giant snapping turtles lay 5-10 eggs in a clutch. Unsurprisingly, they also give a shell when butchered, which can be useful for moody dwarves, but no tannable skin, as they have scales.

Giant snapping turtles are exotic mounts, sometimes arriving in elven sieges.

Some dwarves like giant snapping turtles for their *vicious bites* and their *long necks*.

    [CREATURE:GIANT_SNAPPING_TURTLE]
        [COPY_TAGS_FROM:SNAPPING TURTLE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1380]
        [GO_TO_START]
        [NAME:giant snapping turtle:giant snapping turtles:giant snapping turtle]
        [CASTE_NAME:giant snapping turtle:giant snapping turtles:giant snapping turtle]
        [DESCRIPTION:A large monster with an enormous shell and immensely powerful jaw.]
        [POPULATION_NUMBER:25:50]
        [CREATURE_TILE:'T']
        [COLOR:2:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:vicious bites]
        [PREFSTRING:long necks]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
