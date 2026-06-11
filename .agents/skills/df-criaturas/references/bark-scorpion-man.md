# Bark scorpion man

> Fonte: [Bark scorpion man](https://dwarffortresswiki.org/index.php/Bark_scorpion_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bark scorpion men for their stinging tail.**
- **Biome**
- **Any Desert Tropical Grassland Tropical Savanna Tropical Shrubland Tropical Coniferous Forest**
- **Variations**
- **Bark scorpion - Bark scorpion man - Giant bark scorpion**
- **Attributes**
- **Alignment:** Savage
- **No Stun · No Pain · Learns · Syndrome · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,001.5 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head, pincers and tail of a bark scorpion.*

**Bark scorpion men** are humanoid versions of the common bark scorpion, and a species of animal people, found in savage deserts and tropical areas. They are a bit over half the size of dwarves and spawn in groups of 1-3 individuals. With a total of 6 arms (each with a hand) and 2 pincers, they can equip multiple items at once and also retain the poisonous sting of their animal counterparts, which causes pain in the victim when injected. The creatures themselves are additionally immune to pain, stunning, fear and paralysis, never need to sleep and possess extravision. All bark scorpion men are born with Legendary skill in climbing.

Like other savage animal people, bark scorpion men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode. If playing as a bark scorpion man, your stinger can be used to sting foes, which forces them into a prone state and applies a good amount of pain that will stun most enemies. The sting can force even undead into a prone state, but it will not stun them or even cost them a turn. Also, note that they cannot jump.

Some dwarves like bark scorpion men for their *pincers* and their *stinging tail*.

Not the friendly type.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Bark Scorpion Men are known to use their stinging tails as harpoons or hooks of a sort, and some have been observed to cry "Get over here!" when pulling in their prey. Some dubious tales report pyrokinetic powers and teleportation being among a Scorpion Man's abilities, but the lack of these attributes in any other creatures leaves scholars in denial.

    [CREATURE:BARK_SCORPION_MAN]
        [COPY_TAGS_FROM:BARK_SCORPION]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:bark scorpion]
            [CVCT_REPLACEMENT:bark scorpion man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:bark scorpion]
            [CVCT_REPLACEMENT:bark scorpion man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:bark scorpion]
            [CVCT_REPLACEMENT:bark scorpion man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:BARK_SCORPION]
            [CVCT_REPLACEMENT:BARK_SCORPION_MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:bark scorpion man:bark scorpion men:bark scorpion man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:bark scorpion woman:bark scorpion women:bark scorpion woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:TAIL_STING_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:PINCER_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:bark scorpion man:bark scorpion men:bark scorpion man]
        [DESCRIPTION:A person with the head, pincers and tail of a bark scorpion.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:6:0:1]
