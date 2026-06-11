# Wild boar

> Fonte: [Wild boar](https://dwarffortresswiki.org/index.php/Wild_boar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes wild boars for their tusks.**
- **Biome**
- **Any Savanna Any Grassland Any Shrubland Any Forest Any Wetland**
- **Variations**
- **Wild boar - Wild boar man - Giant wild boar**
- **Attributes**
- **Horn**
- **Tamed Attributes**
- **Pet value:** 100
- **Not hunting/war trainable**
- **Size**
- **Birth:** 8,000 cm 3
- **Mid:** 40,000 cm 3
- **Max:** 80,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 15-20
- **Butchering returns**
- **Food items**
- **Meat:** 8-9
- **Fat:** 8-9
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
- **Bones:** 12-14
- **Skull:** 1
- **Ivory:** 2
- **Hooves:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized beast, known for its tusks and powerful build.*

**Wild boars** are creatures found in various types of biomes, appearing in groups of 5-10 individuals. While they're larger than dwarves and possess a nasty reputation in real life of being aggressive and dangerous, wild boars in-game are benign meanderers who'll rather flee from dwarves than fight back against their attempts to hunt them. Males of the species are simply called *wild boars*, while females are *wild boar sows* and their young are *wild boar piglets*.

Wild boars can be captured in cage traps and trained into exotic pets. Compared to their domesticated pig cousins, wild boars provide more returns when butchered but can't be milked, and as they appear in large groups, many can be captured or hunted quickly to help fuel a meat industry. Wild boars are also a good source of ivory, which normal pigs don't produce.

Some dwarves like wild boars for their *tusks* and their *ferocious charges*.

|  |
|----|
| "Wild boar" in other / Languages / Dwarven / : / omrist dùstik / Elven / : / theÿise lebeyu / Goblin / : / muso oke / Human / : / kozi stral |

Admired for their *ferocious charges*.

    Wild boars were sponsored by the generous contributions of the Bay 12 community.

        Ben "Vattic" Cartwright sponsored this fine beast.
        Somnambulist
        TheWanderer

    [CREATURE:WILD_BOAR]
        [DESCRIPTION:A medium-sized beast, known for its tusks and powerful build.]
        [NAME:wild boar:wild boars:wild boar]
        [CHILD:1][GENERAL_CHILD_NAME:wild boar piglet:wild boar piglets]
        [CREATURE_TILE:'B'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:100]
        [PET_EXOTIC]
        [VISION_ARC:50:310]
        [PREFSTRING:tusks]
        [PREFSTRING:ferocious charges]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [BIOME:ANY_SAVANNA]
        [BIOME:ANY_GRASSLAND]
        [BIOME:ANY_SHRUBLAND]
        [BIOME:ANY_FOREST]
        [BIOME:ANY_WETLAND]
        [BENIGN][MEANDERER][NATURAL]
        [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH:2TUSKS:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:IVORY:TOOTH_TEMPLATE]
                [STATE_NAME:ALL_SOLID:ivory]
                [STATE_ADJ:ALL_SOLID:ivory]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_TISSUE_TEMPLATE:IVORY:IVORY_TEMPLATE]
                [TISSUE_NAME:ivory:NP]
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
        [BODY_SIZE:0:0:8000]
        [BODY_SIZE:1:0:40000]
        [BODY_SIZE:2:0:80000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:15:20]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_REAR]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_CANLATCH]
        [APPLY_CREATURE_VARIATION:TUSK_STAB_ATTACK]
        [DIURNAL]
        [HOMEOTHERM:10065]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
            [CASTE_NAME:wild boar sow:wild boar sows:wild boar sow]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
            [CASTE_NAME:wild boar:wild boars:wild boar]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
