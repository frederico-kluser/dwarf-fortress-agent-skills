# Gigantic tortoise

> Fonte: [Gigantic tortoise](https://dwarffortresswiki.org/index.php/Gigantic_tortoise) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gigantic tortoises for their great size.**
- **Biome**
- **Tropical Shrubland Tropical Savanna**
- **Variations**
- **Giant tortoise - Giant tortoise man - Gigantic tortoise**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Shell · Egglaying**
- **Tamed Attributes**
- **Pet value:** 1,500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 660.8 cm 3
- **Mid:** 1,239,000 cm 3
- **Max:** 2,478,000 cm 3
- **Food products**
- **Eggs:** 5-10
- **Age**
- **Adult at:** 1
- **Max age:** 100-200
- **Butchering returns**
- **Food items**
- **Meat:** 25-65
- **Fat:** 13-19
- **Brain:** 1-3
- **Heart:** 1
- **Lungs:** 2-6
- **Intestines:** 3-9
- **Liver:** 1-3
- **Kidneys:** 2
- **Tripe:** 1-3
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 22-38
- **Skull:** 1
- **Shell:** 5-15
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster with an enormous shell.*

**Gigantic tortoises** are the monstrous version of giant tortoises. Along with gigantic pandas and gigantic squids, they receive the "gigantic" title instead of "giant", since there is a normal version of those creatures that is already referred to as "giant".

Due to the fact that tortoises are not only benign, they also react first and foremost by retracting into their shell, if a herd of gigantic tortoises walk onto your map, it is possible to actually build cage traps directly underneath a tortoise that is in its shell to capture it without worry.

With the males half the size of an elephant at full size (5 years), these creatures provide enough food products to feed a decent-sized fortress for a year. Also, due to the fact that they are born in clutches of 5-10 at a time, a breeding pair and offspring of gigantic tortoises is fully capable of supplying all the food a fortress will ever need. For moods, they also provide shells.

While they are benign, they can still be used for your fortress defense; their shells are impressively difficult for enemy troops to penetrate (and nigh unbreakable for unarmed enemies), making them a great distraction that may as well be used to buy time as to give your dwarves a chance to attack unsuspecting goblins.

"That shell could be our second dining hall!"\
*Art by Romain Kurdi*

    [CREATURE:GIGANTIC TORTOISE]
        [COPY_TAGS_FROM:GIANT TORTOISE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [CHANGE_BODY_SIZE_PERC:826]
        [GO_TO_START]
        [NAME:gigantic tortoise:gigantic tortoises:gigantic tortoise]
        [CASTE_NAME:gigantic tortoise:gigantic tortoises:gigantic tortoise]
        [GENERAL_CHILD_NAME:gigantic tortoise hatchling:gigantic tortoise hatchlings]
        [DESCRIPTION:A huge monster with an enormous shell.]
        [POPULATION_NUMBER:10:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'T']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [PETVALUE:1500]
        [GO_TO_END]
        [PREFSTRING:great size]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:4732:4026:3327:1097:5922:7567] 8 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
