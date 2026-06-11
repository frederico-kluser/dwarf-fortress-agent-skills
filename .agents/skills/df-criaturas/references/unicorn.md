# Unicorn

> Fonte: [Unicorn](https://dwarffortresswiki.org/index.php/Unicorn) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes unicorns for their horns.**
- **Biome**
- **Taiga Any Temperate Forest Any Tropical Forest Temperate Shrubland Tropical Shrubland**
- **Attributes**
- **Alignment:** Good
- **Grazer · Mount · Horn · Horn**
- **Tamed Attributes**
- **Pet value:** 1,000
- **Not hunting/war trainable**
- **Size**
- **Birth:** 60,000 cm 3
- **Mid:** 300,000 cm 3
- **Max:** 600,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×4)**
- **Food items**
- **Meat:** 10-22
- **Fat:** 9
- **Brain:** 2
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 14
- **Skull:** 1
- **Hooves:** 4
- **Horns:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A horse-like creature with a spiral horn growing from its forehead.*

**Unicorns** are large creatures found in good-aligned forests and shrublands, where they spawn in fairly large herds. Somewhat larger than the average horse, unicorns will normally flee when approached by a dwarf, though if cornered, they will attempt to impale them with their horns. Despite this, a crossbow-wielding hunter or an equipped military squad will usually fare well against unicorns, providing your fort with a big equine meal.

Unicorns can be captured in cage traps and trained into very valuable pets, and tame ones may be brought in elven caravans. While they're not considered domestic animals to elves (like beak dogs are to goblins), they're usually found under their employ anyway, and may appear as attack animals or mounts in the event of a siege. Raiding an elven settlement may lead your dwarves to bring numerous tame unicorns to your fortress as spoils, which is the easiest way to get a hold of the creatures. They give a decent amount of returns when butchered, and products made from their parts are worth four times as much as those made from common animals, making unicorn theft in the name of profit an attractive proposition.

Some dwarves like unicorns for their *horns*.

The beauty of embarking in a good biome.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

It's been rumored that some unicorns (especially purple ones with an affinity for books) are able to cast spells, making them among the first creatures to use magic, but this has yet to have concrete proof. It is also believed that the movement of the sun and the moon is also due to some similar form of equine magic, but that's just silly, as it implies geocentrism, and we all know that Armok likes his worlds flat and square.

Tales about a noble human falling in love with a unicorn and teaching her regret are most definitely probably just that, tales. Although beasts made of flame, which feature prominently in the most widespread version of the story, are of course a common occurrence. Investigations about the story's veracity have mostly concentrated on finding a so-called "Man's Road" in the sea. The lack of safe sea travel alone makes finding that road neigh impossible. That's all I've got to say.

    [CREATURE:UNICORN]
        [DESCRIPTION:A horse-like creature with a spiral horn growing from its forehead.]
        [NAME:unicorn:unicorns:unicorn]
        [CASTE_NAME:unicorn:unicorns:unicorn]
        [CREATURE_TILE:'U'][COLOR:7:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:1000]
        [PREFSTRING:horns]
        [VISION_ARC:50:310]
        [GOOD]
        [LARGE_ROAMING]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [GRASSTRAMPLE:0]
        [NO_VEGETATION_PERTURB]
        [STANDARD_GRAZER]
        [BIOME:FOREST_TAIGA]
        [BIOME:ANY_TEMPERATE_FOREST]
        [BIOME:ANY_TROPICAL_FOREST]
        [BIOME:SHRUBLAND_TEMPERATE]
        [BIOME:SHRUBLAND_TROPICAL]
        [BENIGN][MEANDERER]
        [BODY:QUADRUPED_NECK_HOOF:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE:HEAD_HORN:EYELIDS:CHEEKS]
        [PET]
        [MOUNT]
        [PACK_ANIMAL]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
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
        [BODY_SIZE:0:0:60000]
        [BODY_SIZE:1:0:300000]
        [BODY_SIZE:2:0:600000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:BITE:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:stab:stabs]
            [ATTACK_CONTACT_PERC:5]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:HOOF_REAR]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_CANLATCH]
        [CHILD:1][GENERAL_CHILD_NAME:unicorn foal:unicorn foals]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:375:250:125:1900:2900] 70 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
            [TL_COLOR_MODIFIER:WHITE:1]
                [TLCM_NOUN:hair:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:WHITE:1]
                [TLCM_NOUN:skin:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
            [TL_COLOR_MODIFIER:IRIS_EYE_GOLD:1]
                [TLCM_NOUN:eyes:PLURAL]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:4]
