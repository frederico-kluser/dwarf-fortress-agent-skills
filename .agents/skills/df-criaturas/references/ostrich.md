# Ostrich

> Fonte: [Ostrich](https://dwarffortresswiki.org/index.php/Ostrich) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ostriches for their giant eggs.**
- **Biome**
- **Tropical Savanna Tropical Grassland Any Desert**
- **Variations**
- **Ostrich - Ostrich man - Giant ostrich**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 100
- **Not hunting/war trainable**
- **Size**
- **Birth:** 1,800 cm 3
- **Mid:** 45,000 cm 3
- **Max:** 90,000 cm 3
- **Food products**
- **Eggs:** 10-15
- **Age**
- **Adult at:** 1
- **Max age:** 35-45
- **Butchering returns**
- **Food items**
- **Meat:** 15-20
- **Fat:** 13
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 19-25
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 0-1
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large flightless bird that runs through the savanna. It has a long neck and legs.*

**Ostriches** are flightless birds who inhabit deserts, tropical savannas and tropical grasslands, appearing in groups of anywhere between 1-10 individuals. They are a half again as large as the average dwarf but are completely benign, doing little but meandering the area cluelessly. The sprite for ostriches will have black feathers for males, and greyish-brown feathers for females. They will normally flee when attacked, but if enraged they may attempt to defend themselves, preferably with kick attacks. Male ostriches are called *ostrich cocks*, while females are called *ostrich hens*.

Ostriches can be captured in cage traps and trained into pets. They produce a good quantity of products when butchered and lay a fairly high amount of eggs if placed in a nest box; these traits combine to make them good choices to serve as the basis for egg production and a meat industry. Among the large ratite birds in the game (ostriches, emus and cassowaries), ostriches are by far the largest, though they may not live as long as a cassowary. Ostriches appear to be the smallest creature to yield either feathers or gizzard stones when butchered.

Some dwarves like ostriches for their *long necks* and their *giant eggs*.

Admired for their *long necks*.

    1 kph

    Ostriches were sponsored by the generous contributions of the Bay 12 community.

        Pangaron
        HBC: "ostriches are cool"
        BlargityBlarg lived on a farm of these things 'til he was five!
        Priestly
        Tristan Hayes

    [CREATURE:BIRD_OSTRICH]
        [DESCRIPTION:A large flightless bird that runs through the savanna.  It has a long neck and legs.]
        [NAME:ostrich:ostriches:ostrich]
        [CHILD:1][GENERAL_CHILD_NAME:ostrich chick:ostrich chicks]
        [CREATURE_TILE:'O'][COLOR:0:0:1]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:GRASSLAND_TROPICAL]
        [BIOME:ANY_DESERT]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:10] should be seasonal
        [NATURAL]
        [LARGE_ROAMING]
        [PETVALUE:100]
        [BENIGN][MEANDERER]
        [PET_EXOTIC]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:657:438:219:1900:2900] 40 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [PREFSTRING:long necks]
        [PREFSTRING:giant eggs]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:2TOES:BEAK:TONGUE:RIBCAGE:TAIL]
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
        [BODY_SIZE:0:0:1800]
        [BODY_SIZE:1:0:45000]
        [BODY_SIZE:2:0:90000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:35:45]
        [EXTRA_BUTCHER_OBJECT:BY_CATEGORY:GIZZARD]
            [EBO_ITEM:SMALLGEM:NONE:ANY_HARD_STONE]
            [EBO_SHAPE:GIZZARD_STONE]
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
        [MUNDANE]
        [CASTE:FEMALE]
            [CASTE_NAME:ostrich hen:ostrich hens:ostrich hen]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:2000]
                [CLUTCH_SIZE:10:15]
        [CASTE:MALE]
            [CASTE_NAME:ostrich cock:ostrich cocks:ostrich cock]
            [MALE]
        [SELECT_CASTE:MALE]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:FEATHER]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:FEATHER]
             [PLUS_TL_GROUP:BY_CATEGORY:WING:FEATHER]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:feathers:PLURAL]
        [SELECT_CASTE:FEMALE]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:FEATHER]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:FEATHER]
             [PLUS_TL_GROUP:BY_CATEGORY:WING:FEATHER]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:feathers:PLURAL]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:TAIL:FEATHER]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:tail feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:FEATHER]
             [PLUS_TL_GROUP:BY_CATEGORY:NECK:FEATHER]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:head and neck down:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
