# Polar bear man

> Fonte: [Polar bear man](https://dwarffortresswiki.org/index.php/Polar_bear_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes polar bear men for their strength.**
- **Biome**
- **Glacier Tundra**
- **Variations**
- **Polar bear - Polar bear man - Giant polar bear**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals drink · Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 23,500 cm 3
- **Mid:** 117,500 cm 3
- **Max:** 235,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large person with the head of a polar bear.*

**Polar bear men** are animal people versions of the polar bear that inhabit savage tundras and glaciers. They spawn in groups of 2-10 individuals and can pose a threat to passing civilians. In terms of size, they are almost 4 times larger than a dwarf and should not be trifled with, though they will stand little chance against an armed military squad. Polar bear men love alcohol and will happily steal it and drink it from stockpiles. As a result, they may consume an entire caravan's reserves when arriving in a savage area, if the wagon is left unguarded, not hesitating to drink themselves to death if the supply happens to be sufficient - thus, polar bear men can be lured into traps baited with alcohol stockpiles by placing them behind cage traps. Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like polar bear men for their *strength*.

A humanoid that should be rightfully feared.\
*Art by urbanjeager*

    >[CREATURE:BEAR_POLAR_MAN]
        [COPY_TAGS_FROM:BEAR_POLAR]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:polar bear man:polar bear men:polar bear man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:polar bear woman:polar bear women:polar bear woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:polar bear man:polar bear men:polar bear man]
        [DESCRIPTION:A large person with the head of a polar bear.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'B']
        [COLOR:7:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
