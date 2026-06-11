# Anaconda man

> Fonte: [Anaconda man](https://dwarffortresswiki.org/index.php/Anaconda_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes anaconda men for their great size.**
- **Biome**
- **Any Tropical Wetland**
- **Variations**
- **Anaconda - Anaconda man - Giant anaconda**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 85 cm 3
- **Mid:** 42,500 cm 3
- **Max:** 85,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large anaconda with the torso and arms of a man.*

**Anaconda men** are animal people variants of the common anaconda who can be found in savage tropical wetlands, spawning in groups of 1-5 individuals, and may injure dwarves who attempt to provoke them. In terms of size, they are a little larger than humans.

Like other savage animal people, anaconda men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like anaconda men for their *great size*.

An anaconda man as a shaman.\
*Art by conorburkeart*

    [CREATURE:ANACONDA_MAN]
        [COPY_TAGS_FROM:ANACONDA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:anaconda man:anaconda men:anaconda man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:anaconda woman:anaconda women:anaconda woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:anaconda man:anaconda men:anaconda man]
        [DESCRIPTION:A large anaconda with the torso and arms of a man.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'A']
        [COLOR:2:0:1]
