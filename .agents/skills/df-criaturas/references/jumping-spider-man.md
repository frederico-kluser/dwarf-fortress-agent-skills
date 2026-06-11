# Jumping spider man

> Fonte: [Jumping spider man](https://dwarffortresswiki.org/index.php/Jumping_spider_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes jumping spider men for their ability to leap.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Jumping spider - Jumping spider man - Giant jumping spider**
- **Attributes**
- **Alignment:** Savage
- **No Stun · No Pain · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and arms of a jumping spider.*

**Jumping spider men** are animal people variants of the common jumping spider, who can inhabit most savage biomes. They spawn in groups of 1-3 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, jumping spider men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode. They feel no fear or pain and can't be stunned, and their three pairs of arms allow them to carry multiple weapons and shields at once.

Some dwarves like jumping spider men for their *striking appearance* and their *ability to leap*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Why don't YOU guess what goes here? Guess. Just guess.

Incidentally, the ASCII character '`j`' looks like a person jumping forwards!

It is currently unknown whether jumping spider women throw tea parties or hold bake sales.

Does whatever a ju- Nah, too easy.\
*Art by Devilingo*

|  |
|----|
| "Jumping spider man" in other / Languages / Dwarven / : / mâtzang sethal udos / Elven / : / efami thepani onino / Goblin / : / stoxus utes ngorûg / Human / : / itni azoc abo |

    [CREATURE:JUMPING_SPIDER_MAN]
        [COPY_TAGS_FROM:SPIDER_JUMPING]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:jumping spider man:jumping spider men:jumping spider man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:jumping spider woman:jumping spider women:jumping spider woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_EDGE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:jumping spider man:jumping spider men:jumping spider man]
        [DESCRIPTION:A person with the head and arms of a jumping spider.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'j']
        [COLOR:0:0:1]
