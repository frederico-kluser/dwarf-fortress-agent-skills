# Cavy

> Fonte: [Cavy](https://dwarffortresswiki.org/index.php/Cavy) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cavies for their three toes.**
- **Biome**
- **Tropical Shrubland Tropical Savanna Tropical Grassland Domesticated**
- **Attributes**
- **Grazer**
- **Tamed Attributes**
- **Pet value:** 3
- **Not hunting/war trainable**
- **Size**
- **Birth:** 80 cm 3
- **Mid:** 400 cm 3
- **Max:** 800 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 4-8
- **Butchering returns**
- **Food items**
- **Raw materials**
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small rodent with no tail. It can be found roaming the grassland in herds. It has three toes on its hind feet.*

**Cavies** are small domestic animals that can also be found roaming tropical plains. They are not usable as livestock as they are too small to be used in a meat industry - butchering them will only give a skull in return - and they are tied with rabbits and chinchillas as the least valuable pets in the game. Unclaimed tame cavies will require a pasture to survive, otherwise they will starve. The males of the species are known as *boars*, the females are *sows*, and the young are *pups*.

Cavies make excellent live-bait in place of cats if you want your bait to survive. They are quite agile and because of their small size, larger creatures such as forgotten beasts have trouble landing a proper attack on them, with many attacks simply glancing off because of force calculation overflow.

Cavies are more commonly known as *guinea pigs*, but they are never referred as such in *Dwarf Fortress*.

Some dwarves like cavies for their *adorable call* and their *three toes*.

Admired for its *three toes*.

    [CREATURE:CAVY]
        [DESCRIPTION:A small rodent with no tail.  It can be found roaming the grassland in herds.  It has three toes on its hind feet.]
        [NAME:cavy:cavies:cavy]
        [CHILD:1][GENERAL_CHILD_NAME:cavy pup:cavy pups]
        [CREATURE_TILE:'c'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:3]
        [PET]
        [VISION_ARC:50:310]
        [STANDARD_GRAZER]
        [NATURAL]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:GRASSLAND_TROPICAL]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [BENIGN][MEANDERER]
        [PREFSTRING:three toes]
        [PREFSTRING:adorable call]
        [BODY:QUADRUPED_NECK:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:3TOES_RQ_REG:MOUTH:TONGUE:RODENT_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [GRASSTRAMPLE:0]
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
        [BODY_SIZE:0:0:80]
        [BODY_SIZE:0:168:400]
        [BODY_SIZE:1:0:800]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:4:8]
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
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:707:513:283:1900:2900] 31 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:cavy sow:cavy sows:cavy sow]
            [FEMALE]
        [CASTE:MALE]
            [CASTE_NAME:cavy boar:cavy boars:cavy boar]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
