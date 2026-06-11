# Peregrine falcon

> Fonte: [Peregrine falcon](https://dwarffortresswiki.org/index.php/Peregrine_falcon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes peregrine falcons for their ability to dive through the air.**
- **Biome**
- **Any Wetland Any Temperate Forest Tropical Coniferous Forest Tropical Dry Broadleaf Forest Taiga Any Shrubland Any Savanna Any Grassland Any Desert Mountain Tundra**
- **Variations**
- **Peregrine falcon - Peregrine falcon man - Giant peregrine falcon**
- **Attributes**
- **Flying · Egglaying**
- **Tamed Attributes**
- **Pet value:** 25
- **Not hunting/war trainable**
- **Size**
- **Birth:** 44 cm 3
- **Mid:** 300 cm 3
- **Max:** 600 cm 3
- **Food products**
- **Eggs:** 3-4
- **Age**
- **Adult at:** 1
- **Max age:** 12-15
- **Butchering returns**
- **Food items**
- **Raw materials**
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small bird of prey that is capable of great speed. They dive on unsuspecting vermin.*

**Peregrine falcons** are small birds who can be found in almost every biome, excluding oceans, glaciers, and tropical rain forests. They spawn one at a time and occasionally dive down from the sky to kill vermin on the ground, being harmless to a dwarf and benign to other creatures. Females are known as *peregrine falcons*, while males are known as *tiercel peregrines* (tiercel meaning third, referring to the males being about 1/3rd smaller than the females, which is reflected in-game as a smaller body size for males) and their young are called *peregrine falcon chicks*. All peregrine falcons are born with Legendary skill in climbing.

Peregrine falcons can be captured with cage traps and trained into low-value pets. They can be put into nest boxes in order to be part of a fort's egg production, but hatching them for meat is worthless – peregrine falcons are too small to produce anything but a skull. While they are the fastest birds in real life, reaching dive speeds of 200+ mph (320 km/h), *Dwarf Fortress* does not handle gaits faster than 87 km/h, instead using this as maximum flight speed, which nonetheless makes them the fastest fliers in the game. Note that trained peregrine falcons will no longer display their dive-hunting behavior, but when tamed they may hunt vermin, reflecting their real-life use in falconry.

Some dwarves like peregrine falcons for their *ability to dive through the air*.

Admired for its *ability to dive through the air*.

    1 kph

    Peregrine falcons were sponsored by the generous contributions of the Bay 12 community.

        Demon
        PMantix
        MAShapiro
        John Tait from Harrow, Middlesex: "Hunting food for vermin"

    [CREATURE:BIRD_FALCON_PEREGRINE]
        [DESCRIPTION:A small bird of prey that is capable of great speed.  They dive on unsuspecting vermin.]
        [NAME:peregrine falcon:peregrine falcons:peregrine falcon]
        [GENERAL_CHILD_NAME:peregrine falcon chick:peregrine falcon chicks]
        [CREATURE_TILE:'p'][COLOR:6:0:0]
        [POPULATION_NUMBER:15:30]
        [NATURAL]
        [LARGE_ROAMING]
        [PETVALUE:25]
        [BENIGN]
        [PET]
        [FLIER]
        [BONECARN]
        [DIVE_HUNTS_VERMIN]
        [CHILD:1]
        [ALL_ACTIVE]
        [MUNDANE]
        everywhere but oceans, glaciers and tropical rainforests
        [BIOME:ANY_WETLAND]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:FOREST_TROPICAL_CONIFER]
        [BIOME:FOREST_TROPICAL_DRY_BROADLEAF]
        [BIOME:FOREST_TAIGA]
        [BIOME:ANY_SHRUBLAND]
        [BIOME:ANY_SAVANNA]
        [BIOME:ANY_GRASSLAND]
        [BIOME:ANY_DESERT]
        [BIOME:MOUNTAIN]
        [BIOME:TUNDRA]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:300:200:100:1900:2900] 87+ kph (110), need to work on base speed for fliers
                                                dive ~320
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [PREFSTRING:ability to dive through the air]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:TONGUE:RIBCAGE]
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
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:12:15]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:TALON]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:snatch at:snatches at]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [CASTE:FEMALE]
            [CASTE_NAME:peregrine falcon:peregrine falcons:peregrine falcon]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:46]
                [CLUTCH_SIZE:3:4]
            [BODY_SIZE:0:0:44]
            [BODY_SIZE:1:0:550]
            [BODY_SIZE:2:0:1100]
        [CASTE:MALE]
            [CASTE_NAME:tiercel peregrine:tiercel peregrines:tiercel peregrine]
            [MALE]
            [BODY_SIZE:0:0:44]
            [BODY_SIZE:1:0:300]
            [BODY_SIZE:2:0:600]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
