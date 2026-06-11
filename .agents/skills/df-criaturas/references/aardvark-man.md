# Aardvark man

> Fonte: [Aardvark man](https://dwarffortresswiki.org/index.php/Aardvark_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes aardvark men for their long ears.**
- **Biome**
- **Tropical Shrubland Tropical Savanna Tropical Grassland**
- **Variations**
- **Aardvark - Aardvark man - Giant aardvark**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 600 cm 3
- **Mid:** 30,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

*A person with the head and tail of an aardvark.*

**Aardvark men** are the savage half-man/half-beast variant of the standard aardvark. They can be found topside in tropical biomes, wandering in groups of 1-5. Because of the double 'a', they appear near the top of alphabetized lists, including the create creature list in the object testing arena. Like their aardvarkian brethren, aardvark people do not actually eat vermin.

Like other savage animal people, aardvark men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves prefer aardvark men for their *long ears* and *snout*.

\

Egyptian god Set, possibly with the head of an aardvark.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some Aardvark men are known to wear glasses, and form tight relationships with many other types of humanoid animals, most notably the hare man. They can often be found in your fortress' library.

Aardvark men appear at the very top of the alphabetical order list for all creature based stockpiles - not really important but it is nice to know.

    [CREATURE:AARDVARK_MAN]
        [COPY_TAGS_FROM:AARDVARK]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:aardvark man:aardvark men:aardvark man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:aardvark woman:aardvark women:aardvark woman]
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
        [NAME:aardvark man:aardvark men:aardvark man]
        [DESCRIPTION:A person with the head and tail of an aardvark.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'a']
        [COLOR:7:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
