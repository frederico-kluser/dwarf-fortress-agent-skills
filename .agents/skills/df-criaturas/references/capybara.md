# Capybara

> Fonte: [Capybara](https://dwarffortresswiki.org/index.php/Capybara) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes capybaras for their graceful swimming.**
- **Biome**
- **Any Wetland**
- **Variations**
- **Capybara - Capybara man - Giant capybara**
- **Attributes**
- **Amphibious · Grazer**
- **Tamed Attributes**
- **Pet value:** 100
- **Not hunting/war trainable**
- **Size**
- **Birth:** 4,500 cm 3
- **Mid:** 22,500 cm 3
- **Max:** 45,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-12
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 11
- **Fat:** 11
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
- **Bones:** 11
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized semi-aquatic rodent. It lives in large herds and barks when alarmed.*

**Capybaras** are amphibious creatures who can be found in wetlands, appearing in groups of anywhere between 5-10 individuals. Smaller than dwarves, they aren't entirely benign but will rarely pose a threat to civilians, preferring to avoid confrontation if possible (however they will attack pet dogs and the like, and even can gain a name from their kills out in your pastures). They hold the distinction of being one of the few creatures who emit noises in adventurer mode (alongside the kakapo), with the game describing their whistling, barks, clicks, grunts and purrs as you approach them. A newborn capybara is called a *pup*.

Capybaras can be captured in cage traps and tamed into pets. Given their large cluster numbers, capturing a large number of them is relatively easy, and they provide a good amount of returns when butchered, making them acceptable targets for a meat industry. Note that tamed capybaras are grazers, and therefore require a pasture to survive. Products made from capybara parts are worth twice more than those made out of common domestic animals.

Some dwarves like capybaras for their *enormous rodentness*, their *graceful swimming*, or their *resonant barking*.

Admired for its *enormous rodentness*

    Capybaras were sponsored by the generous contributions of the Bay 12 community.

        Speak!
        DrVoke
        happybara
        Izzy
        Rokoko
        Cameo

    [CREATURE:CAPYBARA]
        [DESCRIPTION:A medium-sized semi-aquatic rodent.  It lives in large herds and barks when alarmed.]
        [NAME:capybara:capybaras:capybara]
        [CASTE_NAME:capybara:capybaras:capybara]
        [CHILD:1][GENERAL_CHILD_NAME:capybara pup:capybara pups]
        [CREATURE_TILE:'c'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:100]
        [PET]
        [NATURAL]
        [STANDARD_GRAZER]
        [AMPHIBIOUS]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:20:30]
        [CLUSTER_NUMBER:5:10]
        [BIOME:ANY_WETLAND]
        [GRASSTRAMPLE:0]
        [MEANDERER]
        [VISION_ARC:50:310]
        [SOUND:ALERT:100:1000:VOCALIZATION:bark:barks:a loud bark]
        [SOUND:PEACEFUL_INTERMITTENT:100:10000:VOCALIZATION:whistle:whistles:whistling]
        [SOUND:PEACEFUL_INTERMITTENT:25:10000:VOCALIZATION:grunt:grunts:a grunt]
        [SOUND:PEACEFUL_INTERMITTENT:5:10000:VOCALIZATION:purr:purrs:a purr]
        [SOUND:PEACEFUL_INTERMITTENT:25:10000:NONE:click:clicks:a click]
        [PREFSTRING:enormous rodentness]
        [PREFSTRING:graceful swimming]
        [PREFSTRING:resonant barking]
        [BODY:QUADRUPED_NECK:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:3TOES_RQ_REG:MOUTH:TONGUE:RODENT_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
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
        [BODY_SIZE:0:0:4500]
        [BODY_SIZE:1:0:22500]
        [BODY_SIZE:2:0:45000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:12]
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
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:LIGHT_BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:DARK_PINK:1] need more info
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_DARK_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
