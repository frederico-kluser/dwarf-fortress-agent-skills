# Giant peregrine falcon

> Fonte: [Giant peregrine falcon](https://dwarffortresswiki.org/index.php/Giant_peregrine_falcon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant peregrine falcons for their ability to dive through the air.**
- **Biome**
- **Any Wetland Any Temperate Forest Tropical Coniferous Forest Tropical Dry Broadleaf Forest Taiga Any Shrubland Any Savanna Any Grassland Any Desert Mountain Tundra**
- **Variations**
- **Peregrine falcon - Peregrine falcon man - Giant peregrine falcon**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 8,308.08 cm 3
- **Mid:** 56,646 cm 3
- **Max:** 113,292 cm 3
- **Food products**
- **Eggs:** 3-4
- **Age**
- **Adult at:** 1
- **Max age:** 12-15
- **Butchering returns**
- **Food items**
- **Meat:** 18
- **Fat:** 11
- **Brain:** 1
- **Gizzard:** 1
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
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large bird monster that is the same shape as a peregrine falcon.*

**Giant peregrine falcons** are enlarged cousins of the common peregrine falcon, found in most savage biomes. Despite being nearly twice the size of the average dwarf, these somewhat small giants are as benign as their original counterparts, spending their time diving down to kill vermin in the surface, though their larger size means they can potentially scare livestock and cause job cancellations from dwarves venturing outside. Like normal falcons, males of the species are known as giant tiercel peregrins and are significantly smaller than females. All giant peregrine falcons are born with Legendary skill in climbing.

Like their small cousins, one can capture giant peregrine falcons with cage traps and train them into pets, who possess the standard high value of a giant creature. They are not any better than normal peregrine falcons when it comes to laying eggs, though they differ for being actually useful for a meat industry, being large enough to produce meat, bones and fat when butchered. Giant peregrine falcons are also exotic mounts, so you may see elves riding them into battle in the event of a siege, which coupled with their incredible flying speed may lead to unexpected amounts of fun.

Some dwarves like giant peregrine falcons for their *ability to dive through the air*.

    [CREATURE:GIANT PEREGRINE FALCON]
        [COPY_TAGS_FROM:BIRD_FALCON_PEREGRINE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:18882]
        [GO_TO_START]
        [NAME:giant peregrine falcon:giant peregrine falcons:giant peregrine falcon]
        [GENERAL_CHILD_NAME:giant peregrine falcon chick:giant peregrine falcon chicks]
        [DESCRIPTION:A large bird monster that is the same shape as a peregrine falcon.]
        [CREATURE_TILE:'P']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:giant tiercel peregrine:giant tiercel peregrines:giant tiercel peregrine]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:giant peregrine falcon:giant peregrine falcons:giant peregrine falcon]
        [SELECT_CASTE:ALL]
        [PREFSTRING:ability to dive through the air]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:300:200:100:1900:2900] 87+ kph (110), need to work on base speed for fliers
                                                dive ~320
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
