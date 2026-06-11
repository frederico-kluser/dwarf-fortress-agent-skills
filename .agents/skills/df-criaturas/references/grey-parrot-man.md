# Grey parrot man

> Fonte: [Grey parrot man](https://dwarffortresswiki.org/index.php/Grey_parrot_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes grey parrot men for their intelligence.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Grey parrot - Grey parrot man - Giant grey parrot**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,520 cm 3
- **Mid:** 17,600 cm 3
- **Max:** 35,200 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a grey parrot.*

**Grey parrot men** are animal people variants of the common grey parrot, who inhabit savage tropical moist broadleaf forests. They spawn in groups of 3-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All grey parrot men are born with Legendary skill in climbing.

Like other savage animal people, grey parrot men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like grey parrot men for their *social nature* and their *intelligence*.

Some have less beak.\
*Art by Enothar*

    [CREATURE:GREY_PARROT_MAN]
        [COPY_TAGS_FROM:BIRD_PARROT_GREY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:grey parrot man:grey parrot men:grey parrot man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:grey parrot woman:grey parrot women:grey parrot woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:grey parrot man:grey parrot men:grey parrot man]
        [DESCRIPTION:A person with the head and wings of a grey parrot.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:3:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'p']
        [COLOR:7:0:0]
