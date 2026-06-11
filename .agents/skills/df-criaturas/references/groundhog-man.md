# Groundhog man

> Fonte: [Groundhog man](https://dwarffortresswiki.org/index.php/Groundhog_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes groundhog men for their ability to burrow.**
- **Biome**
- **Temperate Shrubland Temperate Savanna Temperate Grassland**
- **Variations**
- **Groundhog - Groundhog man - Giant groundhog**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,650 cm 3
- **Mid:** 18,250 cm 3
- **Max:** 36,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and fur of a groundhog.*

**Groundhog men** are animal people variants of the common groundhog who can be found in savage temperate grasslands. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like groundhog men for their *ability to burrow*.

May sometimes get cursed to repeat the same days over and over.\
*Art by syam-arifin*

    >[CREATURE:GROUNDHOG_MAN]
        [COPY_TAGS_FROM:GROUNDHOG]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:groundhog man:groundhog men:groundhog man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:groundhog woman:groundhog women:groundhog woman]
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
        [NAME:groundhog man:groundhog men:groundhog man]
        [DESCRIPTION:A person with the head and fur of a groundhog.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'g']
        [COLOR:6:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
