# Desert tortoise man

> Fonte: [Desert tortoise man](https://dwarffortresswiki.org/index.php/Desert_tortoise_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes desert tortoise men for their longevity.**
- **Biome**
- **Any Desert**
- **Variations**
- **Desert tortoise - Desert tortoise man - Giant desert tortoise**
- **Attributes**
- **Alignment:** Savage
- **Learns · Shell · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 274.54545454545 cm 3
- **Mid:** 18,875 cm 3
- **Max:** 37,750 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A reptile person with the head and tail of a desert tortoise.*

**Desert tortoise men** are humanoid versions of the common desert tortoise and a species of unremarkable animal people, found in savage desert biomes. They are a little over half the size of an adult dwarf and spawn in groups of 1-5 individuals, who are unlikely to pose any danger to your fortress.

Like other savage animal people, desert tortoise men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like desert tortoise men for their *shells* and their *longevity*.

    [CREATURE:DESERT_TORTOISE_MAN]
        [COPY_TAGS_FROM:DESERT TORTOISE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:desert tortoise man:desert tortoise men:desert tortoise man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:desert tortoise woman:desert tortoise women:desert tortoise woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:desert tortoise man:desert tortoise men:desert tortoise man]
        [DESCRIPTION:A reptile person with the head and tail of a desert tortoise.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'t']
        [COLOR:6:0:0]
