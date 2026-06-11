# Mongoose man

> Fonte: [Mongoose man](https://dwarffortresswiki.org/index.php/Mongoose_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mongoose men for their cunning.**
- **Biome**
- **Tropical Savanna Tropical Shrubland**
- **Variations**
- **Mongoose - Mongoose man - Giant mongoose**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
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

*A small person with the head and tail of a mongoose.*

**Mongoose men** are animal people variants of the common mongoose who can be found in savage tropical shrublands and savannas. They spawn in groups of 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like mongoose men for their *cunning* and their *agility*.

Short, fierce, and short.\
*Art by Dave Rapoza*

    [CREATURE:MONGOOSE_MAN]
        [COPY_TAGS_FROM:MONGOOSE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:mongoose man:mongoose men:mongoose man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:mongoose woman:mongoose women:mongoose woman]
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
        [NAME:mongoose man:mongoose men:mongoose man]
        [DESCRIPTION:A small person with the head and tail of a mongoose.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'m']
        [COLOR:7:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
