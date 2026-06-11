# White stork man

> Fonte: [White stork man](https://dwarffortresswiki.org/index.php/White_stork_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes white stork men for their long necks.**
- **Biome**
- **Any Grassland Any Wetland**
- **Variations**
- **White stork - White stork man - Giant white stork**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,216.6666666667 cm 3
- **Mid:** 18,250 cm 3
- **Max:** 36,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a stork, also standing on long legs.*

**White stork men** are animal people variants of the common white stork who inhabit savage wetlands and grasslands. They spawn in groups of 2-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, white stork men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like white stork men for their *long necks*, their *long legs* and their *long bills*.

Heard all the "baby carrying" jokes.\
*Art by ivanprime93*

    [CREATURE:WHITE_STORK_MAN]
        [COPY_TAGS_FROM:BIRD_STORK_WHITE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:white stork man:white stork men:white stork man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:white stork woman:white stork women:white stork woman]
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
        [NAME:white stork man:white stork men:white stork man]
        [DESCRIPTION:A person with the head and wings of a stork, also standing on long legs.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:7:0:1]
