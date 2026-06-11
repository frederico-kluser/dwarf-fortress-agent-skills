# Emu man

> Fonte: [Emu man](https://dwarffortresswiki.org/index.php/Emu_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes emu men for their size.**
- **Biome**
- **Temperate Shrubland Any Temperate Forest**
- **Variations**
- **Emu - Emu man - Giant emu**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,200 cm 3
- **Mid:** 26,250 cm 3
- **Max:** 52,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A feathered person with the head of an emu.*

**Emu men** are animal people variants of the common emu, who inhabit savage temperate forests and shrublands, spawning in groups of anywhere between 1-5 individuals, and are generally content to keep to themselves. In terms of size, they are a little smaller than the average dwarf.

Like other savage animal people, emu men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like emu men for their *size* and their *inquisitive nature*.

Clothing in-game is vastly different.\
*Art by Frits Ahlefeldt*

    [CREATURE:EMU_MAN]
        [COPY_TAGS_FROM:BIRD_EMU]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:emu man:emu men:emu man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:emu woman:emu women:emu woman]
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
        [NAME:emu man:emu men:emu man]
        [DESCRIPTION:A feathered person with the head of an emu.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'E']
        [COLOR:6:0:0]
