# Grackle man

> Fonte: [Grackle man](https://dwarffortresswiki.org/index.php/Grackle_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes grackle men for their raucous calls.**
- **Biome**
- **Temperate Grassland Temperate Savanna**
- **Variations**
- **Grackle - Grackle man - Giant grackle**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,213.8333333333 cm 3
- **Max:** 35,060 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a grackle.*

**Grackle men** are animal people variants of the common grackle who inhabit savage temperate savannas and grasslands. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All grackle men are born with Legendary skill in climbing.

Like other savage animal people, grackle men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like grackle men for their *raucous calls*.

Always brings her famous "Earthworm Wine" to taverns, and it tastes better than it sounds.\
*Art by Cynthia Burke*

    [CREATURE:GRACKLE_MAN]
        [COPY_TAGS_FROM:BIRD_GRACKLE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:grackle man:grackle men:grackle man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:grackle woman:grackle women:grackle woman]
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
        [NAME:grackle man:grackle men:grackle man]
        [DESCRIPTION:A person with the head and wings of a grackle.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'g']
        [COLOR:0:0:1]
