# Octopus

> Fonte: [Octopus](https://dwarffortresswiki.org/index.php/Octopus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes octopuses for their many arms.**
- **Biome**
- **Any Ocean**
- **Variations**
- **Octopus - Octopus man - Giant octopus**
- **Attributes**
- **Aquatic · Horn**
- **Cannot be tamed**
- **Size**
- **Birth:** 20 cm 3
- **Max:** 5,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 2-10
- **Fat:** 2-10
- **Brain:** 0-1
- **Raw materials**
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized underwater mollusk with eight arms. It is the most clever of its kind.*

**Octopuses** (the correct in-game term) are a species of marine creature who may be found in any ocean biome. Only as large as a cat, they are a negligible presence to dwarves and provide few returns when butchered. Unlike squids, octopuses aren't vermin and can't be fished by fisherdwarves, but can be caught with the use of a drowning chamber. They possess copper-based blue blood instead of a usual dark red.

The most notable ability of the octopus is being able to squirt ink when threatened (or when controlled in the arena by clicking "Assume Control"). This has the effect of *hiding* the octopus from view (due to its interaction token), as well as preventing it from being viewed (clicked on) or listed in the u units menu. Octopus ink turns water a dark grey, similar to other contaminants. When controlling another creature in adventurer mode, the You've spotted an octopus! message will appear, while in fortress mode you'll see An octopus has sprung from ambush! instead. Due to their tiny size, however, you shouldn't have to worry about it.

Some dwarves like octopuses for their *many arms* and their *intelligence*.

Admired for its *many arms*.

    Octopuses were sponsored by the generous contributions of the Bay 12 community.

        David Kidd
        Willis
        Gigalith

    [CREATURE:OCTOPUS]
        [DESCRIPTION:A medium-sized underwater mollusk with eight arms.  It is the most clever of its kind.]
        [NAME:octopus:octopuses:octopus]
        [CASTE_NAME:octopus:octopuses:octopus]
        [CREATURE_TILE:'o'][COLOR:7:0:0]
        [PETVALUE:10]
        [LARGE_ROAMING]
        [FREQUENCY:100]
        [CARNIVORE]
        [AQUATIC][NOBONES][IMMOBILE_LAND][UNDERSWIM]
        [NATURAL]
        [BIOME:ANY_OCEAN]
        [NO_DRINK]
        [POPULATION_NUMBER:50:100]
        [PREFSTRING:intelligence]
        [PREFSTRING:many arms]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:2EYES:BEAK:8_SIMPLE_HEAD_ARMS:BRAIN]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
            [REMOVE_MATERIAL:CARTILAGE]
            [USE_MATERIAL_TEMPLATE:CHITIN:CHITIN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
            [REMOVE_TISSUE:CARTILAGE]
            [USE_TISSUE_TEMPLATE:CHITIN:CHITIN_TEMPLATE]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:CHITIN:CHITIN]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
            [STATE_COLOR:ALL:BLUE] copper not iron based
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [USE_MATERIAL_TEMPLATE:INK:INK_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen octopus ink]
            [STATE_ADJ:ALL_SOLID:frozen octopus ink]
            [STATE_NAME:LIQUID:octopus ink]
            [STATE_ADJ:LIQUID:octopus ink]
            [STATE_NAME:GAS:boiling octopus ink]
            [STATE_ADJ:GAS:boiling octopus ink]
            [PREFIX:NONE]
            [STATE_COLOR:ALL:BLACK]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:657:438:219:1900:2900] 40 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [BODY_SIZE:0:0:20]
        [BODY_SIZE:0:168:5000]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION_WITH_HIDE_EFFECT]
            [CDI:TOKEN:SQUIRT_INK]
            [CDI:ADV_NAME:Squirt ink]
            [CDI:USAGE_HINT:FLEEING]
            [CDI:LOCATION_HINT:IN_WATER]
            [CDI:BP_REQUIRED:BY_TYPE:UPPERBODY]
            [CDI:MATERIAL:LOCAL_CREATURE_MAT:INK:SPATTER_LIQUID]
            [CDI:VERB:squirt ink:squirts ink:NA]
            [CDI:TARGET:C:SELF_ONLY]
            [CDI:TARGET:D:SELF_ONLY]
            [CDI:WAIT_PERIOD:200]
            [CDI:FREE_ACTION]
        [MAXAGE:2:3]
        [CREPUSCULAR]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:ECRU:1] should be able to change its color
                [TLCM_NOUN:skin:SINGULAR]
