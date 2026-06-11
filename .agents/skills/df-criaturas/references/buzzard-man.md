# Buzzard man

> Fonte: [Buzzard man](https://dwarffortresswiki.org/index.php/Buzzard_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes buzzard men for their striking red face.**
- **Biome**
- **Temperate Freshwater Marsh Temperate Saltwater Marsh Temperate Grassland Temperate Savanna Any Desert**
- **Variations**
- **Buzzard - Buzzard man - Giant buzzard**
- **Attributes**
- **Alignment:** Savage
- **Flying · Steals food · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,275 cm 3
- **Mid:** 17,850 cm 3
- **Max:** 35,700 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

*A person with the head and wings of a buzzard.*

If you dislike buzzards because those flying pests steal all the food from your fortress where they can lay their claws on... You'll certainly hate their bigger, stronger and smarter relatives, the **buzzard (wo)men**.

While these animal people generally show little interest in attacking your dwarves directly, their presence causes serious disruption to the operation of a fortress; they don't mind attacking any food-hauler who does not voluntarily "donate" the hauled food; scare the hell out of your cattle and so on. They even "help" you harvesting outdoor crops, of course for their own gain.

The real bad part is that these intelligent creatures can not be tamed and dwarves refuse to butcher and eat them.

Some dwarves like buzzard men for their *striking red face*.

|  |
|----|
| "Buzzard man" in other / Languages / Dwarven / : / setnek udos / Elven / : / acithe onino / Goblin / : / âng ngorûg / Human / : / jozi abo |

    >[CREATURE:BUZZARD_MAN]
        [COPY_TAGS_FROM:BIRD_BUZZARD]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:buzzard man:buzzard men:buzzard man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:buzzard woman:buzzard women:buzzard woman]
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
        [NAME:buzzard man:buzzard men:buzzard man]
        [DESCRIPTION:A person with the head and wings of a buzzard.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'b']
        [COLOR:0:0:1]
