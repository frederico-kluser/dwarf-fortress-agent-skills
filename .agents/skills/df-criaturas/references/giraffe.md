# Giraffe

> Fonte: [Giraffe](https://dwarffortresswiki.org/index.php/Giraffe) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giraffes for their long necks.**
- **Biome**
- **Tropical Savanna Tropical Shrubland**
- **Variations**
- **Giraffe - Giraffe man - Giant giraffe**
- **Attributes**
- **Grazer · Exotic mount · Horn**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 100,000 cm 3
- **Mid:** 500,000 cm 3
- **Max:** 1,000,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 25-30
- **Butchering returns ( Value multiplier ×5)**
- **Food items**
- **Meat:** 21-31
- **Fat:** 13
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
- **Bones:** 20-24
- **Skull:** 1
- **Horns:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge leaf-eating mammal. It has an extremely long neck. Its skin has a distinctive brown and white pattern.*

**Giraffes** are huge animals found in tropical savannas and shrublands, where they appear in herds of 3-7 individuals. They're over 16 times heavier than the average dwarf, but are generally benign and timid creatures who flee rather than fight, but if they do fight, their large size can allow them to easily dispatch a lone hunter who ventures too close; in combat, their hooves and mass make a good natural weapon. A new born giraffe is called a *calf*.

Giraffes can be captured in cage traps and trained into valuable exotic pets. Their large size means they provide great amounts of returns when butchered, making them good targets for a meat industry. Products made from giraffe parts are worth 5 times more than those made from common animals. They take 10 years to reach adulthood, but are fully grown by the age of 5. When trained, giraffes become grazers, and as such they'll require a constant source of grass to survive; tree browsing has yet to be implemented, so giraffes will not deforest your surroundings, though the ability for them to browse trees is a planned feature. Giraffes are mounts and may be used against you during sieges, in which case, their large size will truly become a problem to your fortress.

Due to an error, giraffes walk far slower than they can stroll. Their strolling speed is equal to 60 kph, much greater than either their trot or canter speed. As a consequence, giraffes are very difficult to chase, as they will never get tired from maintaining this speed. They may also sneak at this speed without suffering penalty to their stealth, but will likely never abuse this in game.

Some dwarves like giraffes for their *long necks*.

Admired for their *long necks*

    1 kph

    [CREATURE:GIRAFFE]
        [DESCRIPTION:A huge leaf-eating mammal.  It has an extremely long neck.  Its skin has a distinctive brown and white pattern.]
        [NAME:giraffe:giraffes:giraffe]
        [CASTE_NAME:giraffe:giraffes:giraffe]
        [CHILD:10][GENERAL_CHILD_NAME:giraffe calf:giraffe calves]
        [CREATURE_TILE:'G'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:500]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [STANDARD_GRAZER] no tree browsing yet
        [VISION_ARC:50:310]
        [LARGE_ROAMING]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [BENIGN][MEANDERER][NATURAL]
        [PREFSTRING:long necks]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE:2HEAD_HORN]
        [RELSIZE:BY_CATEGORY:NECK:1000]
        [RELSIZE:BY_CATEGORY:HEAD:150]
        [RELSIZE:BY_CATEGORY:HORN:30]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
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
        [BODY_SIZE:0:0:100000]
        [BODY_SIZE:2:0:500000]
        [BODY_SIZE:5:0:1000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:25:30]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [DIURNAL]
        [HOMEOTHERM:10066]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:438:292:146:1900:2900] 60 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:STRIPES_BROWN_WHITE:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1:IRIS_EYE_GOLD:1:IRIS_EYE_YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:5]
