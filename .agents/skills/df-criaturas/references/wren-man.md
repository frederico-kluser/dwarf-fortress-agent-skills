# Wren man

> Fonte: [Wren man](https://dwarffortresswiki.org/index.php/Wren_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes wren men for their intricate songs.**
- **Biome**
- **Any Forest Any Grassland Any Savanna Any Shrubland Any Wetland Any Desert**
- **Variations**
- **Wren - Wren man - Giant wren**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,377.5 cm 3
- **Max:** 35,020 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and wings of a wren.*

**Wren men** are humanoid versions of the common wren and a species of unremarkable animal people, found in most savage biomes. They are only half the size of an adult dwarf and as such, are unlikely to be a threat to even an unarmed civilian, though their ability to fly may make them difficult to hit. Like other savage animal people, wren men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors, become historical figures, or be playable in adventurer mode.

Some dwarves like wren men for their *intricate songs*.

Tolto: Wren woman guardian of Singemetal and slayer of the werepanda. Her muscular form contrasts her diminutive stature.\
*Art by Paranoid_metroid*

    [CREATURE:WREN_MAN]
        [COPY_TAGS_FROM:BIRD_WREN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:wren man:wren men:wren man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:wren woman:wren women:wren woman]
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
        [NAME:wren man:wren men:wren man]
        [DESCRIPTION:A person with the head and wings of a wren.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'w']
        [COLOR:6:0:0]
