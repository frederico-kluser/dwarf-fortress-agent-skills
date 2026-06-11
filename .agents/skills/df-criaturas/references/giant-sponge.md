# Giant sponge

> Fonte: [Giant sponge](https://dwarffortresswiki.org/index.php/Giant_sponge) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant sponges for their squishy texture.**
- **Biome**
- **Any Ocean Any Lake Any River**
- **Variations**
- **Sponge - Sponge man - Giant sponge**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Genderless · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 560,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 20-30
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge immobile sponge.*

**Giant sponges** are larger versions of sponges, being found in savage rivers, lakes and oceans.

Physically, giant sponges are blobs made of "sponge" tissue. Their lack of articulations or body parts means they can only be killed through thorough pulping, but due to the sponge's weak material properties (even weaker than flesh), doing so with blunt weapons is not too difficult. However, their large size means they can shatter bones, articulations, bruise organs or even kill a dwarf via headshot using their default push attack. They may also themselves pulp body parts beyond recognition, as the push attack is also a blunt attack. How a giant sponge's soft structural tissue can break a dwarven skull is a mystery for the ages.

If some hapless dwarf appears near their water, giant sponges may feel suddenly threatened and charge (!) the hapless dwarf and engage in combat - the only occasion when they move at all. They may also become enraged or unconscious or feel pain, as utterly improbable as that sounds.

*"Without a nervous system, the only thing it can feel is ANGER."*

According to its raws, the giant sponge can not only be tamed but even *ridden as a war beast* by invaders. No reports of goblins or elves riding giant sponges has been documented, but maybe its strictly aquatic lifestyle prevents it from being chosen.

Some dwarves like giant sponges for their *squishy texture*.

## History

Before pulping was introduced in v0.40, giant sponges were virtually unkillable (atom smashing and cave-ins still worked). Due to this, they were widely considered the aquatic king of beasts.

## Bugs

- Rangers and Hunters may try to hunt giant sponges, wasting bolts that become lost in the water or lodged in the sponge itself. This may also lead to near-endless "Urist McHunterpants, Ranger cancels Hunt: Could Not Find Path" messages.

Still tickles to the touch.

    [CREATURE:GIANT_SPONGE]
        [COPY_TAGS_FROM:SPONGE]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1120]
        [GO_TO_START]
        [NAME:giant sponge:giant sponges:giant sponge]
        [CASTE_NAME:giant sponge:giant sponges:giant sponge]
        [DESCRIPTION:A huge immobile sponge.]
        [POPULATION_NUMBER:250:500]
        [CREATURE_TILE:'S']
        [COLOR:4:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:squishy texture]
