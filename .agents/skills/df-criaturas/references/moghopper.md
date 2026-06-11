# Moghopper

> Fonte: [Moghopper](https://dwarffortresswiki.org/index.php/Moghopper) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes moghoppers for their round tummies.**
- **Biome**
- **Any Pool**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Exotic pet · Extract · Fishable**
- **Pet value:** 20
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small mud-dwelling amphibian.*

**Moghoppers** are a species of amphibious vermin found in any savage area near pools during summer, and can be fished and cleaned for food. Moghoppers are, notably, the only creatures in the game usable in fish dissecting; they can be captured alive and have mog juice extracted from them, which can be used as a cooking ingredient.

Some dwarves like moghoppers for their *round tummies*.

    [CREATURE:MOGHOPPER]
        [DESCRIPTION:A small mud-dwelling amphibian.]
        [NAME:moghopper:moghoppers:moghopper]
        [CASTE_NAME:moghopper:moghoppers:moghopper]
        [CREATURE_TILE:249][COLOR:6:0:0]
        [PETVALUE:20]
        [VERMIN_GROUNDER][FISHITEM][FREQUENCY:10]
        [AMPHIBIOUS][SMALL_REMAINS][NO_SPRING][NO_AUTUMN][NO_WINTER][SAVAGE]
        [NATURAL][PET_EXOTIC]
        [NOT_BUTCHERABLE]
        [BIOME:ANY_POOL]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:round tummies]
        [BODY:QUADRUPED_NECK:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:MOG_JUICE:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen mog juice]
            [STATE_ADJ:ALL_SOLID:frozen mog juice]
            [STATE_NAME:LIQUID:mog juice]
            [STATE_ADJ:LIQUID:mog juice]
            [STATE_NAME:GAS:boiling mog juice]
            [STATE_ADJ:GAS:boiling mog juice]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [EXTRACT:LOCAL_CREATURE_MAT:MOG_JUICE]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:300]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [CREPUSCULAR]
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GREEN:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
