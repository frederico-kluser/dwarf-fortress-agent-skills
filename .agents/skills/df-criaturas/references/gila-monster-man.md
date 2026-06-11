# Gila monster man

> Fonte: [Gila monster man](https://dwarffortresswiki.org/index.php/Gila_monster_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gila monster men for their venomous bite.**
- **Biome**
- **Any Desert**
- **Variations**
- **Gila monster - Gila monster man - Giant gila monster**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Syndrome · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 540 cm 3
- **Mid:** 18,000 cm 3
- **Max:** 36,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A venomous person with the head and tail of a gila monster.*

**Gila monster men** are animal people variants of the common gila monster who inhabit savage deserts. They spawn in groups of 1-3 individuals and like the template animal, they possess a venomous bite that causes pain and swelling on the victim, which they will likely use on any creature who provokes them. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, gila monster men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like gila monster men for their *venomous bite* and their *coloration*.

Will at least yell a warning before poisoning you.

    [CREATURE:GILA_MONSTER_MAN]
        [COPY_TAGS_FROM:GILA_MONSTER]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:gila monster]
            [CVCT_REPLACEMENT:gila monster man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:gila monster]
            [CVCT_REPLACEMENT:gila monster man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:gila monster]
            [CVCT_REPLACEMENT:gila monster man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:GILA_MONSTER]
            [CVCT_REPLACEMENT:GILA_MONSTER_MAN]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:gila monster man:gila monster men:gila monster man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:gila monster woman:gila monster women:gila monster woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_VENOM_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:gila monster man:gila monster men:gila monster man]
        [DESCRIPTION:A venomous person with the head and tail of a gila monster.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'g']
        [COLOR:4:0:1]
