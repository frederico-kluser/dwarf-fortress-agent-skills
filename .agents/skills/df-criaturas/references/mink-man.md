# Mink man

> Fonte: [Mink man](https://dwarffortresswiki.org/index.php/Mink_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mink men for their long bodies.**
- **Biome**
- **Any Temperate Lake Any Temperate River**
- **Variations**
- **Mink - Mink man - Giant mink**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,540 cm 3
- **Mid:** 17,700 cm 3
- **Max:** 35,400 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a mink.*

**Mink men** are animal people variants of the common mink, who can be found in savage temperate lakes and rivers. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, mink men can join civilizations, become historical figures, appear as visitors, and be playable in adventurer mode.

Some dwarves like mink men for their *long bodies*.

    [CREATURE:MINK_MAN]
        [COPY_TAGS_FROM:MINK]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:mink man:mink men:mink man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:mink woman:mink women:mink woman]
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
        [NAME:mink man:mink men:mink man]
        [DESCRIPTION:A person with the head and tail of a mink.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'m']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
