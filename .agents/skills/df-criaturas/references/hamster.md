# Hamster

> Fonte: [Hamster](https://dwarffortresswiki.org/index.php/Hamster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hamsters for their puffy cheeks.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Hamster - Hamster man - Giant hamster**
- **Attributes**
- **Devours food · Hateable · Pet**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny rodent that burrows by day and scurries about at night.*

**Hamsters** are a species of hateable vermin who may be found in any area that isn't freezing. Like rats, they can pose a risk to stockpiled food, bones, and shells, and may inspire unhappy thoughts to dwarves who hold a particular antipathy towards them.

Hamsters may be captured by trappers and turned into low-value pets. They have the [`[GNAWER]`](/index.php/Creature_token#GNAWER "Creature token") tag, so they can escape wooden animal traps and cages. They will escape from them almost instantly, pausing the game and giving a message, so if you plan on doing any trapping on a map that has them, you should make only metal animal traps and discard all others.

Hamsters may be kept in a cage like other vermin. Multiple hamsters may be kept in a single cage.

Some dwarves like hamsters for their *puffy cheeks*.

Admired for its *puffy cheeks*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Rumors of miniature giant space hamsters are spreading. Reportedly, they resemble ordinary hamsters but are a distinct sentient race. As of now, it is unknown whether they are a threat, valuable ~~pets~~ allies, or just a rumor.

    Hamsters were sponsored by the generous contributions of the Bay 12 community.

        Nominated by UnFleshedOne, patron of hamsters. Come Megabeast, lil critter!

    [CREATURE:HAMSTER]
        [DESCRIPTION:A tiny rodent that burrows by day and scurries about at night.]
        [NAME:hamster:hamsters:hamster]
        [CASTE_NAME:hamster:hamsters:hamster]
        [CREATURE_TILE:249][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:10]
        [VERMIN_EATER][PENETRATEPOWER:2][FREQUENCY:100][VERMIN_HATEABLE][VERMIN_GROUNDER]
        [GNAWER:gnawed]
        [BENIGN][SMALL_REMAINS][NATURAL][PET]
        [VISION_ARC:50:310]
        [NOT_BUTCHERABLE]
        [BIOME:NOT_FREEZING]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:puffy cheeks]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:RODENT_TEETH:RIBCAGE]
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
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:150]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:3:5]
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
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:MOTTLED_WHITE_BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
