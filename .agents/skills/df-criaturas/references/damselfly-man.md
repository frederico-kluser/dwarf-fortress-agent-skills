# Damselfly man

> Fonte: [Damselfly man](https://dwarffortresswiki.org/index.php/Damselfly_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes damselfly men for their coloration.**
- **Biome**
- **Any Lake**
- **Variations**
- **Damselfly - Damselfly man - Giant damselfly**
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

*A person with the wings and head of a damselfly.*

**Damselfly men** are animal people variants of the common damselfly who can appear in savage lakes. They spawn in groups of 2-5 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf. All damselfly men are born with Legendary skill in climbing.

\
Some dwarves like damselfly men for their *coloration*.

## Trivia

- The damselfly man uses the exact same sprite as the dragonfly man.

    [CREATURE:DAMSELFLY_MAN]
        [COPY_TAGS_FROM:DAMSELFLY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:damselfly man:damselfly men:damselfly man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:damselfly woman:damselfly women:damselfly woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:damselfly man:damselfly men:damselfly man]
        [DESCRIPTION:A person with the wings and head of a damselfly.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'d']
        [COLOR:3:0:1]
