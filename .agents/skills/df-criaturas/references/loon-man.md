# Loon man

> Fonte: [Loon man](https://dwarffortresswiki.org/index.php/Loon_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes loon men for their coloration.**
- **Biome**
- **Temperate Saltwater Lake Temperate Brackish Lake Temperate Freshwater Lake**
- **Variations**
- **Loon - Loon man - Giant loon**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 950 cm 3
- **Mid:** 19,000 cm 3
- **Max:** 38,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a loon.*

**Loon men** are animal people variants of the common loon, who inhabit savage, temperate lakes. They spawn in groups of anywhere between 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a bit over half the weight of the average dwarf. All loon men are born with Legendary skill in climbing.

Like other savage animal people, loon men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like loon men for their *coloration* and their *haunting call*.

Painting of loon women.

    [CREATURE:LOON_MAN]
        [COPY_TAGS_FROM:BIRD_LOON]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:loon man:loon men:loon man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:loon woman:loon women:loon woman]
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
        [NAME:loon man:loon men:loon man]
        [DESCRIPTION:A person with the head and wings of a loon.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'l']
        [COLOR:0:0:1]
