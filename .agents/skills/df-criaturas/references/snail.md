# Snail

> Fonte: [Snail](https://dwarffortresswiki.org/index.php/Snail) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes snails for their shells.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Snail - Snail man - Giant snail**
- **Attributes**
- **Hateable · Pet · Shell**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny land mollusk with a large shell.*

**Snails** are a species of hateable vermin who may be found in any non-freezing biome. They will cause unhappy thoughts on dwarves who absolutely detest them should they encounter one. They possess a pet value of 10, but may not be caught in animal traps.

Some dwarves like snails for their *shells*.

|  |
|----|
| "Snail" in other / Languages / Dwarven / : / nasod / Elven / : / limi / Goblin / : / snuslû / Human / : / copgur |

Admired for their *shells*.

    1 kph

    Snails were sponsored by the generous contributions of the Bay 12 community.

        Liegrean

    [CREATURE:SNAIL]
        [DESCRIPTION:A tiny land mollusk with a large shell.]
        [NAME:snail:snails:snail]
        [CASTE_NAME:snail:snails:snail]
        [CREATURE_TILE:249][COLOR:7:0:0]
        [PETVALUE:10]
        [VERMIN_SOIL][FREQUENCY:100][VERMIN_HATEABLE]
        [SMALL_REMAINS][VERMIN_NOTRAP][NOBONES]
        [BENIGN][NATURAL][PET]
        [NOT_BUTCHERABLE]
        [BIOME:NOT_FREEZING]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:shells]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:HEART:GUTS:BRAIN:MOUTH:SHELL:2EYESTALKS]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
            [USE_MATERIAL_TEMPLATE:SHELL:SHELL_TEMPLATE]
                [STATE_COLOR:ALL:BROWN]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
            [USE_TISSUE_TEMPLATE:SHELL:SHELL_TEMPLATE]
        [BODY_DETAIL_PLAN:MOLLUSC_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [HAS_NERVES]
        [MUNDANE]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:1]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:20:35]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [CANNOT_JUMP]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SHELL]
            [TL_COLOR_MODIFIER:BROWN:1]
                [TLCM_NOUN:shell:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:GRAY:1]
                [TLCM_NOUN:skin:SINGULAR]
