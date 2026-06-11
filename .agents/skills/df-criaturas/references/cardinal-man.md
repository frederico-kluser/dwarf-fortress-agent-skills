# Cardinal man

> Fonte: [Cardinal man](https://dwarffortresswiki.org/index.php/Cardinal_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cardinal men for their coloration.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Temperate Broadleaf Forest Temperate Coniferous Forest**
- **Variations**
- **Cardinal - Cardinal man - Giant cardinal**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 5,604 cm 3
- **Max:** 35,025 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a cardinal.*

**Cardinal men** are animal people variants of the common cardinal, who inhabit a number of savage temperate biomes, spawn in groups of anywhere between 5-10 individuals, and are generally content to keep to themselves. In terms of size, they are little over half the weight of the average dwarf. All cardinal men are born with Legendary skill in climbing.

Like other savage animal people, cardinal men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like cardinal men for their *coloration*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Cardinal men, despite popular belief, do not elect religious leaders.

Some cardinal men display an obsessive interest in fortress administration and will campaign aggressively for the Bookkeeper noble position. Such cardinal men are rarely satisfied with the standard "Highest" precision setting, claiming it only accounts for a limited infinity of inventory. They are vocal proponents of quantum stockpiles and will frequently pause work to lecture the Manager that a single 1x1 tile containing an infinite stack of ☼masterwork koala roasts☼ can easily accommodate a caravan bringing an infinite number of additional roasts, provided that haulers are instructed to shift roasts to a new barrel number. They claim that even an infinite number of caravans cannot exhaust the stockpile space, provided that haulers shift roasts in a diagonal fashion. Cardinal men with the stonecutter labor activated will build fortifications by recursively adding the middle third of the next block, arguing that the resulting fortification lets in zero sunlight but still provides an infinite number of holes to shoot bolts through.

Cardinal men are often antagonized by rival leopard men who strictly prefer integer-based accounting. These leopard men will publicly denounce the cardinal man's theories as "Elven charlatanism", often shouting that "Armok made the integers, all else is the work of dwarves." Unfortunately, this harassment often interrupts cardinal men during their strange mood. Unable to locate the quires required to complete their transfinite book, and blocked by the leopard man from the craftsdwarf's workshop, the cardinal man will inevitably fail his mood and succumb to melancholy. They will sadly wander the fortress hospital zone, refusing to eat or drink, eventually dehydrating to death.

The feathers almost sparkle at you.\
*Art by Codaine420*

    [CREATURE:CARDINAL_MAN]
        [COPY_TAGS_FROM:BIRD_CARDINAL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:cardinal man:cardinal men:cardinal man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:cardinal woman:cardinal women:cardinal woman]
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
        [NAME:cardinal man:cardinal men:cardinal man]
        [DESCRIPTION:A person with the head and wings of a cardinal.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:4:0:1]
