# Giant eagle

> Fonte: [Giant eagle](https://dwarffortresswiki.org/index.php/Giant_eagle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant eagles for their high soaring.**
- **Biome**
- **Any Wetland Any Forest Any Shrubland Any Savanna Any Grassland Any Desert Mountain Tundra**
- **Variations**
- **Eagle - Eagle man - Giant eagle**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 7,981.4 cm 3
- **Mid:** 114,020 cm 3
- **Max:** 228,040 cm 3
- **Food products**
- **Eggs:** 1-3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 18
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
- **Bones:** 23
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of an eagle.*

**Giant eagles** are the over-sized version of eagles, found in the same wide array of savage biomes. They can be extremely annoying to an early fortress due to their ability to fly over your fortress defenses and kill your unarmed civilians. Unlike other aerial pests, giant eagles will generally not path into your fortress, and usually only attack if provoked. They may also appear as mounts during a siege, resulting in a highly-maneuverable and dangerous squad of attackers. All giant eagles are born with Legendary skill in climbing.

Captured giant eagles may be kept as exotic pets, requiring substantial time and effort to tame. Unfortunately, they cannot be trained to increase their combat effectiveness. Elven caravans may offer to trade tame giant eagles if the elven civilization is situated in a mountainous area.

Giant eagles are relatively useless for egg production thanks to their small clutch sizes, but they are a viable choice for your meat industry, yielding a respectable amount of food without grazing. Once hatched, giant eagle hatchlings take roughly one year to reach adulthood.

There is a current bug where tamed animals that have the \[FLYING\] tag won't actually fly. Once tamed, your giant eagles will remain earthbound and never take to the sky, which makes them somewhat less deadly than they would otherwise be.

Some dwarves like giant eagles for their *high soaring*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Through the use of the latest magma-powered and minecart-driven science, we have solved the riddle of whether a dwarf carrying a ◄gold ring► can be flown to a volcano to dispose of said ring: It cannot.

-

  The terror of the skies.

-

  Nice once you get to know them.

    [CREATURE:GIANT_EAGLE]
        [COPY_TAGS_FROM:BIRD_EAGLE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:5701]
        [GO_TO_START]
        [NAME:giant eagle:giant eagles:giant eagle]
        [CASTE_NAME:giant eagle:giant eagles:giant eagle]
        [GENERAL_CHILD_NAME:giant eagle chick:giant eagle chicks]
        [DESCRIPTION:A huge monster in the form of an eagle.]
        [POPULATION_NUMBER:15:30]
        [CREATURE_TILE:'E']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:high soaring]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
