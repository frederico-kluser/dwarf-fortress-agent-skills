# Brown recluse spider

> Fonte: [Brown recluse spider](https://dwarffortresswiki.org/index.php/Brown_recluse_spider) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes brown recluse spiders for their venomous bite.**
- **Biome**
- **Temperate Broadleaf Forest**
- **Variations**
- **Brown recluse spider - Brown recluse spider man - Giant brown recluse spider**
- **Attributes**
- **Exotic pet · Extract · Hateable · Syndrome · Webs**
- **Pet value:** 0
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny brown bug known for its powerful poison.*

**Brown recluse spiders** are hateable vermin that, on top of giving unhappy thoughts to dwarves who detest them, are very venomous. Brown recluse spider bites cause immediate nausea, fever, and pain, and a short time later result in severe localized necrosis. They are also much faster than your average rat. Thankfully, the spiders don't seek the vicinity of dwarven settlements and even when a dwarf encounters a spider, this will almost never result in a bite.

Brown recluse spiders spin webs which can be collected by weavers for the production of silk. In their native biomes, brown recluse spider silk can be an important resource of the textile industry.

Some dwarves like brown recluse spiders for their *venomous bite*.

|  |
|----|
| "Brown recluse spider" in other / Languages / Dwarven / : / neb orstist sethal / Elven / : / bideÿe éniri thepani / Goblin / : / urso ästspub utes / Human / : / tasar zinga azoc |

Admired for its *venomous bite*.

    1 kph

    Brown recluse spiders were sponsored by the generous contributions of the Bay 12 community.

        Arthemax

    [CREATURE:SPIDER_BROWN_RECLUSE]
        [DESCRIPTION:A tiny brown bug known for its powerful poison.]
        [NAME:brown recluse spider:brown recluse spiders:brown recluse spider]
        [CASTE_NAME:brown recluse spider:brown recluse spiders:brown recluse spider]
        [CREATURE_TILE:249][COLOR:6:0:0]
        [CARNIVORE]
        [PET_EXOTIC]
        [WEBIMMUNE]
        [NATURAL]
        [BIOME:FOREST_TEMPERATE_BROADLEAF]
        [VERMIN_GROUNDER][VERMIN_HATEABLE]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [PREFSTRING:venomous bite]
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
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen brown recluse spider venom]
            [STATE_ADJ:ALL_SOLID:frozen brown recluse spider venom]
            [STATE_NAME:LIQUID:brown recluse spider venom]
            [STATE_ADJ:LIQUID:brown recluse spider venom]
            [STATE_NAME:GAS:boiling brown recluse spider venom]
            [STATE_ADJ:GAS:boiling brown recluse spider venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:brown recluse spider bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:SPIDER_BROWN_RECLUSE:ALL]
                [SYN_INJECTED]
                [CE_NECROSIS:SEV:100:PROB:37:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:100:PEAK:500:END:2400]
                [CE_NAUSEA:SEV:50:PROB:14:RESISTABLE:SIZE_DILUTES:START:50:PEAK:500:END:1500]
                [CE_FEVER:SEV:50:PROB:14:RESISTABLE:SIZE_DILUTES:START:50:PEAK:500:END:1500]
                [CE_PAIN:SEV:25:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:100:PEAK:500:END:2400]
        [USE_MATERIAL_TEMPLATE:SILK:SILK_TEMPLATE]
        [EXTRACT:LOCAL_CREATURE_MAT:VENOM]
        [VERMIN_BITE:1:bitten:LOCAL_CREATURE_MAT:VENOM:LIQUID]
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
        [BODY_SIZE:0:0:1]
        [MAXAGE:1:2]
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
