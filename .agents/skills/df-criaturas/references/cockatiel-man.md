# Cockatiel man

> Fonte: [Cockatiel man](https://dwarffortresswiki.org/index.php/Cockatiel_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cockatiel men for their crests.**
- **Biome**
- **Any Desert Temperate Grassland**
- **Variations**
- **Cockatiel - Cockatiel man - Giant cockatiel**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,893.8888888889 cm 3
- **Max:** 35,045 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A crested person with the head and wings of a cockatiel.*

**Cockatiel men** are animal people variants of the common cockatiel who inhabit savage deserts and temperate grasslands. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All cockatiel men are born with Legendary skill in climbing.

Like other savage animal people, cockatiel men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like cockatiel men for their *crests*.

    [CREATURE:COCKATIEL_MAN]
        [COPY_TAGS_FROM:BIRD_COCKATIEL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:cockatiel man:cockatiel men:cockatiel man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:cockatiel woman:cockatiel women:cockatiel woman]
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
        [NAME:cockatiel man:cockatiel men:cockatiel man]
        [DESCRIPTION:A crested person with the head and wings of a cockatiel.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:7:0:1]
