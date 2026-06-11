# Giant green tree frog

> Fonte: [Giant green tree frog](https://dwarffortresswiki.org/index.php/Giant_green_tree_frog) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant green tree frogs for their distinct mating call.**
- **Biome**
- **Temperate Freshwater Pool Temperate Freshwater Lake Temperate Freshwater Swamp Temperate Freshwater Marsh**
- **Variations**
- **Green tree frog - Green tree frog man - Giant green tree frog**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,700 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-5
- **Butchering returns**
- **Food items**
- **Meat:** 11-12
- **Fat:** 11
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 0
- **Spleen:** 1
- **Raw materials**
- **Bones:** 17
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a green tree frog.*

**Giant green tree frogs** are much larger cousins of the common green tree frog, found in savage temperate freshwater biomes where they spawn one at a time. Despite being as big as a giant cave toad, these frogs are benign and will run away from dwarves who approach them, only fighting if cornered. While a civilian can get hurt if they get entangled into a fight with one, they should pose no threat to a hunter or a half-competent military squad. All giant green tree frogs are born with Legendary skill in climbing.

Giant green tree frogs can be captured in cage traps and trained into pets, possessing the standard high value of a giant creature. They produce an average amount of meat, bones and fat when butchered, making them a choice for a meat industry if a breeding pair is obtained. They are considered exotic mounts, so you may see elves riding them into battle in the event of a siege.

Some dwarves like giant green tree frogs for their *distinct mating call*.

    [CREATURE:GIANT_GREEN_TREE_FROG]
        [COPY_TAGS_FROM:GREEN_TREE_FROG]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:200700]
        [GO_TO_START]
        [NAME:giant green tree frog:giant green tree frogs:giant green tree frog]
        [CASTE_NAME:giant green tree frog:giant green tree frogs:giant green tree frog]
        [DESCRIPTION:A large monster in the shape of a green tree frog.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'F']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:distinct mating call]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:3512:2634:1756:878:4900:6900]
