# Saltwater crocodile man

> Fonte: [Saltwater crocodile man](https://dwarffortresswiki.org/index.php/Saltwater_crocodile_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes saltwater crocodile men for their strength.**
- **Biome**
- **Tropical Freshwater Swamp Tropical Freshwater Marsh Tropical Saltwater Swamp Tropical Saltwater Marsh Mangrove Swamp Tropical Saltwater River Tropical Brackish River Tropical Freshwater River**
- **Variations**
- **Saltwater crocodile - Saltwater crocodile man - Giant saltwater crocodile**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Learns · Egglaying · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 32.625 cm 3
- **Mid:** 217,500 cm 3
- **Max:** 435,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A person with the head and tail of a saltwater crocodile.*

**Saltwater crocodile men** are a species of animal people that happens to appear as humanoid versions of the common saltwater crocodile, found in savage tropical wetlands. Their most remarkable trait is their great size; they are over seven times the size of a dwarf and can make quick work of civilians and sometimes inexperienced military squads due to their aggressiveness, meaning caution should be taken when they are wandering through the map.

Like other savage animal people, saltwater crocodile men may occasionally join civilizations, becoming full-fledged citizens who may appear in your fortress as visitors, or be playable in adventurer mode. Due to being based on the raw files of the normal animal, they lack the ability to jump.

Some dwarves like saltwater crocodile men for their *strength*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Crocodile men are often known to favor using large, two-handed bladed weapons in combat. They are also known for their apparent hatred of Jackal Men, who they will go to great lengths to kill. The reason behind this hatred is currently unclear to Dwarven scholars.

Despite popular belief, crocodile men are not interested in computer rooms.

Murderous saltwater crocodile men (but not women) have been known to make their homes in sewers, feast on human flesh, and occasionally fight with bat men.

Still wins "strongest bite" contests.\
*Art by vladgheneli*

    [CREATURE:CROCODILE_SALTWATER_MAN]
        [COPY_TAGS_FROM:CROCODILE_SALTWATER]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:saltwater crocodile man:saltwater crocodile men:saltwater crocodile man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:saltwater crocodile woman:saltwater crocodile women:saltwater crocodile woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:CLAW_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:saltwater crocodile man:saltwater crocodile men:saltwater crocodile man]
        [DESCRIPTION:A person with the head and tail of a saltwater crocodile.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [MAXAGE:60:80]
        [CREATURE_TILE:'C']
        [COLOR:2:0:0]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
