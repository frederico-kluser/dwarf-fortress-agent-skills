# Snowy owl man

> Fonte: [Snowy owl man](https://dwarffortresswiki.org/index.php/Snowy_owl_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes snowy owl men for their yellow eyes.**
- **Biome**
- **Tundra**
- **Variations**
- **Snowy owl - Snowy owl man - Giant snowy owl**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,080 cm 3
- **Mid:** 18,000 cm 3
- **Max:** 36,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the wings and head of a snowy owl.*

**Snowy owl men** are animal people variants of the common snowy owl who inhabit savage tundras. They spawn in groups of anywhere between 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All snowy owl men are born with Legendary skill in climbing.

Like other savage animal people, snowy owl men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like snowy owl men for their *coloration* and their *yellow eyes*.

    [CREATURE:SNOWY_OWL_MAN]
        [COPY_TAGS_FROM:BIRD_OWL_SNOWY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:snowy owl man:snowy owl men:snowy owl man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:snowy owl woman:snowy owl women:snowy owl woman]
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
        [NAME:snowy owl man:snowy owl men:snowy owl man]
        [DESCRIPTION:A person with the wings and head of a snowy owl.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'o']
        [COLOR:7:0:1]
