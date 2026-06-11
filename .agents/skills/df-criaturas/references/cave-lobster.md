# Cave lobster

> Fonte: [Cave lobster](https://dwarffortresswiki.org/index.php/Cave_lobster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cave lobsters for their beauty.**
- **Biome**
- **Underground Depth: 1-2**
- **Attributes**
- **Aquatic**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, pale arthropod found in underground streams and ponds.*

**Cave lobsters** are a type of aquatic vermin found only in underground bodies of water. Cave lobsters cannot be caught by fishing, but instead must be caught in baited animal traps. Once caught, processing it will yield an edible cave lobster and a shell that can be used to craft or decorate items.

Some dwarves like cave lobsters for their *beauty*.

|  |
|----|
| "Cave lobster" in other / Languages / Dwarven / : / äs zedot / Elven / : / garetho ruÿava / Goblin / : / omo ospun / Human / : / ngethac duslud |

Admired for its *beauty*.

    [CREATURE:LOBSTER_CAVE]
        [DESCRIPTION:A small, pale arthropod found in underground streams and ponds.]
        [NAME:cave lobster:cave lobsters:cave lobster]
        [CASTE_NAME:cave lobster:cave lobsters:cave lobster]
        [CREATURE_TILE:157][COLOR:7:0:1]
        [VERMIN_FISH][FISHITEM][VERMIN_NOFISH]
        [AQUATIC][SMALL_REMAINS][UNDERSWIM]
        [NATURAL]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:2]
        [POPULATION_NUMBER:250:500]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [NATURAL_SKILL:CLIMBING:15]
        [PREFSTRING:beauty]
        [ALL_ACTIVE]
        [NO_DRINK][NO_SLEEP]
        [NOT_BUTCHERABLE][COOKABLE_LIVE]
        [NOPAIN][EXTRAVISION][NOSTUN][NOFEAR]
        [NOBONES]
        [CANNOT_JUMP]
        [BODY:SPIDER:SHELL:2EYES:HEART:GUTS:BRAIN:MOUTH:TAIL:UPPERBODY_PINCERS]
        [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
        [BODY_DETAIL_PLAN:CHITIN_TISSUES]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [SELECT_MATERIAL:CHITIN]
            [STATE_COLOR:ALL:WHITE]
            [SHELL]
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
        [BODY_SIZE:0:0:600]
        [MAXAGE:1:1]
        [HOMEOTHERM:10040]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
