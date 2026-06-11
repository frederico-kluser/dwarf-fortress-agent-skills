# Molemarian

> Fonte: [Molemarian](https://dwarffortresswiki.org/index.php/Molemarian) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes molemarians for their freakish appearance.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **No Pain**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,000 cm 3
- **Mid:** 12,000 cm 3
- **Max:** 90,000 cm 3
- **Age**
- **Adult at:** 10
- **Max age:** 20-30
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 19
- **Fat:** 19
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
- **Bones:** 21
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A hideous monster that has the body of a giant mole-rat and the torso of a mole-rat man. It is found deep underground.*

**Molemarians** are relatively uncommon creatures found in caverns, from the second layer downwards. They spawn in tiny groups of 1-3 and roam the underground, possibly clashing with dwarves they find in their path. They are able to freely open unforbidden doors and can theoretically equip weapons and armor due to having the [`[EQUIPS]`](/index.php/Creature_token#EQUIPS "Creature token") token.

Molemarians possess the anatomy of a centaur, but rather than being half-human and half-horse, they possess the upper body of a humanoid mole-rat and the lower body of a giant mole-rat - essentially, they are centaur-shaped mole-rats. Like actual naked mole-rats, molemarians are immune to pain and so will not give in to it during combat. Note that, despite having a humanoid mole-rat half, there is no such thing as a mole-rat man in *Dwarf Fortress*.

Despite their centaurid appearance and their ability to equip items, molemarians are not intelligent creatures and can be freely butchered into meat by your dwarves. Products made from their parts are worth twice as much as those made out of common animals. Molemarians possess a pet value of 400, but lack the necessary tokens to be trainable. They can't be spawned in the object testing arena.

Some dwarves like molemarians for their *freakish appearance*.

## Gallery

-

  Stuff of night terrors.\
  *Art by hou_jae04*

-

  *Concept art by Bay 12 Games.*

    [CREATURE:MOLEMARIAN]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A hideous monster that has the body of a giant mole-rat and the torso of a mole-rat man.   It is found deep underground.]
        [NAME:molemarian:molemarians:molemarian]
        [CASTE_NAME:molemarian:molemarians:molemarian]
        [CHILD:10][GENERAL_CHILD_NAME:molemarian puppy:molemarian puppies]
        [PETVALUE:400]
        [CREATURE_TILE:'M'][COLOR:4:0:1]
        [CREATURE_CLASS:MAMMAL]
        [NATURAL]
        [LARGE_ROAMING][FREQUENCY:20]
        [LARGE_PREDATOR]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:1:3]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [PREFSTRING:freakish appearance]
        [NOPAIN]
        [BODY:HAND_FOOT_CENTAUR_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4FINGERS:4TOES:MOUTH:TONGUE:RODENT_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
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
        [EQUIPS]
        [CANOPENDOORS]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:6000]
        [BODY_SIZE:2:0:12000]
        [BODY_SIZE:12:0:90000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:PINK:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
