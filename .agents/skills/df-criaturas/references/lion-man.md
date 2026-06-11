# Lion man

> Fonte: [Lion man](https://dwarffortresswiki.org/index.php/Lion_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes lion men for their roars.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland**
- **Variations**
- **Lion - Lion man - Giant lion**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 13,500 cm 3
- **Mid:** 67,500 cm 3
- **Max:** 135,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head of a lion.*

**Lion men** are animal people variants of the common lion who can be found in savage tropical flatlands. They spawn in groups of 1-5 individuals and can pose a threat to anyone who provokes them. In terms of size, they are a little over twice the weight of the average dwarf. While they are smaller than the similar tiger man, their great size still makes them dangerous in combat.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like lion men for their *roars*.

Susceptible to stampedes and high falls.\
*Art by AlsaresLynx*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Lion men are known for their distinctive battle cry of *Lion men, lion men, lion men, ho!*

|  |
|----|
| "Lion man" in other / Languages / Dwarven / : / kurel udos / Elven / : / alatha onino / Goblin / : / dostom ngorûg / Human / : / san abo |

    [CREATURE:LION_MAN]
        [COPY_TAGS_FROM:LION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:lion man:lion men:lion man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:lion woman:lion women:lion woman]
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
        [NAME:lion man:lion men:lion man]
        [DESCRIPTION:A person with the head of a lion.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'L']
        [COLOR:6:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
