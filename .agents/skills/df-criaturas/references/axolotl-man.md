# Axolotl man

> Fonte: [Axolotl man](https://dwarffortresswiki.org/index.php/Axolotl_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes axolotl men for their gills.**
- **Biome**
- **Tropical Saltwater Lake Tropical Brackish Lake Tropical Freshwater Lake**
- **Variations**
- **Axolotl - Axolotl man - Giant axolotl**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,100 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of an axolotl.*

**Axolotl men** are humanoid versions of the common axolotl and a species of unremarkable animal people, found in savage tropical lakes. They are a bit over half the size of dwarves when adults and spawn in groups of 1-5 individuals. They should pose no threat to dwarves unless provoked.

Like other savage animal people, axolotl men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like axolotl men for their *gills*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite their cute appearance, axolotl men are known for their short temper and will go berserk easily.

\

An Axolotl man armed with an obsidian short sword.\
*Drawn by Albino Axolotl*

.

    [CREATURE:AXOLOTL_MAN]
        [COPY_TAGS_FROM:AXOLOTL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:axolotl man:axolotl men:axolotl man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:axolotl woman:axolotl women:axolotl woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:axolotl man:axolotl men:axolotl man]
        [DESCRIPTION:A person with the head and tail of an axolotl.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'a']
        [COLOR:5:0:0]
