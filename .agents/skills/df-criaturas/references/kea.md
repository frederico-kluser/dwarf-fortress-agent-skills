# Kea

> Fonte: [Kea](https://dwarffortresswiki.org/index.php/Kea) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kea for their curiosity.**
- **Biome**
- **Any Temperate Forest Temperate Shrubland Mountain**
- **Variations**
- **Kea - Kea man - Giant kea**
- **Attributes**
- **Flying · Steals food · Steals items · Egglaying**
- **Tamed Attributes**
- **Pet value:** 25
- **Not hunting/war trainable**
- **Size**
- **Birth:** 60 cm 3
- **Mid:** 500 cm 3
- **Max:** 1,000 cm 3
- **Food products**
- **Eggs:** 2-5
- **Age**
- **Adult at:** 1
- **Max age:** 30-50
- **Butchering returns**
- **Food items**
- **Meat:** 0-2
- **Raw materials**
- **Skull:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, green, intelligent mountain parrot.*

**Kea** are flying pests that like to steal valuable items. They are attracted to things like cloth, gems, metal bars, stacks of crossbow bolts, and even wheelbarrows or anvils. They may even steal fish from a barrel after interrupting the dwarf hauling it - and anyone else nearby. They are similar to a raccoon or rhesus macaque, but smaller and winged; their ability to fly makes them extremely annoying if they find a way into any unoccupied areas of your fortress.

Kea are skittish around other creatures, so pastured livestock are generally enough to send them winging away empty-clawed. Unfortunately, the livestock appear to be equally scared of the pilfering pests, so your dwarves will spend considerable time herding them back into their pastures when a kea flock appears.

Kea are too small to be butchered, but may be a source of eggs if captured and trained. They can and will draw blood on small pets, like cats, and d(unarmored) dwarves. A newly-embarking group of dwarves will sometimes find their wagon "Wagon (embark)") immediately beset by a flock of kea, their stuff stolen, and days ruined thereby. (It is *always* a good defensive measure is to move the contents of your wagon underground as quickly as possible, using temporary stockpiles in your fortress entrance if necessary. This will force the pests to stop flying if they want to come and steal something, making them no more or less threatening than other thieving beasts.)

Some dwarves like kea for their *curiosity* and their *intelligence*.

Admired for its *curiosity*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Apparently, undead versions of kea are instantly transformed into kung-fu masters at the moment of their ensorcelment, being witnessed on multiple occasions to shatter the bones of dwarf-sized creatures (including femurs) through bronze and steel armor with no more than a light tap from one of their toes -- as utterly improbable as it may seem for a bird their size. The only scholarly explanation for this odd phenomenon so far is that it may be a cruel joke by Armok himself.

Axes stolen by these birds are destined to never appear again, whisked away to some distant location. Explorers have been recorded seeking the massive amounts of metals that these avian caches must contain, but none have ever hit paydirt.

    1 kph

    Kea were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:BIRD_KEA]
        [DESCRIPTION:A small, green, intelligent mountain parrot.]
        [NAME:kea:kea:kea]
        [CASTE_NAME:kea:kea:kea]
        [GENERAL_CHILD_NAME:kea chick:kea chicks]
        [CREATURE_TILE:'k'][COLOR:2:0:0]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:5:10][LOOSE_CLUSTERS]
        [NATURAL]
        [LARGE_ROAMING]
        [CURIOUSBEAST_EATER]
        [CURIOUSBEAST_ITEM]
        [PETVALUE:25]
        [PET_EXOTIC]
        [FLIER]
        [BONECARN]
        [CHILD:1]
        [ALL_ACTIVE]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:MOUNTAIN]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [MUNDANE]
        [PREFSTRING:curiosity]
        [PREFSTRING:intelligence]
        [BODY:HUMANOID_ARMLESS_NECK:2WINGS:2EYES:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES:BEAK:TONGUE:RIBCAGE]
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
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [BODY_SIZE:0:0:60]
        [BODY_SIZE:1:0:500]
        [BODY_SIZE:2:0:1000]
        [MAXAGE:30:50]
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
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:62]
                [CLUTCH_SIZE:2:5]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:FEATHER]
                [TL_COLOR_MODIFIER:OLIVE:1]
                    [TLCM_NOUN:feathers:PLURAL]
                want orange feathers under the wings
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
