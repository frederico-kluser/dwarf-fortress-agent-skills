# Oriole man

> Fonte: [Oriole man](https://dwarffortresswiki.org/index.php/Oriole_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes oriole men for their coloration.**
- **Biome**
- **Temperate Broadleaf Forest**
- **Variations**
- **Oriole - Oriole man - Giant oriole**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,128.5 cm 3
- **Max:** 35,020 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of an oriole.*

**Oriole men** are animal people variants of the common oriole, who inhabit savage temperate broadleaf forests. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All oriole men are born with Legendary skill in climbing.

Like other savage animal people, oriole men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like oriole men for their *coloration*.

    [CREATURE:ORIOLE_MAN]
        [COPY_TAGS_FROM:BIRD_ORIOLE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:oriole man:oriole men:oriole man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:oriole woman:oriole women:oriole woman]
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
        [NAME:oriole man:oriole men:oriole man]
        [DESCRIPTION:A person with the head and wings of an oriole.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'o']
        [COLOR:6:0:1]
