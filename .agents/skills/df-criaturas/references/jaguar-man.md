# Jaguar man

> Fonte: [Jaguar man](https://dwarffortresswiki.org/index.php/Jaguar_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes jaguar men for their spotted coats.**
- **Biome**
- **Any Tropical Badlands Rocky Wasteland Sand Desert**
- **Variations**
- **Jaguar - Jaguar man - Giant jaguar**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 7,250 cm 3
- **Mid:** 38,666.666666667 cm 3
- **Max:** 72,500 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A spotted person with the head and tail of a jaguar.*

**Jaguar men** are animal people variants of the common jaguar who can be found in savage deserts and tropical regions. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little larger than the average human.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode. Jaguar men make a good choice for players in adventurer mode, as they can wear human-sized armour.

Some dwarves like jaguar men for their *spotted coats*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite the insistence of human scholars, there is no evidence of jaguar man soldiers holding any preference to using obsidian short swords.

Jaguar men are known for their taste in wagons.

*Art by Devilingo*

    [CREATURE:JAGUAR_MAN]
        [COPY_TAGS_FROM:JAGUAR]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:jaguar man:jaguar men:jaguar man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:jaguar woman:jaguar women:jaguar woman]
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
        [NAME:jaguar man:jaguar men:jaguar man]
        [DESCRIPTION:A spotted person with the head and tail of a jaguar.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'J']
        [COLOR:6:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
