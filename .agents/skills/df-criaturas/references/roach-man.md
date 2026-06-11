# Roach man

> Fonte: [Roach man](https://dwarffortresswiki.org/index.php/Roach_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes roach men for their ability to disgust.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **- Roach man - Large roach - Giant roach**
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

*A person with the wings and head of a roach.*

**Roach men** are humanoid versions of the common large roach and a species of unremarkable animal people, found in most non-freezing savage biomes. They are only a little over half the size of an adult dwarf and are unlikely to pose a threat to a fortress' inhabitants. All roach men are born with Legendary skill in climbing.

Like other savage animal people, roach men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like roach men for their *ability to disgust*.

Still as disgusting as the original roach.

    [CREATURE:ROACH_MAN]
        [COPY_TAGS_FROM:ROACH_LARGE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:roach man:roach men:roach man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:roach woman:roach women:roach woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:roach man:roach men:roach man]
        [DESCRIPTION:A person with the wings and head of a roach.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'r']
        [COLOR:6:0:0]
