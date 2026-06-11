# Sturgeon

> Fonte: [Sturgeon](https://dwarffortresswiki.org/index.php/Sturgeon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sturgeons for their bony scutes.**
- **Biome**
- **Arctic Ocean Temperate Ocean Temperate Freshwater River Temperate Brackish River Temperate Saltwater River**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 10,000 cm 3
- **Mid:** 300,000 cm 3
- **Max:** 1,500,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 46
- **Fat:** 11
- **Brain:** 4
- **Heart:** 2
- **Intestines:** 12
- **Liver:** 4
- **Kidneys:** 4
- **Tripe:** 4
- **Sweetbread:** 2
- **Eyes:** 2
- **Spleen:** 2
- **Raw materials**
- **Bones:** 13
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large oceanic fish covered with bony plates.*

**Sturgeons** are a species of massive fish who can be found in temperate and arctic oceans, as well as temperate rivers. At one and a half tons, they're the largest species of bony fish (fish with skeletons made of bone rather than cartilage) in the game, tied with hippos as the largest mundane animals found in freshwater. Due to their giant size, they provide a great amount of returns when butchered. As non-vermin fish, sturgeons can't be fished by fisherdwarves, but can be caught with the use of a drowning chamber. Infant sturgeons are called *sturgeon fry*.

Sturgeons are benign, but if confronted, may very easily kill a dwarf or adventurer in adventurer mode.

Some dwarves like sturgeons for their *bony scutes*.

Admired for its *bony scutes*.

## Trivia

- In real life, sturgeons are a family made up of various different species of varying sizes. The massive size of the in-game animal may indicate they are specifically based on the beluga, the largest species of sturgeon.

    [CREATURE:FISH_STURGEON]
        [DESCRIPTION:A large oceanic fish covered with bony plates.]
        [NAME:sturgeon:sturgeons:sturgeon]
        [CASTE_NAME:sturgeon:sturgeons:sturgeon]
        [CHILD:1][GENERAL_CHILD_NAME:sturgeon fry:sturgeon fry]
        [CREATURE_TILE:224][COLOR:6:0:0]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [BENIGN][NATURAL]
        [PETVALUE:300]
        [BIOME:OCEAN_ARCTIC]
        [BIOME:OCEAN_TEMPERATE]
        [BIOME:RIVER_TEMPERATE_FRESHWATER]
        [BIOME:RIVER_TEMPERATE_BRACKISHWATER]
        [BIOME:RIVER_TEMPERATE_SALTWATER]
        [POPULATION_NUMBER:15:30]
        [PREFSTRING:bony scutes]
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
        [BODY_SIZE:0:0:10000]
        [BODY_SIZE:1:0:300000]
        [BODY_SIZE:5:0:1500000]
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
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
