# Bushmaster man

> Fonte: [Bushmaster man](https://dwarffortresswiki.org/index.php/Bushmaster_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bushmaster men for their deadly bite.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Bushmaster - Bushmaster man - Giant bushmaster**
- **Attributes**
- **Alignment:** Savage
- **Learns · Syndrome · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 92.352941176471 cm 3
- **Mid:** 19,625 cm 3
- **Max:** 39,250 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large bushmaster with the arms of a man.*

**Bushmaster men** are animal people variants of the common bushmaster, who can be found in savage tropical moist broadleaf forests, spawning in groups of 1-3 individuals, and share their animal counterparts' syndrome, leading to a quick death by asphyxiation to those they bite - because of this, they should be approached with caution. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, bushmaster men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like bushmaster men for their *deadly bite*.

|  |
|----|
| "Bushmaster man" in other / Languages / Dwarven / : / rorul-kôn udos / Elven / : / alithi-ithera onino / Goblin / : / ngontek-âs ngorûg / Human / : / iwo-siñur abo |

    [CREATURE:BUSHMASTER_MAN]
        [COPY_TAGS_FROM:BUSHMASTER]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:bushmaster]
            [CVCT_REPLACEMENT:bushmaster man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:bushmaster]
            [CVCT_REPLACEMENT:bushmaster man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:bushmaster]
            [CVCT_REPLACEMENT:bushmaster man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:BUSHMASTER]
            [CVCT_REPLACEMENT:BUSHMASTER_MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:bushmaster man:bushmaster men:bushmaster man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:bushmaster woman:bushmaster women:bushmaster woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:bushmaster man:bushmaster men:bushmaster man]
        [DESCRIPTION:A large bushmaster with the arms of a man.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:6:0:0]
