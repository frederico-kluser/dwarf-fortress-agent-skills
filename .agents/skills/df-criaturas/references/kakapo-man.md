# Kakapo man

> Fonte: [Kakapo man](https://dwarffortresswiki.org/index.php/Kakapo_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kakapo men for their flightlessness.**
- **Biome**
- **Temperate Shrubland Temperate Savanna Temperate Grassland Any Temperate Forest**
- **Variations**
- **Kakapo - Kakapo man - Giant kakapo**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 608.33333333333 cm 3
- **Mid:** 18,250 cm 3
- **Max:** 36,500 cm 3
- **Age**
- **Adult at:** 7
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a kakapo.*

**Kakapo men** are humanoid versions of the common kakapo and a species of unremarkable animal people, found in some savage temperate biomes. They are only a little over half the size of an adult dwarf and are unlikely to pose a threat to a fortress' inhabitants.

Like other savage animal people, kakapo men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like kakapo men for their *longevity*, their *flightlessness*, and their *booming calls*.

Just as fat as the standard birds.\
*Art by alymccart*

    [CREATURE:KAKAPO_MAN]
        [COPY_TAGS_FROM:BIRD_KAKAPO]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:kakapo man:kakapo men:kakapo man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:kakapo woman:kakapo women:kakapo woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:kakapo man:kakapo men:kakapo man]
        [DESCRIPTION:A person with the head and wings of a kakapo.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'k']
        [COLOR:2:0:0]
