# Phantom spider

> Fonte: [Phantom spider](https://dwarffortresswiki.org/index.php/Phantom_spider) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes phantom spiders for their creepiness.**
- **Biome**
- **Any Temperate Forest Any Tropical Forest**
- **Attributes**
- **Alignment:** Evil
- **Exotic pet · Extract · Syndrome · Webs**
- **Pet value:** 0
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny translucent creature, found in evil forests.*

**Phantom spiders** are vermin that occur in evil forest biomes. Closely related to cave spiders, they produce webs that can be collected and woven into thread at a loom, and bite creatures to inject a venom which causes numbness and dizziness for approximately one month. An animal dissector can use a caught phantom spider to make venom. Note that stripping an area of available trees reduces the amount of webbing present, due to dwarves trampling it.

True to the creature's description, the sprite of the spider is partially transparent.

Some dwarves like phantom spiders for their *translucence* and their *creepiness*.

Ghostly spider. Not-so-ghostly venom.

|  |
|----|
| "Phantom spider" in other / Languages / Dwarven / : / zimesh sethal / Elven / : / vilela thepani / Goblin / : / kung utes / Human / : / warosp azoc |

    [CREATURE:SPIDER_PHANTOM]
        [DESCRIPTION:A tiny translucent creature, found in evil forests.]
        [NAME:phantom spider:phantom spiders:phantom spider]
        [CASTE_NAME:phantom spider:phantom spiders:phantom spider]
        [CREATURE_TILE:249][COLOR:7:0:1]
        [CREATURE_CLASS:POISONOUS]
        [CARNIVORE]
        [PET_EXOTIC][EVIL]
        [PARALYZEIMMUNE]
        [WEBIMMUNE]
        [NATURAL]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:ANY_TROPICAL_FOREST]
        [VERMIN_GROUNDER]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [PREFSTRING:translucence]
        [PREFSTRING:creepiness]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [HOMEOTHERM:10071]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [NOT_BUTCHERABLE]
        [NOPAIN][EXTRAVISION][NOSTUN][NOFEAR]
        [NOBONES]
        [BODY:SPIDER:2EYES:HEART:GUTS:BRAIN:MOUTH]
        [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
        [BODY_DETAIL_PLAN:CHITIN_TISSUES]
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen phantom spider venom]
            [STATE_ADJ:ALL_SOLID:frozen phantom spider venom]
            [STATE_NAME:LIQUID:phantom spider venom]
            [STATE_ADJ:LIQUID:phantom spider venom]
            [STATE_NAME:GAS:boiling phantom spider venom]
            [STATE_ADJ:GAS:boiling phantom spider venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:phantom spider bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:SPIDER_PHANTOM:ALL]
                [SYN_INJECTED]
                [CE_NUMBNESS:SEV:100:PROB:100:START:5:PEAK:10:END:33600]
                [CE_DIZZINESS:SEV:25:PROB:100:START:5:PEAK:10:END:33600]
        [USE_MATERIAL_TEMPLATE:SILK:SILK_TEMPLATE]
        [EXTRACT:LOCAL_CREATURE_MAT:VENOM]
        [VERMIN_BITE:10:bitten:LOCAL_CREATURE_MAT:VENOM:LIQUID]
        [WEBBER:LOCAL_CREATURE_MAT:SILK]
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
        [BODY_SIZE:0:0:500]
        [MAXAGE:1:1]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:exterior:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
