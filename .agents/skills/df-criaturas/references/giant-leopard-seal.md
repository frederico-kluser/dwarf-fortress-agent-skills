# Giant leopard seal

> Fonte: [Giant leopard seal](https://dwarffortresswiki.org/index.php/Giant_leopard_seal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant leopard seals for their fierce nature.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Leopard seal - Leopard seal man - Giant leopard seal**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 326,800 cm 3
- **Mid:** 1,634,000 cm 3
- **Max:** 3,268,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 89-113
- **Fat:** 18-22
- **Brain:** 7-9
- **Heart:** 3-4
- **Lungs:** 14-18
- **Intestines:** 22-28
- **Liver:** 7-9
- **Kidneys:** 6-8
- **Tripe:** 7-9
- **Sweetbread:** 3-4
- **Eyes:** 2
- **Spleen:** 3-4
- **Raw materials**
- **Bones:** 23-30
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant monster in the form of a leopard seal.*

**Giant leopard seals** are the second-largest seal-like creature in the game (with giant elephant seals being about twice as large for females and 9 times as large for males - see this page for more information).

Giant leopard seals are *massive* compared to ordinary leopard seals - nearly 10 times bigger, in fact. Since healthy dwarves eat about twice per season and giant leopard seals can provide up to 230 units of food, a giant leopard seal could feed 115 dwarves for a season (3 months or 84 days), 28 dwarves for a year (4 seasons), or a single dwarf for *115 seasons* (over 28 *years*). And if that sounds like a lot, an adult giant sperm whale is over 50 times larger.

Giant leopard seals are extremely fun around dwarves, and can easily kill unarmed dwarves (even highly skilled swimmers) by ripping off limbs. Even grand master fighters usually lose to giant leopard seals, inflicting only bruises upon their opponent. The best defense against these creatures is a dwarf's best friend.

Admired for the amount of meat it can produce.

    [CREATURE:GIANT_LEOPARD_SEAL]
        [COPY_TAGS_FROM:LEOPARD_SEAL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:817]
        [GO_TO_START]
        [NAME:giant leopard seal:giant leopard seals:giant leopard seal]
        [CASTE_NAME:giant leopard seal:giant leopard seals:giant leopard seal]
        [GENERAL_CHILD_NAME:giant leopard seal pup:giant leopard seal pups]
        [DESCRIPTION:A giant monster in the form of a leopard seal.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'L']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:fierce nature]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:734:568:366:1900:2900]
