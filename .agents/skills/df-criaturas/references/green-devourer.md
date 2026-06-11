# Green devourer

> Fonte: [Green devourer](https://dwarffortresswiki.org/index.php/Green_devourer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes green devourers for their bizarre appearance.**
- **Biome**
- **Underground Depth: 2-3**
- **Cannot be tamed**
- **Size**
- **Birth:** 2,000 cm 3
- **Mid:** 20,000 cm 3
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** 2
- **Max age:** 30-50
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 13
- **Fat:** 9
- **Brain:** 1
- **Heart:** 1
- **Intestines:** 1
- **Raw materials**
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized monster walking on two clawed legs. It has two mouths on the ends of a pair of tentacles. It uses its mouths to digest its victims with acid and rows of razor-like teeth.*

**Green devourers** are very rare creatures who inhabit the second and third layers of the caverns. These tentacled monsters, with each tendril ending in a toothy mouth, spawn individually and wander the underground, potentially picking fights with other creatures who provoke them (like passing dwarves). They are as large as humans and may deliver some nasty damage to unarmed civilians with their bites, but an armored squad will have very little problem dispatching them.

A dead green devourer can be butchered for a fair amount of returns, except bones, as they, bizarrely, lack those. Products made from their parts are worth 3 times more than those made from common domestic animals. Green devourers possess a pet value of 200, but lack the necessary tokens to be trainable.

Unlike most creatures, green devourers can't be spawned in the object testing arena.

Some dwarves like green devourers for their *bizarre appearance*.

|  |
|----|
| "Green devourer" in other / Languages / Dwarven / : / omer noshtath / Elven / : / liba famolo / Goblin / : / astru usmka / Human / : / el stom |

## Gallery

-

  The stuff of night terrors.\
  *Art by Quinmael*

-

  Second depiction in standard anatomical position.\
  *Art by Rhynca-Rook*

-

  "Latch-on suckers that secrete acid, then devour."\
  *Concept art by Bay 12 Games.*

    [CREATURE:GREEN_DEVOURER]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A medium-sized monster walking on two clawed legs.  It has two mouths on the ends of a pair of tentacles.  It uses its mouths to digest its victims with acid and rows of razor-like teeth.]
        [NAME:green devourer:green devourers:green devourer]
        [CASTE_NAME:green devourer:green devourers:green devourer]
        [CREATURE_TILE:'G'][COLOR:2:0:1]
        [PETVALUE:200]
        [NATURAL]
        [LARGE_ROAMING][FREQUENCY:10]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [PREFSTRING:bizarre appearance]
        [EXTRAVISION]
        [BODY:HUMANOID_ARMLESS:TWO_NO_CLAW_TENTACLES:TENTACLE_MOUTH:TENTACLE_TEETH:HEART:GUTS:BRAIN]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:BONE]
            [REMOVE_MATERIAL:CARTILAGE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:BONE]
            [REMOVE_TISSUE:CARTILAGE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:NONE:NONE]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
            [TL_MAJOR_ARTERIES]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [NOBONES]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:2000]
        [BODY_SIZE:2:0:20000]
        [BODY_SIZE:10:0:70000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:30:50]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:TENTACLE:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [CHILD:2]
        [ALL_ACTIVE]
        [HOMEOTHERM:10040]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [SWIMS_INNATE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GREEN:1]
                    [TLCM_NOUN:skin:SINGULAR]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
