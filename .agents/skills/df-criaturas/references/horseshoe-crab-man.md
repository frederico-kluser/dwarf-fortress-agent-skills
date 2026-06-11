# Horseshoe crab man

> Fonte: [Horseshoe crab man](https://dwarffortresswiki.org/index.php/Horseshoe_crab_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes horseshoe crab men for their ability to hide in sand.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Horseshoe crab - Horseshoe crab man - Giant horseshoe crab**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 36,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head, shell, and tail of a horseshoe crab.*

**Horseshoe crab men** are animal people variants of the common horseshoe crab, who can be found in savage oceans. They spawn in groups of 1-3 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like horseshoe crab men for their *ability to hide in sand*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Horseshoe crab men are known to be great weaponsmiths, supplying the squid men with armaments for their war against the octopus men.

Look better from the back. At all times.\
*Art by both Cupra and DruidaV*

    [CREATURE:HORSESHOE_CRAB_MAN]
        [COPY_TAGS_FROM:HORSESHOE_CRAB]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_TAG:BODY]
        [CV_REMOVE_TAG:BODY]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [BODY:HUMANOID:HEART:BRAIN:TAIL]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:horseshoe crab man:horseshoe crab men:horseshoe crab man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:horseshoe crab woman:horseshoe crab women:horseshoe crab woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:horseshoe crab man:horseshoe crab men:horseshoe crab man]
        [DESCRIPTION:A person with the head, shell, and tail of a horseshoe crab.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:6:0:0]
