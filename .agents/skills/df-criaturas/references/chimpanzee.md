# Chimpanzee

> Fonte: [Chimpanzee](https://dwarffortresswiki.org/index.php/Chimpanzee) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes chimpanzees for their antics.**
- **Biome**
- **Tropical Moist Broadleaf Forest Tropical Shrubland**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 10,000 cm 3
- **Mid:** 25,000 cm 3
- **Max:** 50,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 40-80
- **Butchering returns**
- **Food items**
- **Meat:** 12-13
- **Fat:** 12
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
- **Bones:** 10
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large ape which lives in the tropical forests. It lives in complex social groups of many members. Though it is quite intelligent, it has been known for ferocious attacks.*

**Chimpanzees** are social animals rarely found in tropical forest biomes that visit your fortress in clusters of 5-10 individuals, who are virtually identical to bonobos. Chimpanzees have a good pet value of 500, and can be trained with an animal trainer; this makes capturing and taming them a desirable activity. They can live up to eighty years, so a dwarf that takes a chimpanzee as a pet will have it a long time. Young chimpanzees only take two years to reach full size, but require a full ten years to reach adulthood. Chimpanzees are all born with Legendary skill in climbing.

Chimpanzees are benign meanderers and will rarely start fights on their own, but if cornered or enraged, they may fight back against dwarves. In combat they can be dangerous when in a group: an unarmed peasant will usually prevail over a solitary chimpanzee, but generally falls to two or more. Usually, there are two or more. Simple solution: don't send out unarmed peasants to fight chimpanzees raw, unless they really deserve it. Chimpanzees are some of the only wild animals in the game who aren't innate swimmers, and as such they'll likely drown if pushed into a body of water.

Some dwarves like chimpanzees for their *antics*.

Admired for its *antics*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Seeing as there are so many animal men in the world, dwarves debate on the whereabouts of the mythical chimpanzee man. Some scholars suggest it may be the true name of the human race, though they don't appreciate being told that up-front.

For the other small, screeching ape-creature who bites and scratches people, see goblins.

    1 kph

    [CREATURE:CHIMPANZEE]
        [DESCRIPTION:A large ape which lives in the tropical forests.  It lives in complex social groups of many members.  Though it is quite intelligent, it has been known for ferocious attacks.]
        [NAME:chimpanzee:chimpanzees:chimpanzee]
        [CASTE_NAME:chimpanzee:chimpanzees:chimpanzee]
        [CREATURE_TILE:'c'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [CREATURE_CLASS:HUMANOID_TRACKING_SYMBOL]
        [PETVALUE:500]
        [PET_EXOTIC]
        [NATURAL]
        [BENIGN][MEANDERER]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING][FREQUENCY:5]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:5:10]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [BIOME:SHRUBLAND_TROPICAL]
        [PREFSTRING:antics]
        [BODY:QUADRUPED_NECK_FRONT_GRASP:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:5TOES_FQ_FINGERS:5TOES_RQ_ANON:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE:FACIAL_FEATURES]
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
        [BODY_SIZE:0:0:10000]
        [BODY_SIZE:1:0:25000]
        [BODY_SIZE:2:0:50000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:40:80]
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
        [CHILD:10]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_LEARNED]
        [MUNDANE]
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
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
