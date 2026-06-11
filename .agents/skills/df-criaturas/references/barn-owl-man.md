# Barn owl man

> Fonte: [Barn owl man](https://dwarffortresswiki.org/index.php/Barn_owl_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes barn owl men for their coloration.**
- **Biome**
- **Any Wetland Any Temperate Forest Tropical Coniferous Forest Tropical Dry Broadleaf Forest Any Shrubland Any Savanna Any Grassland Any Desert**
- **Variations**
- **Barn owl - Barn owl man - Giant barn owl**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 2,115 cm 3
- **Mid:** 17,625 cm 3
- **Max:** 35,250 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the arms and wings of a barn owl.*

**Barn owl men** are humanoid versions of the common barn owl and a species of unremarkable animal people, found in a wide variety of savage biomes. They are a little over half the size of an adult dwarf and spawn in groups of 5-10 individuals, who are unlikely to pose any danger to your fortress unless provoked. All barn owl men are born with Legendary skill in climbing.

Like other savage animal people, barn owl men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like barn owl men for their *coloration*.

Sleeps during the day, but blames it on his owl DNA. Not his laziness.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Despite some myths and tales told by humans to their young, barn owl men have not been observed to be any wiser than other creatures, though their natural attraction to museums and scholarly careers may lead one to believe such a thing is true, especially when said owls blather on incessantly about whatever artifact is brought up in a conversation.

    [CREATURE:BARN_OWL_MAN]
        [COPY_TAGS_FROM:BIRD_OWL_BARN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:barn owl man:barn owl men:barn owl man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:barn owl woman:barn owl women:barn owl woman]
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
        [NAME:barn owl man:barn owl men:barn owl man]
        [DESCRIPTION:A person with the arms and wings of a barn owl.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:6:0:0]
