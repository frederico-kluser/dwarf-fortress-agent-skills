# Raven

> Fonte: [Raven](https://dwarffortresswiki.org/index.php/Raven) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ravens for their intelligence.**
- **Biome**
- **Temperate Grassland Temperate Savanna Temperate Shrubland Taiga Any Temperate Forest Any Temperate Wetland Tundra Any Desert**
- **Variations**
- **Raven - Raven man - Giant raven**
- **Attributes**
- **Flying · Egglaying**
- **Tamed Attributes**
- **Pet value:** 25
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50 cm 3
- **Max:** 1,200 cm 3
- **Food products**
- **Eggs:** 3-7
- **Age**
- **Adult at:** 1
- **Max age:** 20-40
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Not to be confused with crows.*

*A small, foreboding black bird that feeds on carrion. It is social, very intelligent, and knows how to use tools.*

**Ravens** are small and very common birds who are found in almost all biomes in the game, where they appear in flocks of anywhere between 2-10 individuals. They are benign and do little but fly across the area aimlessly, rarely if ever paying mind to dwarves or other creatures, and even if they attack, they are unable to deal any significant damage to anything with so much as clothes on. Due to their [`[NOT_BUTCHERABLE]`](/index.php/Creature_token#NOT_BUTCHERABLE "Creature token") token, they are not butcherable if killed by a hunter, but tame ones will yield a skull and occassional 2 meat when slaughtered. All ravens are born with Legendary skill in climbing.

Ravens can be captured in cage traps and trained into cheap pets. They are useless for a meat industry due to giving nothing but a skull if trained and butchered, but can be a minor source of eggs (who are nonetheless surpassed by all domestic birds).

In reanimating evil biomes, undead raven swarms can absolutely live up to their grim reputation. Necromancers or evil biome reanimating ravens, even without being "giant", are existential threats to a whole fortress, as are nearly any mid-to-large size flyer.

Some dwarves like ravens for their *intelligence*.

|  |
|----|
| "Raven" in other / Languages / Dwarven / : / toltot / Elven / : / ceca / Goblin / : / rosp / Human / : / tuma |

Admired for its *intelligence*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Ravens have a decent pet value, though they sometimes have the disconcerting habit of tapping on your chamber doors.

Also, a high-ranking female Noble may require a tower full of ravens to keep as a symbol of her nobility. To satisfy her request, make sure you devoid the tower of any mean of escape, and only use the magnificent wild ravens (or even better, giant wild ravens). She will appreciate it.

Some moody hood makers have claimed that a raven is like a writing desk, but whether or not that's true is a secret closely guarded by the clothier's guild, who simply smile when asked.

    1 kph

    Ravens were sponsored by the generous contributions of the Bay 12 community.

        Corvus Corax sponsored by Melkorp
        "Ravens are 'inventors'; that is, they have the ability to solve problems presented to them."
        Thes33 - "Neverdwarf."

    [CREATURE:BIRD_RAVEN]
        [DESCRIPTION:A small, foreboding black bird that feeds on carrion.  It is social, very intelligent, and knows how to use tools.]
        [NAME:raven:ravens:raven]
        [CASTE_NAME:raven:ravens:raven]
        [GENERAL_CHILD_NAME:raven hatchling:raven hatchlings]
        [CREATURE_TILE:'r'][COLOR:0:0:1]
        [PETVALUE:25][NATURAL][PET]
        [BIOME:GRASSLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:FOREST_TAIGA]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:ANY_TEMPERATE_WETLAND]
        [BIOME:TUNDRA]
        [BIOME:ANY_DESERT]
        [LARGE_ROAMING][FREQUENCY:100]
        [POPULATION_NUMBER:250:500]
        [CLUSTER_NUMBER:2:10]
        [SMALL_REMAINS]
        [BENIGN][FLIER]
        [CHILD:1]
        [DIURNAL]
        [HOMEOTHERM:10071]
        [SWIMS_INNATE]
        [MUNDANE]
        [NOT_BUTCHERABLE]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [PREFSTRING:intelligence]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:RIBCAGE]
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
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:50]
        [BODY_SIZE:1:0:1200]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:40]
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
                [EGG_SIZE:52]
                [CLUTCH_SIZE:3:7]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:feathers:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
