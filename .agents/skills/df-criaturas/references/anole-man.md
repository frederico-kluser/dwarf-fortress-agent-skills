# Anole man

> Fonte: [Anole man](https://dwarffortresswiki.org/index.php/Anole_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes anole men for their ability to change color.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Anole - Anole man - Giant anole**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,045 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of an anole.*

**Anole men** are humanoid versions of the common anole; a species of animal people, found in savage tropical forests. They are a little over half the size of dwarves when adults and spawn in groups of 1-5 individuals. They should pose no threat unless provoked. All anole men are born with Legendary skill in climbing.

Like other savage animal people, anole men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like anole men for their *dewlaps* and their *ability to change color*.

    [CREATURE:ANOLE_MAN]
        [COPY_TAGS_FROM:ANOLE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:anole man:anole men:anole man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:anole woman:anole women:anole woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:anole man:anole men:anole man]
        [DESCRIPTION:A person with the head and tail of an anole.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'a']
        [COLOR:2:0:1]
