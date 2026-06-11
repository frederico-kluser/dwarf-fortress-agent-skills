# Draltha

> Fonte: [Draltha](https://dwarffortresswiki.org/index.php/Draltha) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes dralthas for their lustrous manes.**
- **Biome**
- **Underground Depth: 1-2**
- **Attributes**
- **Grazer**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 50,000 cm 3
- **Mid:** 100,000 cm 3
- **Max:** 2,500,000 cm 3
- **Age**
- **Adult at:** 5
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 25-108
- **Fat:** 12-36
- **Brain:** 2-3
- **Heart:** 1
- **Lungs:** 4-6
- **Intestines:** 7-10
- **Liver:** 2-3
- **Kidneys:** 2
- **Tripe:** 2-3
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 28-40
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large, long-bodied grazer with a thick mane that feeds on the tops of towercap mushrooms deep under the earth.*

**Dralthas** are massive creatures who dwell on the first and second underground layers. They don't actively seek fights but are huge creatures—about half the weight of an elephant—and able to kill a dwarf with ease, often ripping them in half in the process. It is advisable to herd them into cage traps, or keep dwarves away from them if they make their way into commonly used pathways, as they will attack if dwarves brush by them enough.

Once captured, dralthas can be trained with an animal trainer, and have a high pet value of 500. Draltha products are worth three times as much as those from domestic animals, and they are common enough to make capturing a herd for breeding easy. Their large size means they produce a good amount of meat and bones when butchered. Keep in mind that they are grazing creatures, which require a pasture in order to survive once trained. Because of their size, each will need a fairly large pasture.

Unlike most animals, dralthas can't be spawned in the object testing arena.

Some dwarves like dralthas for their *lustrous manes*.

## Gallery

-

  *Art by kruggsmash*

-

  *Concept art by Bay 12 Games.*

-

  *Art by Neoriceisgood.*

    [CREATURE:DRALTHA]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A large, long-bodied grazer with a thick mane that feeds on the tops of towercap mushrooms deep under the earth.]
        [NAME:draltha:dralthas:draltha]
        [CASTE_NAME:draltha:dralthas:draltha]
        [CHILD:5]
        [CREATURE_TILE:'D'][COLOR:6:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:500]
        [PET_EXOTIC]
        [STANDARD_GRAZER]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:2]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:2:5]
        [BENIGN][MEANDERER][NATURAL]
        [PREFSTRING:lustrous manes]
        [BODY:QUADRUPED_NECK:2EYES:2EARS:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
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
        [BODY_SIZE:0:0:50000]
        [BODY_SIZE:2:0:100000]
        [BODY_SIZE:5:0:2500000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ATTACK:KICK:BODYPART:BY_CATEGORY:FOOT_FRONT]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_WITH]
            [ATTACK_FLAG_BAD_MULTIATTACK]
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
        [LOW_LIGHT_VISION:10000]
        [HOMEOTHERM:10050]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:YELLOW:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:ECRU:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_BROWN:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
