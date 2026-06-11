# Red-winged blackbird man

> Fonte: [Red-winged blackbird man](https://dwarffortresswiki.org/index.php/Red-winged_blackbird_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes red-winged blackbird men for their coloration.**
- **Biome**
- **Temperate Freshwater Marsh Temperate Saltwater Marsh**
- **Variations**
- **Red-winged blackbird - Red-winged blackbird man - Giant red-winged blackbird**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 7,005 cm 3
- **Max:** 35,025 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a red-winged blackbird.*

**Red-winged blackbird men** are animal people variants of the common red-winged blackbird who inhabit savage temperate wetlands. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All red-winged blackbird men are born with Legendary skill in climbing.

Like other savage animal people, red-winged blackbird men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like red-winged blackbird men for their *coloration*.

    [CREATURE:RW_BLACKBIRD_MAN]
        [COPY_TAGS_FROM:BIRD_RW_BLACKBIRD]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:red-winged blackbird man:red-winged blackbird men:red-winged blackbird man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:red-winged blackbird woman:red-winged blackbird women:red-winged blackbird woman]
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
        [NAME:red-winged blackbird man:red-winged blackbird men:red-winged blackbird man]
        [DESCRIPTION:A person with the head and wings of a red-winged blackbird.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'r']
        [COLOR:0:0:1]
