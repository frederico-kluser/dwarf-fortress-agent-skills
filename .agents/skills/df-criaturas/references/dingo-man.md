# Dingo man

> Fonte: [Dingo man](https://dwarffortresswiki.org/index.php/Dingo_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes dingo men for their coloration.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Dingo - Dingo man - Giant dingo**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,500 cm 3
- **Mid:** 22,500 cm 3
- **Max:** 45,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head of a dingo.*

**Dingo men** are animal people variants of the common dingo who can be found in most savage biomes. They spawn in groups of 3-10 individuals and may pick fights with dwarves who provoke them, inevitably leading to injuries, but most dwarves should be able to defeat a dingo man one-on-one. They are close to dwarves in size, but overall smaller.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like dingo men for their *coloration*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite what some forms of media may portray, there are no dingo men infused with crocodiles at the genetic level. They also do not antagonize humanoid bandicoot men, nor do they operate large flamethrowers. It is debatable whether they speak in an Australian accent or not.

Only speaks in an Australian accent if comically appropriate.

    [CREATURE:DINGO_MAN]
        [COPY_TAGS_FROM:DINGO]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:dingo man:dingo men:dingo man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:dingo woman:dingo women:dingo woman]
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
        [NAME:dingo man:dingo men:dingo man]
        [DESCRIPTION:A person with the head of a dingo.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:3:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'d']
        [COLOR:6:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
