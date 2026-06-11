# Copperhead snake man

> Fonte: [Copperhead snake man](https://dwarffortresswiki.org/index.php/Copperhead_snake_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes copperhead snake men for their attractive scale patterns.**
- **Biome**
- **Temperate Broadleaf Forest Any Temperate Swamp**
- **Variations**
- **Copperhead snake - Copperhead snake man - Giant copperhead snake**
- **Attributes**
- **Alignment:** Savage
- **Learns · Syndrome · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,525 cm 3
- **Mid:** 21,150 cm 3
- **Max:** 35,250 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large copperhead snake with the arms of a man.*

**Copperhead snake men** are animal people variants of the common copperhead snake who can be found in some savage temperate regions. They spawn in groups of 1-3 individuals and possess their animal cousins' venomous syndrome, which causes nausea, pain and swelling on the victim, which is inconvenient but not fatal in most cases. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like copperhead snake men for their *attractive scale patterns*.

|  |
|----|
| "Copperhead snake man" in other / Languages / Dwarven / : / gusil-ser therleth udos / Elven / : / canò-íne imaza onino / Goblin / : / saxo-ostam slorust ngorûg / Human / : / gugir-aru rosha abo |

    [CREATURE:COPPERHEAD_SNAKE_MAN]
        [COPY_TAGS_FROM:COPPERHEAD_SNAKE]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:copperhead snake]
            [CVCT_REPLACEMENT:copperhead snake man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:copperhead snake]
            [CVCT_REPLACEMENT:copperhead snake man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:copperhead snake]
            [CVCT_REPLACEMENT:copperhead snake man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:COPPERHEAD_SNAKE]
            [CVCT_REPLACEMENT:COPPERHEAD_SNAKE_MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:copperhead snake man:copperhead snake men:copperhead snake man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:copperhead snake woman:copperhead snake women:copperhead snake woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:copperhead snake man:copperhead snake men:copperhead snake man]
        [DESCRIPTION:A large copperhead snake with the arms of a man.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:6:0:0]
