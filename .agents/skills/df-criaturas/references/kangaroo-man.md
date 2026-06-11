# Kangaroo man

> Fonte: [Kangaroo man](https://dwarffortresswiki.org/index.php/Kangaroo_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kangaroo men for their pouches.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Any Desert**
- **Variations**
- **Kangaroo - Kangaroo man - Giant kangaroo**
- **Attributes**
- **Alignment:** Savage
- **Learns · Grazer · Milkable · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 8,000 cm 3
- **Mid:** 40,000 cm 3
- **Max:** 80,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and powerful legs of a kangaroo.*

**Kangaroo men** are humanoid versions of the common kangaroo and a species of unremarkable animal people, save for their stronger-than-average kick, found in savage desert and temperate biomes. They are about a third heavier than a dwarf, but should pose no real threat unless provoked.

Like other savage animal people, kangaroo men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors or be playable in adventurer mode.

As the animal person template does not remove it, kangaroo women produce milk.

Some dwarves like kangaroo men for their *pouches* and their *great leaps*.

White men *can* jump.

    [CREATURE:KANGAROO_MAN]
        [COPY_TAGS_FROM:KANGAROO]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:kangaroo]
            [CVCT_REPLACEMENT:kangaroo man]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:kangaroo]
            [CVCT_REPLACEMENT:kangaroo man]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:kangaroo man:kangaroo men:kangaroo man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:kangaroo woman:kangaroo women:kangaroo woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_HIGHVEL_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:kangaroo man:kangaroo men:kangaroo man]
        [DESCRIPTION:A person with the head and powerful legs of a kangaroo.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:5:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'K']
        [COLOR:6:0:0]
