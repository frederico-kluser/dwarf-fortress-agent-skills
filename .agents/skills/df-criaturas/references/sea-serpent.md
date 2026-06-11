# Sea serpent

> Fonte: [Sea serpent](https://dwarffortresswiki.org/index.php/Sea_serpent) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sea serpents for their majesty.**
- **Biome**
- **Any Ocean**
- **Attributes**
- **Alignment:** Savage
- **Aquatic · Egglaying**
- **Tamed Attributes**
- **Pet value:** 1,000
- **Not hunting/war trainable**
- **Size**
- **Birth:** 6,000 cm 3
- **Max:** 9,000,000 cm 3
- **Food products**
- **Eggs:** 1
- **Age**
- **Adult at:** 6
- **Max age:** 150-175
- **Butchering returns ( Value multiplier ×5)**
- **Food items**
- **Meat:** 104-412
- **Fat:** 35-85
- **Brain:** 18-24
- **Heart:** 8-12
- **Lungs:** 36-46
- **Intestines:** 54-70
- **Liver:** 18-24
- **Kidneys:** 18-24
- **Tripe:** 18-24
- **Sweetbread:** 8-12
- **Eyes:** 2
- **Spleen:** 8-12
- **Raw materials**
- **Bones:** 58-79
- **Skull:** 1
- **Teeth:** 3
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant limbless dragon that lives in the sea.*

**Sea serpents** are gigantic aquatic predators who inhabit savage oceans. Purely aquatic creatures, sea serpents will not leave water to attack your dwarves, but any dwarf that foolishly falls in will not have long to live. At 9,000,000 cm³, they're one of the largest creatures found in the sea. Sea serpents can appear in any savage ocean, but have a population limit of one per biome - so if you want more than one to appear, you'll need an embark where two different ocean biomes overlap. They can have children, but will only lay one egg at a time. Young sea serpents become adults at the age of six, but do not reach their full size until they are twenty years old. They have an extremely long (for a non-sapient creature) lifespan, living to be 150 to 170 years old - the same as dwarves.

Sea serpents have been discussed as a replacement for merfolk in aquatic farming operations due to their high body part multiplier as well as their massive size. Unfortunately, they cannot currently breed due to a bug with submerged nest boxes.Bug:4105 While described as limbless (and being depicted as such in their Premium graphical sprite), they in fact possess both front and rear flippers, which presumably makes them resemble some sort of draconic plesiosaurus.

Some dwarves like sea serpents for their *majesty*.

|  |
|----|
| "Sea serpent" in other / Languages / Dwarven / : / allas shethel / Elven / : / lene relira / Goblin / : / ozob olsmu / Human / : / iño ithrat |

Admired for its *majesty*.

    [CREATURE:SEA_SERPENT]
        [DESCRIPTION:A giant limbless dragon that lives in the sea.]
        [NAME:sea serpent:sea serpents:sea serpent]
        [CASTE_NAME:sea serpent:sea serpents:sea serpent]
        [CREATURE_TILE:'S'][COLOR:3:0:1]
        [PETVALUE:1000]
        [PET_EXOTIC]
        [AQUATIC][IMMOBILE_LAND]
        [POPULATION_NUMBER:1:1]
        [LARGE_ROAMING]
        [BIOME:ANY_OCEAN]
        [NO_DRINK]
        [LARGE_PREDATOR][SAVAGE]
        [BONECARN]
        [PREFSTRING:majesty]
        [MAXAGE:150:175]
        [CHILD:6][CHILDNAME:sea serpent hatchling:sea serpent hatchlings]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:FRONT_BODY_FLIPPERS:REAR_BODY_FLIPPERS:TAIL:2EYES:2LUNGS:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
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
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:6000]
        [BODY_SIZE:20:0:9000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
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
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:711:521:293:1900:2900] 30 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:6100]
                [CLUTCH_SIZE:1:1]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:AQUA:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:5]
