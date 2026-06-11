# Fly man

> Fonte: [Fly man](https://dwarffortresswiki.org/index.php/Fly_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes fly men for their ability to annoy.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra Any Pool**
- **Variations**
- **Fly - Fly man - Giant fly**
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

*A person with the wings and head of a fly.*

**Fly men** are humanoid versions of the common fly and a species of animal people, found in just about every savage biome but mountains, glacier and tundra. They are also supposed to appear in savage pools, but as non-vermin can't spawn in pools, this never happens. They are a little over half the size of an adult dwarf and are unlikely to pose a threat to a fortress' inhabitants. All fly men are born as full-sized adults, and with Legendary skill in climbing.

Some dwarves like fly men for their *ability to annoy*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Despite the rumors you might've heard, fly men are not that great at quantum teleportation science.

Still equally annoying as a normal fly.

|  |
|----|
| "Fly man" in other / Languages / Dwarven / : / fenglel udos / Elven / : / yetine onino / Goblin / : / atu ngorûg / Human / : / ngáthi abo |

    [CREATURE:FLY_MAN]
        [COPY_TAGS_FROM:FLY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:fly man:fly men:fly man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:fly woman:fly women:fly woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:fly man:fly men:fly man]
        [DESCRIPTION:A person with the wings and head of a fly.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'f']
        [COLOR:0:0:1]
