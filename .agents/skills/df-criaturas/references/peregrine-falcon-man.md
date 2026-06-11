# Peregrine falcon man

> Fonte: [Peregrine falcon man](https://dwarffortresswiki.org/index.php/Peregrine_falcon_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes peregrine falcon men for their ability to dive through the air.**
- **Biome**
- **Any Wetland Any Temperate Forest Tropical Coniferous Forest Tropical Dry Broadleaf Forest Taiga Any Shrubland Any Savanna Any Grassland Any Desert Mountain Tundra**
- **Variations**
- **Peregrine falcon - Peregrine falcon man - Giant peregrine falcon**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 2,588.6666666667 cm 3
- **Mid:** 17,650 cm 3
- **Max:** 35,300 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a peregrine falcon.*

**Peregrine falcon men** are humanoid versions of the common peregrine falcon and a species of animal people, found in most savage biomes. They are only a little over half the size of an adult dwarf and retain many characteristics from their non-humanoid cousins, including diving from the sky to hunt vermin and an exceptional flight speed - peregrine falcon men are the fastest fliers of all animal people, moving at the maximum gait of 87 kph. Unlike normal falcons, a male peregrine falcon man is not called a tiercel peregrine. All peregrine falcon men are born with Legendary skill in climbing.

Like other savage animal people, peregrine falcon men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode. Their incredible flight speed makes them an attractive choice for an adventurer when flight speed is a priority.

Some dwarves like peregrine falcon men for their *ability to dive through the air*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
When engaged in combat, peregrine falcon men will demand their foes "Come on!" and "Show me your moves!" at any given opportunity. Their preferable style of combat is throwing punches of immense strength at their unfortunate opponent.

Highly competitive with other birds.\
*Art by lupinemoonfeather\
Commissioned by gyrflcn*

    [CREATURE:PEREGRINE FALCON MAN]
        [COPY_TAGS_FROM:BIRD_FALCON_PEREGRINE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [CV_REMOVE_TAG:DIVE_HUNTS_VERMIN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:peregrine falcon man:peregrine falcon men:peregrine falcon man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:peregrine falcon woman:peregrine falcon women:peregrine falcon woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TALON_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:300:200:100:1900:2900] 87+ kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:peregrine falcon man:peregrine falcon men:peregrine falcon man]
        [DESCRIPTION:A person with the head and wings of a peregrine falcon.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'p']
        [COLOR:6:0:0]
