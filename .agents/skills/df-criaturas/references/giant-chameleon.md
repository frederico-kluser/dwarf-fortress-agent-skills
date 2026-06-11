# Giant chameleon

> Fonte: [Giant chameleon](https://dwarffortresswiki.org/index.php/Giant_chameleon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant chameleons for their ability to change color.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland Tropical Savanna Any Desert**
- **Variations**
- **Chameleon - Chameleon man - Giant chameleon**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 201,049.5 cm 3
- **Food products**
- **Eggs:** 40-50
- **Age**
- **Adult at:** Birth
- **Max age:** 5-10
- **Butchering returns**
- **Food items**
- **Meat:** 15
- **Fat:** 13
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
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a chameleon.*

**Giant chameleons** are the giant animal versions of the chameleon, found in a variety of savage biomes including deserts and tropical forests. They are 1340 times larger than their vermin equivalents, or over 3 times the size of the average dwarf. Giant chameleons spawn one at a time, wandering through the biome and generally minding their own business. Due to their size, they can easily kill a civilian if provoked, but they should prove no big threat to a crossbow-wielding hunter or a military squad. All giant chameleons possess Legendary skill in climbing.

Giant chameleons are tied with giant iguanas as the second best egg-layers of all giant creatures (losing only to the giant saltwater crocodile), a trait carried over from their vermin counterparts. They lay 40 to 50 eggs at a time, which makes them one of the best creatures for egg production in the game. They also possess the standard high pet value of all giant creatures, which makes them valuable pets.

Unlike most reptiles, which hatch as tiny compared to their adult forms, giant chameleons hatch as fully-grown adults. If you can acquire a breeding pair, then a single clutch of eggs can produce over 800 meat, making them ideal for the meat industry or unleashing scaly hordes upon goblin intruders, assuming the fortress survives the ensuing iguanasplosion.

Some dwarves like giant chameleons for their *ability to change color* and their *eyes*.

Can disguise itself as entire forests.

    [CREATURE:GIANT_CHAMELEON]
        [COPY_TAGS_FROM:CHAMELEON]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:134033]
        [GO_TO_START]
        [NAME:giant chameleon:giant chameleons:giant chameleon]
        [CASTE_NAME:giant chameleon:giant chameleons:giant chameleon]
        [DESCRIPTION:A large monster in the shape of a chameleon.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'C']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ability to change color]
        [PREFSTRING:eyes]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
