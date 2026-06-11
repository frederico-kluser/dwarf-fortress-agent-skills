# Tapir

> Fonte: [Tapir](https://dwarffortresswiki.org/index.php/Tapir) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes tapirs for their floppy noses.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Tapir - Tapir man - Giant tapir**
- **Attributes**
- **Grazer · Milkable**
- **Tamed Attributes**
- **Pet value:** 200
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20,000 cm 3
- **Mid:** 100,000 cm 3
- **Max:** 200,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 25-30
- **Butchering returns**
- **Food items**
- **Meat:** 13
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
- **Bones:** 18
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized mammal with a prehensile nose. It lives in the tropical rainforest.*

**Tapirs** are creatures who inhabit tropical moist broadleaf forests. Weighing over three times more than a dwarf, they spawn individually and meander the area, paying no mind to other creatures. Tapirs are benign herbivores and will flee from attackers, but if cornered they may attempt to defend themselves with kicks and bites. In adventurer mode, they are more easily sighted at twilight and at night. A baby tapir is called a *tapir calf*.

Tapirs can be captured in cage traps and trained into pets of respectable value. They are grazers and therefore require a pasture to survive after being trained, but are distinct for being one of the only exotic sources of milk and cheese (the other being the kangaroo). Because of their size, they produce a good amount of returns when butchered, making the idea of a tapir farm an attractive one for the long term. Tapirs reach their full size at 2 years of age and therefore should be butchered at that point for maximum returns.

Some dwarves like tapirs for their *floppy noses*.

\

Admired for their *floppy noses*.

    1 kph

    Tapirs were sponsored by the generous contributions of the Bay 12 community.

        Samthere - Release the war tapirs!

    [CREATURE:TAPIR]
        [DESCRIPTION:A medium-sized mammal with a prehensile nose.  It lives in the tropical rainforest.]
        [NAME:tapir:tapirs:tapir]
        [CASTE_NAME:tapir:tapirs:tapir]
        [CHILD:1][GENERAL_CHILD_NAME:tapir calf:tapir calves]
        [CREATURE_TILE:'T'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [PETVALUE:200]
        [VISION_ARC:50:310]
        [PREFSTRING:floppy noses]
        [LARGE_ROAMING]
        [BENIGN][MEANDERER][PET_EXOTIC]
        [STANDARD_GRAZER]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:3TOES_RQ_REG:MOUTH:GENERIC_TEETH:RIBCAGE]
        [NATURAL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
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
        [BODY_SIZE:0:0:20000]
        [BODY_SIZE:1:0:100000]
        [BODY_SIZE:2:0:200000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:25:30]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_REAR]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:SECOND]
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
        [NOCTURNAL]
        [CREPUSCULAR]
        [HOMEOTHERM:10068]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:703:505:274:1900:2900] 32 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [TRADE_CAPACITY:1500]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [USE_MATERIAL_TEMPLATE:MILK:MILK_TEMPLATE]
                [STATE_NAME:ALL_SOLID:frozen tapir's milk]
                [STATE_ADJ:ALL_SOLID:frozen tapir's milk]
                [STATE_NAME:LIQUID:tapir's milk]
                [STATE_ADJ:LIQUID:tapir's milk]
                [STATE_NAME:GAS:boiling tapir's milk]
                [STATE_ADJ:GAS:boiling tapir's milk]
                [PREFIX:NONE]
            [MILKABLE:LOCAL_CREATURE_MAT:MILK:20000]
            [USE_MATERIAL_TEMPLATE:CHEESE:CREATURE_CHEESE_TEMPLATE]
                [STATE_NAME:SOLID:tapir cheese]
                [STATE_ADJ:SOLID:tapir cheese]
                [STATE_NAME:SOLID_POWDER:tapir cheese powder]
                [STATE_ADJ:SOLID_POWDER:tapir cheese powder]
                [STATE_NAME:LIQUID:melted tapir cheese]
                [STATE_ADJ:LIQUID:melted tapir cheese]
                [STATE_NAME:GAS:boiling tapir cheese]
                [STATE_ADJ:GAS:boiling tapir cheese]
                [PREFIX:NONE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1] work needed
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
