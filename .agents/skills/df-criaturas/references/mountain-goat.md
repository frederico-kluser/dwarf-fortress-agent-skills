# Mountain goat

> Fonte: [Mountain goat](https://dwarffortresswiki.org/index.php/Mountain_goat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mountain goats for their surefootedness.**
- **Biome**
- **Mountain**
- **Variations**
- **Mountain goat - Mountain goat man - Giant mountain goat**
- **Attributes**
- **Grazer · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 5,000 cm 3
- **Mid:** 10,000 cm 3
- **Max:** 50,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 9
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
- **Bones:** 9
- **Skull:** 1
- **Horns:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized herbivore that lives in the high mountains, able to navigate the slopes despite its hooved feet.*

**Mountain goats** are wild animals who may be found inhabiting mountains. They appear in groups of 1-4 individuals and meander around the area, minding their own business. They are benign and will normally flee from dwarves, but may rarely defend themselves with bites and kicks. A baby mountain goat is called a *mountain goat kid*.

Mountain goats may be captured in cage traps and trained into pets. In terms of size and value, mountain goats are identical to common goats and as such perform the same way in a meat industry, though unlike their domesticated cousins, they don't produce milk. Like domestic goats, a trained mountain goat will require a pasture to survive.

Some dwarves like mountain goats for their *beards*, their *long horns* and their *surefootedness*.

## In real life

Despite the name (and similarity in *Dwarf Fortress*), mountain goats are not true goats (members of the genus Capra). Instead, they are a more distant relative on par with the sheep and the muskox.

Admired for their *beards*.

\

|  |
|----|
| "Mountain goat" in other / Languages / Dwarven / : / onol belbez / Elven / : / thele efafi / Goblin / : / ngosla orang / Human / : / thakom apsong |

    [CREATURE:GOAT_MOUNTAIN]
        [DESCRIPTION:A medium-sized herbivore that lives in the high mountains, able to navigate the slopes despite its hooved feet.]
        [NAME:mountain goat:mountain goats:mountain goat]
        [CASTE_NAME:mountain goat:mountain goats:mountain goat]
        [GENERAL_CHILD_NAME:mountain goat kid:mountain goat kids]
        [CREATURE_TILE:'g'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PREFSTRING:beards]
        [PREFSTRING:long horns]
        [PREFSTRING:surefootedness]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:4]
        [GRASSTRAMPLE:0]
        [BIOME:MOUNTAIN]
        [BENIGN][MEANDERER]
        [PETVALUE:50]
        [VISION_ARC:50:310]
        [PET]
        [STANDARD_GRAZER]
        [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:2HEAD_HORN:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        [NATURAL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:200]
            [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
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
        [BODY_SIZE:0:0:5000]
        [BODY_SIZE:1:0:10000]
        [BODY_SIZE:2:0:50000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
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
        [CHILD:1]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
