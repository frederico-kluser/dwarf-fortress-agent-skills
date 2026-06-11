# Ostrich man

> Fonte: [Ostrich man](https://dwarffortresswiki.org/index.php/Ostrich_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ostrich men for their long necks.**
- **Biome**
- **Tropical Savanna Tropical Grassland Any Desert**
- **Variations**
- **Ostrich - Ostrich man - Giant ostrich**
- **Attributes**
- **Alignment:** Savage
- **Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,600 cm 3
- **Mid:** 40,000 cm 3
- **Max:** 80,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*This is a medium-sized creature with legs and arms, but the long neck and head of an ostrich.*

**Ostrich men** are animal people variants of the common ostrich who inhabit savage deserts and some tropical grasslands. They spawn in groups of anywhere between 5-10 individuals and are generally content to keep to themselves. In terms of size, they are a little bigger than the average human. Like standard ostriches, the sprite for male ostrich men will have black feathers, with ostrich women having greyish-brown feathers.

Like other savage animal people, ostrich men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like ostrich men for their *long necks* and their *giant eggs*.

Note: May lay very strange eggs.\
*Art by Arne*

    [CREATURE:OSTRICH MAN]
        [COPY_TAGS_FROM:BIRD_OSTRICH]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:ostrich man:ostrich men:ostrich man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:ostrich woman:ostrich women:ostrich woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TALON_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:ostrich man:ostrich men:ostrich man]
        [DESCRIPTION:This is a medium-sized creature with legs and arms, but the long neck and head of an ostrich.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'O']
        [COLOR:0:0:1]
