# Skink man

> Fonte: [Skink man](https://dwarffortresswiki.org/index.php/Skink_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes skink men for their colorful tongues.**
- **Biome**
- **Any Temperate Any Tropical Any Desert**
- **Variations**
- **Skink - Skink man - Giant skink**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,250 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A long-bodied person with the head and tail of a skink.*

**Skink men** are humanoid versions of the common skink and a species of unremarkable animal people, found in a variety of savage regions. They are a bit over half the size of dwarves when adults and should pose no threat unless provoked. They spawn in groups of 1-5 individuals. All skink men are born with Legendary skill in climbing.

Like other savage animal people, skink men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like skink men for their *colorful tongues*.

    [CREATURE:SKINK_MAN]
        [COPY_TAGS_FROM:SKINK]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:skink man:skink men:skink man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:skink woman:skink women:skink woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:skink man:skink men:skink man]
        [DESCRIPTION:A long-bodied person with the head and tail of a skink.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:7:0:0]
