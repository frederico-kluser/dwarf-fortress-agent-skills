# Gazelle man

> Fonte: [Gazelle man](https://dwarffortresswiki.org/index.php/Gazelle_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gazelle men for their grace.**
- **Biome**
- **Tropical Savanna Tropical Grassland**
- **Variations**
- **Gazelle - Gazelle man - Giant gazelle**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,500 cm 3
- **Mid:** 22,500 cm 3
- **Max:** 45,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A horned person with the head of a gazelle.*

**Gazelle men** are animal people variants of the common gazelle who can be found in savage tropical grasslands and savannas. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like gazelle men for their *grace*.

-

-

    [CREATURE:GAZELLE_MAN]
        [COPY_TAGS_FROM:GAZELLE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:gazelle man:gazelle men:gazelle man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:gazelle woman:gazelle women:gazelle woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:HOOF_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:gazelle man:gazelle men:gazelle man]
        [DESCRIPTION:A horned person with the head of a gazelle.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'g']
        [COLOR:6:0:0]
