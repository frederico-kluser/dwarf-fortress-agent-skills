# Jabberer

> Fonte: [Jabberer](https://dwarffortresswiki.org/index.php/Jabberer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes jabberers for their frightening beaks.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **War animals · Hunting animals · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 1,500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 5,000 cm 3
- **Mid:** 2,000,000 cm 3
- **Max:** 4,500,000 cm 3
- **Food products**
- **Eggs:** 1-2
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×4)**
- **Food items**
- **Meat:** 107-153
- **Fat:** 30-43
- **Brain:** 6-9
- **Gizzard:** 6-9
- **Heart:** 3-4
- **Lungs:** 12-18
- **Intestines:** 19-27
- **Liver:** 6-9
- **Kidneys:** 6-8
- **Tripe:** 6-9
- **Sweetbread:** 3-4
- **Eyes:** 2
- **Spleen:** 3-4
- **Raw materials**
- **Bones:** 52-69
- **Skull:** 1
- **Skin:** Raw hide
- **Feather:** 1
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster that lurks in caverns deep under the earth. It uses its wide beak to reach down and pluck up unsuspecting intruders.*

**Jabberers** are colossal flightless birds who live at the deeper levels of subterranean caverns - the much nastier cousin of the elk bird. These carnivorous beasts, nearly the size of an elephant, prowl the underground while terrorizing anything that approaches them, these usually being hapless dwarves who just happened to take the wrong turn on their hauling job. The typical result of a civilian stumbling into a jabberer is a new body for the fortress' cemetery.

Jabberers are a threat due to their great size; they are among the largest creatures in the underground (losing only to blind cave ogres, forgotten beasts and cave dragons) and will use all of their strength to tear through unarmed or inexperienced dwarves. Even a heavily armored dwarf is at risk of dying immediately by being grabbed by the head and shaken by the jabberer, causing their upper spine to collapse. When facing jabberers, a powerful military is essential, though they are also equally vulnerable to cage traps. Uncommonly, the creatures are also encountered in goblin sieges, where they are used by the enemy as mounts.

Jabberers possess a pet value of 1,500; one of the highest in the game, and the great amount of returns they give when butchered means players should consider them more valuable alive than dead. Should a jabberer couple be captured and assigned to a nest box, they can be used to steadily provide the fortress with a force of giant, bloodthirsty and delicious bodyguards. Jabberers can be trained not just as pets but also as war and hunting beasts, and products made from their parts are worth four times as much as those made from common animals.

Unlike most animals, jabberers can't be spawned in the object testing arena.

Some dwarves like jabberers for their *frightening beaks*.

## Gallery

-

  A jabberer, drawn in crayon by Bay 12 Games.

-

  *Concept art by Bay 12 Games.*

    [CREATURE:JABBERER]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A huge monster that lurks in caverns deep under the earth.  It uses its wide beak to reach down and pluck up unsuspecting intruders.]
        [NAME:jabberer:jabberers:jabberer]
        [CASTE_NAME:jabberer:jabberers:jabberer]
        [GENERAL_CHILD_NAME:jabberer hatchling:jabberer hatchlings]
        [CREATURE_TILE:'J'][COLOR:5:0:1]
        [PETVALUE:1500]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [TRAINABLE]
        [NATURAL]
        [LARGE_ROAMING][DIFFICULTY:3]
        [POPULATION_NUMBER:15:30]
        [LARGE_PREDATOR][NATURAL]
        [BONECARN]
        [CHILD:1]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [PREFSTRING:frightening beaks]
        [BODY:HUMANOID_ARMLESS_NECK:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:TONGUE:RIBCAGE]
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
        [EXTRA_BUTCHER_OBJECT:BY_CATEGORY:GIZZARD]
            [EBO_ITEM:SMALLGEM:NONE:ANY_HARD_STONE]
            [EBO_SHAPE:GIZZARD_STONE]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:5000]
        [BODY_SIZE:1:0:2000000]
        [BODY_SIZE:2:0:4500000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
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
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:snatch at:snatches at]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:5100]
                [CLUTCH_SIZE:1:2]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:PURPLE:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:4]
