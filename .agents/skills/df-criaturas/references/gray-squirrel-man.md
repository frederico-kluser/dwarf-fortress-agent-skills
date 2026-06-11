# Gray squirrel man

> Fonte: [Gray squirrel man](https://dwarffortresswiki.org/index.php/Gray_squirrel_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gray squirrel men for their tails.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Gray squirrel - Gray squirrel man - Giant gray squirrel**
- **Attributes**
- **Alignment:** Savage
- **Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 35,150 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a gray squirrel.*

**Gray squirrel men** are animal people variants of the common gray squirrel who can be found in savage temperate forests. They spawn in groups of anywhere between 1-5 individuals and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All gray squirrel men are born with Legendary skill in climbing.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like gray squirrel men for their *tails*.

Still runs *across* the road when a caravan is coming.

    [CREATURE:SQUIRREL_GRAY_MAN]
        [COPY_TAGS_FROM:SQUIRREL_GRAY]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:gray squirrel man:gray squirrel men:gray squirrel man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:gray squirrel woman:gray squirrel women:gray squirrel woman]
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
        [NAME:gray squirrel man:gray squirrel men:gray squirrel man]
        [DESCRIPTION:A person with the head and tail of a gray squirrel.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'s']
        [COLOR:7:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
