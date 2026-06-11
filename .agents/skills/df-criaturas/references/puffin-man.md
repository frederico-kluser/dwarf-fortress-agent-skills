# Puffin man

> Fonte: [Puffin man](https://dwarffortresswiki.org/index.php/Puffin_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes puffin men for their colorful beaks.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Puffin - Puffin man - Giant puffin**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,415 cm 3
- **Mid:** 17,687.5 cm 3
- **Max:** 35,375 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A feathered person with the head of a puffin.*

**Puffin men** are animal people variants of the common puffin, who inhabit savage arctic oceans. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, puffin men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like puffin men for their *colorful beaks*.

A drawing of a puffin man and a cliff in coloured pencil on paper. All craftsdwarfship is of the highest quality. The puffin man is sitting on the cliff. The puffin man is smiling.\
*Art by HockeyRaven*

    [CREATURE:PUFFIN_MAN]
        [COPY_TAGS_FROM:BIRD_PUFFIN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:puffin man:puffin men:puffin man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:puffin woman:puffin women:puffin woman]
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
        [NAME:puffin man:puffin men:puffin man]
        [DESCRIPTION:A feathered person with the head of a puffin.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'p']
        [COLOR:0:0:1]
