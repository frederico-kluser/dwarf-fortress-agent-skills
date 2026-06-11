# Giant bluejay

> Fonte: [Giant bluejay](https://dwarffortresswiki.org/index.php/Giant_bluejay) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant bluejays for their coloration.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Temperate Broadleaf Forest Temperate Coniferous Forest**
- **Variations**
- **Blue jay - Bluejay man - Giant bluejay**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,070 cm 3
- **Max:** 200,700 cm 3
- **Food products**
- **Eggs:** 2-7
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 19-21
- **Fat:** 12-14
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
- **Bones:** 24-26
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a bluejay.*

**Giant bluejays** are the giant animal version of blue jays, who appear in savage temperate biomes. While each giant bluejay is bigger than a grizzly bear, and they appear in flocks of 5-10 individuals, they pose little threat to your fortress, mostly flying idly over it in the skies. (They are not harmless, however, and can be agitated, with entire flocks of enraged azure birds attacking relentlessly and posing dangers to newly established dwarven colonies.)

If you get your marksdwarves to shoot them down or manage to catch one, they give a decent amount of meat, bone, fat, and edible organs, though nothing spectacular. A female giant bluejay lays clusters of 2-7 eggs, which makes them a worse alternative for egg production than all the common domestic poultry, but a better choice for the meat industry as they grow even quicker than both chickens and turkeys, and reach a much bigger size.

Giant bluejays can be tamed and sold by elves, and mounted by them in sieges.

Some dwarves like giant blue jays for their *coloration*.

So big that some dwarves mistake one for half the sky.\
*Art by GreenBox Art*

    [CREATURE:GIANT_BLUEJAY]
        [COPY_TAGS_FROM:BIRD_BLUEJAY]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:200700]
        [GO_TO_START]
        [NAME:giant bluejay:giant bluejays:giant bluejay]
        [CASTE_NAME:giant bluejay:giant bluejays:giant bluejay]
        [GENERAL_CHILD_NAME:giant bluejay hatchling:giant bluejay hatchlings]
        [DESCRIPTION:A huge monster in the form of a bluejay.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'B']
        [COLOR:1:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100]
