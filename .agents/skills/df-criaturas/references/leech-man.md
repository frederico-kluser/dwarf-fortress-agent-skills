# Leech man

> Fonte: [Leech man](https://dwarffortresswiki.org/index.php/Leech_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes leech men for their feeding habits.**
- **Biome**
- **Any Lake Any Lake**
- **Variations**
- **Leech - Leech man - Giant leech**
- **Attributes**
- **Alignment:** Savage
- **Genderless · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,050 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large slug-like creature with the torso of a man. Its face is a mockery of teeth and slime.*

**Leech men** are humanoid versions of the common leech and a species of unremarkable animal people, found in savage pools and lakes. They are a bit over half the size of dwarves when adults and spawn in groups of 1-5 individuals. They have no legs and move about by crawling. They will automatically suck blood out of enemies on successful bite attacks.

Like other savage animal people, leech men may occasionally join civilizations, becoming full-fledged citizens, who may appear in your fortress as visitors, or be playable in adventurer mode.

Some dwarves like leech men for their *feeding habits*.

## Trivia

- Leech men have no legs using `ANIMAL_PERSON_LEGLESS` template, but the sprite depicts them with humanoid legs.

Three times the size, three times the hunger.\
*Art by Devilingo*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
One of the more evil residents of savage lakes, **leech men** have been proven quite a challenge to kill, even by the most skilled dwarven leech hunters.

Not to be confused with Noble

|  |
|----|
| "Leech man" in other / Languages / Dwarven / : / subol udos / Elven / : / awathi onino / Goblin / : / axson ngorûg / Human / : / quigos abo |

    [CREATURE:LEECH_MAN]
        [COPY_TAGS_FROM:LEECH]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_SUCK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:leech man:leech men:leech man]
        [CASTE_NAME:leech man:leech men:leech man]
        [DESCRIPTION:A large slug-like creature with the torso of a man.  Its face is a mockery of teeth and slime.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'l']
        [COLOR:0:0:1]
