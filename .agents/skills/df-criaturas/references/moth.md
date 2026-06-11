# Moth

> Fonte: [Moth](https://dwarffortresswiki.org/index.php/Moth) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes moths for their coloration.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Moth - Moth man - Giant moth**
- **Attributes**
- **Flying**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny nocturnal insect. It flies toward flames in the night.*

**Moths** are a species of unremarkable above ground vermin who may be found in any non-freezing biome. They may be caught by trappers in animal traps, but will not stumble into baited ones. They do not appear during the winter.

Technically, moths possess Legendary skill in climbing, though only for moth men and giant moths to inherit - being vermin, moths themselves have no skills at all.

Some dwarves like moths for their *coloration*.

|  |
|----|
| "Moth" in other / Languages / Dwarven / : / alen / Elven / : / ìnevi / Goblin / : / atan / Human / : / dunem |

Admired for its *coloration*.

    1 kph

    Moths were sponsored by the generous contributions of the Bay 12 community.

        Rafael Fiol
        Shakkara thinks this game had a serious lack of cute moths

    [CREATURE:MOTH]
        [DESCRIPTION:A tiny nocturnal insect.  It flies toward flames in the night.]
        [CREATURE_TILE:249][COLOR:6:0:0]
        [NAME:moth:moths:moth]
        [CASTE_NAME:moth:moths:moth]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_GROUNDER][FREQUENCY:100]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS][NO_WINTER]
        [PREFSTRING:coloration]
        [BENIGN][FLIER]
        [NOCTURNAL]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
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
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
