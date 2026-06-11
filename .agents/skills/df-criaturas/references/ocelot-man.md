# Ocelot man

> Fonte: [Ocelot man](https://dwarffortresswiki.org/index.php/Ocelot_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ocelot men for their coat patterns.**
- **Biome**
- **Any Tropical Forest Mangrove Swamp Tropical Savanna Tropical Grassland**
- **Variations**
- **Ocelot - Ocelot man - Giant ocelot**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 475 cm 3
- **Mid:** 23,750 cm 3
- **Max:** 47,500 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of an ocelot.*

**Ocelot men** are animal people variants of the common ocelot who can be found in most savage tropical regions. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like ocelot men for their *coat patterns*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
**Ocelot men** are best known for their tendency to spin around while dual-wielding crossbows. They may spawn alongside Snake men, but whether they are hostile to each other depends on the version of the game.

Might be tamable with fish.\
*Art by Palelady*

    [CREATURE:OCELOT_MAN]
        [COPY_TAGS_FROM:OCELOT]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:ocelot man:ocelot men:ocelot man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:ocelot woman:ocelot women:ocelot woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:CLAW_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:ocelot man:ocelot men:ocelot man]
        [DESCRIPTION:A person with the head and tail of an ocelot.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'o']
        [COLOR:6:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
