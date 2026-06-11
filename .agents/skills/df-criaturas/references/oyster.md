# Oyster

> Fonte: [Oyster](https://dwarffortresswiki.org/index.php/Oyster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes oysters for their beauty.**
- **Biome**
- **Any Ocean**
- **Attributes**
- **Aquatic · Fishable · Hateable · Shell**
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small marine creature that lives in a shell rooted to the sea floor.*

**Oysters** are a common source of food for fortresses located near an ocean. They are also one of the few types of creatures, along with mussels, pond turtles, nautiluses, and cave lobsters, that are sources of shells. They can't be butchered, but are cleaned at a fishery, which generates a shell and prepared oyster. Oysters can also be cooked whole (as "raw oysters") and even cooked *live* (if you happen to catch one in an animal trap using the "catch live fish" job).

Oysters are hateable vermin and will give unhappy thoughts to dwarves who absolutely detest oysters when they encounter them.

Some dwarves like oysters for their *beauty*.

Admired for its *beauty*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
The Whole World Is Not An Oyster

    [CREATURE:OYSTER]
        [DESCRIPTION:A small marine creature that lives in a shell rooted to the sea floor.]
        [NAME:oyster:oysters:oyster]
        [CASTE_NAME:oyster:oysters:oyster]
        [CREATURE_TILE:'o'][COLOR:7:0:1]
        [PETVALUE:10]
        [VERMIN_FISH]
        [FREQUENCY:100][VERMIN_HATEABLE]
        [AQUATIC][SMALL_REMAINS][FISHITEM][NOBONES][IMMOBILE_LAND][UNDERSWIM][COOKABLE_LIVE]
        [PEARL]
        [NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:ANY_OCEAN]
        [NO_DRINK]
        [MUNDANE]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:beauty]
        [BODY:BASIC_1PARTBODY:SHELL]
        [USE_MATERIAL_TEMPLATE:SKIN:SKIN_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:FAT:FAT_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:MUSCLE:MUSCLE_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:SHELL:SHELL_TEMPLATE]
            [STATE_COLOR:ALL:GRAY]
        [USE_MATERIAL_TEMPLATE:LEATHER:LEATHER_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:PARCHMENT:PARCHMENT_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:TALLOW:TALLOW_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:SOAP:SOAP_TEMPLATE]
        [USE_TISSUE_TEMPLATE:SKIN:SKIN_TEMPLATE]
        [USE_TISSUE_TEMPLATE:FAT:FAT_TEMPLATE]
        [USE_TISSUE_TEMPLATE:MUSCLE:MUSCLE_TEMPLATE]
        [USE_TISSUE_TEMPLATE:SHELL:SHELL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:BODY:MUSCLE:NORMAL]
        [TISSUE_LAYER_OVER:BY_CATEGORY:BODY:FAT:NORMAL]
        [TISSUE_LAYER_OVER:BY_CATEGORY:BODY:SKIN:NORMAL]
        [TISSUE_LAYER:BY_CATEGORY:SHELL:SHELL:NORMAL]
        [BODY_DETAIL_PLAN:SHELL_POSITIONS]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
            [STATE_COLOR:ALL:BLUE] copper not iron based
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:200]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:GRAY:1]
                [TLCM_NOUN:skin:SINGULAR]
