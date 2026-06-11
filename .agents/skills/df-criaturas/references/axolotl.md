# Axolotl

> Fonte: [Axolotl](https://dwarffortresswiki.org/index.php/Axolotl) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes axolotls for their gills.**
- **Biome**
- **Tropical Saltwater Lake Tropical Brackish Lake Tropical Freshwater Lake**
- **Variations**
- **Axolotl - Axolotl man - Giant axolotl**
- **Attributes**
- **Amphibious · Exotic pet**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small salamander found in remote lakes. It has the mysterious ability to regrow limbs.*

**Axolotls** are a species of unremarkable vermin who can be found in tropical lakes. They may be captured by trappers and turned into low-value pets.

Some dwarves like axolotls for their *gills*.

Admired for its *gills*.

    12 kph

    Axolotls were sponsored by the generous contributions of the Bay 12 community.

        Sponsored by Cheesetroll, because it pays his bills.
        Paul W.

    [CREATURE:AXOLOTL]
        [DESCRIPTION:A small salamander found in remote lakes.  It has the mysterious ability to regrow limbs.]
        [NAME:axolotl:axolotls:axolotl]
        [CASTE_NAME:axolotl:axolotls:axolotl]
        [CREATURE_TILE:249][COLOR:5:0:0]
        [PETVALUE:10]
        [PET_EXOTIC]
        [VERMIN_GROUNDER][FREQUENCY:100]
        [SMALL_REMAINS]
        [AMPHIBIOUS][UNDERSWIM]
        [NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:LAKE_TROPICAL_SALTWATER]
        [BIOME:LAKE_TROPICAL_BRACKISHWATER]
        [BIOME:LAKE_TROPICAL_FRESHWATER]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:gills]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE]
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
        [BODY_SIZE:0:0:200]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:25]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [HOMEOTHERM:10040]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:1945:1504:1062:548:3100:4500] 16 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
