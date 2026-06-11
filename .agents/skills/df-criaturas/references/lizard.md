# Lizard

> Fonte: [Lizard](https://dwarffortresswiki.org/index.php/Lizard) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes lizards for their beauty.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Lizard - Lizard man - Giant lizard**
- **Attributes**
- **Devours food · Exotic pet · Hateable**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small reptile.*

**Lizards** are a species of hateable above ground vermin found in any area that is not freezing, but will not be found in winter. They are known to eat stockpiled food, and some dwarves will get an unhappy thought from encountering one. They can be captured by trappers and turned into pets. All lizards possess Legendary skill in climbing.

Some dwarves like lizards for their *beauty*.

|  |
|----|
| "Lizard" in other / Languages / Dwarven / : / bungek / Elven / : / cimathi / Goblin / : / asp / Human / : / ramac |

Admired for its *beauty*.

    [CREATURE:LIZARD]  zootoca vivipara, no eggs
        [DESCRIPTION:A small reptile.]
        [NAME:lizard:lizards:lizard]
        [CASTE_NAME:lizard:lizards:lizard]
        [CREATURE_TILE:249][COLOR:6:0:0]
        [PETVALUE:10]
        [VERMIN_EATER][PENETRATEPOWER:1][FREQUENCY:100][VERMIN_HATEABLE][VERMIN_GROUNDER]
        [SMALL_REMAINS][NO_WINTER]
        [NATURAL][PET_EXOTIC]
        [NOT_BUTCHERABLE]
        [CARNIVORE]
        [BIOME:NOT_FREEZING]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:beauty]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH:TONGUE:RIBCAGE:5TOES_FQ_REG:5TOES_RQ_REG]
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
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
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
        [SWIMS_INNATE]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:200]
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
        [DIURNAL]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:LIGHT_BROWN:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
