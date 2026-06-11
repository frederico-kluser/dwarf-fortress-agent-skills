# Louse

> Fonte: [Louse](https://dwarffortresswiki.org/index.php/Louse) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes lice for their ability to infest.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Louse - Louse man - Giant louse**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny parasitic insect. It feeds on skin and blood.*

**Lice** are a species of unremarkable above ground vermin who may be found in any non-freezing biome. They may not be caught in animal traps. A comment on their raw files states they should not survive without a host, implying Toady One plans them to be parasitic in a future update. All lice possess Legendary skill in climbing.

Some dwarves like lice for their *ability to infest*.

|  |
|----|
| "Louse" in other / Languages / Dwarven / : / sosmil / Elven / : / lenipe / Goblin / : / baru / Human / : / slupi |

Admired for its *ability to infest*.

    1 kph

    Lice were sponsored by the generous contributions of the Bay 12 community.

        Maldoror

    [CREATURE:LOUSE]
        Should not be able to survive away from host.
        [DESCRIPTION:A tiny parasitic insect.  It feeds on skin and blood.]
        [NAME:louse:lice:louse]
        [CASTE_NAME:louse:lice:louse]
        [CREATURE_TILE:250][COLOR:6:0:0]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_SOIL][FREQUENCY:100]
        [UBIQUITOUS]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [PREFSTRING:ability to infest]
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
        [BODY:INSECT:2EYES:HEART:GUTS:BRAIN:MOUTH]
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
                [TL_COLOR_MODIFIER:BEIGE:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
