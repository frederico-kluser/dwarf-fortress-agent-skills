# Flying squirrel man

> Fonte: [Flying squirrel man](https://dwarffortresswiki.org/index.php/Flying_squirrel_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes flying squirrel men for their large eyes.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Flying squirrel - Flying squirrel man - Giant flying squirrel**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,100 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a flying squirrel.*

**Flying squirrel men** are animal people variants of the common flying squirrel, who can be found in savage temperate forests, spawn in groups of 3-5 individuals, and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. They are born with Legendary skill in climbing.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like flying squirrel men for their *gliding* and their *large eyes*.

*Art by Jeff Agudelo*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Flying squirrel people do not have any kind of alliance with hedgehog men, fox men nor echidna men, or armadillo men. They also do not have any egg-shaped human rivals capable of world domination.

Despite what the artistic depictions of humans would convey, flying squirrel men are not companions of moose men.

    [CREATURE:FLYING_SQUIRREL_MAN]
        [COPY_TAGS_FROM:SQUIRREL_FLYING]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:flying squirrel man:flying squirrel men:flying squirrel man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:flying squirrel woman:flying squirrel women:flying squirrel woman]
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
        [NAME:flying squirrel man:flying squirrel men:flying squirrel man]
        [DESCRIPTION:A person with the head and wings of a flying squirrel.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:3:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
