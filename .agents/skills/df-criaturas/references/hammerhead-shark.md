# Hammerhead shark

> Fonte: [Hammerhead shark](https://dwarffortresswiki.org/index.php/Hammerhead_shark) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hammerhead sharks for their oddly-shaped heads.**
- **Biome**
- **Temperate Ocean Tropical Ocean**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 10,000 cm 3
- **Mid:** 200,000 cm 3
- **Max:** 500,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 17
- **Fat:** 8
- **Brain:** 1
- **Heart:** 1
- **Intestines:** 4
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large, dangerous fish, often found hunting solitarily along coastlines.*

**Hammerhead sharks** are large cartilaginous fish that can be found in tropical and temperate oceans. Adult hammerheads are enormous, nearly nine times the size of an average dwarf, and as such provide a great amount of meat when butchered. As fully-sized creatures, they can't be fished by fisherdwarves, but can be caught with a drowning chamber. An infant hammerhead shark is called a *hammerhead shark pup*.

Being cartilaginous, hammerhead sharks won't give bones if butchered (though they'll still provide a skull).

Some dwarves like hammerhead sharks for their *oddly-shaped heads*.

|  |
|----|
| "Hammerhead shark" in other / Languages / Dwarven / : / nil ser taran / Elven / : / ÿeri íne cequova / Goblin / : / ospum ostam slångo / Human / : / ongu aru gorhax |

Admired for their *oddly-shaped heads*.

    [CREATURE:SHARK_HAMMERHEAD]
        [DESCRIPTION:A large, dangerous fish, often found hunting solitarily along coastlines.]
        [NAME:hammerhead shark:hammerhead sharks:hammerhead shark]
        [CASTE_NAME:hammerhead shark:hammerhead sharks:hammerhead shark]
        [CHILD:1][GENERAL_CHILD_NAME:hammerhead shark pup:hammerhead shark pups]
        [CREATURE_TILE:'S'][COLOR:6:0:0]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [LARGE_PREDATOR][NATURAL]
        [PETVALUE:500]
        [BIOME:OCEAN_TEMPERATE]
        [BIOME:OCEAN_TROPICAL]
        [POPULATION_NUMBER:15:30]
        [PREFSTRING:oddly-shaped heads]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:SIDE_FINS:DORSAL_FIN:TAIL:2EYES:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE:GENERIC_TEETH]
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
        [BODY_SIZE:0:0:10000]
        [BODY_SIZE:1:0:200000]
        [BODY_SIZE:5:0:500000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
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
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
