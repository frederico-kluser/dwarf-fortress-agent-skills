# Chinchilla man

> Fonte: [Chinchilla man](https://dwarffortresswiki.org/index.php/Chinchilla_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes chinchilla men for their fur.**
- **Biome**
- **Mountain**
- **Variations**
- **Chinchilla - Chinchilla man - Giant chinchilla**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,525 cm 3
- **Mid:** 17,625 cm 3
- **Max:** 35,250 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A hairy person with the head and tail of a chinchilla.*

**Chinchilla men** are animal people variants of the common chinchilla, who can inhabit savage mountains, spawning in groups of 3-5 individuals, and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf.

Like other savage animal people, chinchilla men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like chinchilla men for their *fur*.

No one takes him seriously because of his cuteness.\
*Art by AssasinMonkey*

    [CREATURE:CHINCHILLA_MAN]
        [COPY_TAGS_FROM:CHINCHILLA]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:chinchilla man:chinchilla men:chinchilla man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:chinchilla woman:chinchilla women:chinchilla woman]
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
        [NAME:chinchilla man:chinchilla men:chinchilla man]
        [DESCRIPTION:A hairy person with the head and tail of a chinchilla.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:3:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:7:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
