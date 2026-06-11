# Two-legged rhino lizard

> Fonte: [Two-legged rhino lizard](https://dwarffortresswiki.org/index.php/Two-legged_rhino_lizard) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes two-legged rhino lizards for their horn.**
- **Biome**
- **Any Land**
- **Attributes**
- **Alignment:** Savage
- **Devours food · Exotic pet**
- **Pet value:** 20
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny reptile, running on two legs. It has a horn on the end of its nose.*

**Two-legged rhino lizards** are a (fictional) type of vermin unique to savage areas. Aside from the savage requirement, however, they are ubiquitous, from scorching deserts to glaciers. They are essentially a lizard larger than a crow with only two legs. They are VERMIN_EATER with a PENETRATEPOWER of 2, which means they're better at gnawing their way through your barrels than most vermin.

Unlike lizards (i.e., the common lizard, *zootoca vivipara*, as stated in the raws), two-legged rhino lizards are not hateable. They have twice the pet value of lizards.

Some dwarves like two-legged rhino lizards for their *horn*.

Admired for its *horn*.

    [CREATURE:LIZARD_RHINO_TWO_LEGGED]
        [DESCRIPTION:A tiny reptile, running on two legs.  It has a horn on the end of its nose.]
        [NAME:two-legged rhino lizard:two-legged rhino lizards:two-legged rhino lizard]
        [CASTE_NAME:two-legged rhino lizard:two-legged rhino lizards:two-legged rhino lizard]
        [GNAWER:gnawed]
        [CREATURE_TILE:249][COLOR:7:0:0]
        [PETVALUE:20]
        [VERMIN_EATER][PENETRATEPOWER:2][FREQUENCY:100][VERMIN_GROUNDER]
        [SMALL_REMAINS][SAVAGE][PET_EXOTIC][NATURAL]
        [NOT_BUTCHERABLE]
        [BIOME:ANY_LAND]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:horn]
        [BODY:HUMANOID_ARMLESS_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:RIBCAGE:HEAD_HORN]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
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
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:703:505:274:1900:2900] 32 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:30]
        [BODY_SIZE:1:0:1000]
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
        [HOMEOTHERM:10070]
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:40]
                [CLUTCH_SIZE:10:30]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
