# Harp seal man

> Fonte: [Harp seal man](https://dwarffortresswiki.org/index.php/Harp_seal_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes harp seal men for their adorable pups.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Harp seal - Harp seal man - Giant harp seal**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,175 cm 3
- **Mid:** 58,750 cm 3
- **Max:** 117,500 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and flippers of a harp seal.*

**Harp seal men** are animal people variants of the common harp seal who can be found in savage arctic oceans. They spawn in groups of 3-7 individuals and are generally content to keep to themselves. In terms of size, they are almost twice the weight of the average dwarf, and may pose a threat to civilians who pick fights with them.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like harp seal men for their *adorable pups*.

*Art by Devilingo*

    [CREATURE:HARP_SEAL_MAN]
        [COPY_TAGS_FROM:HARP_SEAL]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:FRONT_BODY_FLIPPERS:REAR_BODY_FLIPPERS]
            [CVCT_REPLACEMENT:REAR_BODY_FLIPPERS]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:harp seal man:harp seal men:harp seal man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:harp seal woman:harp seal women:harp seal woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:703:505:274:1900:2900] 32 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:harp seal man:harp seal men:harp seal man]
        [DESCRIPTION:A person with the head and flippers of a harp seal.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:3:7]
        [MAXAGE:60:80]
        [CREATURE_TILE:'h']
        [COLOR:7:0:0]
