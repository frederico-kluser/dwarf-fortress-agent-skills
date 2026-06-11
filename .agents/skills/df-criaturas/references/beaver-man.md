# Beaver man

> Fonte: [Beaver man](https://dwarffortresswiki.org/index.php/Beaver_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes beaver men for their tree-felling habits.**
- **Biome**
- **Any Temperate Lake Any Temperate River**
- **Variations**
- **Beaver - Beaver man - Giant beaver**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,500 cm 3
- **Mid:** 22,500 cm 3
- **Max:** 45,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and flat tail of a beaver.*

**Beaver men** are animal people variants of the common beaver, who can be found in savage temperate lakes and rivers, spawn in groups of 2-5 individuals, and are generally content to keep to themselves. In terms of size, they are over half the weight of the average dwarf.

Like other savage animal people, beaver men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like beaver men for their *dams* and their *tree-feeding habits*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite popular belief, there are no two beaver siblings with the moniker of "Norbert" and "Daggett". Beaver men also do not live in human-like houses that double as a living space as well as a dam.

There is also no known documentation of a human lumberjack (owning an axe named "Lucy") having a curse of becoming a werebeaver once chopping down enough trees.

*Art by half-rose*

    [CREATURE:BEAVER_MAN]
        [COPY_TAGS_FROM:BEAVER]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:beaver man:beaver men:beaver man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:beaver woman:beaver women:beaver woman]
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
        [NAME:beaver man:beaver men:beaver man]
        [DESCRIPTION:A person with the head and flat tail of a beaver.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
