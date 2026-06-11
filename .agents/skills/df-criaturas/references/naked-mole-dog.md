# Naked mole dog

> Fonte: [Naked mole dog](https://dwarffortresswiki.org/index.php/Naked_mole_dog) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes naked mole dogs for their wrinkly skin.**
- **Biome**
- **Underground Depth: 1**
- **Attributes**
- **No Pain · Steals food · Steals drink**
- **Tamed Attributes**
- **Pet value:** 350
- **Not hunting/war trainable**
- **Size**
- **Birth:** 6,000 cm 3
- **Mid:** 30,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 12-13
- **Fat:** 11-13
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
- **Bones:** 10-11
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large, pale rodent with loose, hanging, hairless skin. It has long teeth and an incredibly powerful bite. It is found underground.*

**Naked mole dogs** are among the most common creatures found in the first layer of the caverns, where they appear in groups of 5-10 individuals. These dwarf-sized naked mole-rats will prowl the underground, seeking your stockpiles so they may steal your food and drink, though they're largely benign and will flee at the first sign of resistance. Due to their thieving behavior, dwarves will react aggressively to their presence, often leading to civilians randomly charging at any naked mole dog that gets into their field of vision. Much like real naked mole-rats, naked mole dogs are immune to pain, and as such they won't give in to it during combat. A newborn naked mole dog is called a *puppy*.

Naked mole dogs can be captured in cage traps and trained into fairly valuable exotic pets. Food stockpiles can be used as bait for them, and due to appearing in large numbers, it's easy to capture a high number of them in one spawn wave. Compared to normal dogs, they give about twice the amount of returns when butchered, but as they only live for about three years, farming them may be difficult. Their benign disposition and lack of war/hunting training also makes them inferior to common dogs for the purpose of fortress defense.

Some dwarves like naked mole dogs for their *wrinkly skin*.

Weird and leathery.\
*Art by Kruggsmash*

    [CREATURE:MOLE_DOG_NAKED]
        [DESCRIPTION:A large, pale rodent with loose, hanging, hairless skin.  It has long teeth and an incredibly powerful bite.  It is found underground.]
        [NAME:naked mole dog:naked mole dogs:naked mole dog]
        [CASTE_NAME:naked mole dog:naked mole dogs:naked mole dog]
        [CHILD:1][GENERAL_CHILD_NAME:naked mole puppy:naked mole puppies]
        [CREATURE_TILE:'n'][COLOR:4:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:350]
        [PET_EXOTIC]
        [NATURAL]
        [LARGE_ROAMING][FREQUENCY:100]
        [BENIGN]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:1]
        [CURIOUSBEAST_EATER]
        [CURIOUSBEAST_GUZZLER]
        [PREFSTRING:wrinkly skin]
        [NOPAIN]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:4TOES_RQ_REG:MOUTH:TONGUE:RODENT_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
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
        [BODY_SIZE:0:0:6000]
        [BODY_SIZE:1:0:30000]
        [BODY_SIZE:2:0:60000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:2:3]
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
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [LOW_LIGHT_VISION:10000]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:PINK:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
