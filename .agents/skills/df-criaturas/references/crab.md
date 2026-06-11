# Crab

> Fonte: [Crab](https://dwarffortresswiki.org/index.php/Crab) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes crabs for their sideways walk.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Crab - Crab man - Giant crab**
- **Attributes**
- **Amphibious**
- **Cannot be tamed**
- **Size**
- **Birth:** 1 cm 3
- **Max:** 8,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 10
- **Fat:** 10
- **Brain:** 1
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny shelled ocean creature with many long legs. It has two large pincers on its front limbs.*

**Crabs** are multi-legged critters found on beaches, usually running away from any threats. Butchering them yields a surprisingly large amount of meat - despite being described as "tiny", they are actually significantly larger than adult cats. All crabs possess Legendary skill in climbing as well as blue-colored blood.

Note that, despite their description, they do not yield a shell when butchered, they drop "Chitin" instead. Unlike most animals, they cannot be trained. Also, unlike crabs in real life, they do not lay eggs and instead give live birth.

Some dwarves like crabs for their *pincers* and their *sideways walk*.

Admired for its *sideways walk*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Crabs have been known to gather in droves at beaches and perform a fast-paced swaying dance of some kind, with their claws raised as if celebrating something.

|  |
|----|
| "Crab" in other / Languages / Dwarven / : / ozsit / Elven / : / ditari / Goblin / : / slalsto / Human / : / julosm |

    40 kph

    Crabs were sponsored by the generous contributions of the Bay 12 community.

        Aqizzar

    [CREATURE:CRAB]
        [DESCRIPTION:A tiny shelled ocean creature with many long legs.  It has two large pincers on its front limbs.]
        [NAME:crab:crabs:crab]
        [CASTE_NAME:crab:crabs:crab]
        [CREATURE_TILE:'c'][COLOR:4:0:1]
        [NATURAL]
        [BIOME:ANY_OCEAN]
        [FREQUENCY:100]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:pincers]
        [PREFSTRING:sideways walk]
        [AMPHIBIOUS][UNDERSWIM]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [HOMEOTHERM:10071]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [NATURAL_SKILL:CLIMBING:15]
        [MUNDANE]
        [NOBONES]
        [BODY:CRAB_BODY:2EYES:HEART:BRAIN:UPPERBODY_PINCERS]
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
        [BODY_SIZE:0:0:1]
        [BODY_SIZE:1:0:8000]
        [APPLY_CREATURE_VARIATION:PINCER_ATTACK]
        [MAXAGE:10:20]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:RED:1]
                    [TLCM_NOUN:chitin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
