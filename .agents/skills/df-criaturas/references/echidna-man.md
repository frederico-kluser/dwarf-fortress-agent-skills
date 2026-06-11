# Echidna man

> Fonte: [Echidna man](https://dwarffortresswiki.org/index.php/Echidna_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes echidna men for their egg-laying.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland Any Desert**
- **Variations**
- **Echidna - Echidna man - Giant echidna**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4 cm 3
- **Mid:** 20,000 cm 3
- **Max:** 40,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A spiny person with the head of an echidna.*

**Echidna men** are animal people variants of the common echidna who can be found in savage temperate and desert regions. They spawn in groups of 1-5 individuals and are generally peaceful, as well as surprisingly resilient. Even crossbow bolts and whips seem to be unable to penetrate past their muscles, leading to long, drawn-out battles waiting for them to bleed out. This makes echidna men relatively useful for live training, or as bait in a devious trap. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like echidna men for their *spines* and their *egg-laying*.

## Bugs

If a curled-up or retracted creature dies, and is then reanimated by a necromancer, it retains the effects of being curled-up, but can move and attack as normal. As a result, for example an undead echidna is invulnerable to destructionBug:11463. It combines well with a separate bug that allows curled-up undead to attackBug:10519.

As a result, the undead echidna may at the same time be curled-up (making it unkillable) and move/attack. The same problem also affects the echidna man, giant echidna, giant hedgehog and hedgehog man.

Modding the game and removing \[PREVENTS_PARENT_COLLAPSE\] from the spine body part of the affected animals will allow them to be pulped and killed while curled up. While it makes normal echidnas weaker, this is not a major problem, as echidnas are not supposed to be really hard to kill. This workaround may restore otherwise unplayable games.

It was also reported that in adventure mode "I was able to finally kill the zombie by lighting fires underneath him/around him then waiting for a long time; eventually he 'died in the heat.'"Bug:10519.

## D for Dwarf

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Echidna men practice a religion known as 'The Way.' They actively and enthusiastically seek out other worshippers of their deity, but seem unwilling to proselytize to those not familiar with their beliefs.

Echidna men generally find shows of strength to be more entertaining than comedy. Accounts of echidna men chuckling are few and far between. They do not guard large emeralds on floating islands, nor do they have access to sanctuaries in the sky. They also do not accompany hedgehog men on adventures against technologically-advanced villains.

Dwarven scientists have, as of yet, not determined whether echidna men possess 4-headed penises.

    [CREATURE:ECHIDNA_MAN]
        [COPY_TAGS_FROM:ECHIDNA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:echidna man:echidna men:echidna man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:echidna woman:echidna women:echidna woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:echidna man:echidna men:echidna man]
        [DESCRIPTION:A spiny person with the head of an echidna.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'e']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
