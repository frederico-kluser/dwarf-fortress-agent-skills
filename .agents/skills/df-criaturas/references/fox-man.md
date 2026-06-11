# Fox man

> Fonte: [Fox man](https://dwarffortresswiki.org/index.php/Fox_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes fox men for their cunning.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Fox - Fox man - Giant fox**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,800 cm 3
- **Mid:** 19,000 cm 3
- **Max:** 38,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a fox.*

**Fox men** are animal people variants of the common fox, who inhabit savage temperate forests and taigas, spawning in groups of 2-10 individuals, and are generally content to keep to themselves. In terms of size, they are roughly half the weight of the average dwarf.

Like other savage animal people, fox men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like fox men for their *cunning*.

Not the arwing-flying type.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
They do not seem to be great at piloting fighters, contrary to popular belief.

The culture of fox men places a high value on tradition, family, and national pride. Their preferred economic model is free-market capitalism, in stark contrast to the dwarves' centrally-planned economy.

They are not ox men.(an easy mistake to make if you're not paying attention.) If in doubt, ox men tend to have stronger body odor.

Fox men prefer to settle conflicts with other fox men by one on one unarmed combat on even ground. They consider conducting these duels with weapons or on ground that is not perfectly flat to be unthinkable.

    >[CREATURE:FOX_MAN]
        [COPY_TAGS_FROM:FOX]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:fox man:fox men:fox man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:fox woman:fox women:fox woman]
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
        [NAME:fox man:fox men:fox man]
        [DESCRIPTION:A person with the head and tail of a fox.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'f']
        [COLOR:4:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
