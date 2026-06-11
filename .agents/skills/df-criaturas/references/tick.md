# Tick

> Fonte: [Tick](https://dwarffortresswiki.org/index.php/Tick) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ticks for their ability to expand.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Tick - Tick man - Giant tick**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For the time unit, see Time*

*A tiny, blood-sucking bug found in wooded areas.*

**Ticks** are a species of ubiquitous above-ground vermin, found in all non-freezing biomes. Their bite attack drains some blood out of the victim, though it is a negligible detail due to the difference in size between them and a dwarf. All ticks possess Legendary skill in climbing.

Some dwarves like ticks for their *ability to expand*.

Admired for its *ability to expand*.

|  |
|----|
| "Tick" in other / Languages / Dwarven / : / nobgost / Elven / : / pamène / Goblin / : / stâsost / Human / : / slushu |

    1 kph

    Ticks were sponsored by the generous contributions of the Bay 12 community.

        infection vector extraordinaire!

    [CREATURE:TICK]
        [DESCRIPTION:A tiny, blood-sucking bug found in wooded areas.]
        [NAME:tick:ticks:tick]
        [CASTE_NAME:tick:ticks:tick]
        [CREATURE_TILE:250][COLOR:0:0:1]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_SOIL][FREQUENCY:100]
        [UBIQUITOUS]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [PREFSTRING:ability to expand]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [CANNOT_JUMP]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [NOBONES]
        [BODY:SPIDER:2EYES:HEART:GUTS:BRAIN:MOUTH]
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
        [APPLY_CREATURE_VARIATION:MOUTH_SUCK_ATTACK]
        [MAXAGE:2:2]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:RED:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
