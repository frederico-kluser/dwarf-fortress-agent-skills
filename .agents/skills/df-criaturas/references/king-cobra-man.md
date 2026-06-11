# King cobra man

> Fonte: [King cobra man](https://dwarffortresswiki.org/index.php/King_cobra_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes king cobra men for their charming hood.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **King cobra - King cobra man - Giant king cobra**
- **Attributes**
- **Alignment:** Savage
- **Learns · Syndrome · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 25.333333333333 cm 3
- **Mid:** 19,000 cm 3
- **Max:** 38,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A legless person with the head and tail of a king cobra.*

**King cobra men** are animal people variants of the common king cobra who inhabit tropical forests. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, king cobra men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like king cobra men for their *charming hood*.

Both smart and venomous.

|  |
|----|
| "King cobra man" in other / Languages / Dwarven / : / etar gisëk udos / Elven / : / afedo vicira onino / Goblin / : / zozlo gusslax ngorûg / Human / : / deng nasñok abo |

    [CREATURE:KING_COBRA_MAN]
        [COPY_TAGS_FROM:KING_COBRA]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:king cobra]
            [CVCT_REPLACEMENT:king cobra man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:king cobra]
            [CVCT_REPLACEMENT:king cobra man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:king cobra]
            [CVCT_REPLACEMENT:king cobra man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:KING_COBRA]
            [CVCT_REPLACEMENT:KING_COBRA_MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:king cobra man:king cobra men:king cobra man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:king cobra woman:king cobra women:king cobra woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:king cobra man:king cobra men:king cobra man]
        [DESCRIPTION:A legless person with the head and tail of a king cobra.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'k']
        [COLOR:0:0:1]
