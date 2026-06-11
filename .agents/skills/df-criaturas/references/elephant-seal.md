# Elephant seal

> Fonte: [Elephant seal](https://dwarffortresswiki.org/index.php/Elephant_seal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes elephant seals for their great size.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Elephant seal - Elephant seal man - Giant elephant seal**
- **Attributes**
- **Amphibious**
- **Tamed Attributes**
- **Pet value:** 400
- **Not hunting/war trainable**
- **Size**
- **Birth:** 300,000 cm 3
- **Mid:** 1,500,000 cm 3
- **Max:** 3,000,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 22-107
- **Fat:** 8-21
- **Brain:** 1-8
- **Heart:** 1-4
- **Lungs:** 2-16
- **Intestines:** 5-26
- **Liver:** 1-8
- **Kidneys:** 2-8
- **Tripe:** 1-8
- **Sweetbread:** 1-4
- **Eyes:** 2
- **Spleen:** 1-4
- **Raw materials**
- **Bones:** 13-26
- **Skull:** 1
- **Teeth:** 0-1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large, predatory marine mammal.*

**Elephant seals** are amphibious mammals significantly larger than common domestic livestock (2-5 times the size of a standard cow). They inhabit arctic oceans in groups of 5-10, living both on the surface of the ice and in the water underneath it.

Elephant seals can be trained and kept as pets, but their real value lies in their butchering returns. By breeding elephant seals, your meat industry can sustain your entire fortress with food to spare. Note, however, that it takes five years for elephant seal pups to reach full adult size.

Unlike most animals, there is a significant size difference between the sexes of elephant seals. Males grow to more than three times the size of females, resulting in large variances in butchering returns. Only the males will drop a tooth when butchered.

Some dwarves like elephant seals for their *large floppy noses* and their *great size*.

Male and female elephant seals; admired for their *large floppy noses* and their *great size*.

    30 kph

    Elephant seals were sponsored by the generous contributions of the Bay 12 community.

        Cruxador

    [CREATURE:ELEPHANT_SEAL]
        [DESCRIPTION:A large, predatory marine mammal.]
        [NAME:elephant seal:elephant seals:elephant seal]
        [CASTE_NAME:elephant seal:elephant seals:elephant seal]
        [CHILD:1][GENERAL_CHILD_NAME:elephant seal pup:elephant seal pups]
        [CREATURE_TILE:'S'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:400]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [AMPHIBIOUS][UNDERSWIM]
        [BIOME:OCEAN_ARCTIC]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [BENIGN][MEANDERER][NATURAL]
        [PREFSTRING:large floppy noses]
        [PREFSTRING:great size]
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
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:25]
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
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:1945:1504:1062:548:3100:4500] 16 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [BODY_SIZE:0:0:91000]
        [BODY_SIZE:2:0:455000]
        [BODY_SIZE:5:0:910000]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [BODY_SIZE:0:0:300000]
        [BODY_SIZE:2:0:1500000]
        [BODY_SIZE:5:0:3000000]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_GRAY:1]
                    [TLCM_NOUN:eyes:PLURAL]
