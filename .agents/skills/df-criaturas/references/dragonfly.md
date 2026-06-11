# Dragonfly

> Fonte: [Dragonfly](https://dwarffortresswiki.org/index.php/Dragonfly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes dragonflies for their faceted eyes.**
- **Biome**
- **Any Pool**
- **Variations**
- **Dragonfly - Dragonfly man - Giant dragonfly**
- **Attributes**
- **Flying**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A relatively large insect found in swamps and marshland.*

**Dragonflies** are a type of above ground vermin found near pools, and can be seen in any season other than winter. They may not be caught in built animal traps. All dragonflies possess Legendary skill in climbing. In real life they have four wings, but in RAW has only two wings.

Some dwarves like dragonflies for their *faceted eyes*.

|  |
|----|
| "Dragonfly" in other / Languages / Dwarven / : / måmgoz-fenglel / Elven / : / vutheni-yetine / Goblin / : / kusnath-atu / Human / : / tamun-ngáthi |

Admired for its *faceted eyes*.

    1 kph

    [CREATURE:DRAGONFLY]
        [DESCRIPTION:A relatively large insect found in swamps and marshland.]
        [NAME:dragonfly:dragonflies:dragonfly]
        [CASTE_NAME:dragonfly:dragonflies:dragonfly]
        [CREATURE_TILE:249][COLOR:3:0:1]
        [NATURAL]
        [BIOME:ANY_POOL]
        [VERMIN_GROUNDER][FREQUENCY:100]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS][NO_WINTER]
        [PREFSTRING:faceted eyes]
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
                [TL_COLOR_MODIFIER:AQUAMARINE:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
