# King cobra

> Fonte: [King cobra](https://dwarffortresswiki.org/index.php/King_cobra) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes king cobras for their charming hood.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **King cobra - King cobra man - Giant king cobra**
- **Attributes**
- **Syndrome · Egglaying**
- **Tamed Attributes**
- **Pet value:** 200
- **Not hunting/war trainable**
- **Size**
- **Birth:** 4 cm 3
- **Mid:** 3,000 cm 3
- **Max:** 6,000 cm 3
- **Food products**
- **Eggs:** 10-30
- **Age**
- **Adult at:** Birth
- **Max age:** 15-25
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 2-3
- **Fat:** 2-3
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 0-2
- **Tripe:** 1
- **Sweetbread:** 0-1
- **Spleen:** 0-1
- **Raw materials**
- **Bones:** 2-4
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small limbless reptile known for its deadly venom and the warning of its hood.*

**King cobras** are small animals, weighing a tenth as much as the average adult dwarf upon reaching maturity, which makes them roughly the same size as their real life counterparts. They can be found roaming about by themselves in tropical forests. If threatened, they can bite and deliver a syndrome which causes paralysis, severe localized pain, dizziness, and drowsiness. The paralysis by itself may be enough to kill a dwarf due to suffocation.

King cobras can be captured in cage traps and trained into exotic pets of decent value. They are born adults and as such can't be fully tamed. While too small to give worthy returns if butchered, they are prolific egg-layers, and as such make good targets for egg production. Products made from king cobra parts are worth twice more than those made from common animals.

Some dwarves like king cobras for their *charming hood*.

|  |
|----|
| "King cobra" in other / Languages / Dwarven / : / etar gisëk / Elven / : / afedo vicira / Goblin / : / zozlo gusslax / Human / : / deng nasñok |

Admired for its *charming hood*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
The name of this beast is somewhat of a misnomer, as it is not a true cobra, and snakes are typically self-governing.

    1 kph

    King cobras were sponsored by the generous contributions of the Bay 12 community.

        Sponsored by cosh - <3 DF

    [CREATURE:KING_COBRA]
        [DESCRIPTION:A small limbless reptile known for its deadly venom and the warning of its hood.]
        [NAME:king cobra:king cobras:king cobra]
        [CASTE_NAME:king cobra:king cobras:king cobra]
        [CREATURE_TILE:'k'][COLOR:0:0:1]
        [CREATURE_CLASS:POISONOUS]
        [PETVALUE:200]
        [PET_EXOTIC]
        [FREQUENCY:20]
        [NATURAL]
        [CARNIVORE]
        [LARGE_ROAMING]
        [BIOME:ANY_TROPICAL_FOREST]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [PREFSTRING:charming hood]
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
            [STATE_NAME:ALL_SOLID:frozen king cobra venom]
            [STATE_ADJ:ALL_SOLID:frozen king cobra venom]
            [STATE_NAME:LIQUID:king cobra venom]
            [STATE_ADJ:LIQUID:king cobra venom]
            [STATE_NAME:GAS:boiling king cobra venom]
            [STATE_ADJ:GAS:boiling king cobra venom]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:king cobra bite]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:KING_COBRA:ALL]
                [SYN_INJECTED]
                [CE_PAIN:SEV:75:PROB:100:RESISTABLE:SIZE_DILUTES:LOCALIZED:VASCULAR_ONLY:START:10:PEAK:50:END:1200]
                [CE_DIZZINESS:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:30:PEAK:100:END:1200]
                [CE_DROWSINESS:SEV:50:PROB:100:RESISTABLE:SIZE_DILUTES:START:30:PEAK:100:END:1200]
                [CE_PARALYSIS:SEV:100:PROB:100:RESISTABLE:SIZE_DILUTES:START:60:PEAK:100:END:1200]
        [BODY_SIZE:0:0:4]
        [BODY_SIZE:2:0:3000]
        [BODY_SIZE:5:0:6000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [MAXAGE:15:25]
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
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:3512:2634:1756:878:4900:6900] 10 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
            [LAYS_EGGS]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGGSHELL:SOLID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_WHITE:LIQUID]
                [EGG_MATERIAL:LOCAL_CREATURE_MAT:EGG_YOLK:LIQUID]
                [EGG_SIZE:5]
                [CLUTCH_SIZE:10:30] 20 to 40
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SCALE]
                [TL_COLOR_MODIFIER:OLIVE:1:TAN:1:BLACK:1]
                    [TLCM_NOUN:scales:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
