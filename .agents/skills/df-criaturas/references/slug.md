# Slug

> Fonte: [Slug](https://dwarffortresswiki.org/index.php/Slug) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes slugs for their slime trails.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Slug - Slug man - Giant slug**
- **Attributes**
- **Hateable · Pet**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny land mollusk. It can be found under rotten logs and in gardens.*

**Slugs** are a species of hateable vermin who may be found in any non-freezing biome. They will cause unhappy thoughts on dwarves who absolutely detest them should they encounter one. They possess a pet value of 10, but may not be caught in animal traps.

Some dwarves like slugs for their *slime trails*.

|  |
|----|
| "Slug" in other / Languages / Dwarven / : / tozör / Elven / : / ralu / Goblin / : / omu / Human / : / dush |

Admired for its *slime trails*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
The average slug weighs 0.00006 slugs.

    1 kph

    Slugs were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:SLUG]
        [DESCRIPTION:A tiny land mollusk.  It can be found under rotten logs and in gardens.]
        [NAME:slug:slugs:slug]
        [CASTE_NAME:slug:slugs:slug]
        [CREATURE_TILE:'~'][COLOR:6:0:0]
        [PETVALUE:10]
        [VERMIN_SOIL][FREQUENCY:100][VERMIN_HATEABLE]
        [SMALL_REMAINS][VERMIN_NOTRAP][NOBONES]
        [NATURAL][PET]
        [BENIGN][NOT_BUTCHERABLE]
        [BIOME:NOT_FREEZING]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:slime trails]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:HEART:GUTS:BRAIN:MOUTH:2EYESTALKS]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:MOLLUSC_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [HAS_NERVES]
        [CANNOT_JUMP]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [MUNDANE]
        [BODY_SIZE:0:0:1]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:1:1]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:ECRU:1]
                [TLCM_NOUN:skin:SINGULAR]
