# Hippo

> Fonte: [Hippo](https://dwarffortresswiki.org/index.php/Hippo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hippos for their strength.**
- **Biome**
- **Tropical Saltwater River Tropical Brackish River Tropical Freshwater River Tropical Saltwater Lake Tropical Brackish Lake Tropical Freshwater Lake**
- **Variations**
- **Hippo - Hippo man - Giant hippo**
- **Attributes**
- **Amphibious**
- **Tamed Attributes**
- **Pet value:** 400
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50,000 cm 3
- **Mid:** 750,000 cm 3
- **Max:** 1,500,000 cm 3
- **Age**
- **Adult at:** 5
- **Max age:** 40-50
- **Butchering returns**
- **Food items**
- **Meat:** 14-54
- **Fat:** 13-19
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2-4
- **Intestines:** 4-6
- **Liver:** 1-2
- **Kidneys:** 2
- **Tripe:** 1-2
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 21-29
- **Skull:** 1
- **Ivory:** 2-3
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge, round, hairless river creature. It is a plant-eating animal but has long tusks and can be aggressive and deadly if disturbed.*

**Hippos** are large amphibious creatures who can be found in tropical lakes and rivers, where they appear in clusters of 3-7 individuals. They are the largest mundane animals that may be found in freshwater, though unlike in real life, in-game hippos are benign meanderers who will rarely fight back if threatened, though they may potentially be deadly due to their large size and tendency to knock or herd dwarves into rivers. An infant hippo is known as a *hippo calf*.

Hippos can be captured in cage traps and trained into valuable exotic pets. Since they can become very tall and heavy (~ 1.5 tons), they are a great food source when butchered, and also provide ivory. They may also be a great source of occupied coffins. Hippos take 5 years to reach their full size, considerably more than most other animals.

Some dwarves like hippos for their *strength*.

Admired for its *strength*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Some scholars question whether a hippopotamus is a hippopotamus, or just a really cool opotamus.

    [CREATURE:HIPPO]
        [DESCRIPTION:A huge, round, hairless river creature.  It is a plant-eating animal but has long tusks and can be aggressive and deadly if disturbed.]
        [NAME:hippo:hippos:hippo]
        [CASTE_NAME:hippo:hippos:hippo]
        [CHILD:5][GENERAL_CHILD_NAME:hippo calf:hippo calves]
        [CREATURE_TILE:'H'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:400]
        [PET_EXOTIC]
        [AMPHIBIOUS]
        [LARGE_ROAMING]
        [BIOME:RIVER_TROPICAL_SALTWATER]
        [BIOME:RIVER_TROPICAL_BRACKISHWATER]
        [BIOME:RIVER_TROPICAL_FRESHWATER]
        [BIOME:LAKE_TROPICAL_SALTWATER]
        [BIOME:LAKE_TROPICAL_BRACKISHWATER]
        [BIOME:LAKE_TROPICAL_FRESHWATER]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [BENIGN][MEANDERER][NATURAL]
        [PREFSTRING:strength]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:IVORY:TOOTH_TEMPLATE]
                [STATE_NAME:ALL_SOLID:ivory]
                [STATE_ADJ:ALL_SOLID:ivory]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:IVORY:IVORY_TEMPLATE]
                [TISSUE_NAME:ivory:NP]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [SELECT_TISSUE_LAYER:ALL:BY_TOKEN:R_EYE_TOOTH]
         [PLUS_TISSUE_LAYER:ALL:BY_TOKEN:L_EYE_TOOTH]
            [SET_LAYER_TISSUE:IVORY]
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
        [BODY_SIZE:2:0:750000]
        [BODY_SIZE:5:0:1500000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:40:50]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:4732:4026:3327:1097:5922:7567] 8 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
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
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
