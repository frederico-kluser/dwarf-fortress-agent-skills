# Impala man

> Fonte: [Impala man](https://dwarffortresswiki.org/index.php/Impala_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes impala men for their mighty leaps.**
- **Biome**
- **Tropical Savanna Tropical Grassland**
- **Variations**
- **Impala - Impala man - Giant impala**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,000 cm 3
- **Mid:** 30,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A slender, horned man with the head and tail of a impala.*

**Impala men** are animal people versions of the common impala, found in tropical savanna and grasslands. They spawn in groups of 5-10 individuals and are generally content to keep to themselves. In terms of size, they are the same size as the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode. Impala men are able to wear dwarf-sized armor and clothing, making it a good choice for adventurers of their species to start in a dwarven civilization.

Some dwarves like impala men for their *mighty leaps*.

    [CREATURE:IMPALA_MAN]
        [COPY_TAGS_FROM:IMPALA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:impala man:impala men:impala man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:impala woman:impala women:impala woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:HOOF_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:impala man:impala men:impala man]
        [DESCRIPTION:A slender, horned man with the head and tail of a impala.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'i']
        [COLOR:6:0:0]
