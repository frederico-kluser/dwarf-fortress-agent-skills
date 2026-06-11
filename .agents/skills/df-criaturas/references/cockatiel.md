# Cockatiel

> Fonte: [Cockatiel](https://dwarffortresswiki.org/index.php/Cockatiel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cockatiels for their crests.**
- **Biome**
- **Any Desert Temperate Grassland**
- **Variations**
- **Cockatiel - Cockatiel man - Giant cockatiel**
- **Attributes**
- **Flying · Pet**
- **Pet value:** 30
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny crested parrot. They are prized as domestic companions.*

**Cockatiels** are a species of above ground vermin who inhabit deserts and temperate grasslands. They may be captured in animal traps and turned into pets. All cockatiels possess Legendary skill in climbing.

Some dwarves like cockatiels for their *crests*.

Admired for their *crests*.

    1 kph

    Cockatiels were sponsored by the generous contributions of the Bay 12 community.

        To Beth, from Andy

    [CREATURE:BIRD_COCKATIEL]
        [DESCRIPTION:A tiny crested parrot.  They are prized as domestic companions.]
        [NAME:cockatiel:cockatiels:cockatiel]
        [CASTE_NAME:cockatiel:cockatiels:cockatiel]
        [GENERAL_CHILD_NAME:cockatiel hatchling:cockatiel hatchlings]
        [CREATURE_TILE:249][COLOR:7:0:1]
        [PETVALUE:30][NATURAL][PET]
        [BIOME:ANY_DESERT]
        [BIOME:GRASSLAND_TEMPERATE]
        [VERMIN_GROUNDER][FREQUENCY:100]
        [POPULATION_NUMBER:250:500]
        [SMALL_REMAINS]
        [BENIGN][FLIER]
        [CHILD:1]
        [DIURNAL]
        [HOMEOTHERM:10071]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [PREFSTRING:crests]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS:FEATHER]
        [USE_MATERIAL_TEMPLATE:TALON:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:TALON:TALON_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:TALON:FRONT]
        [BODY_DETAIL_PLAN:EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:10]
        [BODY_SIZE:1:0:90]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:30]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:TALON]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:snatch at:snatches at]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:11]
                [CLUTCH_SIZE:2:8]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:WHITE:1] yellow head
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
