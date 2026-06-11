# Bushmaster

> Fonte: [Bushmaster](https://dwarffortresswiki.org/index.php/Bushmaster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bushmasters for their deadly bite.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Bushmaster - Bushmaster man - Giant bushmaster**
- **Attributes**
- **Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Birth:** 20 cm 3
- **Mid:** 4,250 cm 3
- **Max:** 8,500 cm 3
- **Food products**
- **Eggs:** 10-20
- **Age**
- **Adult at:** Birth
- **Max age:** 12-24
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 2
- **Fat:** 2
- **Brain:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Tripe:** 1
- **Raw materials**
- **Bones:** 2
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny venomous snake. It is the longest of the pit vipers.*

**Bushmasters** are medium-sized solitary snakes that only appear in tropical moist broadleaf forests. They flee contact, but when threatened their venomous bites provide a more than adequate defense - several nasty and unpleasant health effects, followed shortly by complete paralysis and death by suffocation. Don't approach without a crossbow unless your dwarves are wearing full military armor, upon pain of a quick death. Like all other species of snake, bushmasters take the whole extent of their lives to reach their maximum size, but because of their bite they're still dangerous as juveniles.

Bushmasters can be captured with cage traps and trained into low-value pets. They are somewhat prolific egg-layers, with each clutch ranging between 10 and 20 eggs, which makes them a good target for egg production. Butchering bushmasters for food is not too worth it, as they are small and provide few returns, though products made from bushmaster parts are 2 times more valuable than products made from common animals.

Some dwarves admire bushmasters for their *deadly bite*.

Admired for its *deadly bite*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
The ruler of all shrubs and vegetation; a truly fearsome foe! No, really. This thing causes pain, paralysis, nausea, unconsciousness, dizziness, bleeding, and most likely being eaten by the snake.

|  |
|----|
| "Bushmaster" in other / Languages / Dwarven / : / rorul-kôn / Elven / : / alithi-ithera / Goblin / : / ngontek-âs / Human / : / iwo-siñur |

    12 kph

    Bushmasters were sponsored by the generous contributions of the Bay 12 community.

     |\___/"""""\  ___
    =##BUSHMASTER#|cwc|
     `""""##|_)##\ \==|
          HH    \#\

    [CREATURE:BUSHMASTER]
        [DESCRIPTION:A tiny venomous snake.  It is the longest of the pit vipers.]
        [NAME:bushmaster:bushmasters:bushmaster]
        [CASTE_NAME:bushmaster:bushmasters:bushmaster]
        [CREATURE_TILE:'s'][COLOR:6:0:0]
        [CREATURE_CLASS:POISONOUS]
        [PETVALUE:50]
        [PET_EXOTIC]
        [FREQUENCY:30]
        [NATURAL]
        [CARNIVORE]
        [LARGE_ROAMING]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [POPULATION_NUMBER:10:25]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:deadly bite]
        [BODY:BASIC_1PARTBODY:BASIC_HEAD:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:GENERIC_TEETH_WITH_FANGS:RIBCAGE]
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
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [USE_MATERIAL_TEMPLATE:VENOM:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen bushmaster venom]
            [STATE_ADJ:ALL_SOLID:frozen bushmaster venom]
            [STATE_NAME:LIQUID:bushmaster venom]
            [STATE_ADJ:LIQUID:bushmaster venom]
            [STATE_NAME:GAS:boiling bushmaster venom]
            [STATE_ADJ:GAS:boiling bushmaster venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:bushmaster bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:BUSHMASTER:ALL]
                [SYN_INJECTED]
                [CE_PAIN:SEV:75:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:10:PEAK:50:END:1200]
                [CE_BLEEDING:SEV:10:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:10:PEAK:30:END:50]
                [CE_DIZZINESS:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:50:PEAK:100:END:1200]
                [CE_UNCONSCIOUSNESS:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:50:PEAK:100:END:200]
                [CE_NAUSEA:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:60:PEAK:200:END:300]
                [CE_PAIN:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:100:PEAK:200:END:300]
                [CE_PARALYSIS:SEV:100:PROB:100:RESISTABLE:SIZE_DILUTES:START:125:PEAK:200:END:1200]
        [BODY_SIZE:0:0:20]
        [BODY_SIZE:2:0:4250]
        [BODY_SIZE:20:0:8500]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:12:24]
        [MUNDANE]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_CANLATCH]
            [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:VENOM:LIQUID:100:100]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:22]
                [CLUTCH_SIZE:10:20]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:STRIPES_BROWN_BLACK:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
