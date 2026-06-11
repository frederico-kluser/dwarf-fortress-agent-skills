# Beetle man

> Fonte: [Beetle man](https://dwarffortresswiki.org/index.php/Beetle_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes beetle men for their protective shells.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Beetle - Beetle man - Giant beetle**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the carapace and head of a beetle.*

**Beetle men** are animal people variants of the common beetle, who can inhabit most savage biomes, spawning in groups of 2-5 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf. Like normal beetles, they have a pair of wings, but are unable to fly with them. All beetle men are born with Legendary skill in climbing.

Like other savage animal people, beetle men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like beetle men for their *protective shells*.

## Gallery

-

  Sort of "comes with" armor.

-

  Art by Jeff Agudelo

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
If allowed residence in a fortress, Beetle men may form immensely popular rock 'n roll bands. These bands have been known to cause a strange mood that primarily affects young female dwarves.

Beetle men wearing masks have been seen interacting with slug men, showing particular aggression towards red-tinted members.

Beetle men in groups of five are known to be dirty vile repulsive cheating scumbags who should never be given a happy ending.

|  |
|----|
| "Beetle man" in other / Languages / Dwarven / : / ngárak udos / Elven / : / pama onino / Goblin / : / strog ngorûg / Human / : / agthreb abo |

    [CREATURE:BEETLE_MAN]
        [COPY_TAGS_FROM:BEETLE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:beetle man:beetle men:beetle man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:beetle woman:beetle women:beetle woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:beetle man:beetle men:beetle man]
        [DESCRIPTION:A person with the carapace and head of a beetle.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:4:0:0]
