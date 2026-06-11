# Saltwater crocodile

> Fonte: [Saltwater crocodile](https://dwarffortresswiki.org/index.php/Saltwater_crocodile) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes saltwater crocodiles for their strength.**
- **Biome**
- **Tropical Freshwater Swamp Tropical Freshwater Marsh Tropical Saltwater Swamp Tropical Saltwater Marsh Mangrove Swamp Tropical Saltwater River Tropical Brackish River Tropical Freshwater River**
- **Variations**
- **Saltwater crocodile - Saltwater crocodile man - Giant saltwater crocodile**
- **Attributes**
- **Amphibious · Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 700
- **Not hunting/war trainable**
- **Size**
- **Birth:** 60 cm 3
- **Mid:** 400,000 cm 3
- **Max:** 800,000 cm 3
- **Food products**
- **Eggs:** 20-70
- **Age**
- **Adult at:** 3
- **Max age:** 60-100
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 0-33
- **Fat:** 0-28
- **Brain:** 0-1
- **Heart:** 0-1
- **Lungs:** 0-2
- **Intestines:** 0-2
- **Liver:** 0-1
- **Kidneys:** 0-2
- **Tripe:** 0-1
- **Sweetbread:** 0-1
- **Eyes:** 0-2
- **Spleen:** 0-1
- **Raw materials**
- **Bones:** 0-34
- **Skull:** 0-1
- **Skin:** Scales
- **Gizzard stone:** 1

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge, predatory reptile found in coastal marshes and river deltas. It ambushes its prey at the shore and uses its great size to drag the victim under and drown them.*

**Saltwater crocodiles** are large and aggressive exotic reptiles. Found in many wetland biomes (including freshwater biomes, despite their name), these creatures have a considerable pet value and are trainable. Though wild saltwater crocodiles generally do not wade far from the water's edge, they can be a major hazard to any dwarf whose job takes him near water. Fortunately, they are hard to provoke and most of the time will not chase your dwarves far.

Saltwater crocodiles have the greatest egg-laying potential of any animal in the game, with 20-70 eggs per clutch. This makes them ideal animals to use for egg production. Considering the value of a single crocodile and the benefits of having 100+ tamed crocs watching over your dwarves, a breeding pair can be quite valuable. Taking two years to reach full size, they could power a valuable meat industry for a patient player. Tame saltwater crocodiles are also excellent animals to put into your moat, as they are amphibious, aggressive towards enemies when trained and most goblins do not know how to swim, giving a serious edge to your reptilian guards. They will also NOT attack your dwarves. Putting wild crocodiles into your moat or putting any crocodile into your magma moat is of course a recipe for fun.

Some dwarves like saltwater crocodiles for their *strength*.

Admired for its *strength*

Crocodile leather armor

\

    1 kph

    [CREATURE:CROCODILE_SALTWATER]
        [DESCRIPTION:A huge, predatory reptile found in coastal marshes and river deltas.  It ambushes its prey at the shore and uses its great size to drag the victim under and drown them.]
        [NAME:saltwater crocodile:saltwater crocodiles:saltwater crocodile]
        [CASTE_NAME:saltwater crocodile:saltwater crocodiles:saltwater crocodile]
        [CHILD:3][GENERAL_CHILD_NAME:saltwater crocodile hatchling:saltwater crocodile hatchlings]
        [CREATURE_TILE:'C'][COLOR:2:0:0]
        [PETVALUE:700]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [AMPHIBIOUS]
        [BIOME:SWAMP_TROPICAL_FRESHWATER]
        [BIOME:MARSH_TROPICAL_FRESHWATER]
        [BIOME:SWAMP_TROPICAL_SALTWATER]
        [BIOME:MARSH_TROPICAL_SALTWATER]
        [BIOME:SWAMP_MANGROVE]
        [BIOME:RIVER_TROPICAL_SALTWATER]
        [BIOME:RIVER_TROPICAL_BRACKISHWATER]
        [BIOME:RIVER_TROPICAL_FRESHWATER]
        [LARGE_ROAMING][FREQUENCY:5][DIFFICULTY:2]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:3]
        [CARNIVORE][NATURAL]
        [MEANDERER]
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
        [BODY_SIZE:0:0:60] 60 grams!
        [BODY_SIZE:1:0:400000]
        [BODY_SIZE:2:0:800000]
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
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:1683:1315:947:516:2800:4100] 17 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:714:529:303:1900:2900] 29 kph
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:100]
                [CLUTCH_SIZE:20:70]
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
