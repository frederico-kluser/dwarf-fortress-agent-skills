# Snail man

> Fonte: [Snail man](https://dwarffortresswiki.org/index.php/Snail_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes snail men for their shells.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Snail - Snail man - Giant snail**
- **Attributes**
- **Alignment:** Savage
- **Genderless · Learns · Shell · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,000.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A creature with the shape of a man, but with stalks for eyes, and a great shell on its back.*

**Snail men** are animal people variants of the common snail, who can inhabit most savage biomes. They spawn in groups of 1-3 individuals and are generally content to keep to themselves, but may pick fights if provoked. In terms of size, they are a little over half the weight of the average dwarf. Although standard snails have no legs, snail men have legs, which is shown in their sprites.

Like other savage animal people, snail men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like snail men for their *shells*.

Has trouble fleeing from trouble.\
*Art by Quinmael*

|  |
|----|
| "Snail man" in other / Languages / Dwarven / : / nasod udos / Elven / : / limi onino / Goblin / : / snuslû ngorûg / Human / : / copgur abo |

    [CREATURE:SNAIL_MAN]
        [COPY_TAGS_FROM:SNAIL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:snail man:snail men:snail man]
        [CASTE_NAME:snail man:snail men:snail man]
        [DESCRIPTION:A creature with the shape of a man, but with stalks for eyes, and a great shell on its back.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:7:0:0]
