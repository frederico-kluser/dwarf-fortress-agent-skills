# Hare man

> Fonte: [Hare man](https://dwarffortresswiki.org/index.php/Hare_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hare men for their long ears.**
- **Biome**
- **Temperate Savanna Temperate Grassland**
- **Variations**
- **Hare - Hare man - Giant hare**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,675 cm 3
- **Mid:** 18,375 cm 3
- **Max:** 36,750 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A long-eared person with the head and tail of a hare.*

**Hare men** are animal people variants of the common hare who can be found in savage temperate grasslands and savannas. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like hare men for their *long ears* and *fluffy tails*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some **hare men** are known to fool hunters with their wit and guile, they also have a penchant for wisecracks and munching on carrots. Even during "rabbit season".

One case reports an ambitious hare woman becoming a citizen of a dwarven fortress and ascending the ranks until she became a guard, while also getting a pardon for a fox man and letting him join.

Nyeeeh! What's up dwarf?

|  |
|----|
| "Hare man" in other / Languages / Dwarven / : / thetdel udos / Elven / : / iri onino / Goblin / : / sluto ngorûg / Human / : / setduk abo |

    [CREATURE:HARE_MAN]
        [COPY_TAGS_FROM:HARE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:hare man:hare men:hare man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:hare woman:hare women:hare woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:585:390:195:1900:2900] 45 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:hare man:hare men:hare man]
        [DESCRIPTION:A long-eared person with the head and tail of a hare.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'h']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
