# Worm

> Fonte: [Worm](https://dwarffortresswiki.org/index.php/Worm) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes worms for their wriggling.**
- **Biome**
- **Taiga Any Temperate Any Tropical**
- **Variations**
- **Worm - Worm man**
- **Attributes**
- **Hateable · Pet**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny burrowing creature, found in moist soil. It is legless, long and thin.*

**Worms** are a species of soil-dwelling vermin found in the soil of taiga, temperate, and tropical areas, that can be tamed as pets. While they are very common, the combination of the [`[VERMIN_SOIL]`](/index.php/Creature_token#VERMIN_SOIL "Creature token") and [`[VERMIN_NOTRAP]`](/index.php/Creature_token#VERMIN_NOTRAP "Creature token") tokens prevents them from being trappable\[Verify\].

Some dwarves like worms for their *wriggling*, but others can "absolutely detest worms" getting unhappy thoughts when they encounter them.

Admired for its *wriggling*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Inquiring whether one would still be loved after transforming into a wereworm is a popular test of fidelity among dwarven couples.

|  |
|----|
| "Worm" in other / Languages / Dwarven / : / vesrul / Elven / : / nema / Goblin / : / osle / Human / : / slinpa |

    [CREATURE:WORM]
        [DESCRIPTION:A tiny burrowing creature, found in moist soil.  It is legless, long and thin.]
        [NAME:worm:worms:worm]
        [CASTE_NAME:worm:worms:worm]
        [CREATURE_TILE:'~'][COLOR:7:0:0]
        [PETVALUE:10]
        [VERMIN_SOIL][FREQUENCY:100][VERMIN_HATEABLE]
        [SMALL_REMAINS][VERMIN_NOTRAP][NOBONES]
        [NATURAL][PET]
        [NOT_BUTCHERABLE]
        [BIOME:FOREST_TAIGA]
        [BIOME:ANY_TEMPERATE]
        [BIOME:ANY_TROPICAL]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:wriggling]
        [BODY:BODY_WITH_HEAD_FLAG:HEART:GUTS:BRAIN:MOUTH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [HAS_NERVES]
        [MUNDANE]
        [GAIT:WALK:Crawl:2900:NO_BUILD_UP:0:LAYERS_SLOW:STRENGTH:AGILITY]
        [GAIT:CRAWL:Crawl:2900:NO_BUILD_UP:0:LAYERS_SLOW:STRENGTH:AGILITY]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:100]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
        [CANNOT_JUMP]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:GRAY:1]
                [TLCM_NOUN:skin:SINGULAR]
