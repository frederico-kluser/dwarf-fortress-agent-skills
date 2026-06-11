# Buzzard

> Fonte: [Buzzard](https://dwarffortresswiki.org/index.php/Buzzard) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes buzzards for their striking red face.**
- **Biome**
- **Temperate Freshwater Marsh Temperate Saltwater Marsh Temperate Grassland Temperate Savanna Any Desert**
- **Variations**
- **Buzzard - Buzzard man - Giant buzzard**
- **Attributes**
- **Flying · Steals food · Egglaying**
- **Tamed Attributes**
- **Pet value:** 30
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50 cm 3
- **Mid:** 700 cm 3
- **Max:** 1,400 cm 3
- **Food products**
- **Eggs:** 2-3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 0-2
- **Fat:** 0-2
- **Raw materials**
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized, red-faced black bird that searches the temperate lands for carrion.*

**Buzzards** are incredibly weak and extremely annoying animals that should be prepared for on embark to any biome where they are present. An individual buzzard can steal a stack of food and they travel in groups of 5-10. They can be particularly devastating for a newly set up fortress which hasn't yet planted a farm; while the buzzards feast upon prepared warthog kidney, you'll be searching for vermin to eat. They also have no qualms about stealing directly from your above-ground farm, biting at your farmers, and grabbing strawberries right out from under their noses.

It is possible to capture them in cage traps, providing you with a neat bird to release into your zoo. They can be trained into pets, but generally aren't worth it due to their low pet value. Buzzards will claim and lay eggs in an available nest box, should you wish to create a swarm of buzzards for your latest project, though they only lay 2 - 3 eggs at a time which is rather poor to egg production compared to all domesticated poultry. Buzzard eggs, like all eggs, hatch after exactly 3 months.

Buzzards leave very little when butchered. Around half of them will be stripped down to nothing more than a skull for your bone carvers.

The creature used in-game is known in real life as the turkey vulture, popularly called buzzard in North America, even though they are not actually related to common buzzards.

Some dwarves like buzzards for their *striking red face*.

Admired for its *striking red face*.

|  |
|----|
| "Buzzard" in other / Languages / Dwarven / : / setnek / Elven / : / acithe / Goblin / : / âng / Human / : / jozi |

    11 kph

    [CREATURE:BIRD_BUZZARD]
        [DESCRIPTION:A medium-sized, red-faced black bird that searches the temperate lands for carrion.]
        [NAME:buzzard:buzzards:buzzard]
        [CASTE_NAME:buzzard:buzzards:buzzard]
        [GENERAL_CHILD_NAME:buzzard hatchling:buzzard hatchlings]
        [CREATURE_TILE:'b'][COLOR:0:0:1]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10]
        [LOOSE_CLUSTERS]
        [PETVALUE:30]
        [NATURAL]
        [LARGE_ROAMING]
        [CURIOUSBEAST_EATER]
        [PET_EXOTIC]
        [FLIER]
        [BONECARN]
        [CHILD:1]
        [ALL_ACTIVE]
        [BIOME:MARSH_TEMPERATE_FRESHWATER]
        [BIOME:MARSH_TEMPERATE_SALTWATER]
        [BIOME:GRASSLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:ANY_DESERT]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [PREFSTRING:striking red face]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:TONGUE:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_FEATHER_TISSUE_LAYERS_NO_HEAD:FEATHER]
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
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:50]
        [BODY_SIZE:1:0:700]
        [BODY_SIZE:2:0:1400]
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
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:snatch at:snatches at]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:60]
                [CLUTCH_SIZE:2:3]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BROWN:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:RED:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
