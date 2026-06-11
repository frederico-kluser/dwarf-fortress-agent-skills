# Carp

> Fonte: [Carp](https://dwarffortresswiki.org/index.php/Carp) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes carp for their protruding mouths.**
- **Biome**
- **Temperate Freshwater River Tropical Freshwater River Temperate Freshwater Lake Tropical Freshwater Lake**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 4,000 cm 3
- **Mid:** 20,000 cm 3
- **Max:** 40,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 8-9
- **Fat:** 8
- **Brain:** 1
- **Heart:** 1
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 12
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized fish found in lakes and streams. They are bottom-feeders and tend to gather in groups.*

**Carp** are a species of fish found in tropical freshwater rivers and lakes, where they appear in groups of 5-10 individuals. Infamous in previous versions of the game for their aggression and disproportionately powerful bite attacks, carp in the current version are an inconvenience at worst. Newborn carp are known as *carp fry*.

Carp are nearly as heavy as dwarves but are entirely benign, and due to being aquatic, they will never attack civilians out of their own volition. While old carp were vicious, today they are overcome with terror at the sight of fisherdwarves and serve only as target practice for your hunters. Undead carp, however, are a different story altogether. They possess an unused pet value of 50, but like most fish, are completely untrainable.

Some dwarves like carp for their *protruding mouths*.

Admired for their *protruding mouths*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

In prior versions of the game, carp had teeth that could inflict 3 times as much damage as an unarmed dwarf's fist, and so could dispatch an unarmed and unarmored dwarf (e.g. a fisherman, or a miner going for a drink) with ease. They were also strangely aggressive for fish, something which was kept for many releases because it was funny.

*"I think I made fish too hardcore"* --Toady One

Legends of terrifying carp persist from days of yore\
*Art by Skullamity*

    [CREATURE:FISH_CARP]
        [DESCRIPTION:A medium-sized fish found in lakes and streams.  They are bottom-feeders and tend to gather in groups.]
        [NAME:carp:carp:carp]
        [CASTE_NAME:carp:carp:carp]
        [CHILD:1][GENERAL_CHILD_NAME:carp fry:carp fry]
        [CREATURE_TILE:224][COLOR:3:0:0]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [BENIGN][MEANDERER][NATURAL]
        [PETVALUE:50]
        [BIOME:RIVER_TEMPERATE_FRESHWATER]
        [BIOME:RIVER_TROPICAL_FRESHWATER]
        [BIOME:LAKE_TEMPERATE_FRESHWATER]
        [BIOME:LAKE_TROPICAL_FRESHWATER]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [PREFSTRING:protruding mouths]
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
        [BODY_SIZE:0:0:4000]
        [BODY_SIZE:1:0:20000]
        [BODY_SIZE:5:0:40000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SLAP:BODYPART:BY_CATEGORY:TAIL]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:slap:slaps]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ALL_ACTIVE]
        [NO_DRINK]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:657:438:219:1900:2900] 40 kph, NO DATA
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
