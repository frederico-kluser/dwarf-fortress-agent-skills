# Worm man

> Fonte: [Worm man](https://dwarffortresswiki.org/index.php/Worm_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes worm men for their wriggling.**
- **Biome**
- **Taiga Any Temperate Any Tropical**
- **Variations**
- **Worm - Worm man**
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

*A worm-like creature with the torso of a man.*

**Worm men** are animal people versions of the common worm, who can be found in savage tropical, temperate and taiga regions. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like worm men for their *wriggling*.

A drawing of a worm man and a pipe. All craftsdwarfship is of the highest quality. The worm man is smoking the pipe. The worm man is standing peacefully.\
*Art by Arne*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
An archaeological expedition brought to the scholarly dwarven community a theory; that the worm men inhabiting the world are in fact an evolutionary subspecies. According to historical data, the original classification Lumbricina Militus went extinct after they started an Armageddon event claiming the majority of their own in a global civil war. If the historical accounts are to be believed, accomplished worm men could exploit the wind to further amplify the kinetic damage of their projectiles and could weaponize cattle as explosive ordinance. This is a developing field of study, and all dwarven scholars are analyzing the viability in substituting these bovine munitions for elven alternatives.

The spirit of duty in a worm man is not to be besmirched, however. It has been confirmed at least one worm man could harness the use of an elastic pastry to heroically save a litter of puppies from a malevolent crow man.

Be wary of worm men claiming to be doctors, as such claims are highly likely to be false. Worm men have shown a strange propensity for drum-playing and often adopt false titles as 'stage names,' though they tend to be accepting of critique and are generally curious creatures, provided that you show an interest in their music.

|  |
|----|
| "Worm man" in other / Languages / Dwarven / : / vesrul udos / Elven / : / nema onino / Goblin / : / osle ngorûg / Human / : / slinpa abo |

    [CREATURE:WORM_MAN]
        [COPY_TAGS_FROM:WORM]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:worm man:worm men:worm man]
        [CASTE_NAME:worm man:worm men:worm man]
        [DESCRIPTION:A worm-like creature with the torso of a man.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'w']
        [COLOR:7:0:0]
        [EXTRAVISION]
