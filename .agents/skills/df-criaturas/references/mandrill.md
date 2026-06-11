# Mandrill

> Fonte: [Mandrill](https://dwarffortresswiki.org/index.php/Mandrill) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mandrills for their colorful faces.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Mandrill - Mandrill man - Giant mandrill**
- **Attributes**
- **Steals food · Steals items · War animals · Hunting animals**
- **Tamed Attributes**
- **Pet value:** 50
- **Trainable : Hunting War**
- **Size**
- **Birth:** 2,000 cm 3
- **Mid:** 10,000 cm 3
- **Max:** 20,000 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 13
- **Fat:** 13
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 1
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 11
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monkey with blue face and rump. It lives in large groups and often survives by destroying crops and stealing garbage. The males are larger, with powerful jaws.*

**Mandrills** are uncommon animals exclusively found in tropical moist broadleaf forests, where they appear in loose groups of 5 to 10 mayhem-minded individuals. While famed in previous versions of the game for their great aggression (being particularly prominent in the story of Boatmurdered), mandrills in the current version typically won't go out of their way to attack dwarves and while they'll fight back if confronted, they're only a third of a dwarf's size and as such, even an unarmed peasant should be able to dispose of them, albeit after receiving some nasty bites and scratches. While not aggressive, mandrills are thieves and will eagerly steal both your food and items if given the chance, and as such should be left far away from your stockpiles. All mandrills are born with Legendary skill in climbing.

Mandrills can be captured in cage traps and trained into exotic pets. Due to their thieving disposition, food stockpiles surrounded by traps can be used as bait for them, and many can potentially be captured in a single spawn wave. They can receive further training and become war or hunting beasts, however due to being the second smallest war/hunting trainable creature in the game (losing only to the bobcat), they'll only truly be effective in large numbers. If butchered for a meat industry, mandrills give a decent amount of returns.

Despite their description, mandrill faces and rumps have the same color as the rest of their skin, never being blue. There exists a note from the developers in the raws to remind themselves to add these face colors.

Some dwarves like mandrills for their *colorful faces*.

Admired for their *colorful faces*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Labyrinths may sometimes generate with every single wall engraved with images of mandrills.

    1 kph

    [CREATURE:MANDRILL]
        [DESCRIPTION:A large monkey with blue face and rump.  It lives in large groups and often survives by destroying crops and stealing garbage.  The males are larger, with powerful jaws.]
        [NAME:mandrill:mandrills:mandrill]
        [CASTE_NAME:mandrill:mandrills:mandrill]
        [CREATURE_TILE:'m'][COLOR:1:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:50]
        [PET_EXOTIC]
        [TRAINABLE]
        [NATURAL]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING][FREQUENCY:10][LOOSE_CLUSTERS]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:5:10]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [CURIOUSBEAST_EATER]
        [CURIOUSBEAST_ITEM]
        [PREFSTRING:colorful faces]
        [BODY:QUADRUPED_NECK_FRONT_GRASP:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_FINGERS:5TOES_RQ_ANON:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE:FACIAL_FEATURES]
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
        [BODY_SIZE:0:0:2000]
        [BODY_SIZE:1:0:10000]
        [BODY_SIZE:2:0:20000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:25]
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
        [CHILD:3]
        [DIURNAL]
        [HOMEOTHERM:10069]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                NOTE: Need face colors.
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_ORANGE:1]
                    [TLCM_NOUN:eyes:PLURAL]
