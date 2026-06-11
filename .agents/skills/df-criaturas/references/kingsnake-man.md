# Kingsnake man

> Fonte: [Kingsnake man](https://dwarffortresswiki.org/index.php/Kingsnake_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kingsnake men for their coloration.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Mountain Any Desert**
- **Variations**
- **Kingsnake - Kingsnake man - Giant kingsnake**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 476.66666666667 cm 3
- **Mid:** 17,875 cm 3
- **Max:** 35,750 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A legless person with the head and tail of a kingsnake.*

**Kingsnake men** are animal people variants of the common kingsnake who can be found in various savage biomes. They spawn in groups of 1-3 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like kingsnake men for their *coloration* and their *habit of eating other snakes*.

|  |
|----|
| "Kingsnake man" in other / Languages / Dwarven / : / etar therleth udos / Elven / : / afedo imaza onino / Goblin / : / zozlo slorust ngorûg / Human / : / deng rosha abo |

    [CREATURE:KINGSNAKE_MAN]
        [COPY_TAGS_FROM:KINGSNAKE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:kingsnake man:kingsnake men:kingsnake man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:kingsnake woman:kingsnake women:kingsnake woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:kingsnake man:kingsnake men:kingsnake man]
        [DESCRIPTION:A legless person with the head and tail of a kingsnake.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'k']
        [COLOR:7:0:1]
