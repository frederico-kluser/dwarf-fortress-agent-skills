# Jumping spider

> Fonte: [Jumping spider](https://dwarffortresswiki.org/index.php/Jumping_spider) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes jumping spiders for their striking appearance.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Jumping spider - Jumping spider man - Giant jumping spider**
- **Attributes**
- **Exotic pet · Hateable**
- **Pet value:** 0
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny black bug that lacks a web but can leap short distances.*

**Jumping spiders** are a species of above ground vermin who may be found in any non-freezing biome. Unlike most types of spider, they are neither venomous, nor do they produce any webs (they'll even get caught in the webs of other spiders). Jumping spiders are hateable vermin, and as such will cause unhappy thoughts on dwarves who hold a particular antipathy towards them.

Jumping spiders may be captured by trappers and turned into pets, but have no pet value at all (essentially giving them a value of zero).

Some dwarves like jumping spiders for their *striking appearance* and their *ability to leap*.

|  |
|----|
| "Jumping spider" in other / Languages / Dwarven / : / mâtzang sethal / Elven / : / efami thepani / Goblin / : / stoxus utes / Human / : / itni azoc |

Admired for its *ability to leap*.

    1 kph

    Jumping spiders were sponsored by the generous contributions of the Bay 12 community.

        John 'Chaoseed' Evans

    [CREATURE:SPIDER_JUMPING]
        [DESCRIPTION:A tiny black bug that lacks a web but can leap short distances.]
        [NAME:jumping spider:jumping spiders:jumping spider]
        [CASTE_NAME:jumping spider:jumping spiders:jumping spider]
        [CREATURE_TILE:250][COLOR:0:0:1]
        [CARNIVORE]
        [PET_EXOTIC]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_GROUNDER][VERMIN_HATEABLE]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [PREFSTRING:striking appearance]
        [PREFSTRING:ability to leap]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [NOPAIN][EXTRAVISION][NOSTUN][NOFEAR]
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
        [MAXAGE:2:3]
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
