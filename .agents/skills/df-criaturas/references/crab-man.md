# Crab man

> Fonte: [Crab man](https://dwarffortresswiki.org/index.php/Crab_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes crab men for their sideways walk.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Crab - Crab man - Giant crab**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4.875 cm 3
- **Max:** 39,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and pincers of a crab.*

**Crab men** are animal people variants of the common crab, who can be found in savage oceans. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like crab men for their *pincers* and their *sideways walk*.

Tastes equally as good as standard crab.\
*Art by wallsofwoe*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Due to extensive research by ocean-based fortresses, we can conclude that crab men are, in fact, **not** related to the infamous cavern-dwelling Crab People - that is to say, the ones that taste like crabs, yet talk like people. They are also known to occasionally throw an extreme sleepover party. Crab men are generally unwilling to give up any coins they have obtained, and often enlist the work of sponge men and squid men to prepare food.

Crab men spies are seemingly their own subspecies, and are considered to be very rare.

|  |
|----|
| "Crab man" in other / Languages / Dwarven / : / ozsit udos / Elven / : / ditari onino / Goblin / : / slalsto ngorûg / Human / : / julosm abo |

    [CREATURE:CRAB_MAN]
        [COPY_TAGS_FROM:CRAB]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_TAG:BODY]
        [CV_REMOVE_TAG:BODY]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [BODY:HUMANOID_ARMLESS:2EYES:HEART:GUTS:BRAIN:UPPERBODY_PINCERS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:crab man:crab men:crab man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:crab woman:crab women:crab woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PINCER_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:crab man:crab men:crab man]
        [DESCRIPTION:A person with the head and pincers of a crab.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:4:0:1]
