# Weasel man

> Fonte: [Weasel man](https://dwarffortresswiki.org/index.php/Weasel_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes weasel men for their long bodies.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra Tundra**
- **Variations**
- **Weasel - Weasel man - Giant weasel**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,510 cm 3
- **Mid:** 17,550 cm 3
- **Max:** 35,100 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a weasel.*

**Weasel men** are humanoid versions of the common weasel and a species of unremarkable animal people, found in most savage regions. They are a little over half the size of dwarves when adults and spawn in groups of 1-5 individuals. They should pose no threat unless provoked.

Like other savage animal people, weasel men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like weasel men for their *long bodies* and their *short legs*.

Untrustworthy.

|  |
|----|
| "Weasel man" in other / Languages / Dwarven / : / bamgûs udos / Elven / : / lethina onino / Goblin / : / balu ngorûg / Human / : / lussum abo |

    [CREATURE:WEASEL_MAN]
        [COPY_TAGS_FROM:WEASEL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:weasel man:weasel men:weasel man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:weasel woman:weasel women:weasel woman]
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
        [NAME:weasel man:weasel men:weasel man]
        [DESCRIPTION:A person with the head and tail of a weasel.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'w']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
