# Cougar man

> Fonte: [Cougar man](https://dwarffortresswiki.org/index.php/Cougar_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cougar men for their cunning.**
- **Biome**
- **Any Temperate Forest Any Tropical Forest Temperate Shrubland Tropical Shrubland**
- **Variations**
- **Cougar - Cougar man - Giant cougar**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,500 cm 3
- **Mid:** 32,500 cm 3
- **Max:** 65,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a cougar.*

**Cougar men** are animal people variants of the common cougar who can be found in savage temperate and tropical regions. They spawn in groups of 1-5 individuals and may pick fights with dwarves who provoke them, which may lead to death if the dwarf is just a peasant. In terms of size, they are halfway between dwarves and humans.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode. Cougar men are able to wear human-sized and dwarf-sized equipment, making them a rather good choice for adventurers.

As with cougars, cougar men are carnivorous, and will starve if not allowed access to meat.

Some dwarves like cougar men for their *cunning*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Contrary to popular belief, **cougar men**, or as they are sometimes called, puma men, cannot fly, like a moron or otherwise.

Cougar women are said to follow young male dwarves very closely. Although there are no cases of cougar people attacking and eating dwarves, they tend to refer to them as predators nonetheless.

The female variants heard all the jokes.\
*Art by Nora Potwora*

    >[CREATURE:COUGAR_MAN]
        [COPY_TAGS_FROM:COUGAR]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:cougar man:cougar men:cougar man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:cougar woman:cougar women:cougar woman]
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
        [NAME:cougar man:cougar men:cougar man]
        [DESCRIPTION:A person with the head and tail of a cougar.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
