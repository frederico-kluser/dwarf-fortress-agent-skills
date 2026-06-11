# Large rat

> Fonte: [Large rat](https://dwarffortresswiki.org/index.php/Large_rat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes large rats for their strength.**
- **Biome**
- **Underground Depth: 1**
- **Variations**
- **Rat - Rat man - Large rat - Giant rat**
- **Attributes**
- **Steals food · Steals drink**
- **Tamed Attributes**
- **Pet value:** 250
- **Not hunting/war trainable**
- **Size**
- **Birth:** 2,500 cm 3
- **Mid:** 12,500 cm 3
- **Max:** 25,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 6-13
- **Fat:** 6-13
- **Brain:** 0-1
- **Heart:** 0-1
- **Lungs:** 0-2
- **Intestines:** 0-1
- **Liver:** 0-1
- **Kidneys:** 0-2
- **Tripe:** 0-1
- **Sweetbread:** 0-1
- **Spleen:** 0-1
- **Raw materials**
- **Bones:** 4-12
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge rodent found underground.*

**Large rats** are creatures commonly found in the first layer of the caverns, larger than a common rat but smaller than a giant rat. About the size of a kobold, these creatures will steal your food and drink your booze at every chance, meaning they should be kept away from your food stockpiles by all means necessary. All large rats are born with Legendary skill in climbing, and their infants are called *large rat pups*.

Large rats are benign and will flee from conflict, but dwarves will generally react violently to their presence, leading to them often getting beaten to a pulp by your peasants before they have the chance to cause any trouble. These creatures can be captured with cage traps very easily, as a food stockpile with a couple pieces of food can be used as lure. Once captured, they can be turned into fairly valuable pets, though due to their very short lifespan (no more than 3 years), they make poor companions to dwarves and are better off being butchered.

Items of clothing made from "large rat leather" have names that can sound awkward due to the way the game handles items sized for different creatures. A dwarf-sized tunic made from large rat leather is called, predictably, a "large rat leather tunic". Unfortunately, that means that a tunic made for bigger creatures like a human would be called a "*large* large rat leather tunic", and a tunic made for a smaller creature like a kobold would be called a "*small* large rat leather tunic".

Some dwarves like large rats for their *strength*.

Requires larger cheese.

|  |
|----|
| "Large rat" in other / Languages / Dwarven / : / or atem / Elven / : / lacifa thapa / Goblin / : / sted spödgôz / Human / : / lod othur |

    [CREATURE:RAT_LARGE]
        [DESCRIPTION:A huge rodent found underground.]
        [NAME:large rat:large rats:large rat]
        [CASTE_NAME:large rat:large rats:large rat]
        [CHILD:1][GENERAL_CHILD_NAME:large rat pup:large rat pups]
        [CREATURE_TILE:'r'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:250]
        [PET_EXOTIC]
        [NATURAL]
        [LARGE_ROAMING][FREQUENCY:100]
        [BENIGN]
        [POPULATION_NUMBER:10:20]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:1]
        [CURIOUSBEAST_EATER]
        [CURIOUSBEAST_GUZZLER]
        [PREFSTRING:strength]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:RODENT_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
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
        [BODY_SIZE:0:0:2500]
        [BODY_SIZE:1:0:12500]
        [BODY_SIZE:2:0:25000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [LOW_LIGHT_VISION:10000]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:730:561:351:1900:2900] 25 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
