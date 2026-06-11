# Pangolin

> Fonte: [Pangolin](https://dwarffortresswiki.org/index.php/Pangolin) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes pangolins for their overlapping scales.**
- **Biome**
- **Tropical Grassland Tropical Savanna Tropical Shrubland Any Tropical Forest**
- **Variations**
- **Pangolin - Pangolin man - Giant pangolin**
- **Tamed Attributes**
- **Pet value:** 20
- **Not hunting/war trainable**
- **Size**
- **Birth:** 500 cm 3
- **Mid:** 2,500 cm 3
- **Max:** 5,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 6-7
- **Fat:** 6-7
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small mammal covered in hard scales. It has a long nose and tongue which it uses to feed.*

**Pangolins** are small creatures found in tropical plains and forests. They spawn one at a time and wander through the map, eating bugs along the way. They are only as big as a cat and will run away if threatened, making them harmless to your dwarf civilians and an easy target for your hunters.

Pangolins can be captured in cage traps and trained into low-value pets. If a breeding pair is obtained, they can be bred either to populate the fort with more pangolins or to be butchered for meat, though their small size means they create few products. Additionally, pangolins are distinct for being covered in scales rather than normal hide, which makes them useless for creating leather.

Some dwarves like pangolins for their *overlapping scales*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Despite popular belief, pangolins (alongside bats) will *not* cause a long-lasting outbreak of any type of disease; therefore workshops do not need to be quarantined or outright abandoned. Nor do face masks (aside from armor) need to be made.

Admired for its *overlapping scales*.

    1 kph

    Pangolins were sponsored by the generous contributions of the Bay 12 community.

    [CREATURE:PANGOLIN]
        [DESCRIPTION:A small mammal covered in hard scales.  It has a long nose and tongue which it uses to feed.]
        [NAME:pangolin:pangolins:pangolin]
        [CASTE_NAME:pangolin:pangolins:pangolin]
        [GENERAL_CHILD_NAME:baby pangolin:baby pangolins]
        [CREATURE_TILE:'p'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:20]
        [PET_EXOTIC]
        [VISION_ARC:50:310]
        [NATURAL]
        [BIOME:GRASSLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:ANY_TROPICAL_FOREST]
        [LARGE_ROAMING]
        [GOBBLE_VERMIN_CLASS:EDIBLE_GROUND_BUG]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [BENIGN][MEANDERER]
        [PREFSTRING:overlapping scales]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:5TOES_RQ_REG:MOUTH:TONGUE:RIBCAGE]
        [BODYGLOSS:PAW]
        [GRASSTRAMPLE:0]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:SKIN]
            [REMOVE_MATERIAL:LEATHER]
            [REMOVE_MATERIAL:PARCHMENT]
            [USE_MATERIAL_TEMPLATE:SCALE:SCALE_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:SKIN]
            [USE_TISSUE_TEMPLATE:SCALE:SCALE_TEMPLATE]
            [SELECT_TISSUE:HAIR]
                [INSULATION:100]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SCALE:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
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
        [BODY_SIZE:0:0:500]
        [BODY_SIZE:1:0:2500]
        [BODY_SIZE:2:0:5000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:MOUTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [RETRACT_INTO_BP:BY_CATEGORY:BODY_UPPER:roll into a ball:rolls into a ball:unroll:unrolls]
        [ROOT_AROUND:BY_CATEGORY:NOSE:root around in:roots around in]
        [CHILD:1]
        [NOCTURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:TAN:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:TAN:1]
                    [TLCM_NOUN:scales:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
