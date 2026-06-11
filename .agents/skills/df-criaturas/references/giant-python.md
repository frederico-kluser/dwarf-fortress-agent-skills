# Giant python

> Fonte: [Giant python](https://dwarffortresswiki.org/index.php/Giant_python) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant pythons for their great size.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Python - Python man - Giant python**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 340 cm 3
- **Mid:** 425,000 cm 3
- **Max:** 1,700,000 cm 3
- **Food products**
- **Eggs:** 10-30
- **Age**
- **Adult at:** Birth
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 13-21
- **Fat:** 4
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 3-5
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 10
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a python.*

**Giant pythons** are the largest snakes in the game, larger than hippos and walruses. While not poisonous, their bite is strong enough to reliably tear entire limbs off your dwarves, armor and all. They should only be approached by multiple seasoned military dwarves in full regalia, or better yet, avoided entirely.

Giant pythons can be captured and tamed. With 10 to 30 eggs per clutch, they will breed exponentially if you manage to get a couple of them. Giant pythons require 20 years of growth to reach full size, but only live 10-20 years, meaning they rarely reach their most imposing size.

Some dwarves admire giant pythons for their *great size*.

Allows one human to ride it, but no more.\
*Art by AlexShiga*

    [CREATURE:GIANT_PYTHON]
        [COPY_TAGS_FROM:PYTHON]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:850]
        [GO_TO_START]
        [NAME:giant python:giant pythons:giant python]
        [CASTE_NAME:giant python:giant pythons:giant python]
        [DESCRIPTION:A huge monster in the form of a python.]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:great size]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:3512:2634:1756:878:4900:6900] 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
