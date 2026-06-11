# Honey badger man

> Fonte: [Honey badger man](https://dwarffortresswiki.org/index.php/Honey_badger_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes honey badger men for their tenacity.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland Tropical Savanna Tropical Grassland Any Tropical Wetland Any Desert**
- **Variations**
- **Honey badger - Honey badger man - Giant honey badger**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 2,700 cm 3
- **Mid:** 21,000 cm 3
- **Max:** 42,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A humanoid with the head and stripes of a honey badger.*

**Honey badger men** are animal people variants of the common honey badger who can be found in savage tropical and desert regions. They spawn in groups of 5-10 individuals and may pose a threat to passing dwarves as, like their animal counterparts, they are prone to rage and may flip out at other nearby creatures. Like the normal honey badgers, they are also food thieves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like honey badger men for their *fearlessness* and their *tenacity*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
**Honey badger men** are very loyal creatures, especially towards demigod leopard seal men, following them without question, as long as the reason for following them is entertaining the world and not goblin genocide. Although they do not know how to make weaponry of any sort, they do get particularly confident when armed with pikes, even suicidally so.

Some dwarves say they are nasty, but others don't give a flip.

Less hostile than the animal version.

    [CREATURE:HONEY BADGER MAN]
        [COPY_TAGS_FROM:HONEY BADGER]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_TAG:TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:honey badger man:honey badger men:honey badger man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:honey badger woman:honey badger women:honey badger woman]
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
        [NAME:honey badger man:honey badger men:honey badger man]
        [DESCRIPTION:A humanoid with the head and stripes of a honey badger.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:7:0:1]
        [GO_TO_TAG:SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
        [CV_REMOVE_TAG:SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
        [CV_REMOVE_TAG:PLUS_TL_GROUP:BY_CATEGORY:LEG_REAR:HAIR]
        [CV_REMOVE_TAG:PLUS_TL_GROUP:BY_CATEGORY:FOOT_FRONT:HAIR]
        [CV_REMOVE_TAG:PLUS_TL_GROUP:BY_CATEGORY:FOOT_REAR:HAIR]
        [CV_ADD_TAG:SET_TL_GROUP:BY_CATEGORY:ARM_UPPER:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:ARM_LOWER:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:HAND:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:FINGER:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:LEG:HAIR]
        [CV_ADD_TAG:PLUS_TL_GROUP:BY_CATEGORY:FOOT:HAIR]
        [APPLY_CURRENT_CREATURE_VARIATION]
