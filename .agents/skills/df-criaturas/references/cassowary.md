# Cassowary

> Fonte: [Cassowary](https://dwarffortresswiki.org/index.php/Cassowary) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cassowaries for their casques.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Cassowary - Cassowary man - Giant cassowary**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 100
- **Not hunting/war trainable**
- **Size**
- **Birth:** 500 cm 3
- **Mid:** 25,000 cm 3
- **Max:** 50,000 cm 3
- **Food products**
- **Eggs:** 3-6
- **Age**
- **Adult at:** 1
- **Max age:** 40-50
- **Butchering returns**
- **Food items**
- **Meat:** 14
- **Fat:** 13
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
- **Bones:** 19
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, flightless, brightly-colored bird.*

**Cassowaries** are flightless birds found exclusively in tropical moist broadleaf forests. Despite being described as small, they are, in fact, nearly as heavy as an adult dwarf, though they are benign and will normally flee if provoked. In the event they fight back against dwarves, they will prefer to use kicks for self-defense.

Cassowaries can be captured in cage traps and trained into exotic pets. They give an acceptable amount of returns when butchered, and can also be put on nest boxes to lay a meager amount of eggs. Out of the flightless bird species, cassowaries are the longest lived, outliving ostriches and emus by about three times.

Some dwarves like cassowaries for their *casques*.

\

Admired for their *casques*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Humans often tell tales of incredibly aggressive cassowaries, who can kick and tear apart just about anything that looks at them funny. According to them, the birds have one toe which is literally a spear, made specifically to murder innocents. Dwarves, who are master tamers of the animal kingdom, scoff at the idea of cassowaries being anything but fancy-coloured poultry, though the proposition of weaponizing their spear-toes (and possibly use their head-casques as axes) is an attractive one.

    1 kph

    Cassowaries were sponsored by the generous contributions of the Bay 12 community.

        Spam180
        culling66

    [CREATURE:BIRD_CASSOWARY]
        [DESCRIPTION:A small, flightless, brightly-colored bird.]
        [NAME:cassowary:cassowaries:cassowary]
        [CASTE_NAME:cassowary:cassowaries:cassowary]
        [CHILD:1][GENERAL_CHILD_NAME:cassowary chick:cassowary chicks]
        [CREATURE_TILE:'c'][COLOR:0:0:1]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [POPULATION_NUMBER:15:30]
        [NATURAL]
        [LARGE_ROAMING]
        [PETVALUE:100]
        [BENIGN][MEANDERER]
        [PET_EXOTIC]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [SWIMS_INNATE]
        [MUNDANE]
        [PREFSTRING:casques]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:2TOES:BEAK:CASQUE:TONGUE:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS:FEATHER]
        [USE_MATERIAL_TEMPLATE:TALON:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:TALON:TALON_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:TALON:FRONT]
        [BODY_DETAIL_PLAN:EGG_MATERIALS]
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
        [BODY_SIZE:0:0:500]
        [BODY_SIZE:1:0:25000]
        [BODY_SIZE:2:0:50000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [MAXAGE:40:50]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_CANLATCH]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:550]
                [CLUTCH_SIZE:3:6]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN] neck skin is mostly blue
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
