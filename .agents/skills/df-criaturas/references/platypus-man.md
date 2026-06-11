# Platypus man

> Fonte: [Platypus man](https://dwarffortresswiki.org/index.php/Platypus_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes platypus men for their venomous spurs.**
- **Biome**
- **Any River**
- **Variations**
- **Platypus - Platypus man - Giant platypus**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Syndrome · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 180 cm 3
- **Mid:** 18,000 cm 3
- **Max:** 36,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A humanoid with the head, tail and poison spurs of a platypus.*

**Platypus men** are animal people variants of the common platypus who can be found in savage rivers. They spawn in groups of 5-10 individuals and are generally content to keep to themselves. Like the common animal, platypus men can inject poison via kick attacks which causes considerable pain and swelling on the victim, while platypus women lack this ability entirely. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, platypus men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like platypus men for their *bizarre appearance*, their *venomous spurs*, their *flat tails*, and their *large bills*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Contrary to popular rumors, there are no records of any civilization having ever recruited platypus men as agents.

Always says "I'll send you the bill!" when defeating enemies.

    [CREATURE:PLATYPUS MAN]
        [COPY_TAGS_FROM:PLATYPUS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:platypus]
            [CVCT_REPLACEMENT:platypus man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:platypus]
            [CVCT_REPLACEMENT:platypus man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:platypus]
            [CVCT_REPLACEMENT:platypus man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:PLATYPUS]
            [CVCT_REPLACEMENT:PLATYPUS MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:platypus man:platypus men:platypus man]
            [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
            [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT]
                [ATTACK_SKILL:STANCE_STRIKE]
                [ATTACK_VERB:kick:kicks]
                [ATTACK_CONTACT_PERC:5]
                [ATTACK_PENETRATION_PERC:10]
                [ATTACK_FLAG_EDGE]
                [ATTACK_PREPARE_AND_RECOVER:4:4]
                [ATTACK_PRIORITY:MAIN]
                [ATTACK_FLAG_WITH]
                [ATTACK_FLAG_BAD_MULTIATTACK]
                [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:VENOM:LIQUID:100:100]
            [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:platypus woman:platypus women:platypus woman]
            [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
            [APPLY_CREATURE_VARIATION:KICK_ATTACK]
            [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:platypus man:platypus men:platypus man]
        [DESCRIPTION:A humanoid with the head, tail and poison spurs of a platypus.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'p']
        [COLOR:6:0:0]
