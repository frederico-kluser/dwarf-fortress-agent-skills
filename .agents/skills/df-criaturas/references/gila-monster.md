# Gila monster

> Fonte: [Gila monster](https://dwarffortresswiki.org/index.php/Gila_monster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gila monsters for their coloration.**
- **Biome**
- **Any Desert**
- **Variations**
- **Gila monster - Gila monster man - Giant gila monster**
- **Attributes**
- **Amphibious · Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 30 cm 3
- **Mid:** 1,000 cm 3
- **Max:** 2,000 cm 3
- **Food products**
- **Eggs:** 2-12
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 2-6
- **Fat:** 2-6
- **Raw materials**
- **Bones:** 0-4
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small venomous lizard.*

**Gila monsters** are small reptiles found in all desert biomes. They are solitary creatures who only spawn one at a time. While carnivorous, they are less than half the size of a cat and therefore should not pose a threat to an adult dwarf. They do, however, possess a venomous bite which is *relatively* mild (as far as venoms go), but still causes pain and swelling on the victim; and with a flimsy dwarf, pain can lead to unconsciousness, which is never a good look in combat.

Gila monsters are natural swimmers and are able to path through water and breathe in it, should your desert map possess any.

Gila monsters are fairly standard as far as pets go, should the player choose to train them. They produce similar products to cats when butchered, and so can be used if the player wants some extra meat. They fare relatively well when used for egg production, as they are one of the better egg-layers among desert creatures, laying between 2-12 eggs at a time. However, they are ultimately less productive than ostriches and several domesticated poultry.

Some dwarves like gila monsters for their *venomous bite* and their *colouration*.

Admired for its *venomous bite*.

    5 kph

    Gila monsters were sponsored by the generous contributions of the Bay 12 community.

        Funnyguts

    [CREATURE:GILA_MONSTER]
        [DESCRIPTION:A small venomous lizard.]
        [NAME:gila monster:gila monsters:gila monster]
        [CASTE_NAME:gila monster:gila monsters:gila monster]
        [CHILD:1][GENERAL_CHILD_NAME:gila monster hatchling:gila monster hatchlings]
        [CREATURE_TILE:'g'][COLOR:4:0:1]
        [CREATURE_CLASS:POISONOUS]
        [AMPHIBIOUS]
        [BIOME:ANY_DESERT]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [CARNIVORE][NATURAL]
        [MEANDERER]
        [PETVALUE:50]
        [PET_EXOTIC]
        [GRASSTRAMPLE:0]
        [CANNOT_JUMP]
        [PREFSTRING:venomous bite]
        [PREFSTRING:coloration]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:4TOES_RQ_REG:MOUTH:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
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
        [BODY_SIZE:0:0:30]
        [BODY_SIZE:1:0:1000]
        [BODY_SIZE:2:0:2000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen gila monster venom]
            [STATE_ADJ:ALL_SOLID:frozen gila monster venom]
            [STATE_NAME:LIQUID:gila monster venom]
            [STATE_ADJ:LIQUID:gila monster venom]
            [STATE_NAME:GAS:boiling gila monster venom]
            [STATE_ADJ:GAS:boiling gila monster venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:gila monster bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:GILA_MONSTER:ALL]
                [SYN_INJECTED]
                [CE_PAIN:SEV:75:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:10:PEAK:50:END:1200]
                [CE_SWELLING:SEV:10:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:25:PEAK:50:END:1200]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
            [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:VENOM:LIQUID:100:100]
        [NOCTURNAL]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:32]
                [CLUTCH_SIZE:2:12]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:PINK:1] black too
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
