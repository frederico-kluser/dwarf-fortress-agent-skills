# Monitor lizard man

> Fonte: [Monitor lizard man](https://dwarffortresswiki.org/index.php/Monitor_lizard_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes monitor lizard men for their intelligence.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Monitor lizard - Monitor lizard man - Giant monitor lizard**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 51 cm 3
- **Mid:** 42,500 cm 3
- **Max:** 85,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a monitor lizard.*

**Monitor lizard men** are humanoid versions of the common monitor lizard and a species of unremarkable animal people, found in savage tropical forests and plains. They are a little larger than the average adult dwarf, and may pose a threat if confronted by unarmed civilians. They share their animal counterparts' rarity, and no more than 10 of them will spawn in the biome before they are extinct.

Like other savage animal people, monitor lizard men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like monitor lizard men for their *intelligence*.

    [CREATURE:MONITOR_LIZARD_MAN]
        [COPY_TAGS_FROM:MONITOR_LIZARD]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:monitor lizard man:monitor lizard men:monitor lizard man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:monitor lizard woman:monitor lizard women:monitor lizard woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:CLAW_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:monitor lizard man:monitor lizard men:monitor lizard man]
        [DESCRIPTION:A person with the head and tail of a monitor lizard.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'M']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
