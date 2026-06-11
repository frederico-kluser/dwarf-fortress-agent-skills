# Kestrel man

> Fonte: [Kestrel man](https://dwarffortresswiki.org/index.php/Kestrel_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kestrel men for their hunting prowess.**
- **Biome**
- **Tropical Freshwater Marsh Tropical Saltwater Marsh Temperate Freshwater Marsh Temperate Saltwater Marsh Any Shrubland Any Savanna Any Grassland**
- **Variations**
- **Kestrel - Kestrel man - Giant kestrel**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,215 cm 3
- **Mid:** 17,562.5 cm 3
- **Max:** 35,125 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a kestrel.*

**Kestrel men** are animal people variants of the common kestrel, who inhabit a variety of savage regions. They spawn in groups of anywhere between 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All kestrel men are born with Legendary skill in climbing.

Like other savage animal people, kestrel men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like kestrel men for their *coloration* and their *hunting prowess*.

Such grace! Such poise!\
*Art by Kaivris*

    [CREATURE:KESTREL_MAN]
        [COPY_TAGS_FROM:BIRD_KESTREL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:kestrel man:kestrel men:kestrel man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:kestrel woman:kestrel women:kestrel woman]
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
        [NAME:kestrel man:kestrel men:kestrel man]
        [DESCRIPTION:A person with the head and wings of a kestrel.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'k']
        [COLOR:4:0:0]
