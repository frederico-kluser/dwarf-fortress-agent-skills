# Thrips man

> Fonte: [Thrips man](https://dwarffortresswiki.org/index.php/Thrips_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes thrips men for their prolific breeding.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Thrips - Thrips man - Giant thrips**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a thrips.*

**Thrips men** are animal people variants of the common thrips who can inhabit most savage biomes. They spawn in groups of 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the volume of the average dwarf. All thrips men are born with Legendary skill in climbing.

Like other savage animal people, thrips men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like thrips men for their *prolific breeding*.

    [CREATURE:THRIPS_MAN]
        [COPY_TAGS_FROM:THRIPS]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:thrips man:thrips men:thrips man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:thrips woman:thrips women:thrips woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:thrips man:thrips men:thrips man]
        [DESCRIPTION:A person with the head and wings of a thrips.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'t']
        [COLOR:6:0:0]
