# Black bear man

> Fonte: [Black bear man](https://dwarffortresswiki.org/index.php/Black_bear_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes black bear men for their strength.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Black bear - Black bear man - Giant black bear**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals drink · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 9,500 cm 3
- **Mid:** 47,500 cm 3
- **Max:** 95,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×2)**

*A large person with the head of a black bear.*

**Black bear men** are animal people variants of the common black bear, who can be found in savage temperate forests and taigas, spawning in groups of anywhere between 2-10 individuals, and retain the thieving disposition of their animal counterparts, running off with your food and drinking your booze whenever they can. They are significantly larger than a dwarf and can easily shred a peasant to pieces if provoked.

Like other savage animal people, black bear men can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like black bear men for their *strength*.

## Trivia

- Currently, black bear men and grizzly bear men share the same sprite.

Pretty much invented the "bear boogie" that elves tried to copy.\
*Art by Sarasti*

|  |
|----|
| "Black bear man" in other / Languages / Dwarven / : / udir uvel udos / Elven / : / opa atha onino / Goblin / : / ogur ron ngorûg / Human / : / oth rorec abo |

    >[CREATURE:BEAR_BLACK_MAN]
        [COPY_TAGS_FROM:BEAR_BLACK]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:black bear man:black bear men:black bear man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:black bear woman:black bear women:black bear woman]
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
        [NAME:black bear man:black bear men:black bear man]
        [DESCRIPTION:A large person with the head of a black bear.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:2:10]
        [MAXAGE:60:80]
        [CREATURE_TILE:'B']
        [COLOR:0:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
