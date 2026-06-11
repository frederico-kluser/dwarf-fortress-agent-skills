# Elk man

> Fonte: [Elk man](https://dwarffortresswiki.org/index.php/Elk_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes elk men for their grace.**
- **Biome**
- **Tundra Temperate Grassland**
- **Variations**
- **Elk - Elk man - Giant elk**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Horn · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 18,500 cm 3
- **Mid:** 92,500 cm 3
- **Max:** 185,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head of an elk.*

**Elk men** are animal people variants of the common elk who can be found in savage temperate grasslands and tundras. They spawn in groups of 1-5 individuals and are generally content to keep to themselves, but will fight back if provoked. In terms of size, they are significantly larger than dwarves and will easy cave in their skulls with their hooves when it comes to a fight.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like elk men for their *grace*.

Often gets tangled in things above him.\
*Art by Eric Polak*

    [CREATURE:ELK_MAN]
        [COPY_TAGS_FROM:ELK]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:elk man:elk men:elk man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:elk woman:elk women:elk woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:HOOF_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:elk man:elk men:elk man]
        [DESCRIPTION:A person with the head of an elk.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'E']
        [COLOR:6:0:0]
