# Kea man

> Fonte: [Kea man](https://dwarffortresswiki.org/index.php/Kea_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kea men for their intelligence.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Mountain**
- **Variations**
- **Kea - Kea man - Giant kea**
- **Attributes**
- **Alignment:** Savage
- **Flying · Steals food · Steals items · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 2,130 cm 3
- **Mid:** 17,750 cm 3
- **Max:** 35,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A green person with the head of a kea.*

**Kea men** are animal people variants of the common kea, who inhabit most savage mountains, tropical forests and shrublands. They spawn in groups of anywhere between 5-10 individuals and, just like the normal birds, will eagerly attempt to steal your food and items. In terms of size, they are a little over half the weight of the average dwarf, which makes them fairly weak in general, but a step above the easily-killed tiny parrot. All kea men are born with Legendary skill in climbing.

Like other savage animal people, kea men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like kea men for their *curiosity* and their *intelligence*.

Favorite food: worms.

    [CREATURE:KEA_MAN]
        [COPY_TAGS_FROM:BIRD_KEA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:kea man:kea men:kea man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:kea woman:kea women:kea woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TALON_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:kea man:kea men:kea man]
        [DESCRIPTION:A green person with the head of a kea.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'k']
        [COLOR:2:0:0]
