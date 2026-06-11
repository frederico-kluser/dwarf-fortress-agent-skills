# Bumblebee

> Fonte: [Bumblebee](https://dwarffortresswiki.org/index.php/Bumblebee) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bumblebees for their woolly appearance.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Attributes**
- **Extract · Flying · Syndrome**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small woolly insect that lives in hive colonies. It has an annoying sting which it rarely uses.*

**Bumblebees** are a type of vermin found in any area that isn't freezing. They can sting a nearby dwarf without killing it, causing slight pain but no negative thought for the dwarf. They are not killed by cats.

Bumblebees spawn from "colonies" (  ), and are one of several creatures to do so (the only other notable one being the honey bee). However, unlike the former, bumblebees can't be used for beekeeping, this being an intentional decision by Toady One. Bumblebee mead appears in the food stockpile along with standard honeybee mead, though it is not possible to brew it.

Some dwarves like bumblebees for their *woolly appearance*.

Admired for its *woolly appearance*.

## In real life

Nectar collected by bumblebees was traditionally collected by children in Scandinavian countries and termed "bumblebee honey" or "bumblebee mead"; it was used both as a food and for medicinal purposes. However, because they form annual rather than perennial colonies, they do not store the large amounts of honey that honey bees do.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Some bumblebees have been seen traveling with a giant red and blue robot, and often transform into muscle cars.

## Bugs

- Bumblebee honey/mead/jelly may be preferred by some dwarves since it exists in the raws, but it isn't obtainable. Work-arounds exist in modding bumblebees to have the [`[ARTIFICIAL_HIVEABLE]`](/index.php/Creature_token#ARTIFICIAL_HIVEABLE "Creature token") tag, making them usable for beekeeping, or by removing their beekeeping-related materials so that they don't exist to begin with. Bug:4735

    [CREATURE:BUMBLEBEE]
        [DESCRIPTION:A small woolly insect that lives in hive colonies.  It has an annoying sting which it rarely uses.]
        [NAME:bumblebee:bumblebees:bumblebee]
        [CREATURE_TILE:250][COLOR:6:0:1]
        [NATURAL]
        [BIOME:NOT_FREEZING]
        [VERMIN_SOIL_COLONY][FREQUENCY:100]
        [VERMIN_NOTRAP]
        [POPULATION_NUMBER:250:500]
        [CLUSTER_NUMBER:100:200]
        [SMALL_REMAINS]
        [PREFSTRING:woolly appearance]
        [DIURNAL]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:2206:1692:1178:585:3400:4900] 15 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [USE_MATERIAL_TEMPLATE:WAX:WAX_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:bumblebee wax]
            [STATE_NAME_ADJ:SOLID_PRESSED:bumblebee wax cake]
            [STATE_NAME_ADJ:LIQUID:melted bumblebee wax]
            [STATE_NAME_ADJ:GAS:boiling bumblebee wax]
            [STATE_COLOR:ALL:YELLOW]
            [DISPLAY_COLOR:6:0:1]
            [PREFIX:NONE]
            [MATERIAL_REACTION_PRODUCT:HONEYCOMB_PRESS_MAT:LOCAL_CREATURE_MAT:HONEY]
        [USE_MATERIAL_TEMPLATE:ROYAL_JELLY:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen bumblebee royal jelly]
            [STATE_NAME_ADJ:LIQUID:bumblebee royal jelly]
            [STATE_NAME_ADJ:GAS:boiling bumblebee royal jelly]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
            [PREFIX:NONE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [EDIBLE_RAW]
        [USE_MATERIAL_TEMPLATE:HONEY:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen bumblebee honey]
            [STATE_NAME_ADJ:LIQUID:bumblebee honey]
            [STATE_NAME_ADJ:GAS:boiling bumblebee honey]
            [STATE_COLOR:ALL:AMBER]
            [DISPLAY_COLOR:6:0:0]
            [PREFIX:NONE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [EDIBLE_RAW]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_CREATURE_MAT:MEAD]
        [USE_MATERIAL_TEMPLATE:MEAD:CREATURE_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen bumblebee mead]
            [STATE_NAME_ADJ:LIQUID:bumblebee mead]
            [STATE_NAME_ADJ:GAS:boiling bumblebee mead]
            [MATERIAL_VALUE:2]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen bumblebee venom]
            [STATE_ADJ:ALL_SOLID:frozen bumblebee venom]
            [STATE_NAME:LIQUID:bumblebee venom]
            [STATE_ADJ:LIQUID:bumblebee venom]
            [STATE_NAME:GAS:boiling bumblebee venom]
            [STATE_ADJ:GAS:boiling bumblebee venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:bumblebee sting]
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
        [HIVE_PRODUCT:1:201600:TOOL:ITEM_TOOL_HONEYCOMB:LOCAL_CREATURE_MAT:WAX]
        [HIVE_PRODUCT:1:201600:LIQUID_MISC:NONE:LOCAL_CREATURE_MAT:ROYAL_JELLY]
        [CASTE:WORKER]
            [CASTE_NAME:bumblebee worker:bumblebee workers:bumblebee worker]
            [POP_RATIO:10000]
            [COLONY_EXTERNAL]
            [EXTRACT:LOCAL_CREATURE_MAT:VENOM]
            [VERMIN_BITE:10:stung:LOCAL_CREATURE_MAT:VENOM:LIQUID]
        [CASTE:DRONE]
            [MALE]
            [CASTE_NAME:bumblebee drone:bumblebee drones:bumblebee drone]
            [POP_RATIO:5]
        [CASTE:QUEEN]
            [FEMALE]
            [CASTE_NAME:bumblebee queen:bumblebee queens:bumblebee queen]
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
