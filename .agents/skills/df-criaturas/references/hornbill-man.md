# Hornbill man

> Fonte: [Hornbill man](https://dwarffortresswiki.org/index.php/Hornbill_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hornbill men for their great bills.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Hornbill - Hornbill man - Giant hornbill**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 696 cm 3
- **Mid:** 18,125 cm 3
- **Max:** 36,250 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A feathered person with a brightly-colored bill.*

**Hornbill men** are animal people variants of the common hornbill, who inhabit savage tropical forests. They spawn in groups of 1-5 individuals and are generally content to keep to themselves. In terms of size, they are little over half the weight of the average dwarf. All hornbill men are born with Legendary skill in climbing.

Like other savage animal people, hornbill men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like hornbill men for their *great bills*.

*Art by Aki-rain*

    [CREATURE:HORNBILL_MAN]
        [COPY_TAGS_FROM:BIRD_HORNBILL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:hornbill man:hornbill men:hornbill man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:hornbill woman:hornbill women:hornbill woman]
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
        [NAME:hornbill man:hornbill men:hornbill man]
        [DESCRIPTION:A feathered person with a brightly-colored bill.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'h']
        [COLOR:0:0:1]
