# Moose man

> Fonte: [Moose man](https://dwarffortresswiki.org/index.php/Moose_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes moose men for their large size.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Moose - Moose man - Giant moose**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Horn · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 17,850 cm 3
- **Mid:** 148,750 cm 3
- **Max:** 297,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A humanoid with the head and antlers of a moose.*

**Moose men** are animal people variants of the common moose who can be found in savage temperate forests and taiga. They spawn in groups of 5-10 individuals and, like their animal counterparts, possess notable sexual dimorphism; moose women are about as large as a llama, while moose men are about the size of an elk. Because of their large size, dwarves who provoke them stand little chance unless they happen to be soldiers.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like moose men for their *broad antlers* and *large size*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
They are often found in the company of flying squirrel men.

Note: Headbutting is not recommended. (Elk man substitute)

    [CREATURE:MOOSE MAN]
        [COPY_TAGS_FROM:MOOSE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_TAG:BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:moose man:moose men:moose man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:moose woman:moose women:moose woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:HOOF_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:moose man:moose men:moose man]
        [DESCRIPTION:A humanoid with the head and antlers of a moose.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'M']
        [COLOR:6:0:0]
