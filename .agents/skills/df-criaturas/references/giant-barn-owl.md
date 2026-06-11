# Giant barn owl

> Fonte: [Giant barn owl](https://dwarffortresswiki.org/index.php/Giant_barn_owl) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant barn owls for their coloration.**
- **Biome**
- **Any Wetland Any Temperate Forest Tropical Coniferous Forest Tropical Dry Broadleaf Forest Any Shrubland Any Savanna Any Grassland Any Desert**
- **Variations**
- **Barn owl - Barn owl man - Giant barn owl**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 12,210 cm 3
- **Mid:** 101,750 cm 3
- **Max:** 203,500 cm 3
- **Food products**
- **Eggs:** 3-6
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 18-19
- **Fat:** 11-12
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
- **Bones:** 24
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a barn owl.*

**Giant barn owls** are giant animal versions of the common barn owl, found in a variety of savage biomes. While the normal owl is as small as some species of vermin, their giant cousins are about as big as grizzly bears, though they retain the benign behavior of their normal counterparts; they spawn one at a time and do little but fly around. All giant barn owls are born with Legendary skill in climbing.

Giant barn owls can be captured with cage traps and trained into pets, possessing the standard pet value of savage giants (500). They are large enough to produce a good amount of returns when butchered, and can also be placed in nest boxes to lay eggs, though they aren't any better than normal barn owls when it comes to egg-laying. Giant barn owls are exotic mounts and may be seen being ridden by elves during sieges.

Some dwarves like giant barn owls for their *coloration*.

    [CREATURE:GIANT_BARN_OWL]
        [COPY_TAGS_FROM:BIRD_OWL_BARN]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:40700]
        [GO_TO_START]
        [NAME:giant barn owl:giant barn owls:giant barn owl]
        [CASTE_NAME:giant barn owl:giant barn owls:giant barn owl]
        [GENERAL_CHILD_NAME:giant barn owl chick:giant barn owl chicks]
        [DESCRIPTION:A large monster in the form of a barn owl.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'B']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
