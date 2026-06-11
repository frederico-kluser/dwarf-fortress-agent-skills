# Coyote man

> Fonte: [Coyote man](https://dwarffortresswiki.org/index.php/Coyote_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes coyote men for their howling.**
- **Biome**
- **Mountain Tundra Taiga Any Temperate Forest Temperate Savanna Temperate Grassland Temperate Shrubland Any Temperate Wetland Any Desert**
- **Variations**
- **Coyote - Coyote man - Giant coyote**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,250 cm 3
- **Mid:** 21,250 cm 3
- **Max:** 42,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a coyote.*

**Coyote men** are animal people variants of the common coyote who can be found in a wide range of savage regions. They spawn in groups of 2-10 individuals and are generally content to keep to themselves, but may attack if approached. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like coyote men for their *howling*.

Her howling is hypnotic.\
*Art by Kuhl*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Coyote men do not fixate on catching and consuming road runners, nor do they purchase or create any kind of traps to do so.

    [CREATURE:COYOTE_MAN]
        [COPY_TAGS_FROM:COYOTE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:coyote man:coyote men:coyote man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:coyote woman:coyote women:coyote woman]
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
        [NAME:coyote man:coyote men:coyote man]
        [DESCRIPTION:A person with the head and tail of a coyote.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:7:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
