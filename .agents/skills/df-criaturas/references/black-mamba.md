# Black mamba

> Fonte: [Black mamba](https://dwarffortresswiki.org/index.php/Black_mamba) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes black mambas for their aggression.**
- **Biome**
- **Tropical Savanna Tropical Shrubland Any Tropical Forest Any Tropical Swamp**
- **Variations**
- **Black mamba - Black mamba man - Giant black mamba**
- **Attributes**
- **Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 40 cm 3
- **Mid:** 2,500 cm 3
- **Max:** 5,000 cm 3
- **Food products**
- **Eggs:** 10-30
- **Age**
- **Adult at:** Birth
- **Max age:** 10-15
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 2
- **Fat:** 2
- **Brain:** 0-1
- **Lungs:** 0-2
- **Intestines:** 1
- **Liver:** 0-1
- **Tripe:** 0-1
- **Raw materials**
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small aggressive snake which can move very quickly. Its venom is deadly.*

**Black mambas** are small solitary snakes who inhabit a number of tropical biomes. They are about as heavy as a cat and take 10 years to reach their max size. What distinguishes them from most other snakes is the virulence of their venom, with short-term symptoms including dizziness, drowsiness, strong pain, fever, unconsciousness, and complete paralysis, in ascending order to the size of the creature bitten. For a small creature like a dwarf, a single bite is enough to kill them within seconds, as paralysis of the diaphragm leads to suffocation.

Black mambas are also the only species of snake that is prone to rage; while they don't do it as often as animals like badgers, they have a small chance to flip out and attack any creature in their vicinity, including dwarves. Mamba fangs are too small to pierce normal clothing reliably, but with some luck they can thereafter cause some real damage to your fortress.

Black mambas can be caught in cage traps and trained into exotic pets. They are born adults and can't be permanently tamed. Their females are prolific egg-layers, making them a good target for egg production, though they are subpar in a meat industry compared to most domestic animals.

Some dwarves like black mambas for their *deadly bite* and their *aggression*.

Admired for its *aggression*.

    1 kph

    Black mambas were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:BLACK_MAMBA]
        [DESCRIPTION:A small aggressive snake which can move very quickly.  Its venom is deadly.]
        [NAME:black mamba:black mambas:black mamba]
        [CASTE_NAME:black mamba:black mambas:black mamba]
        [CREATURE_TILE:'s'][COLOR:0:0:1]
        [CREATURE_CLASS:POISONOUS]
        [PETVALUE:50]
        [PET_EXOTIC]
        [FREQUENCY:30]
        [NATURAL]
        [CARNIVORE]
        [LARGE_ROAMING]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:ANY_TROPICAL_FOREST]
        [BIOME:ANY_TROPICAL_SWAMP]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:aggression]
        [PREFSTRING:deadly bite]
        [PRONE_TO_RAGE:1]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH_WITH_FANGS:RIBCAGE]
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
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen black mamba venom]
            [STATE_ADJ:ALL_SOLID:frozen black mamba venom]
            [STATE_NAME:LIQUID:black mamba venom]
            [STATE_ADJ:LIQUID:black mamba venom]
            [STATE_NAME:GAS:boiling black mamba venom]
            [STATE_ADJ:GAS:boiling black mamba venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:black mamba bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:BLACK_MAMBA:ALL]
                [SYN_INJECTED]
                [CE_PARALYSIS:SEV:100:PROB:100:RESISTABLE:SIZE_DILUTES:START:50:PEAK:500:END:1500]
                [CE_DIZZINESS:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:30:PEAK:500:END:1500]
                [CE_DROWSINESS:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:30:PEAK:500:END:1500]
                [CE_UNCONSCIOUSNESS:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:50:PEAK:500:END:1500]
                [CE_FEVER:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:50:PEAK:500:END:1500]
                [CE_PAIN:SEV:75:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:10:PEAK:500:END:1500]
        [BODY_SIZE:0:0:40]
        [BODY_SIZE:2:0:2500]
        [BODY_SIZE:10:0:5000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:10:15]
        [MUNDANE]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_CANLATCH]
            [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:VENOM:LIQUID:100:100]
        [DIURNAL]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:50]
                [CLUTCH_SIZE:10:30]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
