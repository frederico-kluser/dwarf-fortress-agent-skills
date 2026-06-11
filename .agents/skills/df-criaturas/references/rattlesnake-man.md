# Rattlesnake man

> Fonte: [Rattlesnake man](https://dwarffortresswiki.org/index.php/Rattlesnake_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rattlesnake men for their warning rattle.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Rattlesnake - Rattlesnake man - Giant rattlesnake**
- **Attributes**
- **Alignment:** Savage
- **Learns · Syndrome · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 220 cm 3
- **Mid:** 19,250 cm 3
- **Max:** 38,500 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person resembling a large rattlesnake with arms.*

**Rattlesnake men** are animal people versions of the common rattlesnake, who can be found in any non-freezing savage region. They spawn in groups of 1-3 individuals and are generally content to keep to themselves, but like their animal versions, their bite possesses a strong syndrome which should be avoided. In terms of size, they are a little over half the weight of the average dwarf.

Rattlesnake men will attempt to attack your livestock, but not your dwarves.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like rattlesnake men for their *warning rattle*.

Rattle also doubles as a metronome.

    [CREATURE:RATTLESNAKE_MAN]
        [COPY_TAGS_FROM:RATTLESNAKE]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:rattlesnake]
            [CVCT_REPLACEMENT:rattlesnake man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:rattlesnake]
            [CVCT_REPLACEMENT:rattlesnake man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:rattlesnake]
            [CVCT_REPLACEMENT:rattlesnake man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:RATTLESNAKE]
            [CVCT_REPLACEMENT:RATTLESNAKE_MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:rattlesnake man:rattlesnake men:rattlesnake man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:rattlesnake woman:rattlesnake women:rattlesnake woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:rattlesnake man:rattlesnake men:rattlesnake man]
        [DESCRIPTION:A person resembling a large rattlesnake with arms.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:7:0:0]
