# Giant echidna

> Fonte: [Giant echidna](https://dwarffortresswiki.org/index.php/Giant_echidna) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant echidnas for their spines.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland Any Desert**
- **Variations**
- **Echidna - Echidna man - Giant echidna**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 27.05 cm 3
- **Mid:** 135,250 cm 3
- **Max:** 270,500 cm 3
- **Food products**
- **Eggs:** 1
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 13
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
- **Bones:** 18
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the shape of an echidna.*

A larger version of the echidna which elves will sometimes bring to trade. Like its smaller counterpart, a giant echidna will lay an egg in a nest box. Their clutch size is 1, so breeding them can take a while. They cannot be trained into war or hunting animals.

Still has a craving for ants.

## Bugs

If a curled-up or retracted creature dies, and is then reanimated by a necromancer, it retains the effects of being curled-up, but can move and attack as normal. As a result, for example an undead echidna is invulnerable to destructionBug:11463. It combines well with a separate bug that allows curled-up undead to attackBug:10519.

As a result, the undead echidna may at the same time be curled-up (making it unkillable) and move/attack. The same problem also affects the echidna man, giant echidna, giant hedgehog and hedgehog man.

Modding the game and removing \[PREVENTS_PARENT_COLLAPSE\] from the spine body part of the affected animals will allow them to be pulped and killed while curled up. While it makes normal echidnas weaker, this is not a major problem, as echidnas are not supposed to be really hard to kill. This workaround may restore otherwise unplayable games.

It was also reported that in adventure mode "I was able to finally kill the zombie by lighting fires underneath him/around him then waiting for a long time; eventually he 'died in the heat.'"Bug:10519.

    [CREATURE:GIANT_ECHIDNA]
        [COPY_TAGS_FROM:ECHIDNA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:2705]
        [GO_TO_START]
        [NAME:giant echidna:giant echidnas:giant echidna]
        [CASTE_NAME:giant echidna:giant echidnas:giant echidna]
        [GENERAL_CHILD_NAME:giant echidna puggle:giant echidna puggles]
        [DESCRIPTION:A large monster in the shape of an echidna.]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'E']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:spines]
        [PREFSTRING:egg-laying]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
