# Lungfish

> Fonte: [Lungfish](https://dwarffortresswiki.org/index.php/Lungfish) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes lungfish for their gulping.**
- **Biome**
- **Tropical Freshwater River Tropical Brackish River Tropical Saltwater River Tropical Freshwater Lake Tropical Brackish Lake Tropical Saltwater Lake Tropical Freshwater Pool Tropical Brackish Pool Tropical Saltwater Pool**
- **Attributes**
- **Amphibious · Fishable**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small fish which can walk on the land and breathe air. It burrows in the mud when things get dry.*

**Lungfish** are a type of aquatic vermin found in (and next to) tropical rivers, lakes, and pools year-round, and are a ready source of food when cleaned at a fishery. Lungfish are amphibious, and so are able to survive and move on land, where they are easy targets for cats and other vermin-eating domestic animals. Their pet value is equal to 0, so they can't be domesticated by an Animal trainer.

Some dwarves like lungfish for their *gulping*.

|  |
|----|
| "Lungfish" in other / Languages / Dwarven / : / vunom tatlosh / Elven / : / lave thaci / Goblin / : / bostra otu / Human / : / sino amsir |

Admired for its *gulping*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

The lungfish is also well known for its playful nature and ability to fly. Bedazzled dwarves often see these creatures going up and down in the fresh air next to rivers. After conquering water and earth, it is only natural that these terrifying beasts conquer air.

It has been assumed that, soon enough, they will conquer magma and this day is said to be the day all dwarves will accept lungfish as their new, tiny, amphibious overlords.

    [CREATURE:FISH_LUNGFISH]
        [DESCRIPTION:A small fish which can walk on the land and breathe air.  It burrows in the mud when things get dry.]
        [NAME:lungfish:lungfish:lungfish]
        [CASTE_NAME:lungfish:lungfish:lungfish]
        [CREATURE_TILE:224][COLOR:6:0:0]
        [VERMIN_GROUNDER]
        Should be able to breathe air, but this amphib tag makes it beach itself, need new tag.
        [AMPHIBIOUS][SMALL_REMAINS][FISHITEM][UNDERSWIM][VERMIN_NOTRAP]
        [NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:RIVER_TROPICAL_FRESHWATER]
        [BIOME:RIVER_TROPICAL_BRACKISHWATER]
        [BIOME:RIVER_TROPICAL_SALTWATER]
        [BIOME:LAKE_TROPICAL_FRESHWATER]
        [BIOME:LAKE_TROPICAL_BRACKISHWATER]
        [BIOME:LAKE_TROPICAL_SALTWATER]
        [BIOME:POOL_TROPICAL_FRESHWATER]
        [BIOME:POOL_TROPICAL_BRACKISHWATER]
        [BIOME:POOL_TROPICAL_SALTWATER]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:gulping]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:SIDE_FINS:DORSAL_FIN:TAIL:2EYES:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE]
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
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
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
        [ALL_ACTIVE]
        [NO_DRINK]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:3512:2634:1756:878:4900:6900] 10 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
