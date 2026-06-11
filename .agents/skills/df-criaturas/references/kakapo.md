# Kakapo

> Fonte: [Kakapo](https://dwarffortresswiki.org/index.php/Kakapo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kakapo for their booming calls.**
- **Biome**
- **Temperate Shrubland Temperate Savanna Temperate Grassland Any Temperate Forest**
- **Variations**
- **Kakapo - Kakapo man - Giant kakapo**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50 cm 3
- **Mid:** 1,500 cm 3
- **Max:** 3,000 cm 3
- **Food products**
- **Eggs:** 1-4
- **Age**
- **Adult at:** 7
- **Max age:** 60-120
- **Butchering returns**
- **Food items**
- **Meat:** 2-6
- **Fat:** 2-6
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4-6
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small flightless green parrot. It is nocturnal and counts itself among the longest-lived birds.*

**Kakapo** are small, flightless parrots who appear in a number of temperate biomes. A lone kakapo may occasionally appear in the map and do little else but meander around adorably – they are kea, except without all the bad parts. In adventure mode, male kakapo are one of the few creatures in the game who emit noises, with the game describing their booms and chings as the player approaches them.

Kakapo can be captured with cage traps and trained into low-value pets. They can be used to produce a meager quantity of eggs, which is likely the most suitable use for them, as tearing the adorable thing apart only provides enough meat to fill up six dwarves for a season. Still, you may be tempted to send a militia-dwarf to hunt wild kakapo before they leave, since they are too slow to run away. Kakapo are among the longest-living animals in the game, some living up to 120 years, which makes them actually quite long-lasting companions to dwarves who adopt them.

Some dwarves like kakapo for their *longevity*, their *flightlessness* and their *booming calls*.

\

Admired for its *booming calls*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Kakapo are also known to mate with humans given the chance : https://youtu.be/mU13O0gAVmA?t=27s They make good pets, but dangerous scapegoats.

    1 kph

    Kakapo were sponsored by the generous contributions of the Bay 12 community.

        You've just been shagged by a rare parrot!

    [CREATURE:BIRD_KAKAPO]
        [DESCRIPTION:A small flightless green parrot.  It is nocturnal and counts itself among the longest-lived birds.]
        [NAME:kakapo:kakapo:kakapo]
        [CASTE_NAME:kakapo:kakapo:kakapo]
        [CHILD:7][GENERAL_CHILD_NAME:kakapo chick:kakapo chicks]
        [CREATURE_TILE:'k'][COLOR:2:0:0]
        [NATURAL]
        [LARGE_ROAMING]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:GRASSLAND_TEMPERATE]
        [BIOME:ANY_TEMPERATE_FOREST]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [PETVALUE:50]
        [BENIGN][MEANDERER][PET_EXOTIC]
        [NOCTURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:7780:7508:7254:2925:8478:9233] 3 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [PREFSTRING:longevity]
        [PREFSTRING:flightlessness]
        [PREFSTRING:booming calls]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS:FEATHER]
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
        [BODY_SIZE:0:0:50]
        [BODY_SIZE:1:0:1500]
        [BODY_SIZE:2:0:3000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:60:120]
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
                [EGG_SIZE:52] couldn't find this
                [CLUTCH_SIZE:1:4]
        [CASTE:MALE]
            [MALE]
            [SOUND:PEACEFUL_INTERMITTENT:200:1000:VOCALIZATION:boom:booms:a low boom]
            [SOUND:PEACEFUL_INTERMITTENT:50:1000:VOCALIZATION:ching:chings:a metallic ching]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:GREEN:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
