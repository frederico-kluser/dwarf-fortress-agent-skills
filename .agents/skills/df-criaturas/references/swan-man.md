# Swan man

> Fonte: [Swan man](https://dwarffortresswiki.org/index.php/Swan_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes swan men for their beauty.**
- **Biome**
- **Any Temperate Lake Any Temperate Marsh**
- **Variations**
- **Swan - Swan man - Giant swan**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,200 cm 3
- **Mid:** 20,000 cm 3
- **Max:** 40,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a swan.*

**Swan men** are humanoid versions of the common swan and a species of animal people; notable for being the largest playable species capable of flying in adventure mode, found in some savage temperate lakes and marshes. They are a little over half the size of an adult dwarf and are unlikely to pose a threat to a fortress' inhabitants.

Like other savage animal people, swan men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like swan men for their *beauty*.

Elegant/10

    [CREATURE:SWAN_MAN]
        [COPY_TAGS_FROM:BIRD_SWAN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:swan man:swan men:swan man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:swan woman:swan women:swan woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:swan man:swan men:swan man]
        [DESCRIPTION:A person with the head and wings of a swan.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:2]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:7:0:1]
