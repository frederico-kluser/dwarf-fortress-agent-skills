# Pond grabber

> Fonte: [Pond grabber](https://dwarffortresswiki.org/index.php/Pond_grabber) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes pond grabbers for their patience.**
- **Biome**
- **Underground Depth: 1-2**
- **Attributes**
- **Aquatic · Genderless**
- **Cannot be tamed**
- **Size**
- **Birth:** 2,000 cm 3
- **Mid:** 15,000 cm 3
- **Max:** 30,000 cm 3
- **Age**
- **Adult at:** 2
- **Max age:** Immortal
- **Butchering returns**
- **Food items**
- **Meat:** 5
- **Fat:** 1
- **Brain:** 1
- **Heart:** 1
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small creature that lives in watery ditches deep underground. It has a sharp beak and four tentacles with claws at the end.*

**Pond grabbers** are quite small tentacled, clawed, aquatic monsters found in underground bodies of water. They tend to hunt their prey in small groups of 3-5. They will generally leave you alone, but can wrestle and drown a dwarf startlingly easily. They also generally spend years in ponds, doing nothing and possibly blocking other, more interesting creatures from entering your caverns. It is best to defeat them at range with marksdwarves if possible.

Pond grabbers possess a pet value of 50, but lack the necessary tokens to be trainable. Things made from their parts, however, can still be requested from the dwarven caravan thanks to them existing at the first cavern layer. They are notably biologically immortal and only die from violence or disease. They can't be spawned in the object testing arena.

Some dwarves like pond grabbers for their *patience*.

## Gallery

-

  *Art by Arne*.

-

  *Concept art by Bay 12 Games.*

    [CREATURE:POND_GRABBER]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A small creature that lives in watery ditches deep underground.  It has a sharp beak and four tentacles with claws at the end.]
        [NAME:pond grabber:pond grabbers:pond grabber]
        [CASTE_NAME:pond grabber:pond grabbers:pond grabber]
        [CREATURE_TILE:'p'][COLOR:1:0:1]
        [PETVALUE:50]
        [AQUATIC][IMMOBILE_LAND]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:5]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:2]
        [NO_DRINK]
        [LARGE_PREDATOR]
        [BONECARN]
        [PREFSTRING:patience]
        [CHILD:2]
        [EXTRAVISION]
        [BODY:BODY_WITH_HEAD_FLAG:FOUR_TENTACLES:BRAIN:HEART:GUTS:ORGANS:BEAK]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
            [TISSUE_NAME:claw:NP]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
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
        [BODY_SIZE:0:0:2000]
        [BODY_SIZE:0:0:15000]
        [BODY_SIZE:0:0:30000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:STAB:BODYPART:BY_CATEGORY:CLAW]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:stab at:stabs at]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:BLUE:1]
                [TLCM_NOUN:skin:SINGULAR]
