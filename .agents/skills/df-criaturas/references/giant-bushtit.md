# Giant bushtit

> Fonte: [Giant bushtit](https://dwarffortresswiki.org/index.php/Giant_bushtit) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant bushtits for their somewhat great size.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Bushtit - Bushtit man - Giant bushtit**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 40,007 cm 3
- **Max:** 200,035 cm 3
- **Food products**
- **Eggs:** 5-13
- **Age**
- **Adult at:** 1
- **Max age:** 1-2
- **Butchering returns**
- **Food items**
- **Meat:** 27
- **Fat:** 19
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1-2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 32
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a bushtit.*

**Giant bushtits** are giant animal versions of common bushtits found in savage temperate forests. They are much more interesting than their mundane vermin basal creatures; they're quite large, growing to be slightly larger than a full-grown lion, and appear in clusters of five to ten individuals.

Being large, tamable, egg-laying, breeding creatures, they are very much worth capturing and taming, and given their large cluster numbers and a bit of luck you'll be able to hook a breeding pair. With five to thirteen eggs laid per clutch, giant bushtits can be used to establish an exotic egg farm; with a very nice distribution of meat products (if without a value multiplier), they can be made the basis of a strong meat industry; and with a perhaps surprisingly high pet value of 500, they can be made into excellent happiness vehicles for your fortress.

As a savage exotic mount that can fly, they may cause problems on the very small chance of a giant bushtit equipped elven siege.

Some dwarves prefer them for their *somewhat great size* (offhand insult?) and *twittering groups*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
A little known fact to dwarves is that human men will chase these creatures to the end of the earth, seeking little else than to rub a bar of \*Anaconda Soap\* on them.

    [CREATURE:GIANT_BUSHTIT]
        [COPY_TAGS_FROM:BIRD_BUSHTIT]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:4000700]
        [GO_TO_START]
        [NAME:giant bushtit:giant bushtits:giant bushtit]
        [CASTE_NAME:giant bushtit:giant bushtits:giant bushtit]
        [GENERAL_CHILD_NAME:giant bushtit hatchling:giant bushtit hatchlings]
        [DESCRIPTION:A huge monster in the form of a bushtit.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'B']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:somewhat great size]
        [PREFSTRING:twittering groups]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
