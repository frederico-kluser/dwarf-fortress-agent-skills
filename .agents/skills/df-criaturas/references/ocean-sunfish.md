# Ocean sunfish

> Fonte: [Ocean sunfish](https://dwarffortresswiki.org/index.php/Ocean_sunfish) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ocean sunfish for their strange fins.**
- **Biome**
- **Temperate Ocean Tropical Ocean**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 100,000 cm 3
- **Mid:** 400,000 cm 3
- **Max:** 1,000,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 31
- **Fat:** 8
- **Brain:** 2
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 8
- **Liver:** 2
- **Kidneys:** 2
- **Tripe:** 2
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 11
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant oceanic creature resembling a huge fish's head connected to a wide tail.*

**Ocean sunfish** are a species of huge fish who can be found in temperate and tropical oceans. At one ton, they're the heaviest species of Osteichthyes fish (fish with skeletons made of bone rather than cartilage) in real life, but are second to sturgeons in *Dwarf Fortress*. Due to their massive size, they provide a great amount of returns when butchered. As non-vermin fish, ocean sunfish can't be fished by fisherdwarves, but can be caught with the use of a drowning chamber. Infant ocean sunfish are called *ocean sunfish fry*.

Some dwarves like ocean sunfish for their *size* and their *strange fins*.

|  |
|----|
| "Ocean sunfish" in other / Languages / Dwarven / : / migrur ad-tatlosh / Elven / : / romi amiÿa-thaci / Goblin / : / strabo xogak-otu / Human / : / sota sáthra-amsir |

Admired for its *size*.

    [CREATURE:FISH_SUNFISH_OCEAN]
        [DESCRIPTION:A giant oceanic creature resembling a huge fish's head connected to a wide tail.]
        [NAME:ocean sunfish:ocean sunfish:ocean sunfish]
        [CASTE_NAME:ocean sunfish:ocean sunfish:ocean sunfish]
        [CHILD:1][GENERAL_CHILD_NAME:ocean sunfish fry:ocean sunfish fry]
        [CREATURE_TILE:224][COLOR:3:0:0]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [BENIGN][MEANDERER][NATURAL]
        [PETVALUE:500]
        [BIOME:OCEAN_TEMPERATE]
        [BIOME:OCEAN_TROPICAL]
        [POPULATION_NUMBER:15:30]
        [PREFSTRING:size]
        [PREFSTRING:strange fins]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:SIDE_FINS:TAIL:2EYES:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE]
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
        [BODY_SIZE:0:0:100000]
        [BODY_SIZE:1:0:400000]
        [BODY_SIZE:5:0:1000000]
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
