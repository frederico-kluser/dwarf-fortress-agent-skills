# Badger man

> Fonte: [Badger man](https://dwarffortresswiki.org/index.php/Badger_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes badger men for their underground communities.**
- **Biome**
- **Taiga Any Temperate Forest Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Badger - Badger man - Giant badger**
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
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A humanoid with the head and stripes of a badger.*

**Badger men** are animal people variants of the common badger who inhabit savage temperate forests and taigas. They spawn in groups of anywhere between 5-10 individuals and retain the original animal's bad temper, occasionally going into a fit of rage and attacking nearby creatures. In terms of size, they are over half the weight of the average dwarf, and as such can cause significant damage in a confrontation with an unarmed civilian or pet.

Like other savage animal people, badger men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like badger men for their *underground communities* and their *striped faces*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
It is well known that badger men prefer walls made from red materials.

Best not to disturb when they work...

    [CREATURE:BADGER MAN]
        [COPY_TAGS_FROM:BADGER]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_TAG:TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:badger man:badger men:badger man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:badger woman:badger women:badger woman]
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
        [NAME:badger man:badger men:badger man]
        [DESCRIPTION:A humanoid with the head and stripes of a badger.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:7:0:0]
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
