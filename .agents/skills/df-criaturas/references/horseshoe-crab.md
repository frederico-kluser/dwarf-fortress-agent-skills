# Horseshoe crab

> Fonte: [Horseshoe crab](https://dwarffortresswiki.org/index.php/Horseshoe_crab) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes horseshoe crabs for their ability to hide in sand.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Horseshoe crab - Horseshoe crab man - Giant horseshoe crab**
- **Attributes**
- **Amphibious**
- **Cannot be tamed**
- **Size**
- **Max:** 2,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 20-40
- **Butchering returns**
- **Food items**
- **Meat:** 1
- **Fat:** 1
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny sea animal that lives in the sand just offshore. It has a flat body with legs underneath.*

**Horseshoe crabs** are creatures found inhabiting ocean biomes. Smaller than a chicken, they are unable to endanger your dwarves and make ideal defensive training partners in adventurer mode, being nearly harmless save for any lucky hits to the face. Unlike most animals, they can neither be trained nor possess any pet value, and a butchered crab will yield only a single piece of meat and fat.

Some dwarves like horseshoe crabs for their *ability to hide in sand*.

Admired for its *ability to hide in sand*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Contrary to their name, they are not wearable by horses.

    Horseshoe crabs were sponsored by the generous contributions of the Bay 12 community.

        "We were here ages ago, we'll be here after all of you are gone."

    [CREATURE:HORSESHOE_CRAB]
        [DESCRIPTION:A tiny sea animal that lives in the sand just offshore.  It has a flat body with legs underneath.]
        [NAME:horseshoe crab:horseshoe crabs:horseshoe crab]
        [CASTE_NAME:horseshoe crab:horseshoe crabs:horseshoe crab]
        [CREATURE_TILE:'c'][COLOR:6:0:0]
        [NATURAL]
        [BIOME:ANY_OCEAN]
        [LARGE_ROAMING]
        [AMPHIBIOUS][UNDERSWIM]
        [FREQUENCY:100]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:ability to hide in sand]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [MUNDANE]
        [NOBONES]
        [EXTRAVISION]
        [BODY:BODY_WITH_HEAD_FLAG:HEART:BRAIN:TAIL]
        [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
        [BODY_DETAIL_PLAN:CHITIN_TISSUES]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
            [STATE_COLOR:ALL:BLUE] copper not iron based
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:2000]
        [MAXAGE:20:40]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:MAROON:1]
                    [TLCM_NOUN:chitin:SINGULAR]
