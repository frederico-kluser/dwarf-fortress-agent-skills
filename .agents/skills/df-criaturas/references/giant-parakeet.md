# Giant parakeet

> Fonte: [Giant parakeet](https://dwarffortresswiki.org/index.php/Giant_parakeet) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant parakeets for their coloration.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Parakeet - Parakeet man - Giant parakeet**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 16,736.7 cm 3
- **Max:** 200,840.4 cm 3
- **Food products**
- **Eggs:** 2-4
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 17
- **Fat:** 11
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 24
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of a parakeet.*

**Giant parakeets** are much larger cousins of their original counterparts, and fast moving birds found in any tropical land biome except for swamps and marshes. They will pose as a nuisance more than a threat, and are likely to cause mass cancellation spam from anyone working above ground. Tight groups of 5-10 will appear, and haphazardly fly around. They will not attack a dwarf on sight, and can be dispatched by your military fairly easily. In combat, they can overpower and kill an unarmored dwarf unlucky enough to be caught. Fortunately, they will not actively pursue a dwarf as it flees, and will often use its large wings, which inflict much less severe injuries than its beak or talons.

They make a poor choice for your egg industry, with a clutch size of only 2-4, but a very manageable addition to your meat industry if bred. It takes only one year for hatchlings to fully mature; however, with a pet value of 500, they may be worth more as pets in your zoo, than as roasts and crafts. They are considered exotic animals, and your trainers will have no initial knowledge of their habits.

    [CREATURE:GIANT_PARAKEET]
        [COPY_TAGS_FROM:BIRD_PARAKEET]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:167367]
        [GO_TO_START]
        [NAME:giant parakeet:giant parakeets:giant parakeet]
        [CASTE_NAME:giant parakeet:giant parakeets:giant parakeet]
        [GENERAL_CHILD_NAME:giant parakeet hatchling:giant parakeet hatchlings]
        [DESCRIPTION:A large monster in the shape of a parakeet.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'P']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [PREFSTRING:ability to speak]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
