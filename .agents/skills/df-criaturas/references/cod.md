# Cod

> Fonte: [Cod](https://dwarffortresswiki.org/index.php/Cod) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cod for their fins.**
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
- **Meat:** 8-9
- **Fat:** 7-8
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

*A medium-sized oceanic fish, often hunted for its meat.*

**Cod** are medium-sized fish found in arctic and temperate oceans. Large groups of 10-15 cod can appear on the map at once.

Cod produce a fair amount of food, but your fisherdwarves can only catch vermin fish. You can create a drowning chamber to get their remains, or if you want a live one, you can place cage traps in your chamber before refilling it with water. Capturing them with a fishery will not work, as that too is restricted to vermin. They have a high pet value of 200, but this is pointless, as your dwarves can't tame them. Regardless, when you do catch one in a cage, be warned that transferring them to an aquarium may cause them to instantly air-drown.Bug:1590

Some dwarves like cod for their *fins*.

Admired for their *fins*.

    [CREATURE:FISH_COD]
        [DESCRIPTION:A medium-sized oceanic fish, often hunted for its meat.]
        [NAME:cod:cod:cod]
        [CASTE_NAME:cod:cod:cod]
        [CHILD:1][GENERAL_CHILD_NAME:cod fry:cod fry]
        [CREATURE_TILE:224][COLOR:7:0:0]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [BENIGN][MEANDERER][NATURAL]
        [PETVALUE:200]
        [BIOME:OCEAN_ARCTIC]
        [BIOME:OCEAN_TEMPERATE]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:10:15]
        [PREFSTRING:fins]
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
