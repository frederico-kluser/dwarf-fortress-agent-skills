# Conger eel

> Fonte: [Conger eel](https://dwarffortresswiki.org/index.php/Conger_eel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes conger eels for their long bodies.**
- **Biome**
- **Arctic Ocean Temperate Ocean**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 5,000 cm 3
- **Mid:** 20,000 cm 3
- **Max:** 50,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 6
- **Fat:** 5
- **Brain:** 1
- **Heart:** 1
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 9
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized, brown, snake-like fish found in ocean waters.*

**Conger eels** are a species of fish who can be found in temperate and arctic oceans. Slightly smaller than a dwarf, they provide a fair amount of returns when butchered. As non-vermin fish, conger eels can't be fished by fisherdwarves, but can be caught with the use of a drowning chamber. Infant conger eels are called *conger eel fry*.

Some dwarves like conger eels for their *long bodies*.

Admired for their *long bodies*.

    [CREATURE:FISH_CONGER_EEL]
        [DESCRIPTION:A medium-sized, brown, snake-like fish found in ocean waters.]
        [NAME:conger eel:conger eels:conger eel]
        [CASTE_NAME:conger eel:conger eels:conger eel]
        [CHILD:1][GENERAL_CHILD_NAME:conger eel fry:conger eel fry]
        [CREATURE_TILE:'~'][COLOR:7:0:0]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [BENIGN][MEANDERER][NATURAL]
        [PETVALUE:400]
        [BIOME:OCEAN_ARCTIC]
        [BIOME:OCEAN_TEMPERATE]
        [POPULATION_NUMBER:15:30]
        [PREFSTRING:long bodies]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:TAIL:2EYES:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE]
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
        [BODY_SIZE:0:0:5000]
        [BODY_SIZE:1:0:20000]
        [BODY_SIZE:5:0:50000]
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
        [NOCTURNAL]
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
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
