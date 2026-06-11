# Rat man

> Fonte: [Rat man](https://dwarffortresswiki.org/index.php/Rat_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rat men for their friendliness.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Rat - Rat man - Large rat - Giant rat**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,150 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a rat.*

**Rat men** are humanoid versions of the common rat and a species of unremarkable animal people, found in most savage biomes. They are about half the size of the average dwarf when adults and spawn in groups of 5-10 individuals, and are unlikely to pose any danger to your fortress unless provoked. They are a completely different race from the rodent man.

Like other savage animal people, rat men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like rat men for their *friendliness*, their *playfulness*, their *curiosity*, and their *intelligence*.

Just as unlikable as standard rats.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Rat men myths speak of a green glowing mineral known only as "warpstone" that was forged into a legendary Warhammer.

Contrary to widespread rumors, rat men are not known to tame or train turtle men.

|  |
|----|
| "Rat man" in other / Languages / Dwarven / : / atem udos / Elven / : / thapa onino / Goblin / : / spödgôz ngorûg / Human / : / othur abo |

    [CREATURE:RAT_MAN]
        [COPY_TAGS_FROM:RAT]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:rat man:rat men:rat man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:rat woman:rat women:rat woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:rat man:rat men:rat man]
        [DESCRIPTION:A person with the head and tail of a rat.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'r']
        [COLOR:0:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
