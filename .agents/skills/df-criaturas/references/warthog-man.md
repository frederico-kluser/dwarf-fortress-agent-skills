# Warthog man

> Fonte: [Warthog man](https://dwarffortresswiki.org/index.php/Warthog_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes warthog men for their short tempers.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland**
- **Variations**
- **Warthog - Warthog man - Giant warthog**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 8,500 cm 3
- **Mid:** 42,500 cm 3
- **Max:** 85,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head of a warthog.*

**Warthog men** are animal people versions of the common warthog, who can be found in savage tropical flatlands. They spawn in groups of 5-10 individuals and are generally content to keep to themselves, but may pick fights with civilians if approached. In terms of size, they are a little larger than the average human.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like warthog men for their *short tempers*.

|  |
|----|
| "Warthog man" in other / Languages / Dwarven / : / omtug-tarag udos / Elven / : / wiÿeve-ÿara onino / Goblin / : / tomom-snam ngorûg / Human / : / vuk-celo abo |

    [CREATURE:WARTHOG_MAN]
        [COPY_TAGS_FROM:WARTHOG]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:warthog man:warthog men:warthog man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:warthog woman:warthog women:warthog woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:HOOF_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:TUSK_STAB_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:warthog man:warthog men:warthog man]
        [DESCRIPTION:A person with the head of a warthog.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'W']
        [COLOR:6:0:0]
        [GO_TO_TAG:BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [APPLY_CREATURE_VARIATION:NAIL_MATERIALS]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
