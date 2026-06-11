# Elephant

> Fonte: [Elephant](https://dwarffortresswiki.org/index.php/Elephant) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes elephants for their tool use.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland**
- **Variations**
- **Elephant - Elephant man - Giant elephant**
- **Attributes**
- **War animals · Hunting animals · Grazer · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 500,000 cm 3
- **Mid:** 2,500,000 cm 3
- **Max:** 5,000,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 50-70
- **Butchering returns ( Value multiplier ×5)**
- **Food items**
- **Meat:** 36-219
- **Fat:** 13-58
- **Brain:** 4-6
- **Heart:** 2-3
- **Lungs:** 8-12
- **Intestines:** 14-19
- **Liver:** 4-6
- **Kidneys:** 4-6
- **Tripe:** 4-6
- **Sweetbread:** 2-3
- **Spleen:** 2-3
- **Raw materials**
- **Bones:** 49-67
- **Skull:** 1
- **Ivory:** 3
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge, hairless mammal, found grazing in grasslands in groups. It eats plants which it lifts up with its long trunk. When angered, it will attack with its long tusks.*

**Elephants** are massive creatures who inhabit tropical shrublands and forests and the largest terrestrial mundane animals in the game. In past versions of the game, elephants were famed as cold, emotionless, and highly effective dwarf killing machines, blood eternally dripping from their ivory tusks, the bane of even the mightiest of fortresses, so on and so forth. (Size used to be correlated with combat bonuses, both to damage and damage resistance, making them incredibly dangerous animals; today it just translates into more and thicker tissues.) Nonetheless, their sheer size means that they still pack a wallop, sufficient to rip apart even the most well-armored of goblins with ease.

In the wild, elephants appear in clusters of 3-7 individuals, and—their size notwithstanding—can be caught by the same cage traps as any other creature. Elephants may be domesticated by civilizations that settled in tropical regions during worldgen. Additionally, elven caravans may occasionally bring tame elephants with them, if they have settlements in the right locations - the method by which a 1,000 pound donkey carries a 15,000 pound elephant in a cage, on top of whatever else it's carrying, is a deeply veiled elven secret. Trained elephants can be turned further into war and hunting roles (see below; no word yet on how elephant sneaking works, exactly), and are easily the most effective war animals that your fortress can train. In the future, it is planned that they will graze upon trees for food, but for now they eat grass and cave moss like all other grazing animals.

If you plan on breeding elephants, note that elephant calves take 10 years to mature (though they reach full size in only 5 years). Pregnant elephants will give birth to 1-3 calves, and they have longer lives than most animals (50-70 years) as well. Even in death, elephants are wonderful creatures; once butchered, their products are worth *five* times as much as those of more boring animals (like cows), and their great size means that there will be a *lot* of products.

Since they're "War Animals", "Hunting Animals" and "Exotic Mounts", they can also be fielded during sieges. They're used by Human, Elven and Dwarven siegers as tanks - essentially, as budget cave dragons.

Some dwarves like elephants for their *strength*, their *amazing trunks*, their *calves' spirited antics*, their *tusks*, their *great weight*, their *social behavior*, their *flappy ears*, their *uprooting of trees*, their *aggressive sparring*, their *trumpeting*, their *tool use* and their *self-awareness*. They have, by far, the most reasons to be liked by dwarves of all creatures in the game.

\

Admired for its *strength*.

Estimated Elephant Size Comparison.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Every reader will be able to confirm not having ever seen an elephant trying to hide behind a tree. The most astute of these readers will realize that this is due to elephants having an innately sharp hiding ability.

    [CREATURE:ELEPHANT]
        [DESCRIPTION:A huge, hairless mammal, found grazing in grasslands in groups.  It eats plants which it lifts up with its long trunk.  When angered, it will attack with its long tusks.]
        [NAME:elephant:elephants:elephant]
        [CASTE_NAME:elephant:elephants:elephant]
        [CHILD:10][GENERAL_CHILD_NAME:elephant calf:elephant calves]
        [CREATURE_TILE:'E'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:500]
        [PET]
        [STANDARD_GRAZER] don't have browsing trees yet
        [PACK_ANIMAL]
        [MOUNT_EXOTIC]
        [TRAINABLE]
        [LARGE_ROAMING]
        [BIOME:ANY_TROPICAL_FOREST]
        [BIOME:SHRUBLAND_TROPICAL]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [BENIGN][MEANDERER][NATURAL]
        [PREFSTRING:strength]
        [PREFSTRING:amazing trunks]
        [PREFSTRING:calves' spirited antics]
        [PREFSTRING:tusks]
        [PREFSTRING:great weight]
        [PREFSTRING:social behavior]
        [PREFSTRING:flappy ears]
        [PREFSTRING:uprooting of trees]
        [PREFSTRING:aggressive sparring]
        [PREFSTRING:trumpeting]
        [PREFSTRING:tool use]
        [PREFSTRING:self-awareness]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:TRUNK:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:2TUSKS:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:IVORY:TOOTH_TEMPLATE]
                [STATE_NAME:ALL_SOLID:ivory]
                [STATE_ADJ:ALL_SOLID:ivory]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:IVORY:IVORY_TEMPLATE]
                [TISSUE_NAME:ivory:NP]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
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
        [BODY_SIZE:0:0:500000]
        [BODY_SIZE:2:0:2500000]
        [BODY_SIZE:5:0:5000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:50:70]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:GORE:BODYPART:BY_CATEGORY:TUSK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
        [DIURNAL]
        [HOMEOTHERM:10066]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:1422:1127:831:488:2500:3700] 18 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1:IRIS_EYE_GOLD:1:IRIS_EYE_YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:5]
