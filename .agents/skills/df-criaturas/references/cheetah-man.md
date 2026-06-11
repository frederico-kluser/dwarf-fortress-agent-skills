# Cheetah man

> Fonte: [Cheetah man](https://dwarffortresswiki.org/index.php/Cheetah_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cheetah men for their speed.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland**
- **Variations**
- **Cheetah - Cheetah man - Giant cheetah**
- **Attributes**
- **Alignment:** Savage
- **Learns · War animals · Hunting animals · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,000 cm 3
- **Mid:** 30,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 60-80
- **Cannot be butchered ( Value multiplier ×3)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A spotted person with the head and tail of a cheetah.*

**Cheetah men** are animal people variants of the common cheetah who can be found in savage tropical grasslands, spawning in groups of 1-5 individuals, and are not too aggressive, but may pick fights with dwarves who get too close. Much like their animal cousins, cheetah men are fast, running at 40 km/h, making them one of the fastest animal people on land. They are exactly the same size as dwarves.

Like other savage animal people, they can join civilizations, become historical figures, appear as visitors and be playable in adventurer mode.

Some dwarves like cheetah men for their *speed*.

An enemy you'll *never* outrun.\
*Art by Titus Weiss (TitusW)*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Cheetah men were originally going to be explicitly excluded from the game due to the fear of resurrecting ancient glitches. Unfortunately, the elves insisted that all animals deserve their due representation, and secretly let them in. Today, it is speculated that this was the root cause of all glitches to ever be encountered within the game's worlds. Sweet Armok, we tried to stop it. But now, it is too late.

Additionally, Cheetah Men have no relation to any edible puffed cornmeal cheese products.

    [CREATURE:CHEETAH_MAN]
        [COPY_TAGS_FROM:CHEETAH]
        [APPLY_CREATURE_VARIATION:ANIMAL_PERSON]
        [GO_TO_END]
        [SELECT_CASTE:MALE]
            [CASTE_NAME:cheetah man:cheetah men:cheetah man]
        [SELECT_CASTE:FEMALE]
            [CASTE_NAME:cheetah woman:cheetah women:cheetah woman]
        [SELECT_CASTE:ALL]
        [APPLY_CREATURE_VARIATION:PUNCH_ATTACK]
        [APPLY_CREATURE_VARIATION:KICK_ATTACK]
        [APPLY_CREATURE_VARIATION:CLAW_SCRATCH_ATTACK]
        [APPLY_CREATURE_VARIATION:TOOTH_BITE_ATTACK]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [GO_TO_START]
        [NAME:cheetah man:cheetah men:cheetah man]
        [DESCRIPTION:A spotted person with the head and tail of a cheetah.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:5]
        [MAXAGE:60:80]
        [CREATURE_TILE:'c']
        [COLOR:6:0:1]
        [GO_TO_TAG:USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
