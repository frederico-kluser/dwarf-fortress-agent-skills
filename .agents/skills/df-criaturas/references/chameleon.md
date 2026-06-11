# Chameleon

> Fonte: [Chameleon](https://dwarffortresswiki.org/index.php/Chameleon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes chameleons for their eyes.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland Tropical Savanna Any Desert**
- **Variations**
- **Chameleon - Chameleon man - Giant chameleon**
- **Attributes**
- **Exotic pet**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A colorful lizard that spends its life hunting insects with its long tongue. It moves slowly through the trees, spying the surroundings with its independently roving eyes.*

**Chameleons** are a species of above ground vermin found in a variety of biomes, from deserts to tropical forests.

They are notably the greatest egg-layers of all vermin, laying 40 to 50 eggs at a time. However, due to being vermin, these eggs can't be gathered through egg production. Fortunately, they can potentially be requested when trading with other races such as humans if they happen to settle in a region with chameleons in it, and their giant chameleon counterparts lay just as many eggs which can be freely used by your dwarves.

Curiously, chameleons in *Dwarf Fortress* have a body striped with all the colors of the rainbow, as their ability to change color has not been implemented yet.

Some dwarves like chameleons for their *ability to change color* and their *eyes*.

Admired for its *eyes*.

    12 kph

    [CREATURE:CHAMELEON]
        [DESCRIPTION:A colorful lizard that spends its life hunting insects with its long tongue.  It moves slowly through the trees, spying the surroundings with its independently roving eyes.]
        [NAME:chameleon:chameleons:chameleon]
        [CASTE_NAME:chameleon:chameleons:chameleon]
        [CREATURE_TILE:249][COLOR:2:0:1]
        [PETVALUE:10]
        [VERMIN_GROUNDER][FREQUENCY:100]
        [SMALL_REMAINS]
        [NATURAL][PET_EXOTIC]
        [NOT_BUTCHERABLE]
        [CARNIVORE]
        [BIOME:ANY_TROPICAL_FOREST]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:ANY_DESERT]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:ability to change color]
        [PREFSTRING:eyes]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        toes mostly fused into two pads
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:150]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:5:10]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [NOCTURNAL]
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:10]
                [CLUTCH_SIZE:40:50]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:STRIPES_RAINBOW:1] needs to do color changes
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
