# Eagle man

> Fonte: [Eagle man](https://dwarffortresswiki.org/index.php/Eagle_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes eagle men for their high soaring.**
- **Biome**
- **Any Wetland Any Forest Any Shrubland Any Savanna Any Grassland Any Desert Mountain Tundra**
- **Variations**
- **Eagle - Eagle man - Giant eagle**
- **Attributes**
- **Alignment:** Savage
- **Flying · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,295 cm 3
- **Mid:** 18,500 cm 3
- **Max:** 37,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A feathered person with the head and wings of an eagle.*

**Eagle men** are animal people variants of the common eagle, who can be found in most savage biomes, spawning in groups of anywhere between 1-3 individuals, and are generally content to keep to themselves. In terms of size, they are a little over half the weight of the average dwarf. All eagle men are born with Legendary skill in climbing.

Like other savage animal people, eagle men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like eagle men for their *high soaring*.

*Art by Kitslams Art*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Some eagle men musicians will occasionally sing songs about a strange inn that travelers can exit any time they like, but can never truly leave. Such songs are always accompanied by a two-minute solo on a stringed instrument.

|  |
|----|
| "Eagle man" in other / Languages / Dwarven / : / lorsïth udos / Elven / : / osime onino / Goblin / : / kedusm ngorûg / Human / : / ica abo |

    [CREATURE:EAGLE_MAN]
        [COPY_TAGS_FROM:BIRD_EAGLE]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:eagle man:eagle men:eagle man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:eagle woman:eagle women:eagle woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:TALON_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:BEAK_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:eagle man:eagle men:eagle man]
        [DESCRIPTION:A feathered person with the head and wings of an eagle.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'e']
        [COLOR:6:0:0]
