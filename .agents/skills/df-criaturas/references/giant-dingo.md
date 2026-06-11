# Giant dingo

> Fonte: [Giant dingo](https://dwarffortresswiki.org/index.php/Giant_dingo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant dingoes for their coloration.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Dingo - Dingo man - Giant dingo**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 34,180 cm 3
- **Mid:** 170,900 cm 3
- **Max:** 341,800 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 13-19
- **Fat:** 12-16
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 0-2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 18-22
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a dingo.*

Imagine a wild, yellow dog, but slightly smaller than a polar bear. That is the **giant dingo**.

Giant dingoes spawn in every non-freezing savage part of the world, and not only are they far larger than the usual dwarf, they spawn in packs and will attack your dwarves.

Giant dingoes are exotic pets and can breed.

## In adventure mode

They are scary opponents, far more dangerous (and common) than wolves, and a creature you will probably lose a few adventurers to. Do not engage them without full armor and a few friends. They are very fast and in savage worlds can be found in large packs even reaching a dozen dingoes. Be wary when fighting a pack of dingoes head on, and make sure you have space to run. Getting surrounded by these beasts can lead to a lot of fun.

Packs of common giant dingoes are much more dangerous than ones that are named historical figures, since the "legendary" giant dingo will always operate on its own.

## In fortress mode

Do not let non-military dwarves next to them. Alternatively, cage them in traps, tame them, and start a giant dingo breeding program. While not trainable, they are deadlier than most bears and, due to their [`[LARGE_PREDATOR]`](/index.php/Creature_token#LARGE_PREDATOR "Creature token") tag, they will attack enemies. As such, they make a good replacement for your dogs, and making them trainable is only a minor modding task.

He used to have a living squad.\
*Art by Devilingo*

    [CREATURE:GIANT_DINGO]
        [COPY_TAGS_FROM:DINGO]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1709]
        [GO_TO_START]
        [NAME:giant dingo:giant dingoes:giant dingo]
        [CASTE_NAME:giant dingo:giant dingoes:giant dingo]
        [GENERAL_CHILD_NAME:giant dingo pup:giant dingo pups]
        [DESCRIPTION:A huge monster in the form of a dingo.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:3:12]
        [CREATURE_TILE:'D']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:coloration]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
