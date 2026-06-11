# Pond turtle

> Fonte: [Pond turtle](https://dwarffortresswiki.org/index.php/Pond_turtle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes pond turtles for their shells.**
- **Biome**
- **Any Pool**
- **Variations**
- **Pond turtle - Pond turtle man - Giant pond turtle**
- **Attributes**
- **Amphibious · Exotic pet · Fishable · Shell**
- **Pet value:** 10
- **Active Seasons**
- **Spring Summer Autumn Winter**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny reptile with a shell on its back. It can be found in rivers and ponds.*

**Pond turtles** are a common source of food and one of the few sources of shells. They can be found in any pool of water and are gathered by fishing. Pond turtles can also be found by digging into an aquifer or by creating water outside the area of pre-existing water sources such as rivers or cavern water. One tile is sufficient, so long as the fishing zone covers only that one tile.

Similar to how hedgehogs can roll into a ball, pond turtles can hide in their shell.

To harvest a shell, the raw pond turtle must be processed at a fishery. This will produce a pond turtle shell and an edible pond turtle. If a pond turtle is eaten before it is processed or cooked, no shell will be produced. The described process of catching, then cleaning pond turtles is the only way to get shells from them. Processed pond turtles are categorized as fish in the k Stocks and y Labor menu. The "Pond turtle" food that can be purchased from caravans is already processed and thus cannot be used to procure shells.

Tame live pond turtles can sometimes be bought from merchants. These cannot be set up to slaughter, and if one gets killed by a cat or caught by a web or closing door, the only result will be pond turtle remains, not a raw pond turtle you can take to a fisherdwarf's workshop and process to get a shell.

Some dwarves like pond turtles for their *shells*.

\

Admired for their *shells*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

The pond turtle's elusive cousin, the mighty aquifer turtle, is just like a pond turtle but can be fished in dug aquifers. It is entirely similar to the pond turtle, but one wonders how the turtle can swim between grains of rock in the aquifer and then feed a dwarf.

These wondrous beasts seem to spontaneously generate in dug aquifers, for some reason. Maybe they don't like being in aquifers, so squeeze themselves *really hard* between two grains of rock?

    12 kph

    Pond turtles were sponsored by the generous contributions of the Bay 12 community.

        Shane Phillips

    [CREATURE:POND_TURTLE]
        [DESCRIPTION:A tiny reptile with a shell on its back.  It can be found in rivers and ponds.]
        [NAME:pond turtle:pond turtles:pond turtle]
        [CASTE_NAME:pond turtle:pond turtles:pond turtle]
        [CREATURE_TILE:15][COLOR:2:0:0]
        [PETVALUE:10]
        [VERMIN_FISH][FISHITEM]
        [AMPHIBIOUS][SMALL_REMAINS][NO_WINTER]
        [BENIGN][NATURAL][PET_EXOTIC]
        [NOT_BUTCHERABLE]
        [CARNIVORE]
        [BIOME:ANY_POOL]
        [POPULATION_NUMBER:250:500]
        [PREFSTRING:shells]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE:SHELL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [REMOVE_MATERIAL:HAIR]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:SHELL:SHELL_TEMPLATE]
                [STATE_COLOR:ALL:DARK_GREEN]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [REMOVE_TISSUE:HAIR]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [USE_TISSUE_TEMPLATE:SHELL:SHELL_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:LEATHERY_EGG_MATERIALS]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SCALE:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:SHELL_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:734:568:366:1900:2900] 24 kph
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:5]
        [BODY_SIZE:1:0:500]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:40:100]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [RETRACT_INTO_BP:BY_CATEGORY:SHELL:retract into
     shell:retracts into
     shell:come out of
     shell:comes out of
     shell]
        [DIURNAL]
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:6]
                [CLUTCH_SIZE:1:15]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:DARK_GREEN:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
