# Moth man

> Fonte: [Moth man](https://dwarffortresswiki.org/index.php/Moth_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes moth men for their coloration.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Moth - Moth man - Giant moth**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a moth.*

**Moth men** are animal people variants of the common moth, who can inhabit most savage biomes. They spawn in groups of 1-5 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf. All moth men are born with Legendary skill in climbing.

Like other savage animal people, moth men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like moth men for their *coloration*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Moth men are not, in fact, any sort of secretive paranormal monster, as dwarves find and kill them on a semiregular basis. The humans are just overreacting.

Additionally, and contrary to another popular human belief, moth men *do not* appear as a warning before cave-ins, structural failures or other unfortunate accidents. Warnings of such incidents should only be managed by burrow assignment rather than superstition. Get back to work.

Some human peasants have a strange preference for moth women.

|  |
|----|
| "Moth man" in other / Languages / Dwarven / : / alen udos / Elven / : / ìnevi onino / Goblin / : / atan ngorûg / Human / : / dunem abo |

    [CREATURE:MOTH_MAN]
        [COPY_TAGS_FROM:MOTH]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:moth man:moth men:moth man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:moth woman:moth women:moth woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:moth man:moth men:moth man]
        [DESCRIPTION:A person with the head and wings of a moth.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'m']
        [COLOR:6:0:0]
