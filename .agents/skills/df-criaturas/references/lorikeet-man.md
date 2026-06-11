# Lorikeet man

> Fonte: [Lorikeet man](https://dwarffortresswiki.org/index.php/Lorikeet_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes lorikeet men for their playful personalities.**
- **Biome**
- **Tropical Moist Broadleaf Forest Mangrove Swamp**
- **Variations**
- **Lorikeet - Lorikeet man - Giant lorikeet**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,755 cm 3
- **Max:** 35,100 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A colorful person with the head and wings of a lorikeet.*

**Lorikeet men** are animal people variants of the common lorikeet, who inhabit savage mangroves and tropical moist broadleaf forests. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All lorikeet men are born with Legendary skill in climbing.

Like other savage animal people, lorikeet men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like lorikeet men for their *bright coloration* and their *playful personalities*.

    [CREATURE:LORIKEET_MAN]
        [COPY_TAGS_FROM:BIRD_LORIKEET]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:lorikeet man:lorikeet men:lorikeet man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:lorikeet woman:lorikeet women:lorikeet woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TALON_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:lorikeet man:lorikeet men:lorikeet man]
        [DESCRIPTION:A colorful person with the head and wings of a lorikeet.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'l']
        [COLOR:4:0:1]
