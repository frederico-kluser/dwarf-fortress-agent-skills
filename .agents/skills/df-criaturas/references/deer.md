# Deer

> Fonte: [Deer](https://dwarffortresswiki.org/index.php/Deer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes deer for their grace.**
- **Biome**
- **Taiga Any Temperate Forest**
- **Variations**
- **Deer - Deer man - Giant deer**
- **Attributes**
- **Grazer · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 14,000 cm 3
- **Mid:** 70,000 cm 3
- **Max:** 140,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 10
- **Fat:** 9
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
- **Bones:** 13
- **Skull:** 1
- **Hooves:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized hoofed forest creature that grows its antlers back each year.*

**Deer** are animals who can be found in temperate forests and taigas, where they appear in groups of 1-4 individuals. Benign and herbivorous, they do little but meander about aimlessly through your surroundings, fleeing from any dwarf who attempts to confront them and only rarely fighting back. Male deer are distinct for possessing a pair of antlers that can be used for a gore attack, which the females lack entirely. Newborn deer are called *fawns*.

Deer can be captured in cage traps and trained into exotic pets. Being a bit over twice the size of a dwarf, they provide a fair amount of returns when butchered, making them a choice for a meat industry. They're grazing animals after being trained, and as such require a pasture in order to not die of starvation.

Some dwarves like deer for their *grace*.

|  |
|----|
| "Deer" in other / Languages / Dwarven / : / kizbiz / Elven / : / liyìÿi / Goblin / : / unes / Human / : / keth |

Admired for its *grace*.

    12 kph

    [CREATURE:DEER]
        [DESCRIPTION:A medium-sized hoofed forest creature that grows its antlers back each year.]
        [NAME:deer:deer:deer]
        [CASTE_NAME:deer:deer:deer]
        [CHILD:1][GENERAL_CHILD_NAME:deer fawn:deer fawns]
        [CREATURE_TILE:'D'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:50]
        [STANDARD_GRAZER]
        [PREFSTRING:grace]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [BIOME:FOREST_TAIGA]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BENIGN][MEANDERER][NATURAL][PET_EXOTIC]
        [VISION_ARC:50:310]  This is the binocular and non-binocular vision arcs.
        [MAXAGE:20:30]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:411:274:137:1900:2900] 64 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        [CASTE:MALE]
            [MALE]
        [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE:2HEAD_ANTLER]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
            [ATTACK:HGORE:BODYPART:BY_CATEGORY:HORN]
                [ATTACK_SKILL:BITE]
                [ATTACK_VERB:gore:gores]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PREPARE_AND_RECOVER:3:3]
                [ATTACK_FLAG_WITH]
                [ATTACK_PRIORITY:MAIN]
        [SELECT_CASTE:ALL]
            [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_FRONT]
                [ATTACK_SKILL:STANCE_STRIKE]
                [ATTACK_VERB:kick:kicks]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PREPARE_AND_RECOVER:4:4]
                [ATTACK_PRIORITY:MAIN]
                [ATTACK_FLAG_WITH]
                [ATTACK_FLAG_BAD_MULTIATTACK]
            [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_REAR]
                [ATTACK_SKILL:STANCE_STRIKE]
                [ATTACK_VERB:kick:kicks]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PREPARE_AND_RECOVER:4:4]
                [ATTACK_PRIORITY:MAIN]
                [ATTACK_FLAG_WITH]
                [ATTACK_FLAG_BAD_MULTIATTACK]
            [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
                [ATTACK_SKILL:BITE]
                [ATTACK_VERB:bite:bites]
                [ATTACK_CONTACT_PERC:100]
                [ATTACK_PENETRATION_PERC:100]
                [ATTACK_FLAG_EDGE]
                [ATTACK_PREPARE_AND_RECOVER:3:3]
                [ATTACK_PRIORITY:SECOND]
                [ATTACK_FLAG_CANLATCH]
            [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
                [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
                [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
                    [STATE_NAME:ALL_SOLID:antler]
                    [STATE_ADJ:ALL_SOLID:antler]
                    [ANTLER]
            [BODY_DETAIL_PLAN:STANDARD_TISSUES]
                [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
                [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
                    [TISSUE_NAME:antler:NP]
            [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
            [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
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
            [BODY_SIZE:0:0:14000]
            [BODY_SIZE:1:0:70000]
            [BODY_SIZE:2:0:140000]
            [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
            [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
            [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
