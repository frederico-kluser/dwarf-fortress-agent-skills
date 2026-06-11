# Green tree frog

> Fonte: [Green tree frog](https://dwarffortresswiki.org/index.php/Green_tree_frog) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes green tree frogs for their distinct mating call.**
- **Biome**
- **Temperate Freshwater Pool Temperate Freshwater Lake Temperate Freshwater Swamp Temperate Freshwater Marsh**
- **Variations**
- **Green tree frog - Green tree frog man - Giant green tree frog**
- **Attributes**
- **Amphibious · Exotic pet**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny amphibian that lives in the trees.*

**Green tree frogs** are unremarkable amphibious vermin found in temperate freshwater biomes. They can be captured by trappers and turned into low-value pets. All green tree frogs possess Legendary skill in climbing.

Despite the description, they do not live in trees. They will not appear in maps during the winter.

Some dwarves like green tree frogs for their *distinct mating call*.

Admired for its *distinct mating call*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Military dwarves may be expected to eat green tree frogs, if found in a deep trial to survive. This is in addition to going through the rain.

|  |
|----|
| "Green tree frog" in other / Languages / Dwarven / : / omer dák enog / Elven / : / liba thelire amimó / Goblin / : / astru tonspe uxus / Human / : / el akan ihhi |

    1 kph

    Green tree frogs were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:GREEN_TREE_FROG]
        [DESCRIPTION:A tiny amphibian that lives in the trees.]
        [NAME:green tree frog:green tree frogs:green tree frog]
        [CASTE_NAME:green tree frog:green tree frogs:green tree frog]
        [CREATURE_TILE:249][COLOR:2:0:1]
        [PETVALUE:10]
        [VERMIN_GROUNDER][FREQUENCY:100]
        [AMPHIBIOUS][SMALL_REMAINS][NO_WINTER][UNDERSWIM]
        [BENIGN][NATURAL][PET_EXOTIC]
        [NOT_BUTCHERABLE]
        [BIOME:POOL_TEMPERATE_FRESHWATER]
        [BIOME:LAKE_TEMPERATE_FRESHWATER]
        [BIOME:SWAMP_TEMPERATE_FRESHWATER]
        [BIOME:MARSH_TEMPERATE_FRESHWATER]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:distinct mating call]
        [BODY:QUADRUPED_NECK:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE]
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
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:100]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:5]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [NOCTURNAL]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [MUNDANE]
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
