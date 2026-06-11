# Hippo man

> Fonte: [Hippo man](https://dwarffortresswiki.org/index.php/Hippo_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hippo men for their strength.**
- **Biome**
- **Tropical Saltwater River Tropical Brackish River Tropical Freshwater River Tropical Saltwater Lake Tropical Brackish Lake Tropical Freshwater Lake**
- **Variations**
- **Hippo - Hippo man - Giant hippo**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 26,166.666666667 cm 3
- **Mid:** 392,500 cm 3
- **Max:** 785,000 cm 3
- **Age**
- **Adult at:** 5
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large person with the head of a hippo.*

**Hippo men** are animal people variants of the common hippo who can be found in savage temperate lakes and rivers. They spawn in groups of 2-10 individuals and should be approached with extreme caution; a hippo man is over 13 times larger than a dwarf and can make short work of any civilian who provokes them. Do not attempt to fight them without an equipped military squad.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like hippo men for their *strength*.

*Art by aokamidu*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite popular belief, hippo men are not well-trained boxers, and are not the kings of South Pacific islands.

Rumors of hippo men traveling the stars and shooting people with flintlocks are greatly exaggerated.

Hippo men are known to enjoy the company of the largest hippo women in an area. As a result, they are often at odds with giraffes.

Hippo men do not come in other colors (unless they're undead, which would make them indigo). More specifically, male and female hippos that are blue and purple respectively are not normally seen as married couples, let alone seen as in the aforementioned colors.

Groups of hippo men love to dump barrels of tree fruit into murky pools, form a circle around the fruit, and then compete to see who can consume the most food using nothing but their mouth.

    [CREATURE:HIPPO_MAN]
        [COPY_TAGS_FROM:HIPPO]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:hippo man:hippo men:hippo man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:hippo woman:hippo women:hippo woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:hippo man:hippo men:hippo man]
        [DESCRIPTION:A large person with the head of a hippo.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'H']
        [COLOR:7:0:0]
