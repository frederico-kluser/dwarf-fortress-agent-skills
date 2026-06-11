# Aardvark

> Fonte: [Aardvark](https://dwarffortresswiki.org/index.php/Aardvark) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes aardvarks for their long ears.**
- **Biome**
- **Tropical Shrubland Tropical Savanna Tropical Grassland**
- **Variations**
- **Aardvark - Aardvark man - Giant aardvark**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 500 cm 3
- **Mid:** 25,000 cm 3
- **Max:** 50,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 12
- **Fat:** 12
- **Brain:** 1
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
- **Bones:** 12
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, nocturnal mammal. It has a long tongue with which to eat insects.*

**Aardvarks** are benign creatures found in tropical plains. They spawn individually and meander through the map, minding their own business and fleeing from any potential predators who approach them. Adult aardvarks are nearly as heavy as a dwarf, but they will not fight unless cornered nor do they pose any threat, with hunters and poor military squads making short work of them if needed. Because of their creature name, they appear foremost on several lists, including the create creature list in the object testing arena.

Aardvarks can be captured with cage traps and trained into low-value pets. A breeding pair can be used for a fortress's meat industry, as they commonly give birth to more than one cub at a time, providing the player with an average amount of meat, fat and bones. Aardvarks reach their full size at 2 years, and should be preferably butchered at that age for optimal product returns.

Some dwarves like aardvarks for their *snout* and their *long ears*.

Admired for its *snout*.

    1 kph

    Aardvarks were sponsored by the generous contributions of the Bay 12 community.

        Morty TC

    [CREATURE:AARDVARK]
        [DESCRIPTION:A small, nocturnal mammal.  It has a long tongue with which to eat insects.]
        [NAME:aardvark:aardvarks:aardvark]
        [CASTE_NAME:aardvark:aardvarks:aardvark]
        [GENERAL_CHILD_NAME:aardvark cub:aardvark cubs]
        [CREATURE_TILE:'a'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:50]
        [PET_EXOTIC]
        [NATURAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:GRASSLAND_TROPICAL]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:1]
        [BENIGN][MEANDERER]
        [PREFSTRING:long ears]
        [PREFSTRING:snout]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:5TOES_RQ_REG:MOUTH:GENERIC_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [GRASSTRAMPLE:0]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [SELECT_TISSUE:HAIR]
                [INSULATION:10]
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
        [BODY_SIZE:0:0:500]
        [BODY_SIZE:1:0:25000]
        [BODY_SIZE:2:0:50000]
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
        [CHILD:1]
        [NOCTURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:2206:1692:1178:585:3400:4900] 15 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:TAN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
