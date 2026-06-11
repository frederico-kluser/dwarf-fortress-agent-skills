# Common snapping turtle

> Fonte: [Common snapping turtle](https://dwarffortresswiki.org/index.php/Common_snapping_turtle) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes common snapping turtles for their powerful bites.**
- **Biome**
- **Temperate Freshwater River Temperate Brackish River Temperate Freshwater Lake Temperate Brackish Lake Temperate Freshwater Pool Temperate Brackish Pool**
- **Variations**
- **Common snapping turtle - Snapping turtle man - Giant snapping turtle**
- **Attributes**
- **Amphibious · Shell · Egglaying**
- **Tamed Attributes**
- **Pet value:** 25
- **Not hunting/war trainable**
- **Size**
- **Birth:** 40 cm 3
- **Max:** 30,000 cm 3
- **Food products**
- **Eggs:** 5-10
- **Age**
- **Adult at:** Birth
- **Max age:** 30-50
- **Butchering returns**
- **Food items**
- **Meat:** 13
- **Fat:** 13
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
- **Bones:** 12
- **Skull:** 1
- **Shell:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized reptile with a thick shell, which it can retreat into when threatened. This creature can administer a painful bite.*

**Common snapping turtles** are smaller cousins of alligator snapping turtles. They appear individually in temperate lakes and rivers. About half the size of an average dwarf, they are aggressive and will fight back when provoked, though they prefer to flee if given the chance.

They can be caught in cage traps, and are a decent source of eggs and meat, should you capture a breeding pair, but keep in mind that you won't be able to fully domesticate them. They are fairly long-lived and reach their full size at the age of one year, and should be butchered at that time for the maximum amount of returns. Common snapping turtles have low pet value, so you shouldn't consider selling them as pets. All products from them are worth the same as these from domestic animals.

Some dwarves like common snapping turtles for their *powerful bites* and their *long necks*.

Admired for their *powerful bites*.

    12 kph

    Snapping turtles were sponsored by the generous contributions of the Bay 12 community.

        Intelligent Shade of Blue
        Marshall Burns

    [CREATURE:SNAPPING TURTLE]
        [DESCRIPTION:A medium-sized reptile with a thick shell, which it can retreat into when threatened.  This creature can administer a painful bite.]
        [NAME:common snapping turtle:common snapping turtles:common snapping turtle]
        [CASTE_NAME:common snapping turtle:common snapping turtles:common snapping turtle]
        [CREATURE_TILE:'t'][COLOR:2:0:0]
        [PETVALUE:25]
        [LARGE_ROAMING]
        [AMPHIBIOUS]
        [NATURAL][PET_EXOTIC]
        [CARNIVORE]
        [BIOME:RIVER_TEMPERATE_FRESHWATER]
        [BIOME:RIVER_TEMPERATE_BRACKISHWATER]
        [BIOME:LAKE_TEMPERATE_FRESHWATER]
        [BIOME:LAKE_TEMPERATE_BRACKISHWATER]
        [BIOME:POOL_TEMPERATE_FRESHWATER]
        [BIOME:POOL_TEMPERATE_BRACKISHWATER]
        [POPULATION_NUMBER:25:50]
        [PREFSTRING:powerful bites]
        [PREFSTRING:long necks]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:BEAK:RIBCAGE:SHELL]
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
        [BODY_SIZE:0:0:40]
        [BODY_SIZE:1:0:30000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:30:50]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:BEAK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_CANLATCH]
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
                [EGG_SIZE:50]
                [CLUTCH_SIZE:5:10] actually much higher
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:DARK_GREEN:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
