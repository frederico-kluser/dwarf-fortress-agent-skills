# Lynx

> Fonte: [Lynx](https://dwarffortresswiki.org/index.php/Lynx) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes lynx for their ear tufts.**
- **Biome**
- **Taiga**
- **Variations**
- **Lynx - Lynx man - Giant lynx**
- **Attributes**
- **War animals · Hunting animals**
- **Tamed Attributes**
- **Pet value:** 75
- **Trainable : Hunting War**
- **Size**
- **Birth:** 2,500 cm 3
- **Mid:** 12,500 cm 3
- **Max:** 25,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 12
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
- **Bones:** 12
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized mammalian predator. It is known by the tell-tale tufts of hair on the tips of its ears.*

**Lynx** are rare and solitary creatures found exclusively in taigas. While carnivorous, their relatively small size (smaller than the average dog) means they're unlikely to confront dwarves, though they may pose a threat to small domestic animals. No more than 3 lynx will exist in a single region before they're locally extinct. Their newborns are called *cubs*, and all members of the species are born with Legendary skill in climbing.

Lynx could be captured in cage traps and trained into exotic pets. They can be further trained into war or hunting beasts, though fall short in utility due to being smaller than dogs, who are much more accessible. While products made from butchered lynx are worth thrice more than those made from common animal parts, their rarity and extremely low numbers make them poor targets for a meat industry. Lynx take 3 years to reach adulthood, far longer than most other animals of comparable size.

Some dwarves like lynx for their *ear tufts*.

Admired for its *ear tufts*.

    12 kph

    Lynx were sponsored by the generous contributions of the Bay 12 community.

        Glowcat
        When you simply can't have a lobster -- veok, the Lobster Rage Fist

    [CREATURE:LYNX]
        [DESCRIPTION:A medium-sized mammalian predator.  It is known by the tell-tale tufts of hair on the tips of its ears.]
        [NAME:lynx:lynx:lynx]
        [CASTE_NAME:lynx:lynx:lynx]
        [CHILD:3][GENERAL_CHILD_NAME:lynx cub:lynx cubs]
        [CREATURE_TILE:'l'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:75]
        [PET_EXOTIC]
        [TRAINABLE]
        [BIOME:FOREST_TAIGA]
        [LARGE_ROAMING][FREQUENCY:5]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CARNIVORE][NATURAL]
        [MEANDERER]
        [GRASSTRAMPLE:0]
        [PREFSTRING:ear tufts]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:4TOES_RQ_REG:MOUTH:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
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
        [BODY_SIZE:0:0:2500]
        [BODY_SIZE:1:0:12500]
        [BODY_SIZE:2:0:25000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:CLAW]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
        [NOCTURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:SPOTS_BROWN_BLACK:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_GREEN-YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
