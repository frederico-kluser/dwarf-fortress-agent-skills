# Giant bobcat

> Fonte: [Giant bobcat](https://dwarffortresswiki.org/index.php/Giant_bobcat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant bobcats for their short tails.**
- **Biome**
- **Any Forest Any Desert Tropical Freshwater Swamp Tropical Saltwater Swamp Temperate Freshwater Swamp Temperate Saltwater Swamp Mangrove Swamp Mountain**
- **Variations**
- **Bobcat - Bobcat man - Giant bobcat**
- **Attributes**
- **Alignment:** Savage
- **War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 25,632 cm 3
- **Mid:** 128,160 cm 3
- **Max:** 256,320 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-35
- **Butchering returns ( Value multiplier ×2)**
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

*A large monster in the form of a bobcat.*

**Giant bobcats** are the gigantic savage version of regular bobcats. Regular bobcats are some of the smallest predators in the game, but at 256,320 cm3 giant bobcats are not small creatures, lying between tigers (the largest non-giant big cat) and muskoxen in size. Interestingly, their creature definitions do not have a [`[LARGE_PREDATOR]`](/index.php/Creature_token#LARGE_PREDATOR "Creature token") tag, so giant bobcats will still flee from contact with your dwarves, despite being more than four times as large. Like their normal counterparts, giant bobcats are extremely uncommon to encounter and no more than 3 of them will exist in the map before they're locally extinct.

Giant bobcats can be captured, trained, and turned into war or hunting animals. They thus make excellent dwarven companions, given their large size, although in a savage biome you might be able to field a better option - giant tigers, for instance, are almost eight times as large.

Some dwarves like giant bobcats for their *short tails*.

Still chases its tail at the worst possible moments.\
*Art by Anthony Argentin*

    [CREATURE:GIANT_BOBCAT]
        [COPY_TAGS_FROM:BOBCAT]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:3204]
        [GO_TO_START]
        [NAME:giant bobcat:giant bobcats:giant bobcat]
        [CASTE_NAME:giant bobcat:giant bobcats:giant bobcat]
        [GENERAL_CHILD_NAME:giant bobcat kitten:giant bobcat kittens]
        [DESCRIPTION:A large monster in the form of a bobcat.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'B']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:short tails]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:699:497:266:1900:2900] 33 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
