# Giant hedgehog

> Fonte: [Giant hedgehog](https://dwarffortresswiki.org/index.php/Giant_hedgehog) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant hedgehogs for their many spines.**
- **Biome**
- **Temperate Shrubland Temperate Savanna**
- **Variations**
- **Hedgehog - Hedgehog man - Giant hedgehog**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 205,600 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 14
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
- **Teeth:** 0-2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster with the shape of a hedgehog.*

**Giant hedgehogs**, although large, pose little threat to a fortress and have been observed to walk straight into your meeting area and get slaughtered by dogs.

## Bugs

If a curled-up or retracted creature dies, and is then reanimated by a necromancer, it retains the effects of being curled-up, but can move and attack as normal. As a result, for example an undead echidna is invulnerable to destructionBug:11463. It combines well with a separate bug that allows curled-up undead to attackBug:10519.

As a result, the undead echidna may at the same time be curled-up (making it unkillable) and move/attack. The same problem also affects the echidna man, giant echidna, giant hedgehog and hedgehog man.

Modding the game and removing \[PREVENTS_PARENT_COLLAPSE\] from the spine body part of the affected animals will allow them to be pulped and killed while curled up. While it makes normal echidnas weaker, this is not a major problem, as echidnas are not supposed to be really hard to kill. This workaround may restore otherwise unplayable games.

It was also reported that in adventure mode "I was able to finally kill the zombie by lighting fires underneath him/around him then waiting for a long time; eventually he 'died in the heat.'"Bug:10519.

It also appears that if it is trapped in a cage while rolled up (with the cage trap being placed under the hedgehog), it'll stay rolled up permanently, even if tamed and trained.

That's the baby version. It'll get meaner when it's older.

    [CREATURE:GIANT_HEDGEHOG]
        [COPY_TAGS_FROM:HEDGEHOG]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:25700]
        [GO_TO_START]
        [NAME:giant hedgehog:giant hedgehogs:giant hedgehog]
        [CASTE_NAME:giant hedgehog:giant hedgehogs:giant hedgehog]
        [DESCRIPTION:A large monster with the shape of a hedgehog.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'H']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:many spines]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100]
