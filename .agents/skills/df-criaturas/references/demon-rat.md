# Demon rat

> Fonte: [Demon rat](https://dwarffortresswiki.org/index.php/Demon_rat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes demon rats for their diabolical hunger for the food of others.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Attributes**
- **Alignment:** Evil
- **Devours food · Exotic pet**
- **Pet value:** 20
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*An insidious form of vermin. It lives only to steal food from others.*

**Demon rats** are a species of above ground vermin, found in any evil areas that are not freezing. They can steal and eat food in stockpiles, even biting through containers to do so. They can be captured by trappers and turned into low-value pets. Despite their names, they have no relation to you-know-what.

A curious oddity concerning demon rats is their blood is a gray-colored goo.

Some dwarves like demon rats for their *insidious nature* and their *diabolical hunger for the food of others*.

Two types of vermin in one.\
*Art by Arne*

|  |
|----|
| "Demon rat" in other / Languages / Dwarven / : / uthgúr atem / Elven / : / slevina thapa / Goblin / : / arstruk spödgôz / Human / : / rohir othur |

    [CREATURE:RAT_DEMON]
        [DESCRIPTION:An insidious form of vermin.  It lives only to steal food from others.]
        [NAME:demon rat:demon rats:demon rat]
        [CASTE_NAME:demon rat:demon rats:demon rat]
        [CREATURE_TILE:249][COLOR:4:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:20][NATURAL]
        [VERMIN_EATER][PENETRATEPOWER:3][FREQUENCY:100][VERMIN_GROUNDER]
        [GNAWER:gnawed]
        [SMALL_REMAINS][EVIL][PET_EXOTIC]
        [NOT_BUTCHERABLE]
        [BIOME:NOT_FREEZING]
        [POPULATION_NUMBER:250:500]
        [TRIGGERABLE_GROUP:5:50]
        [PREFSTRING:insidious nature]
        [PREFSTRING:diabolical hunger for the food of others]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:RODENT_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:GOO:GOO_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:GOO:LIQUID]
        [BODY_SIZE:0:0:300]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:RED:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
