# Cuttlefish

> Fonte: [Cuttlefish](https://dwarffortresswiki.org/index.php/Cuttlefish) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cuttlefish for their ability to change color.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Cuttlefish - Cuttlefish man - Giant cuttlefish**
- **Attributes**
- **Aquatic · Fishable**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny sea mollusk. It can change color and skin patterns for communication.*

**Cuttlefish** are a type of aquatic vermin found in any ocean year-round, and are a ready source of food when cleaned at a fishery. Their blood is blue and they possess the ability to squirt ink, though this can't be seen, due to them being vermin. All cuttlefish possess Legendary skill in climbing.

Some dwarves like cuttlefish for their *ability to change color* and their *distinctive pupils*.

\

Admired for its *distinctive pupils*.

    24 kph

    Cuttlefish were sponsored by the generous contributions of the Bay 12 community.

        From Timofei to the cuddly denizens of xkcdsucks
        Duncan Pettengill - "If you push something hard enough, it will fall over"

    [CREATURE:CUTTLEFISH]
        [DESCRIPTION:A tiny sea mollusk.  It can change color and skin patterns for communication.]
        [NAME:cuttlefish:cuttlefish:cuttlefish]
        [CASTE_NAME:cuttlefish:cuttlefish:cuttlefish]
        [CREATURE_TILE:11][COLOR:6:0:0]
        [PETVALUE:10]
        [VERMIN_FISH]
        [FREQUENCY:100]
        [AQUATIC][SMALL_REMAINS][FISHITEM][NOBONES][IMMOBILE_LAND][UNDERSWIM][COOKABLE_LIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:ANY_OCEAN]
        [NO_DRINK]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:ability to change color]
        [PREFSTRING:distinctive pupils]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:2EYES:BEAK:2_HEAD_CLUBBED_TENTACLES:8_SIMPLE_HEAD_ARMS]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
            [REMOVE_MATERIAL:CARTILAGE]
            [USE_MATERIAL_TEMPLATE:CHITIN:CHITIN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
            [REMOVE_TISSUE:CARTILAGE]
            [USE_TISSUE_TEMPLATE:CHITIN:CHITIN_TEMPLATE]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:CHITIN:CHITIN]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
            [STATE_COLOR:ALL:BLUE] copper not iron based
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [USE_MATERIAL_TEMPLATE:INK:INK_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen cuttlefish ink]
            [STATE_ADJ:ALL_SOLID:frozen cuttlefish ink]
            [STATE_NAME:LIQUID:cuttlefish ink]
            [STATE_ADJ:LIQUID:cuttlefish ink]
            [STATE_NAME:GAS:boiling cuttlefish ink]
            [STATE_ADJ:GAS:boiling cuttlefish ink]
            [PREFIX:NONE]
            [STATE_COLOR:ALL:SEPIA]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:1000]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION_WITH_HIDE_EFFECT]
            [CDI:TOKEN:SQUIRT_INK]
            [CDI:ADV_NAME:Squirt ink]
            [CDI:USAGE_HINT:FLEEING]
            [CDI:LOCATION_HINT:IN_WATER]
            [CDI:BP_REQUIRED:BY_TYPE:UPPERBODY]
            [CDI:MATERIAL:LOCAL_CREATURE_MAT:INK:SPATTER_LIQUID]
            [CDI:VERB:squirt ink:squirts ink:NA]
            [CDI:TARGET:C:SELF_ONLY]
            [CDI:TARGET:D:SELF_ONLY]
            [CDI:WAIT_PERIOD:200]
            [CDI:FREE_ACTION]
        [MAXAGE:1:2]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:BROWN:1] or pretty much anything
                [TLCM_NOUN:skin:SINGULAR]
