# Great white shark

> Fonte: [Great white shark](https://dwarffortresswiki.org/index.php/Great_white_shark) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes great white sharks for their ability to make one afraid to go into the water.**
- **Biome**
- **Temperate Ocean Tropical Ocean**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 50,000 cm 3
- **Mid:** 500,000 cm 3
- **Max:** 2,000,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 26-122
- **Fat:** 8-21
- **Brain:** 4-5
- **Heart:** 2
- **Intestines:** 14-17
- **Liver:** 4-5
- **Kidneys:** 4
- **Tripe:** 4-5
- **Sweetbread:** 2
- **Eyes:** 2
- **Spleen:** 2
- **Raw materials**
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A giant oceanic fish with rows and rows of razor-sharp pointed teeth.*

**Great white sharks** are massive cartilaginous fish that can be found in temperate and tropical oceans. At two tons, adult great whites are huge creatures, and as such will provide a great amount of returns if butchered. As fully-sized creatures, they can't be fished by fisherdwarves, but can be caught with a drowning chamber. An infant great white shark is called a *great white shark pup*.

Being cartilaginous, great white sharks won't give bones if butchered (though they'll still provide a skull).

Some dwarves like great white sharks for their *ability to make one afraid to go into the water*.

|  |
|----|
| "Great white shark" in other / Languages / Dwarven / : / saràm volal taran / Elven / : / apaca alire cequova / Goblin / : / snuz uslun slångo / Human / : / umon mela gorhax |

Admired for its *ability to make one afraid to go into the water*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
One of the proper uses of a pit is for dumping captured enemies into a shark-infested pool. Unfortunately, functionality to allow one of your dwarves to sit on a throne and pet a cat while doing so has not yet been implemented. (Actually, that might be possible to arrange, since the ability to pet animals was added in 0.47.01.)

    [CREATURE:SHARK_GREAT_WHITE]
        [DESCRIPTION:A giant oceanic fish with rows and rows of razor-sharp pointed teeth.]
        [NAME:great white shark:great white sharks:great white shark]
        [CASTE_NAME:great white shark:great white sharks:great white shark]
        [CHILD:1][GENERAL_CHILD_NAME:great white shark pup:great white shark pups]
        [CREATURE_TILE:'S'][COLOR:7:0:1]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [LARGE_PREDATOR][NATURAL]
        [PETVALUE:500]
        [BIOME:OCEAN_TEMPERATE]
        [BIOME:OCEAN_TROPICAL]
        [POPULATION_NUMBER:15:30]
        [PREFSTRING:ability to make one afraid to go into the water]
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
        [BODY_SIZE:0:0:50000]
        [BODY_SIZE:1:0:500000]
        [BODY_SIZE:5:0:2000000]
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
