# Fly

> Fonte: [Fly](https://dwarffortresswiki.org/index.php/Fly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes flies for their ability to annoy.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra Any Pool**
- **Variations**
- **Fly - Fly man - Giant fly**
- **Attributes**
- **Flying · Hateable**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny flying insect found around rotting meat and garbage. These bugs are widely considered to be a nuisance.*

**Flies** are a type of hateable above ground vermin found in swarms near pools, farms with unpicked rotting food and food stockpiles. Since cats cannot kill flies, the best way to protect against them is to make sure food is not left outside of a container too long. Also, make sure you have enough barrels and large pots to store your food and someone ready to pick food from farms once ready. If there's no food around outside of a container, the flies will go away.

Flies have the dubious distinction of being the only vermin that can cause two separate bad thoughts: "Annoyed by flies", which affects the general populace, and "Accosted by terrible vermin", which affects individual dwarves who have a particular antipathy toward flies. All flies possess Legendary skill in climbing.

Some dwarves, curiously, like flies for their *ability to annoy*.

|  |
|----|
| "Fly" in other / Languages / Dwarven / : / fenglel / Elven / : / yetine / Goblin / : / atu / Human / : / ngáthi |

Admired for its *ability to annoy*.

## Gallery

-

  Swarm of flies sprite.

    [CREATURE:FLY]
        [DESCRIPTION:A tiny flying insect found around rotting meat and garbage.  These bugs are widely considered to be a nuisance.]
        [NAME:fly:flies:fly]
        [CASTE_NAME:fly:flies:fly]
        [CREATURE_TILE:250][COLOR:0:0:1]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [BIOME:ANY_POOL]
        [VERMIN_MICRO][VERMIN_ROTTER][VERMIN_GROUNDER][FREQUENCY:100][VERMIN_HATEABLE]
        [UBIQUITOUS]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:2500:5000]
        [CLUSTER_NUMBER:100:200]
        [SMALL_REMAINS]
        [PREFSTRING:ability to annoy]
        [FLIER]
        [DIURNAL]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [NOBONES]
        [BODY:INSECT:2EYES:HEART:GUTS:BRAIN:MOUTH:2WINGS]
        [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
        [BODY_DETAIL_PLAN:CHITIN_TISSUES]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:1]
        [MAXAGE:1:1]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
