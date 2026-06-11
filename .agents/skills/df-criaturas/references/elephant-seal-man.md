# Elephant seal man

> Fonte: [Elephant seal man](https://dwarffortresswiki.org/index.php/Elephant_seal_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes elephant seal men for their large floppy noses.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Elephant seal - Elephant seal man - Giant elephant seal**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 153,500 cm 3
- **Mid:** 767,500 cm 3
- **Max:** 1,535,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and flippers of an elephant seal.*

**Elephant seal men** are animal people variants of the common elephant seal who can be found in savage arctic oceans, spawning in groups of 5-10 individuals, and can easily dispose of dwarves who provoke them thanks to their enormous size. Much like their animal versions, elephant seal men possess notable sexual dimorphism; males are about as large as a walrus, while females are only about as large as a horse (being nonetheless much larger than dwarves).

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode. Due to their size, elephant seal men (especially males) can make strong adventurers. However, their large size also leaves them unable to equip generated armor, a problem many animal people have in common. Their amphibious nature is an interesting bonus, allowing for exploration of the usually-foreboding ocean.

Some dwarves like elephant seal men for their *large floppy noses* and their *great size*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
It is unknown if the cuteness of elephant seal pups is retained in their humanoid cousins.

Heard a LOT of blubber/fat jokes.\
*Art by Carl Schlesinger*

    [CREATURE:ELEPHANT_SEAL_MAN]
        [COPY_TAGS_FROM:ELEPHANT_SEAL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:FRONT_BODY_FLIPPERS:REAR_BODY_FLIPPERS]
            [CVCT_REPLACEMENT:REAR_BODY_FLIPPERS]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:elephant seal man:elephant seal men:elephant seal man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:elephant seal woman:elephant seal women:elephant seal woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:1945:1504:1062:548:3100:4500] 16 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:elephant seal man:elephant seal men:elephant seal man]
        [DESCRIPTION:A person with the head and flippers of an elephant seal.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
