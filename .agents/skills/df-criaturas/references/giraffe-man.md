# Giraffe man

> Fonte: [Giraffe man](https://dwarffortresswiki.org/index.php/Giraffe_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giraffe men for their long necks.**
- **Biome**
- **Tropical Savanna Tropical Shrubland**
- **Variations**
- **Giraffe - Giraffe man - Giant giraffe**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 53,500 cm 3
- **Mid:** 267,500 cm 3
- **Max:** 535,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×5)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and neck of a giraffe.*

**Giraffe men** are animal people variants of the common giraffe who can be found in savage tropical shrublands and savannas. They spawn in groups of 5-10 individuals and generally do not start fights of their own volition. They are almost nine times larger than the average dwarf.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like giraffe men for their *long necks*.

Has no trouble seeing over things.

    [CREATURE:GIRAFFE_MAN]
        [COPY_TAGS_FROM:GIRAFFE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:giraffe man:giraffe men:giraffe man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:giraffe woman:giraffe women:giraffe woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:NAIL_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:giraffe man:giraffe men:giraffe man]
        [DESCRIPTION:A person with the head and neck of a giraffe.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'G']
        [COLOR:6:0:0]
        [GO_TO_TAG:BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [APPLY_CREATURE_VARIATION:NAIL_MATERIALS]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
