# Cassowary man

> Fonte: [Cassowary man](https://dwarffortresswiki.org/index.php/Cassowary_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cassowary men for their casques.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Cassowary - Cassowary man - Giant cassowary**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 600 cm 3
- **Mid:** 30,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A brightly-colored person with the head of a cassowary.*

**Cassowary men** are humanoid versions of the common cassowary and a species of unremarkable animal people, found in savage tropical moist broadleaf forests. They are exactly the size of dwarves when adults, and spawn in groups of 5-10 individuals, though they are unlikely to pose any danger to your fortress unless provoked.

Like other savage animal people, cassowary men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like cassowary men for their *casques*.

A cassowary woman.\
*Art by MommaCabbit*

    [CREATURE:CASSOWARY_MAN]
        [COPY_TAGS_FROM:BIRD_CASSOWARY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:cassowary man:cassowary men:cassowary man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:cassowary woman:cassowary women:cassowary woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TALON_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:cassowary man:cassowary men:cassowary man]
        [DESCRIPTION:A brightly-colored person with the head of a cassowary.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:0:0:1]
