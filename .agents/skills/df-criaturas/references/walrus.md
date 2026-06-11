# Walrus

> Fonte: [Walrus](https://dwarffortresswiki.org/index.php/Walrus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes walruses for their whiskers.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Walrus - Walrus man - Giant walrus**
- **Attributes**
- **Amphibious**
- **Tamed Attributes**
- **Pet value:** 400
- **Not hunting/war trainable**
- **Size**
- **Birth:** 150,000 cm 3
- **Mid:** 750,000 cm 3
- **Max:** 1,500,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 70
- **Fat:** 10
- **Brain:** 3
- **Heart:** 1
- **Lungs:** 6
- **Intestines:** 10
- **Liver:** 3
- **Kidneys:** 2
- **Tripe:** 3
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 12
- **Skull:** 1
- **Ivory:** 2
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge aquatic mammal with giant tusks and dense whiskers. They are thick and blubbery and live almost exclusively on mussels.*

**Walruses** are amphibious creatures who can be found in arctic oceans, in groups of 3-7 individuals. They are 25 times the size of a dwarf but are shy and benign, preferring to flee from attackers than try and fight them, which makes them relatively easy prey for a hunter. In the event they do fight back, a walrus will defend itself by attempting to stab the enemy with their tusks. An infant walrus is called a *walrus calf*.

Walruses can be captured in cage traps and trained into valuable pets. Because of their large size and fairly long lifespan, they can serve as a good source of exotic livestock in a meat industry, with their tusks serving as a source of ivory. If you try and breed them, note that it takes a walrus five years to reach its full size, considerably longer than most domestic animals.

Some dwarves like walruses for their *tusks* and their *whiskers*.

Admired for their *tusks*.

### Lore

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
It is rumored that eggmen can be sometimes found near walruses. This, however, is yet to be confirmed for DF.

Some dwarven scientists also suggest that walruses' mortal enemies are the red-headed woodpeckers, as these birds will frequently steal their food, destroy their homes, and even go so far as to not let a walrus get a single minute of sleep. The reason for such behavior is still a mystery.

You should never obey the walrus, whichever elf said that should have Armok smite them.

    [CREATURE:WALRUS]
        [DESCRIPTION:A huge aquatic mammal with giant tusks and dense whiskers.  They are thick and blubbery and live almost exclusively on mussels.]
        [NAME:walrus:walruses:walrus]
        [CASTE_NAME:walrus:walruses:walrus]
        [CHILD:1][GENERAL_CHILD_NAME:walrus calf:walrus calves]
        [CREATURE_TILE:'W'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:400]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [AMPHIBIOUS][UNDERSWIM]
        [BIOME:OCEAN_ARCTIC]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [BENIGN][MEANDERER][NATURAL]
        [PREFSTRING:tusks]
        [PREFSTRING:whiskers]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD_NECK:FRONT_BODY_FLIPPERS:REAR_BODY_FLIPPERS:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:2TUSKS:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:IVORY:TOOTH_TEMPLATE]
                [STATE_NAME:ALL_SOLID:ivory]
                [STATE_ADJ:ALL_SOLID:ivory]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:IVORY:IVORY_TEMPLATE]
                [TISSUE_NAME:ivory:NP]
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
        [BODY_SIZE:0:0:150000]
        [BODY_SIZE:2:0:750000]
        [BODY_SIZE:5:0:1500000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [APPLY_CREATURE_VARIATION:TUSK_STAB_ATTACK]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:691:482:251:1900:2900] 35 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_GRAY:1]
                    [TLCM_NOUN:eyes:PLURAL]
