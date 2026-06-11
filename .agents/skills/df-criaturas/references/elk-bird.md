# Elk bird

> Fonte: [Elk bird](https://dwarffortresswiki.org/index.php/Elk_bird) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes elk birds for their elegant horns.**
- **Biome**
- **Underground Depth: 1-3**
- **Attributes**
- **Grazer · Exotic mount · Horn · Egglaying**
- **Tamed Attributes**
- **Pet value:** 400
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50 cm 3
- **Mid:** 50,000 cm 3
- **Max:** 100,000 cm 3
- **Food products**
- **Eggs:** 2-10
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 16
- **Fat:** 10
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 23
- **Skull:** 1
- **Horns:** 2
- **Skin:** Raw hide
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large creature found grazing on mushrooms deep underground. It walks on two legs and has the head of a bird with the antlers of a great elk.*

**Elk birds** are large flightless birds who are among the most common creatures found in caverns, rivaled only by crundles. Though they are generally non-hostile, they will interrupt tasks throughout the fortress and, if engaged, will usually kill an untrained dwarf (or even a war dog) in one-on-one combat. They can also be used as mounts by goblin siegers.

In addition to their meat, bones, organs, etc., elk birds will also produce a single feather and a gizzard stone when butchered. They are one of the more common creatures that leave gizzard stones. Unlike elk, both genders of elk bird have horns. This is nice, because elk bird parts are worth even more than elk parts, with a value multiplier of three.

Trained elk birds require a pasture to survive; despite the description, they can feed on any grass. They are notoriously difficult to breed, as an elk bird hen will starve herself to death rather than abandon her nest box. A well-fed hen can hatch one clutch of eggs before being returned to a nest-box-less pasture to graze; however, infertile eggs or multiple clutches in a row are still problematic.Bug:4637 As an alternative to pasture, they can be chained and then fed by idle dwarves with the animal caretaker labor enabled. They can't be spawned in the object testing arena.

Some dwarves like elk birds for their *elegant horns*.

## Gallery

-

  An elk bird hatchling, drawn in crayon by Bay 12 Games

-

  *Art by Quinmael*

-

  "Mushroom grazer, bird-like."\
  *Concept art by Bay 12 Games.*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some dwarves claim to have seen baby elk hatchling start to become extremely aggressive when their parents were killed. They seem to have a special self defense maneuver where they spin so fast that they turned into a whirlwind. Then, they charge at their enemy ferociously and then start slapping their enemy rapidly with their wings until they turned into an unrecognizable mass. However, after 10 days of experimenting by ramming the elk bird parents with minecarts filled with spike balls, ironically, the elk bird did not seem to care at all of their parent's brutal death and continues to munch on their cave fungus as if nothing happened. Thus, another rumor has been busted by the dwarven scientists.

\

    [CREATURE:ELK_BIRD]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A large creature found grazing on mushrooms deep underground.  It walks on two legs and has the head of a bird with the antlers of a great elk.]
        [NAME:elk bird:elk birds:elk bird]
        [CASTE_NAME:elk bird:elk birds:elk bird]
        [GENERAL_CHILD_NAME:elk bird hatchling:elk bird hatchlings]
        [CREATURE_TILE:'E'][COLOR:6:0:0]
        [POPULATION_NUMBER:25:50]
        [CLUSTER_NUMBER:5:10]
        [NATURAL]
        [LARGE_ROAMING]
        [BENIGN]
        [PETVALUE:400]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [STANDARD_GRAZER]
        [CHILD:1]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:3]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [PREFSTRING:elegant horns]
        [BODY:HUMANOID_ARMLESS_NECK:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:TONGUE:RIBCAGE:2HEAD_ANTLER]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
                [STATE_NAME:ALL_SOLID:antler]
                [STATE_ADJ:ALL_SOLID:antler]
                [ANTLER]
            [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
                [TISSUE_NAME:antler:NP]
            [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS:FEATHER]
        [USE_MATERIAL_TEMPLATE:TALON:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:TALON:TALON_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:TALON:FRONT]
        [BODY_DETAIL_PLAN:EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [EXTRA_BUTCHER_OBJECT:BY_CATEGORY:GIZZARD]
            [EBO_ITEM:SMALLGEM:NONE:ANY_HARD_STONE]
            [EBO_SHAPE:GIZZARD_STONE]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:50]
        [BODY_SIZE:1:0:50000]
        [BODY_SIZE:2:0:100000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:TALON]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:snatch at:snatches at]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:60]
                [CLUTCH_SIZE:2:10]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
