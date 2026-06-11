# Penguin

> Fonte: [Penguin](https://dwarffortresswiki.org/index.php/Penguin) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes penguins for their coloration.**
- **Biome**
- **Arctic Ocean**
- **Variations**
- **Penguin - Penguin man - Giant penguin**
- **Attributes**
- **Egglaying**
- **Cannot be tamed**
- **Size**
- **Birth:** 120 cm 3
- **Mid:** 2,000 cm 3
- **Max:** 4,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 3
- **Fat:** 3
- **Intestines:** 1
- **Raw materials**
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small flightless bird that lives on arctic shorelines.*

**Penguins** are small creatures found inhabiting arctic oceans, where they spawn in groups of 5-10 individuals. Only as big as a blue peafowl, these tiny flightless birds are completely inoffensive, serving as little more than a distraction for a dwarf. They produce very few products when butchered, making hunting them for food rather worthless, though they are arguably useful as target practice, at least.

Penguins possess a pet value of 10, but unlike most animals, they are not trainable.

Some dwarves like penguins for their *coloration*, their *waddling gait*, and their *way of flying through the water*.

Admired for its *waddling gait*.

    12 kph

    Penguins were sponsored by the generous contributions of the Bay 12 community.

        Alluvian Est-Endrati; Bearer of the White Flame
        themel - Note to Urist: R M Laws, A Perspective on Antarctic Cookery
        For my Penga
        For Bs->PhiPhi penguin loop decays! - by Psieye
        Sponsored by penguinofhonor!
        Greenacre
        Theq629

    [CREATURE:BIRD_PENGUIN] (based on Magellanic penguin like the ones in the local zoo, while we only have 3 kinds)
        [DESCRIPTION:A small flightless bird that lives on arctic shorelines.]
        [NAME:penguin:penguins:penguin]
        [CASTE_NAME:penguin:penguins:penguin]
        [CHILD:1][GENERAL_CHILD_NAME:penguin chick:penguin chicks]
        [CREATURE_TILE:'p'][COLOR:0:0:1]
        [NATURAL]
        [LARGE_ROAMING]
        [BIOME:OCEAN_ARCTIC]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [PETVALUE:10]
        [BENIGN][MEANDERER]
        [DIURNAL] DF doesn't have arctic sunlight cycles
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:750:600:439:1900:2900] 20 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [PREFSTRING:coloration]
        [PREFSTRING:waddling gait]
        [PREFSTRING:way of flying through the water]
        [BODY:HUMANOID_ARMLESS_NECK:SIDE_FLIPPERS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:TONGUE:RIBCAGE]
        [RELSIZE:BY_CATEGORY:LEG_UPPER:100] short legs!
        [RELSIZE:BY_CATEGORY:LEG_LOWER:100]
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
        [BODY_SIZE:0:0:120]
        [BODY_SIZE:1:0:2000]
        [BODY_SIZE:2:0:4000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:125]
                [CLUTCH_SIZE:2:2]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:FEATHER]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:FEATHER]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:belly:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
