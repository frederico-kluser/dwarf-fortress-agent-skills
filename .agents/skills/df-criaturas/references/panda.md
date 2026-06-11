# Panda

> Fonte: [Panda](https://dwarffortresswiki.org/index.php/Panda) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes pandas for their lazy nature.**
- **Biome**
- **Any Temperate Forest**
- **Variations**
- **Panda - Panda man - Gigantic panda**
- **Attributes**
- **Grazer**
- **Tamed Attributes**
- **Pet value:** 300
- **Not hunting/war trainable**
- **Size**
- **Birth:** 150 cm 3
- **Mid:** 65,000 cm 3
- **Max:** 130,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×2)**
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
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For the much smaller red animal, see Red panda.*

*A large bear-like creature with a striking coat of black and white hair. It feeds on bamboo forests.*

**Pandas** are large mammals found roaming alone through temperate forests. They are noted for their distinctive black and white coloration, and their dependence upon bamboo; they will only appear in areas where bamboo grows, as its serves as their exclusive diet. Pandas are fairly docile and will generally run away from dwarves, but they aren't entirely benign and will defend themselves if threatened. They are large enough to cause significant damage or even kill an unarmed peasant.

Pandas can be captured in cage traps and trained into fairly valuable pets. A trained or tame panda must be pastured in a patch of bamboo (they won't eat any other kind of grass), otherwise they will die of starvation. The elves will not bother to mention this detail to you when they bring pandas for trade. They can be kept as livestock and bred for a meat industry, however their dietary requirements will necessitate excessive micromanagement. Their butchering returns are twice as valuable as common critters, but there are many easier and more lucrative options for livestock.

In real life, the species is known as the "giant panda", but in-game they are referred to as simply pandas in order to better distinguish them from their savage counterparts.

Some dwarves like pandas for their *striking coloration*, their *big fluffy heads and bellies* and their *lazy nature*.

\

Admired for its *striking coloration*.

    5 kph

    Pandas were sponsored by the generous contributions of the Bay 12 community.

        I bring pandamonium!
        Vorpal
        Ian
        "If you can't do something fast, do it half-fast." Gwen <3 Mike
        Masaka

    [CREATURE:PANDA]
        [DESCRIPTION:A large bear-like creature with a striking coat of black and white hair.  It feeds on bamboo forests.]
        [NAME:panda:pandas:panda]
        [CASTE_NAME:panda:pandas:panda]
        [CHILD:1][GENERAL_CHILD_NAME:panda cub:panda cubs]
        [CREATURE_TILE:'P'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:300]
        [PET]
        [NATURAL]
        [STANDARD_GRAZER]
        [SPECIFIC_FOOD:PLANT:BAMBOO, ARROW]
        [SPECIFIC_FOOD:PLANT:BAMBOO, GOLDEN]
        [SPECIFIC_FOOD:PLANT:BAMBOO, HEDGE]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [BIOME:ANY_TEMPERATE_FOREST]
        [GRASSTRAMPLE:0]
        [MEANDERER]
        [PREFSTRING:striking coloration]
        [PREFSTRING:big fluffy heads and bellies]
        [PREFSTRING:lazy nature]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:200]
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
        [BODY_SIZE:0:0:150] small!
        [BODY_SIZE:1:0:65000]
        [BODY_SIZE:2:0:130000]
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
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [CREPUSCULAR][NOCTURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:2728:2069:1409:675:4000:5700] 13 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:hair around the eyes:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EAR:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:ears:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_REAR:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:FOOT_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:FOOT_REAR:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:TOE:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:legs:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:HAIR]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:upper body:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:TAIL:HAIR]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:other hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:PINK:1] gray under the black parts I guess, but don't want to spoil descriptions with that
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1] have seen various musings on this, but don't have anything solid, and no good pics
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
