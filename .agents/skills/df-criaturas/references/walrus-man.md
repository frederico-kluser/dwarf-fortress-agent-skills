# Walrus man

> Fonte: [Walrus man](https://dwarffortresswiki.org/index.php/Walrus_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes walrus men for their tusks.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Walrus - Walrus man - Giant walrus**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 78,500 cm 3
- **Mid:** 392,500 cm 3
- **Max:** 785,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A legless person with the head and back flippers of a walrus.*

**Walrus men** are animal people versions of the common walrus, who can be found in savage arctic oceans. They spawn in groups of 1-5 individuals and are generally content to keep to themselves, but if provoked, will trounce any unarmed peasant who angers them. In terms of size, they are 13 times the size of a dwarf, and as such should only be engaged by an equipped military squad.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like walrus men for their *tusks* and their *whiskers*.

An "always-overweight-no-matter-what" race of people.\
*Art by Pookas Kreations*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

There have been groups of human deserters who have reported seeing walrus men wearing kilts, who were out hunting with blowdarts during the cold winter days and staying in igloos during the night. Due to the lack of records on walrus man housing and the circumstances the humans were in, these stories should be taken with a grain of salt.

Walrus men are known for setting up settlements in area's full of Undead or Dragons despite the apparent danger. They are known for inviting other races to have soup with them and have a habit of telling very long, boring, and uninteresting stories.

If a fortress has a high supply of sweet pods or dwarven sugar, some walrus men are prone to developing a chronic syndrome that leaves them permanently drowsy and dependent on pig pancreases. Walrus men thus afflicted will cease all labors and spend all their time using their Persuader skill to warn other dwarves of this syndrome, delivering impassioned lectures about the dangers of dwarven syrup consumption. They will also consume only cave wheat and quarry bush leaves foods, despite their dispreference for them, leading to negative thoughts.

    [CREATURE:WALRUS_MAN]
        [COPY_TAGS_FROM:WALRUS]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:FRONT_BODY_FLIPPERS:REAR_BODY_FLIPPERS]
            [CVCT_REPLACEMENT:REAR_BODY_FLIPPERS]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:walrus man:walrus men:walrus man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:walrus woman:walrus women:walrus woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TUSK_STAB_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:walrus man:walrus men:walrus man]
        [DESCRIPTION:A legless person with the head and back flippers of a walrus.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'W']
        [COLOR:6:0:0]
