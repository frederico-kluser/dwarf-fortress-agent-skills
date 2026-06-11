# Giant thrips

> Fonte: [Giant thrips](https://dwarffortresswiki.org/index.php/Giant_thrips) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant thrips for their prolific breeding.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Thrips - Thrips man - Giant thrips**
- **Attributes**
- **Alignment:** Savage
- **Flying · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 1-1
- **Butchering returns**
- **Food items**
- **Meat:** 28-82
- **Fat:** 15-20
- **Brain:** 2
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a thrips.*

A long, short-legged, flying insect the size of a giant cave spider, it has no direct means of attack, but like all insects it will push and wrestle enemies with legs and wings pretty well, even if it shouldn't be intelligent enough to do so. Also, they seem to be able to throw dwarves disproportionately long distances, sometimes resulting in dwarven explosions when thrown. If aggressive, they are a match for a dwarf, and will probably win the ensuing fight.

Thrips and giant thrips, despite being well-known agricultural pests, will do no harm to plants for now. They mostly spend their time flying high above ground in groups of five to ten, generally doing nothing useful and preventing more interesting animals from entering your map. Can be used as a food source or marksdwarf training target. They make for poor livestock since their maximum age is one year.

## Adventure Mode

Giant thrips are useful in Adventure Mode, as they take a long time to die. Because of their armor-like chitin, most attacks, even to the head, won't cause much damage besides shattering the chitin, which does not bleed like flesh does. This means that they make great training dummies to train up weapon skills on. As long as you avoid slicing off body parts so they don't bleed too much, a giant thrips should stay alive for a long time while you slice/bash the heck out of it. They aren't dangerous opponents at all, and most of the time all they will do is charge you harmlessly.

    [CREATURE:GIANT_THRIPS]
        [COPY_TAGS_FROM:THRIPS]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant thrips:giant thrips:giant thrips]
        [CASTE_NAME:giant thrips:giant thrips:giant thrips]
        [DESCRIPTION:A huge monster in the form of a thrips.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'T']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:prolific breeding]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
