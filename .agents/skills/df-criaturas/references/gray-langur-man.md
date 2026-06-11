# Gray langur man

> Fonte: [Gray langur man](https://dwarffortresswiki.org/index.php/Gray_langur_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gray langur men for their social nature.**
- **Biome**
- **Any Desert Any Grassland Any Savanna Any Shrubland Any Forest**
- **Variations**
- **Gray langur - Gray langur man - Giant gray langur**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,250 cm 3
- **Mid:** 21,250 cm 3
- **Max:** 42,500 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A grey person with the head and tail of a gray langur.*

**Gray langur men** are humanoid versions of the common gray langur and a species of animal people, found in a variety of savage biomes. They are a bit over half the size of dwarves when adults and spawn in groups of 5-10 individuals. They share the same thieving disposition of normal langurs, and their greater size in comparison to the animals may make them a threat to civilians who get into fights with them. All gray langur men possess Legendary skill in climbing.

Like other savage animal people, gray langur men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

Some dwarves like gray langur men for their *social nature* and their *vocalizations*.

Still as thieving as a standard langur.

    [CREATURE:GRAY_LANGUR_MAN]
        [COPY_TAGS_FROM:GRAY_LANGUR]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:gray langur man:gray langur men:gray langur man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:gray langur woman:gray langur women:gray langur woman]
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
        [NAME:gray langur man:gray langur men:gray langur man]
        [DESCRIPTION:A grey person with the head and tail of a gray langur.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'l']
        [COLOR:7:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
