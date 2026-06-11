# Tick man

> Fonte: [Tick man](https://dwarffortresswiki.org/index.php/Tick_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes tick men for their ability to expand.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Tick - Tick man - Giant tick**
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

*A person with the head and legs of a tick.*

**Tick men** are humanoid versions of the common tick and a species of animal people, found in most savage biomes in small clusters of 1-3 individuals. They are only half the size of an adult dwarf and as such, are unlikely to be a threat to even an unarmed civilian. Like their vermin counterparts, tick men drain blood during bite attacks, which may lead to interesting scenarios if one attempts to bite a vampire. All tick men are born with Legendary skill in climbing.

Like other savage animal people, tick men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like tick men for their *ability to expand*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

A tick man with blue pigmented skin and high muscle mass has been seen traveling with a moth man.

|  |
|----|
| "Tick man" in other / Languages / Dwarven / : / nobgost udos / Elven / : / pamène onino / Goblin / : / stâsost ngorûg / Human / : / slushu abo |

Has a harder time embedding itself into others.

    [CREATURE:TICK_MAN]
        [COPY_TAGS_FROM:TICK]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:tick man:tick men:tick man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:tick woman:tick women:tick woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_SUCK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:tick man:tick men:tick man]
        [DESCRIPTION:A person with the head and legs of a tick.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'t']
        [COLOR:0:0:1]
