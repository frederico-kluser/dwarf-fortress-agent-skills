# Adder man

> Fonte: [Adder man](https://dwarffortresswiki.org/index.php/Adder_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes adder men for their warning hisses.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Any Temperate Forest Any Temperate Wetland**
- **Variations**
- **Adder - Adder man - Giant adder**
- **Attributes**
- **Alignment:** Savage
- **Learns · Syndrome · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,507.5 cm 3
- **Mid:** 17,537.5 cm 3
- **Max:** 35,075 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large adder with the torso and arms of a man.*

**Adder men** are animal people variants of the common adder who can inhabit a number of savage temperate regions. They spawn in groups of 1-5 individuals and retain their base venomous snakes' poisonous bites, syndromic effects being: strong pain in the short-term and swelling, blisters, and nausea in the long. For this reason, it's not recommended that you use these seemingly weak creatures as military practice targets without multiple ranged weapons and/or a complete set of armor; if your dwarf can't fight because they're doubled over in pain, they're very likely to be ripped apart by their aggressor. Needless to say, avoid provoking them unless prepared. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, adder men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like adder men for their *warning hisses*.

*Art by frankwest16*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Adder men have nothing to do with dwarven computing "Adder (Computing)"), despite what they may say.

A particular lineage of adder men are noted for appearing in wildly disparate periods of history, from the Age of Myth to the Age of the goblin. Although this lineage possesses no physical venom, they can deliver venomous bites via their Legendary Comedian and Persuader skills. They are invariably accompanied by an exceptionally unhygienic Human Peasant companion. This companion, who subsists entirely on raw plump helmets, will frequently present the adder man with a *cunning plan*.

Such adder men, seeking to bolster their coin stockpiles, may receive help from a noble, who will enter a strange mood, take over an Alchemist's laboratory and attempt to construct gold bars. The job order will always fail, filling the workshop with miasma and producing only a single green glob. The noble will then take this glob to a Jeweler's workshop and craft a low-value amulet from it.

    [CREATURE:ADDER_MAN]
        [COPY_TAGS_FROM:ADDER]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:adder]
            [CVCT_REPLACEMENT:adder man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:adder]
            [CVCT_REPLACEMENT:adder man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:adder]
            [CVCT_REPLACEMENT:adder man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:ADDER]
            [CVCT_REPLACEMENT:ADDER_MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:adder man:adder men:adder man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:adder woman:adder women:adder woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:adder man:adder men:adder man]
        [DESCRIPTION:A large adder with the torso and arms of a man.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'a']
        [COLOR:6:0:0]
