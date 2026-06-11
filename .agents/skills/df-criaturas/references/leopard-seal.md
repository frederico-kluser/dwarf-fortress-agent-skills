# Leopard seal

> Fonte: [Leopard seal](https://dwarffortresswiki.org/index.php/Leopard_seal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes leopard seals for their fierce nature.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Leopard seal - Leopard seal man - Giant leopard seal**
- **Attributes**
- **Amphibious**
- **Tamed Attributes**
- **Pet value:** 350
- **Not hunting/war trainable**
- **Size**
- **Birth:** 40,000 cm 3
- **Mid:** 200,000 cm 3
- **Max:** 400,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 12-16
- **Fat:** 7
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2-3
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 13
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large predatory amphibious mammal. It is difficult to evade once in the water.*

**Leopard seals** are amphibious creatures who can be found in arctic oceans. They appear one at a time and do little but either swim or wander around the coast. They are over six times the size of a dwarf but are shy and benign, preferring to flee from attackers than try and fight them, which makes them easy prey for a hunter. In the event they do fight back, a leopard seal will defend itself solely with bites. An infant leopard seal is called a *leopard seal pup*.

Leopard seals can be captured in cage traps and trained into fairly valuable pets. Because of their size and fairly long lifespan, they can serve as a good source of exotic livestock in a meat industry. If you try and breed them, note that it takes a leopard seal five years to reach its full size, considerably longer than most domestic animals.

Some dwarves like leopard seals for their *fierce nature*.

|  |
|----|
| "Leopard seal" in other / Languages / Dwarven / : / mingkil gembish / Elven / : / icemì ricote / Goblin / : / utol uzbad / Human / : / upur epo |

Admired for its *fierce nature*.

    1 kph

    Leopard seals were sponsored by the generous contributions of the Bay 12 community.

        heph

    [CREATURE:LEOPARD_SEAL]
        [DESCRIPTION:A large predatory amphibious mammal.  It is difficult to evade once in the water.]
        [NAME:leopard seal:leopard seals:leopard seal]
        [CASTE_NAME:leopard seal:leopard seals:leopard seal]
        [CHILD:1][GENERAL_CHILD_NAME:leopard seal pup:leopard seal pups]
        [CREATURE_TILE:'L'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:350]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [AMPHIBIOUS][UNDERSWIM]
        [BIOME:OCEAN_ARCTIC]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [BENIGN][NATURAL]
        [PREFSTRING:fierce nature]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD_NECK:FRONT_BODY_FLIPPERS:REAR_BODY_FLIPPERS:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
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
        [BODY_SIZE:0:0:40000]
        [BODY_SIZE:2:0:200000]
        [BODY_SIZE:5:0:400000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:734:568:366:1900:2900] 24 kph
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
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_GRAY:1]
                    [TLCM_NOUN:eyes:PLURAL]
