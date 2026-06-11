# Sea lamprey

> Fonte: [Sea lamprey](https://dwarffortresswiki.org/index.php/Sea_lamprey) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sea lampreys for their suckers.**
- **Biome**
- **Arctic Ocean Temperate Ocean Temperate Freshwater River Temperate Brackish River Temperate Saltwater River Temperate Freshwater Lake Temperate Brackish Lake Temperate Saltwater Lake**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 2,000 cm 3
- **Mid:** 6,000 cm 3
- **Max:** 20,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 5
- **Fat:** 6
- **Heart:** 1
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small oceanic eel-like creature that latches onto the side of its victim and tears into them.*

**Sea lampreys** are a species of fish found in any non-tropical body of water, excluding pools. As big as a kobold, they provide a fair amount of returns when butchered. As non-vermin fish, sea lampreys can't be fished by fisherdwarves, but can be caught with the use of a drowning chamber. Infant sea lampreys are called *larval sea lampreys*. These should not be confused with the brook lamprey, a harmless vermin fish.

Some dwarves like sea lampreys for their *suckers*.

*Admired for their suckers.*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
It also happens to have the [`[LARGE_PREDATOR]`](/index.php/Creature_token#LARGE_PREDATOR "Creature token") tag, despite being half the size of a carp.

Despite being called a sea lamprey, they seem to fare perfectly fine in any body of water.

**Be afraid.**

    35 kph

    [CREATURE:FISH_LAMPREY_SEA]
        [DESCRIPTION:A small oceanic eel-like creature that latches onto the side of its victim and tears into them.]
        [NAME:sea lamprey:sea lampreys:sea lamprey]
        [CASTE_NAME:sea lamprey:sea lampreys:sea lamprey]
        [CHILD:1][GENERAL_CHILD_NAME:larval sea lamprey:larval sea lampreys]
        [CREATURE_TILE:'~'][COLOR:0:0:1]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [LARGE_PREDATOR][NATURAL]
        [PETVALUE:200]
        [BIOME:OCEAN_ARCTIC]
        [BIOME:OCEAN_TEMPERATE]
        [BIOME:RIVER_TEMPERATE_FRESHWATER]
        [BIOME:RIVER_TEMPERATE_BRACKISHWATER]
        [BIOME:RIVER_TEMPERATE_SALTWATER]
        [BIOME:LAKE_TEMPERATE_FRESHWATER]
        [BIOME:LAKE_TEMPERATE_BRACKISHWATER]
        [BIOME:LAKE_TEMPERATE_SALTWATER]
        [POPULATION_NUMBER:15:30]
        [PREFSTRING:suckers]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:TAIL:2EYES:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE]
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
        [BODY_SIZE:0:0:2000]
        [BODY_SIZE:1:0:6000]
        [BODY_SIZE:5:0:20000]
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
            [SPECIALATTACK_SUCK_BLOOD:25:50]
        [ATTACK:SLAP:BODYPART:BY_CATEGORY:TAIL]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:slap:slaps]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ALL_ACTIVE]
        [NO_DRINK]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
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
