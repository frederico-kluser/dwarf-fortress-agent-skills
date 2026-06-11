# Rutherer

> Fonte: [Rutherer](https://dwarffortresswiki.org/index.php/Rutherer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rutherers for their enormous tails.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 600
- **Not hunting/war trainable**
- **Size**
- **Birth:** 300,000 cm 3
- **Mid:** 1,500,000 cm 3
- **Max:** 3,000,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 40-60
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 90
- **Fat:** 13
- **Brain:** 3
- **Heart:** 1
- **Lungs:** 6
- **Intestines:** 10
- **Liver:** 3
- **Kidneys:** 2
- **Tripe:** 3
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 37
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster with an enormous tail, covered with thick fur. They run on four legs and can be found deep under the earth.*

**Rutherers** are massive creatures who can be found meandering on the second and third layers of the caverns, appearing in groups of 3-7 individuals. An adult rutherer weighs around 3 tonnes, which is about 50 times heavier than a dwarf, though, despite this, they are in fact entirely benign, fleeing from anything they may consider a threat. In the event they engage in battle, they will use their massive size to easily tear dwarves apart with bites and kicks. They are exotic mounts and may be ridden by goblins during sieges.

Rutherers can be captured in cage traps and trained into valuable pets. They provide a great quantity of returns when butchered, and products made from their parts are worth 3 times more than those of common domestic animals. This makes the idea of a rutherer farm an attractive one, especially since the creatures constantly give birth to more than one baby at a time. However, rutherers only reach their maximum size after 5 years, considerably longer than most sources of food, and they take **10 years** to become adults, which means domesticating them and building a significant breeding population can take a very long time.

Unlike most beasts, rutherers can't be spawned in the object testing arena.

Some dwarves like rutherers for their *enormous tails*.

## Gallery

-

  Admired for their *enormous tails*.\
  *Art by Buttery_Mess*

-

  Actually an uncomfortable ride.\
  *Art by Arne*

-

  "It is furry with a big tail." Dwarf for scale.\
  *Concept art by Bay 12 Games.*

    [CREATURE:RUTHERER]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A huge monster with an enormous tail, covered with thick fur.  They run on four legs and can be found deep under the earth.]
        [NAME:rutherer:rutherers:rutherer]
        [CASTE_NAME:rutherer:rutherers:rutherer]
        [CHILD:10]
        [CREATURE_TILE:'R'][COLOR:7:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:600]
        [PET_EXOTIC]
        [MOUNT_EXOTIC]
        [LARGE_ROAMING]
        [LOW_LIGHT_VISION:10000]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:7]
        [BENIGN][MEANDERER][NATURAL]
        [PREFSTRING:enormous tails]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:GENERIC_TEETH:RIBCAGE]
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
        [BODY_SIZE:0:0:300000]
        [BODY_SIZE:2:0:1500000]
        [BODY_SIZE:5:0:3000000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:40:60]
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
        [HOMEOTHERM:10050]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:730:561:351:1900:2900] 25 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:HAIR]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:BLUE:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_GREEN:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
