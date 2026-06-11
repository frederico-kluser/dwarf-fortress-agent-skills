# Rhinoceros man

> Fonte: [Rhinoceros man](https://dwarffortresswiki.org/index.php/Rhinoceros_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rhinoceros men for their horns.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland**
- **Variations**
- **Rhinoceros - Rhinoceros man - Giant rhinoceros**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Grazer · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 153,500 cm 3
- **Mid:** 767,500 cm 3
- **Max:** 1,535,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×5)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and horns of a rhinoceros.*

**Rhinoceros men** are animal people versions of the common rhinoceros, who can be found in savage tropical flatlands. They spawn in groups of 5-10 individuals and should never be approached by common peasants, as they rank among the largest of all animal people (being about as heavy as a hippo, or 25 times larger than a dwarf), and, as such, are easily able to tear an unsuspecting intruder apart.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like rhinoceros men for their *horns*.

Why are rhino men such terrible businessmen? They always overcharge.\
*Art by AlsaresLynx*

    [CREATURE:RHINOCEROS_MAN]
        [COPY_TAGS_FROM:RHINOCEROS]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:rhinoceros man:rhinoceros men:rhinoceros man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:rhinoceros woman:rhinoceros women:rhinoceros woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [ATTACK:GORE:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:rhinoceros man:rhinoceros men:rhinoceros man]
        [DESCRIPTION:A person with the head and horns of a rhinoceros.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'R']
        [COLOR:7:0:0]
        [GO_TO_TAG:BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [APPLY_CREATURE_VARIATION:NAIL_MATERIALS]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
