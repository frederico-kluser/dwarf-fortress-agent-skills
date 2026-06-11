# Monitor lizard

> Fonte: [Monitor lizard](https://dwarffortresswiki.org/index.php/Monitor_lizard) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes monitor lizards for their intelligence.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Monitor lizard - Monitor lizard man - Giant monitor lizard**
- **Attributes**
- **Egglaying**
- **Tamed Attributes**
- **Pet value:** 400
- **Not hunting/war trainable**
- **Size**
- **Birth:** 60 cm 3
- **Mid:** 50,000 cm 3
- **Max:** 100,000 cm 3
- **Food products**
- **Eggs:** 15-25
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 6-13
- **Fat:** 6-13
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
- **Bones:** 4-12
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized reptile. They can be found foraging for food such as eggs or worms. They are said to be the most intelligent of their kind.*

**Monitor lizards** are creatures who can be found in tropical plains and forests. They spawn individually, meandering through the area and usually minding their own business. While carnivorous and nearly twice the size of a dwarf, monitor lizards are not especially aggressive animals, and are unlikely to pose a threat unless provoked, though they may attempt to take a bite out of nearby dogs and other small domestic animals. Their population is quite low compared to other creatures, and no more than ten monitor lizards will spawn in the area before they are extinct.

Monitor lizards can be captured with cage traps and trained into valuable exotic pets. They are rather prolific egg-layers, laying from 15 to 25 eggs at a time, which makes them a great target for egg production. Breeding them will quickly fill the fortress with lizards, who can be butchered into a nice amount of food and bones when they reach their maximum size. Products made from monitor lizard parts are worth twice more than those of standard animals.

Some dwarves like monitor lizards for their *intelligence*.

Admired for its *intelligence*.

    1 kph

    Monitor lizards were sponsored by the generous contributions of the Bay 12 community.

        Umiman's objective: sponsor a large land predator to make players scream :)
        Hi, Zari

    [CREATURE:MONITOR_LIZARD]
        [DESCRIPTION:A medium-sized reptile.  They can be found foraging for food such as eggs or worms.  They are said to be the most intelligent of their kind.]
        [NAME:monitor lizard:monitor lizards:monitor lizard]
        [CASTE_NAME:monitor lizard:monitor lizards:monitor lizard]
        [CHILD:1][GENERAL_CHILD_NAME:monitor lizard hatchling:monitor lizard hatchlings]
        [CREATURE_TILE:'M'][COLOR:6:0:0]
        [BIOME:GRASSLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:ANY_TROPICAL_FOREST]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [CARNIVORE][NATURAL]
        [MEANDERER]
        [PETVALUE:400]
        [PET_EXOTIC]
        [GRASSTRAMPLE:20]
        [PREFSTRING:intelligence]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
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
        [BODY_SIZE:0:0:60]
        [BODY_SIZE:1:0:50000]
        [BODY_SIZE:2:0:100000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:70]
                [CLUTCH_SIZE:15:25]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:TAN:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
