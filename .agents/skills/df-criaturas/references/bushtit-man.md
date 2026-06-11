# Bushtit man

> Fonte: [Bushtit man](https://dwarffortresswiki.org/index.php/Bushtit_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bushtit men for their small size.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Bushtit - Bushtit man - Giant bushtit**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 7,000.5 cm 3
- **Max:** 35,002.5 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a bushtit.*

**Bushtit men** are animal people variants of the common bushtit who inhabit savage temperate forests. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All bushtit men are born with Legendary skill in climbing.

Like other savage animal people, bushtit men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like bushtit men for their *small size* and their *twittering groups*.

    [CREATURE:BUSHTIT_MAN]
        [COPY_TAGS_FROM:BIRD_BUSHTIT]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:bushtit man:bushtit men:bushtit man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:bushtit woman:bushtit women:bushtit woman]
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
        [NAME:bushtit man:bushtit men:bushtit man]
        [DESCRIPTION:A person with the head and wings of a bushtit.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:6:0:0]
