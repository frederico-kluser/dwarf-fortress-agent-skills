# Sloth man

> Fonte: [Sloth man](https://dwarffortresswiki.org/index.php/Sloth_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sloth men for their slow movement.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Sloth - Sloth man - Giant sloth**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,800 cm 3
- **Mid:** 19,000 cm 3
- **Max:** 38,000 cm 3
- **Age**
- **Adult at:** 2
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head of a sloth.*

**Sloth men** are animal people variants of the common sloth, appearing in savage tropical forests, in groups of 1-5 individuals. Like other sloth-based creatures, sloth men are quite slow, being about half as fast as a dwarf. They are not particularly dangerous, and generally avoid confrontations.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like sloth men for their *slow movement*.

Takes a while to do things...\
*Art by Gabriel Ramos*

|  |
|----|
| "Sloth man" in other / Languages / Dwarven / : / gäzot udos / Elven / : / timeba onino / Goblin / : / ongo ngorûg / Human / : / thruque abo |

    [CREATURE:SLOTH_MAN]
        [COPY_TAGS_FROM:SLOTH]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:sloth man:sloth men:sloth man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:sloth woman:sloth women:sloth woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:sloth man:sloth men:sloth man]
        [DESCRIPTION:A person with the head of a sloth.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:7:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
