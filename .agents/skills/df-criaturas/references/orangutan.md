# Orangutan

> Fonte: [Orangutan](https://dwarffortresswiki.org/index.php/Orangutan) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes orangutans for their antics.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 8,000 cm 3
- **Mid:** 40,000 cm 3
- **Max:** 80,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 40-80
- **Butchering returns**
- **Food items**
- **Meat:** 12-13
- **Fat:** 12
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
- **Bones:** 14
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge intelligent ape found in the tropical forests. It is bright red and found living in the trees.*

**Orangutans** are very rare and solitary apes found exclusively in tropical moist broadleaf forests. While larger than the average human, they're benign and timid by nature, and as such make easy targets for a dwarven hunter. All orangutans are born with Legendary skill in climbing.

Orangutans can be captured in cage traps and trained into valuable exotic pets. Due to their rarity, they make poor targets for a meat industry, though they give a decent amount of returns if butchered. Orangutans are long-lived for animals, and they take 10 years to reach adulthood, though they're fully grown by the age of 2. Like most species of ape in the game, they aren't naturally capable of swimming and will likely drown if submerged in water.

Some dwarves like orangutans for their *long arms*, their *colourful fur* and *antics*.

Admired for its *antics*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
It should be noted that some orangutans have shown extreme aggression towards dwarves who refer to them as monkeys, as they are actually apes. Also they apparently make good librarians.

Just as goblins are reviled by dwarves for kidnapping their young (among other things), human villagers are openly suspicious of any orangutan nobles snooping about - perhaps if the orangutan "civilization" had any goods to offer in trade for the invention of fire, they would be open to discuss parting with a "man-cub." Dwarves, on the other hand, would never claim to have invented fire, knowing that it is a gift of Armok; nevertheless, lessons on the subject are made available to those who ask for it.

Some orangutans call themselves king, but this is rarely understood except by some human strays.

    [CREATURE:ORANGUTAN]
        [DESCRIPTION:A huge intelligent ape found in the tropical forests.  It is bright red and found living in the trees.]
        [NAME:orangutan:orangutans:orangutan]
        [CASTE_NAME:orangutan:orangutans:orangutan]
        [CREATURE_TILE:'O'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [CREATURE_CLASS:HUMANOID_TRACKING_SYMBOL]
        [PETVALUE:500]
        [PET_EXOTIC]
        [NATURAL]
        [BENIGN][MEANDERER]
        [GRASSTRAMPLE:0]
        [LARGE_ROAMING][FREQUENCY:5]
        [POPULATION_NUMBER:20:50]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [PREFSTRING:colorful hair]
        [PREFSTRING:long arms]
        [PREFSTRING:antics]
        [BODY:QUADRUPED_NECK_FRONT_GRASP:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:5TOES_FQ_FINGERS:5TOES_RQ_ANON:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE:FACIAL_FEATURES]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
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
        [BODY_SIZE:0:0:8000]
        [BODY_SIZE:1:0:40000]
        [BODY_SIZE:2:0:80000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:40:80]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [CHILD:10]
        [DIURNAL]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:5951:5419:4898:1463:6944:8233] 6 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_LEARNED]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:ORANGE:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
