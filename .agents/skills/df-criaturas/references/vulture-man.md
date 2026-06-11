# Vulture man

> Fonte: [Vulture man](https://dwarffortresswiki.org/index.php/Vulture_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes vulture men for their patience.**
- **Biome**
- **Tropical Grassland Tropical Savanna Any Desert**
- **Variations**
- **Vulture - Vulture man - Giant vulture**
- **Attributes**
- **Alignment:** Savage
- **Flying · Steals food · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 219.44444444444 cm 3
- **Mid:** 19,750 cm 3
- **Max:** 39,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a vulture.*

**Vulture men** are humanoid versions of the common vulture and a species of animal people, found in savage deserts and tropical plains. They are only a little over half the size of an adult dwarf, being unlikely to pose a threat to a civilian's life, though they possess two significant traits: flight and the desire to steal your food. The former makes them difficult to attack, and the latter can be annoying to a newly-embarked fortress which has not yet set up their food industry or made farm plots.

Like other savage animal people, vulture men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like vulture men for their *patience*.

No less thieving than the flying kind.\
*Art by SupportCOMMAND*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

*A guide to Vulture Man culture and traditions by Kivish Aughra:*

- Vulture Men consider Elves, or **Elflings** as they call them, their mortal enemies, and make a point of ceremonially devouring their souls in dark rituals.
- They have been steadfast allies of the Crab Men since the dawn of time, and have been known to employ them as bodyguards and soldiers in their military.
- Have a habit of enslaving any race smaller than they are.
- They are very fond of crystalline gems and minerals, especially Amethysts.

|  |
|----|
| "Vulture man" in other / Languages / Dwarven / : / tikis udos / Elven / : / rathóna onino / Goblin / : / uzun ngorûg / Human / : / áspast abo |

    [CREATURE:VULTURE_MAN]
        [COPY_TAGS_FROM:BIRD_VULTURE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:vulture man:vulture men:vulture man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:vulture woman:vulture women:vulture woman]
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
        [NAME:vulture man:vulture men:vulture man]
        [DESCRIPTION:A person with the head and wings of a vulture.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'v']
        [COLOR:4:0:0]
