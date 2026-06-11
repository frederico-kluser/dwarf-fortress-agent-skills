# Alligator

> Fonte: [Alligator](https://dwarffortresswiki.org/index.php/Alligator) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes alligators for their strength.**
- **Biome**
- **Temperate Freshwater Swamp Temperate Freshwater Marsh Tropical Freshwater Swamp Tropical Freshwater Marsh Temperate Freshwater River Tropical Freshwater River Temperate Brackish River Tropical Brackish River**
- **Variations**
- **Alligator - Alligator man - Giant alligator**
- **Attributes**
- **Amphibious · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 650
- **Not hunting/war trainable**
- **Size**
- **Birth:** 60 cm 3
- **Mid:** 200,000 cm 3
- **Max:** 400,000 cm 3
- **Food products**
- **Eggs:** 10-30
- **Age**
- **Adult at:** 1
- **Max age:** 60-100
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 18-22
- **Fat:** 17
- **Brain:** 1
- **Gizzard:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 21
- **Skull:** 1
- **Skin:** Scales
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge reptile, found in rivers and marshlands. It is an ambush predator, solitary and territorial.*

**Alligators** are intimidating beasts found in and around temperate and tropical fresh water rivers and lakes. They are not tremendously aggressive animals, but will attack dwarves who venture foolishly close. They appear in clusters of 1-3, and, surprisingly, are not any faster in the water than an average land-based creature that can swim is - say, a dwarf.

With an egg yield of 10-30 per clutch, a large size (and thus high butchering returns), a derived product value three times that of a much more boring domestic animal, and a high pet value, alligators are one of the best egg producing creatures a fortress could have. As an added bonus, a trained group of gators serves as a credible threat to invaders. As an exotic mount, sieges may occasionally arrive on the map riding tame alligators, giving their riders a significant combat advantage, as well as the ability to cross or swim through large bodies of water (although this occasionally, and hilariously, has lethal results for their air-breathing riders).

Some dwarves like alligators for their *strength*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Rumor has it that the humans tan alligator scales into leather, which is then used to make high boots. Their merchants vociferously deny this, claiming that only elves would try such a thing.

\

Admired for its *strength*.

## See also

- Alligator man

    5 kph

    [CREATURE:ALLIGATOR]
        [DESCRIPTION:A huge reptile, found in rivers and marshlands.  It is an ambush predator, solitary and territorial.]
        [NAME:alligator:alligators:alligator]
        [CASTE_NAME:alligator:alligators:alligator]
        [CHILD:1][GENERAL_CHILD_NAME:alligator hatchling:alligator hatchlings]
        [CREATURE_TILE:'A'][COLOR:2:0:0]
        [AMPHIBIOUS]
        [BIOME:SWAMP_TEMPERATE_FRESHWATER]
        [BIOME:MARSH_TEMPERATE_FRESHWATER]
        [BIOME:SWAMP_TROPICAL_FRESHWATER]
        [BIOME:MARSH_TROPICAL_FRESHWATER]
        [BIOME:RIVER_TEMPERATE_FRESHWATER]
        [BIOME:RIVER_TROPICAL_FRESHWATER]
        [BIOME:RIVER_TEMPERATE_BRACKISHWATER]
        [BIOME:RIVER_TROPICAL_BRACKISHWATER]
        [LARGE_ROAMING][DIFFICULTY:2]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [CARNIVORE][NATURAL]
        [MEANDERER]
        [PETVALUE:650]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [CANNOT_JUMP]
        [LARGE_PREDATOR]
        [GRASSTRAMPLE:20]
        [PREFSTRING:strength]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:GIZZARD:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:4TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
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
        [EXTRA_BUTCHER_OBJECT:BY_CATEGORY:GIZZARD]
            [EBO_ITEM:SMALLGEM:NONE:ANY_HARD_STONE]
            [EBO_SHAPE:GIZZARD_STONE]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:60]
        [BODY_SIZE:1:0:200000]
        [BODY_SIZE:2:0:400000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:60:100]
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
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:1422:1127:831:488:2500:3700] 18 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:3251:2446:1640:798:4600:6500] 11 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:80]
                [CLUTCH_SIZE:10:30]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
