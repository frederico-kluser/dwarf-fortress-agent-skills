# Lion tamarin man

> Fonte: [Lion tamarin man](https://dwarffortresswiki.org/index.php/Lion_tamarin_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes lion tamarin men for their small size.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Lion tamarin - Lion tamarin man - Giant lion tamarin**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,310 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*An orange person with the head and tail of a lion tamarin.*

**Lion tamarin men** are humanoid versions of the common lion tamarin and a species of unremarkable animal people, found in savage tropical moist broadleaf forests. They are a little over half the size of dwarves when adults and spawn in groups of 1-5 individuals. They should pose no threat unless provoked. All lion tamarin men are born with Legendary skill in climbing.

Like other savage animal people, lion tamarin men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like lion tamarin men for their *small size* and their *manes*.

    [CREATURE:LION_TAMARIN_MAN]
        [COPY_TAGS_FROM:LION_TAMARIN]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:lion tamarin man:lion tamarin men:lion tamarin man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:lion tamarin woman:lion tamarin women:lion tamarin woman]
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
        [NAME:lion tamarin man:lion tamarin men:lion tamarin man]
        [DESCRIPTION:An orange person with the head and tail of a lion tamarin.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'l']
        [COLOR:6:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
