# Bluejay man

> Fonte: [Bluejay man](https://dwarffortresswiki.org/index.php/Bluejay_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bluejay men for their coloration.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Temperate Broadleaf Forest Temperate Coniferous Forest**
- **Variations**
- **Blue jay - Bluejay man - Giant bluejay**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,505 cm 3
- **Max:** 35,050 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a bluejay.*

**Bluejay men** are animal people variants of the common blue jay who inhabit a number of temperate biomes. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All bluejay men are born with Legendary skill in climbing. Bluejay men will generally not attack your dwarves, but can cancel work orders.

Like other savage animal people, bluejay men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like bluejay men for their *coloration*.

*Art by TfProxy, obviously*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Bluejay men are often seen befriending raccoon men and yetis, while having a troubled relationship with overweight goblins and ghosts.

Some Bluejay men have been observed hitting balls with clubs over great distances.

    [CREATURE:BLUEJAY_MAN]
        [COPY_TAGS_FROM:BIRD_BLUEJAY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:bluejay man:bluejay men:bluejay man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:bluejay woman:bluejay women:bluejay woman]
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
        [NAME:bluejay man:bluejay men:bluejay man]
        [DESCRIPTION:A person with the head and wings of a bluejay.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:1:0:1]
