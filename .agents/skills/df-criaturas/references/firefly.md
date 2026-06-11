# Firefly

> Fonte: [Firefly](https://dwarffortresswiki.org/index.php/Firefly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes fireflies for their enchanting glow.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Firefly - Firefly man - Giant firefly**
- **Attributes**
- **Flying**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny flying insect that can be seen at night by its glowing tail.*

**Fireflies** are a type of above ground vermin found flying around in any area that is not freezing outside of winter, and may not be caught in built animal traps. In adventurer mode at night, they generate light. All fireflies possess Legendary skill in climbing. Fireflies have a unique graphical setup where there is one sprite for the firefly itself, and another for the light alone.

Some dwarves like fireflies for their *enchanting glow*.

|  |
|----|
| "Firefly" in other / Languages / Dwarven / : / ziril-fenglel / Elven / : / inira-yetine / Goblin / : / zedan-atu / Human / : / usmok-ngáthi |

Admired for its *enchanting glow*.

    1 kph

    [CREATURE:FIREFLY]
        [DESCRIPTION:A tiny flying insect that can be seen at night by its glowing tail.]
        [NAME:firefly:fireflies:firefly]
        [CASTE_NAME:firefly:fireflies:firefly]
        [CREATURE_TILE:249][COLOR:2:0:1]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_GROUNDER][FREQUENCY:100]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [CLUSTER_NUMBER:1:10]
        [SMALL_REMAINS][NO_WINTER]
        [PREFSTRING:enchanting glow]
        [FLIER]
        [VESPERTINE]
        [LIGHT_GEN]
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
