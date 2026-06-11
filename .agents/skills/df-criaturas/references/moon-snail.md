# Moon snail

> Fonte: [Moon snail](https://dwarffortresswiki.org/index.php/Moon_snail) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes moon snails for their predatory nature.**
- **Biome**
- **Temperate Ocean**
- **Variations**
- **Moon snail - Moon snail man - Giant moon snail**
- **Attributes**
- **Aquatic · Hateable · Shell**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny predatory mollusk. It is brightly colored.*

**Moon snails** are a species of hateable vermin found inhabiting temperate oceans. They will cause unhappy thoughts in dwarves who absolutely detest them should they encounter one. They possess a pet value of 10, and can not be caught in built animal traps, but can be caught with a "Capture a Live Land Animal" job, despite being aquatic. Beaches are ideal locations for catching moon snails.

Some dwarves like moon snails for their *predatory nature* and their *striking coloration*.

|  |
|----|
| "Moon snail" in other / Languages / Dwarven / : / ïlon nasod / Elven / : / anaye limi / Goblin / : / zusla snuslû / Human / : / oku copgur |

Admired for its *predatory nature*.

    Moon snails were sponsored by the generous contributions of the Bay 12 community.

        "In soviet russia, snail eats YOU with tiny fork!"

    [CREATURE:MOON_SNAIL]
        [DESCRIPTION:A tiny predatory mollusk.  It is brightly colored.]
        [NAME:moon snail:moon snails:moon snail]
        [CASTE_NAME:moon snail:moon snails:moon snail]
        [CREATURE_TILE:249][COLOR:4:0:1]
        [PETVALUE:10]
        [VERMIN_SOIL][FREQUENCY:100][VERMIN_HATEABLE]
        [AQUATIC][SMALL_REMAINS][VERMIN_NOTRAP][NOBONES]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [NATURAL]
        [NOT_BUTCHERABLE]
        [CANNOT_JUMP]
        [BIOME:OCEAN_TEMPERATE]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:predatory nature]
        [PREFSTRING:striking coloration]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:SHELL:HEART:GUTS:BRAIN:MOUTH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
            [USE_MATERIAL_TEMPLATE:SHELL:SHELL_TEMPLATE]
                [STATE_COLOR:ALL:RED]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
            [USE_TISSUE_TEMPLATE:SHELL:SHELL_TEMPLATE]
        [BODY_DETAIL_PLAN:MOLLUSC_TISSUE_LAYERS:SKIN:FAT:MUSCLE]
        [HAS_NERVES]
        [MUNDANE]
        [USE_MATERIAL_TEMPLATE:ICHOR:ICHOR_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:ICHOR:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:200]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [EXTRAVISION]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SHELL]
            [TL_COLOR_MODIFIER:RED:1]
                [TLCM_NOUN:shell:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:GRAY:1]
                [TLCM_NOUN:skin:SINGULAR]
