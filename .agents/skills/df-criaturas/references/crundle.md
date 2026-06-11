# Crundle

> Fonte: [Crundle](https://dwarffortresswiki.org/index.php/Crundle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes crundles for their nervous energy.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **Horn · Egglaying · Humanoid**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50 cm 3
- **Mid:** 1,000 cm 3
- **Max:** 10,000 cm 3
- **Food products**
- **Eggs:** 5-20
- **Age**
- **Adult at:** Birth
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 2-6
- **Fat:** 2-6
- **Intestines:** 1
- **Raw materials**
- **Bones:** 2-4
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny underground monster with large claws and horns. It walks on two legs and is dangerous when encountered in large numbers.*

The **crundle** is a small, imp-like, reptilian creature that roams the caverns in great packs under the earth. They tend to arrive at a fort in large groups (15 to 20 of them at once) and are very common, probably more common than any other type of underground wildlife, except possibly elk birds. All crundles are born adults and possess Legendary skill in climbing.

They tend to be rather weak and cowardly, even in packs, and are not especially aggressive. They **can**, however, maim or even kill an unarmed dwarf on a lucky hit, but are generally the least dangerous of all underground creatures. They are still annoying, because they will often interrupt your dwarves who perform useful jobs down in the caverns. Thanks to their numbers, wild crundles can be useful for training your military.

Crundles seem to have a chance to spawn inside procedural fortresses in adventure mode. If you are immune to exhaustion, have copper armor and can somehow grab several of them, you can very quickly increase your various combat attributes, more importantly dodging and shield skill, by letting them attack you if you cannot access the surface due to the site isolating itself from it. Basically, they are like the flightless birds of the caverns.

If you rely on traps to defend your fortress, it should be noted that pit traps are fairly ineffective against crundles. They require a long fall to be killed on impact, unless, of course, the ground is flooded with poison, spikes, or best of all, magma. They can be caught in cage traps, and weapon traps with basic weapons are generally enough to severely injure or kill them. Although, due to their sheer numbers, crundles are prone to saturating your trap defenses, allowing much more dangerous beasts to pass through.

Crundles can be trained, and are rather prolific egg-layers, making them viable for egg production. They can also be bred for meat, although there are better animals around since crundles do not provide leather. As they are born as adults, they can never be domesticated. Trained crundles can be used in fortress defense designs, but they should only be used as meatshields and/or distractions because they are very poor fighters. Overall, crundles are poor choices for training (but provide good experience for your animal trainers since they need frequent retraining) when there are many more interesting creatures in the caverns.

Unlike most creatures, they can't be spawned in the object testing arena.

Some dwarves like crundles for their *nervous energy*.

## Gallery

-

  Crundles should present no problems to an experienced adventurer.

-

  Many obnoxious crundles.\
  *Art by kruggsmash*

-

  An almost photogenic crundle.\
  *Art by Arne*

-

  A bigger, nastier looking crundle.\
  *Art by Quinmael*

-

  *Concept art by Bay 12 Games.*

    [CREATURE:CRUNDLE]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A tiny underground monster with large claws and horns.  It walks on two legs and is dangerous when encountered in large numbers.]
        [NAME:crundle:crundles:crundle]
        [CASTE_NAME:crundle:crundles:crundle]
        [CREATURE_TILE:'c'][COLOR:4:0:0]
        [PETVALUE:50]
        [PET_EXOTIC]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_WATER]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [FREQUENCY:100]
        [POPULATION_NUMBER:150:300]
        [CLUSTER_NUMBER:15:20]
        [CARNIVORE]
        [PREFSTRING:nervous energy]
        [BODY:HUMANOID_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4FINGERS:4TOES:MOUTH:TONGUE:2HEAD_HORN]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:IVORY:TOOTH_TEMPLATE]
                [STATE_NAME:ALL_SOLID:ivory]
                [STATE_ADJ:ALL_SOLID:ivory]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:SKIN]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
            [USE_TISSUE_TEMPLATE:IVORY:IVORY_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:CLAW:FRONT]
            [TL_RELATIVE_THICKNESS:10]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
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
        [BODY_SIZE:1:168:1000]
        [BODY_SIZE:2:0:10000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:CLAW]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [HOMEOTHERM:10040]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:60]
                [CLUTCH_SIZE:5:20]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:CRIMSON:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
