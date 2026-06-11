# Giant vulture

> Fonte: [Giant vulture](https://dwarffortresswiki.org/index.php/Giant_vulture) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant vultures for their patience.**
- **Biome**
- **Tropical Grassland Tropical Savanna Any Desert**
- **Variations**
- **Vulture - Vulture man - Giant vulture**
- **Attributes**
- **Alignment:** Savage
- **Flying · Steals food · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,463.5 cm 3
- **Mid:** 131,715 cm 3
- **Max:** 263,430 cm 3
- **Food products**
- **Eggs:** 1-3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 21
- **Fat:** 14
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 26
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a vulture.*

**Giant vultures** are enlarged cousins of the common vulture, found in savage deserts and some tropical plains. While their smaller counterparts usually do little more than cause job cancellation spam and fly off with a plump helmet sometimes, giant vultures are considerably more dangerous; not only do they retain the habit of stealing food, they are over four times the size of a dwarf and can be deadly to civilians who try to stop them during their thieving dives into your supplies (all while still causing lots of job cancellation spam). This makes them a real threat to a young savage embark, and if there are giant vultures in the region, the player should consider taking their food underground as soon as possible.

Like their small cousins, one can capture giant vultures with cage traps and train them into pets, who possess the standard high value of a giant creature. They are not any better than normal vultures when it comes to laying eggs, though they are comparably much better for a meat industry as they create a much higher quantity of meat, bones and fat. Giant vultures are also exotic mounts, so you may see elves riding them into battle in the event of a siege.

Some dwarves like giant vultures for their *patience*.

×4 the size. ×8 the danger.

    [CREATURE:GIANT_VULTURE]
        [COPY_TAGS_FROM:BIRD_VULTURE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2927]
        [GO_TO_START]
        [NAME:giant vulture:giant vultures:giant vulture]
        [CASTE_NAME:giant vulture:giant vultures:giant vulture]
        [GENERAL_CHILD_NAME:giant vulture hatchling:giant vulture hatchlings]
        [DESCRIPTION:A huge monster in the form of a vulture.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'V']
        [COLOR:4:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:patience]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
