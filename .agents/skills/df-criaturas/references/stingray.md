# Stingray

> Fonte: [Stingray](https://dwarffortresswiki.org/index.php/Stingray) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes stingrays for their tail spines.**
- **Biome**
- **Tropical Ocean Tropical Freshwater River Tropical Brackish River Tropical Saltwater River Tropical Freshwater Lake Tropical Brackish Lake Tropical Saltwater Lake**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 500 cm 3
- **Mid:** 1,000 cm 3
- **Max:** 5,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 5
- **Fat:** 5
- **Brain:** 1
- **Intestines:** 1
- **Liver:** 1
- **Tripe:** 1
- **Raw materials**
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized, flat fish. It lives near the beach and will defend itself with sharp barbs.*

**Stingrays** are cartilaginous fish that can be found in tropical oceans and lakes. Only as large as a cat, they give a small amount of returns if butchered. As fully-sized creatures, they can't be fished by fisherdwarves, but can be caught with a drowning chamber. An infant stingray is called a *stingray pup*.

Like real stingrays, they are able to sting enemies with their tails, though they don't have any venom. Unlike real stingrays, however, they do not possess a stinger and thus the sting is more like being slashed with a meaty blade than stabbed with a bony point. Being benign and restricted to water means your dwarves are unlikely to be stung anyway. Being cartilaginous, stingrays won't give bones if butchered (though they'll still provide a skull).

Some dwarves like stingrays for their *tail spines*.

Admired for their *tail spines*.

    [CREATURE:FISH_STINGRAY]
        [DESCRIPTION:A medium-sized, flat fish.  It lives near the beach and will defend itself with sharp barbs.]
        [NAME:stingray:stingrays:stingray]
        [CASTE_NAME:stingray:stingrays:stingray]
        [CHILD:1][GENERAL_CHILD_NAME:stingray pup:stingray pups]
        [CREATURE_TILE:149][COLOR:7:0:0]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [BENIGN][MEANDERER][NATURAL]
        [PETVALUE:200]
        [BIOME:OCEAN_TROPICAL]
        [BIOME:RIVER_TROPICAL_FRESHWATER]
        [BIOME:RIVER_TROPICAL_BRACKISHWATER]
        [BIOME:RIVER_TROPICAL_SALTWATER]
        [BIOME:LAKE_TROPICAL_FRESHWATER]
        [BIOME:LAKE_TROPICAL_BRACKISHWATER]
        [BIOME:LAKE_TROPICAL_SALTWATER]
        [POPULATION_NUMBER:15:30]
        [PREFSTRING:tail spines]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:SIDE_FINS:TAIL:2EYES:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE:GENERIC_TEETH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:CARTILAGE:CARTILAGE]
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
        [BODY_SIZE:0:0:500]
        [BODY_SIZE:1:0:1000]
        [BODY_SIZE:5:0:5000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ATTACK:SLAP:BODYPART:BY_CATEGORY:TAIL]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:stab:stabs]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
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
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
