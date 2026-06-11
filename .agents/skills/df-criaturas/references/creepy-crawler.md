# Creepy crawler

> Fonte: [Creepy crawler](https://dwarffortresswiki.org/index.php/Creepy_crawler) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes creepy crawlers for their freakish wriggling.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Alignment:** Evil
- **Exotic pet**
- **Pet value:** 20
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny underground creature made of a mass of appendages resembling human fingers. It creeps across the ground like a starfish and eats with a mouth on the bottom of its body.*

**Creepy crawlers** are a type of evil subterranean vermin. They are found in deep caverns, and may spawn near rotting food. They can be captured by trappers and turned into low-value pets. When the cavern layer they inhabit is breached, they'll begin appearing on the surface, typically wandering on top of food or refuse stockpiles.

Unlike all other vermin, creepy crawlers can be butchered for a small amount of meat and organs (due to *not* having [`[NOT_BUTCHERABLE]`](/index.php/Creature_token#NOT_BUTCHERABLE "Creature token"), [`[MILKABLE]`](/index.php/Creature_token#MILKABLE "Creature token"), or [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token")). Live creepy crawlers, captured by trappers in animal traps, are automatically lined up for slaughter at a butchery, but only if they have not been tamed yet. If killed, e.g. by a cat, only unusable remains will be left over.

Some dwarves like creepy crawlers for their *freakish wriggling*.

## Gallery

-

  You could almost paint those nails.\
  *Art by Arne*

-

  *Concept art by Bay 12 Games.*

    [CREATURE:CREEPY_CRAWLER]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A tiny underground creature made of a mass of appendages resembling human fingers.  It creeps across the ground like a starfish and eats with a mouth on the bottom of its body.]
        [NAME:creepy crawler:creepy crawlers:creepy crawler]
        [CASTE_NAME:creepy crawler:creepy crawlers:creepy crawler]
        [CREATURE_TILE:'*'][COLOR:6:0:0]
        [PETVALUE:20]
        [PET_EXOTIC]
        [EVIL]
        [FREQUENCY:10][VERMIN_ROTTER][VERMIN_GROUNDER]
        [SMALL_REMAINS][NATURAL]
        [NOBONES]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:3:3]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:freakish wriggling]
        [EXTRAVISION]
        [BODY:BODY_WITH_HEAD_FLAG:HEART:GUTS:BRAIN:MOUTH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [CANNOT_JUMP]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:1000]
        [MAXAGE:5:10]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
    [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
