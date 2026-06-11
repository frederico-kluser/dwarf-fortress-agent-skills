# Hedgehog man

> Fonte: [Hedgehog man](https://dwarffortresswiki.org/index.php/Hedgehog_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hedgehog men for their many spines.**
- **Biome**
- **Temperate Shrubland Temperate Savanna**
- **Variations**
- **Hedgehog - Hedgehog man - Giant hedgehog**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,400 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and spines of a hedgehog.*

**Hedgehog men** are animal people variants of the common hedgehog who can be found in savage temperate shrublands and savannas. They spawn in groups of 1-5 individuals and can curl up into a ball-shape which drastically increases the defense of the creature against blunt damage, causing it only to take damage to the upper body. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like hedgehog men for their *many spines*.

## Bugs

If a curled-up or retracted creature dies, and is then reanimated by a necromancer, it retains the effects of being curled-up, but can move and attack as normal. As a result, for example an undead echidna is invulnerable to destructionBug:11463. It combines well with a separate bug that allows curled-up undead to attackBug:10519.

As a result, the undead echidna may at the same time be curled-up (making it unkillable) and move/attack. The same problem also affects the echidna man, giant echidna and giant hedgehog.

Modding the game and removing \[PREVENTS_PARENT_COLLAPSE\] from the spine body part of the affected animals will allow them to be pulped and killed while curled up. While it makes normal echidnas weaker, this is not a major problem, as echidnas are not supposed to be really hard to kill. This workaround may restore otherwise unplayable games.

It was also reported that in adventure mode "I was able to finally kill the zombie by lighting fires underneath him/around him then waiting for a long time; eventually he 'died in the heat.'"Bug:10519.

*Art by YanisaB*

## Jokes

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Contrary to popular belief, hedgehog men cannot exceed the speed of sound while running. They do not need to collect golden rings to sustain their own life, and will not instantly die if struck by an enemy whilst without these rings. They also do not have a rivalry with intellectual villainous humans.

|  |
|----|
| "Hedgehog man" in other / Languages / Dwarven / : / èfim-tarag udos / Elven / : / ralila-ÿara onino / Goblin / : / slësu-snam ngorûg / Human / : / hob-celo abo |

    [CREATURE:HEDGEHOG_MAN]
        [COPY_TAGS_FROM:HEDGEHOG]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:hedgehog man:hedgehog men:hedgehog man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:hedgehog woman:hedgehog women:hedgehog woman]
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
        [NAME:hedgehog man:hedgehog men:hedgehog man]
        [DESCRIPTION:A person with the head and spines of a hedgehog.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'h']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
