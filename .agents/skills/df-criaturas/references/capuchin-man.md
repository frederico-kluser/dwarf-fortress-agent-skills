# Capuchin man

> Fonte: [Capuchin man](https://dwarffortresswiki.org/index.php/Capuchin_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes capuchin men for their social nature.**
- **Biome**
- **Any Tropical Forest Mangrove Swamp**
- **Variations**
- **Capuchin - Capuchin man - Giant capuchin**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,675 cm 3
- **Mid:** 18,375 cm 3
- **Max:** 36,750 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a capuchin.*

**Capuchin men** are animal people variants of the common capuchin who can be found in savage tropical forests and swamps. They spawn in groups of 5-10 individuals and share their animal counterparts' penchant for thievery, running off with any food or items they may stumble into. In terms of size, they are a little over half the weight of the average dwarf. All capuchin men are born with Legendary skill in climbing.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like capuchin men for their *social nature* and their *intelligence*.

    [CREATURE:CAPUCHIN_MAN]
        [COPY_TAGS_FROM:CAPUCHIN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:capuchin man:capuchin men:capuchin man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:capuchin woman:capuchin women:capuchin woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:capuchin man:capuchin men:capuchin man]
        [DESCRIPTION:A person with the head and tail of a capuchin.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:7:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
