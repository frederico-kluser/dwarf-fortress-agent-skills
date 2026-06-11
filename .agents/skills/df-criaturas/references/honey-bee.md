# Honey bee

> Fonte: [Honey bee](https://dwarffortresswiki.org/index.php/Honey_bee) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes honey bees for their ability to organize.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Attributes**
- **Extract · Flying · Hiveable · Syndrome**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small flying insect that lives in large colonies. It has a powerful stinger on its tail. Its hives are prized for their honey.*

**Honey bees** are a type of vermin found in any area that isn't freezing, and can spawn after embark, even if not originally present. They appear in naturally made hives (  ). Their wild colonies can be transferred into artificial hives and used in the beekeeping industry producing royal jelly, honey and wax as end products. They can sting a nearby dwarf or animal, resulting in the death of the bee, and causing slight pain but no negative thought for the dwarf. This sometimes results in the Recover Wounded task, which may actually give a good thought to the stung dwarf.

There are often tens of thousands inside mature hives. They are not killed by cats, but they can fill up your refuse stockpile if dwarves are regularly stung by them.

Some dwarves like honey bees for their *busy nature*, their *buzzing*, and their *ability to organize*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Despite common belief, bees do not like jazz.

|  |
|----|
| "Honey bee" in other / Languages / Dwarven / : / stetár agêk / Elven / : / arifè aveÿa / Goblin / : / stoz zaxo / Human / : / someg uzu |

Admired for its *busy nature*.

    1 kph

    Bees were sponsored by the generous contributions of the Bay 12 community.

        Alex Fink
        CharlesPeter donated for future honey and bee-based traps.
        Lord Herman - "Urist McBeekeeper cancels Gather Honey: Covered in Bees"
        Mazonas
        John McNeil

    [CREATURE:HONEY_BEE]
        [DESCRIPTION:A small flying insect that lives in large colonies.  It has a powerful stinger on its tail.  Its hives are prized for their honey.]
        [NAME:honey bee:honey bees:honey bee]
        [CREATURE_TILE:250][COLOR:6:0:1]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_SOIL_COLONY][FREQUENCY:100]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [CLUSTER_NUMBER:100:200]
        [SMALL_REMAINS]
        [PETVALUE:1]
        [PETVALUE_DIVISOR:1000]
        [PREFSTRING:busy nature]
        [PREFSTRING:buzzing]
        [PREFSTRING:ability to organize]
        [DIURNAL]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [NO_SLEEP]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [USE_MATERIAL_TEMPLATE:WAX:WAX_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:honey bee wax]
            [STATE_NAME_ADJ:SOLID_PRESSED:honey bee wax cake]
            [STATE_NAME_ADJ:LIQUID:melted honey bee wax]
            [STATE_NAME_ADJ:GAS:boiling honey bee wax]
            [STATE_COLOR:ALL:YELLOW]
            [DISPLAY_COLOR:6:0:1]
            [PREFIX:NONE]
            [MATERIAL_REACTION_PRODUCT:HONEYCOMB_PRESS_MAT:LOCAL_CREATURE_MAT:HONEY]
            [STOCKPILE_GLOB_PRESSED]
        [USE_MATERIAL_TEMPLATE:ROYAL_JELLY:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen honey bee royal jelly]
            [STATE_NAME_ADJ:LIQUID:honey bee royal jelly]
            [STATE_NAME_ADJ:GAS:boiling honey bee royal jelly]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
            [PREFIX:NONE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [EDIBLE_RAW]
        [USE_MATERIAL_TEMPLATE:HONEY:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen honey bee honey]
            [STATE_NAME_ADJ:LIQUID:honey bee honey]
            [STATE_NAME_ADJ:GAS:boiling honey bee honey]
            [STATE_COLOR:ALL:AMBER]
            [DISPLAY_COLOR:6:0:0]
            [PREFIX:NONE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [EDIBLE_RAW]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_CREATURE_MAT:MEAD]
        [USE_MATERIAL_TEMPLATE:MEAD:CREATURE_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen mead]
            [STATE_NAME_ADJ:LIQUID:mead]
            [STATE_NAME_ADJ:GAS:boiling mead]
            [MATERIAL_VALUE:2]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen honey bee venom]
            [STATE_ADJ:ALL_SOLID:frozen honey bee venom]
            [STATE_NAME:LIQUID:honey bee venom]
            [STATE_ADJ:LIQUID:honey bee venom]
            [STATE_NAME:GAS:boiling honey bee venom]
            [STATE_ADJ:GAS:boiling honey bee venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:honey bee sting]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_INJECTED]
                [CE_PAIN:SEV:50:PROB:100:RESISTABLE:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
                [CE_SWELLING:SEV:75:PROB:100:RESISTABLE:LOCALIZED:VASCULAR_ONLY:START:50:PEAK:500:END:1500]
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
        [NOBONES]
        [ARTIFICIAL_HIVEABLE]
        [HIVE_PRODUCT:1:201600:TOOL:ITEM_TOOL_HONEYCOMB:LOCAL_CREATURE_MAT:WAX]
        [HIVE_PRODUCT:1:201600:LIQUID_MISC:NONE:LOCAL_CREATURE_MAT:ROYAL_JELLY]
        [CASTE:WORKER]
            [CASTE_NAME:honey bee worker:honey bee workers:honey bee worker]
            [POP_RATIO:10000]
            [COLONY_EXTERNAL]
            [EXTRACT:LOCAL_CREATURE_MAT:VENOM]
            [VERMIN_BITE:50:stung:LOCAL_CREATURE_MAT:VENOM:LIQUID]
            [DIE_WHEN_VERMIN_BITE]
            [REMAINS_ON_VERMIN_BITE_DEATH]
        [CASTE:DRONE]
            [MALE]
            [CASTE_NAME:honey bee drone:honey bee drones:honey bee drone]
            [POP_RATIO:5]
        [CASTE:QUEEN]
            [FEMALE]
            [CASTE_NAME:honey bee queen:honey bee queens:honey bee queen]
            [POP_RATIO:1]
        [SELECT_CASTE:ALL]
            [BODY:INSECT:2EYES:HEART:GUTS:BRAIN:MOUTH:2WINGS]
            [BODYGLOSS:INSECT_UPPERBODY:INSECT_LOWERBODY]
            [FLIER]
            [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
            [BODY_DETAIL_PLAN:CHITIN_TISSUES]
            [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
            [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:YELLOW:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
