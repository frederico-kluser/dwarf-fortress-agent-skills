# Python man

> Fonte: [Python man](https://dwarffortresswiki.org/index.php/Python_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes python men for their great size.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Python - Python man - Giant python**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 27 cm 3
- **Mid:** 33,750 cm 3
- **Max:** 135,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large python with arms of a man.*

**Python men** are animal people versions of the common python, who can be found in savage tropical moist broadleaf forests. They spawn in groups of 1-3 individuals and are generally content to keep to themselves, but should nonetheless be approached with caution. In terms of size, they are a little over twice the weight of the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like python men for their *great size*.

Can slither-bench about 250lbs.

    [CREATURE:PYTHON_MAN]
        [COPY_TAGS_FROM:PYTHON]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:python man:python men:python man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:python woman:python women:python woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:python man:python men:python man]
        [DESCRIPTION:A large python with arms of a man.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
