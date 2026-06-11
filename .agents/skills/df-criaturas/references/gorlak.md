# Gorlak

> Fonte: [Gorlak](https://dwarffortresswiki.org/index.php/Gorlak) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gorlaks for their impressive tusks.**
- **Biome**
- **Underground Depth: 1-3**
- **Attributes**
- **Alignment:** Good
- **Learns**
- **Cannot be tamed**
- **Size**
- **Birth:** 3,000 cm 3
- **Mid:** 10,000 cm 3
- **Max:** 50,000 cm 3
- **Age**
- **Child at:** 1
- **Adult at:** 12
- **Max age:** 110-150
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small, round humanoid found wandering the caves deep underground. Most of its body is taken up by a huge tusked mouth.*

**Gorlaks** are small, good-aligned sapient humanoids encountered in cavern areas. Despite their appearance, they are benign, and so mostly harmless, although sometimes will cause job cancellationsBug:3348 and occasionally make weak attacks against animals or sleeping dwarves. They are easily dispatched by even an average civilian dwarf.

Gorlaks are able to join civilizations (usually dwarven), making them appear as visitors, and are playable in adventurer mode in a similar fashion to animal people. Before beginning an adventure as a gorlak or enlisting one into your military, note that they have special considerations for armor usage, as they do not have a torso—a gorlak's limbs connect directly to its head. While gorlaks may equip body and leg wear, they are equipped in the head slot while offering no head protection, only serving to take up space and provide coverage for limbs. As an example, though gorlaks can equip breastplates, the lack of a torso means they *don't actually offer any protection* while taking up the "shaped" armor spot for the head, preventing the wearing of a helm. An armor set consisting of a helm, mail shirt (for upper limb protection), gauntlets, and high boots will be the equivalent of full coverage for a gorlak.

Gorlaks cannot kick, and as such don't learn the kicking combat skill via combat training, and may not be able to learn or use the skill at all.

They can't be spawned in the object testing arena.

Some dwarves like gorlaks for their *impressive tusks*, their *stimulating conversation* and their *helpful guidance*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
They are often said to be found traveling with a blue troll and a small girl, and are occasionally found to only have one eye. These cycloptic Gorlaks are admired by some humans to the point where they primarily depict them as such in engravings.

## Gallery

-

  *A gorlak, drawn in crayon by Bay 12 Games.*

-

  *Concept art by Bay 12 Games.*

    [CREATURE:GORLAK]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A small, round humanoid found wandering the caves deep underground.  Most of its body is taken up by a huge tusked mouth.]
        [NAME:gorlak:gorlaks:gorlak]
        [CASTE_NAME:gorlak:gorlaks:gorlak]
        [GOOD]
        [CREATURE_TILE:'g'][COLOR:6:0:1]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:3]
        [LARGE_ROAMING][FREQUENCY:25]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [BENIGN]
        [CAN_LEARN][CAN_SPEAK]
        [LOCAL_POPS_CONTROLLABLE]
        [LOCAL_POPS_PRODUCE_HEROES]
        [PREFSTRING:impressive tusks]
        [PREFSTRING:stimulating conversation]
        [PREFSTRING:helpful guidance]
        [BODY:BODY_HEAD:BASIC_3PARTARMS:BASIC_3PARTLEGS:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:SPINE:BRAIN:SKULL:4FINGERS:3TOES:MOUTH:TONGUE:FACIAL_FEATURES:TEETH:2TUSKS:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:IVORY:TOOTH_TEMPLATE]
                [STATE_NAME:ALL_SOLID:ivory]
                [STATE_ADJ:ALL_SOLID:ivory]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:IVORY:IVORY_TEMPLATE]
                [TISSUE_NAME:ivory:NP]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_TISSUE_TEMPLATE:EYEBROW:EYEBROW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:HEAD:EYEBROW:ABOVE:BY_CATEGORY:EYE]
        [USE_TISSUE_TEMPLATE:EYELASH:EYELASH_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:EYELID:EYELASH:FRONT]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:FACIAL_HAIR_TISSUES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
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
        [USE_MATERIAL_TEMPLATE:SWEAT:SWEAT_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:TEARS:TEARS_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:SPIT:SPIT_TEMPLATE]
        [SECRETION:LOCAL_CREATURE_MAT:SWEAT:LIQUID:BY_CATEGORY:ALL:SKIN:EXERTION]
        [SECRETION:LOCAL_CREATURE_MAT:TEARS:LIQUID:BY_CATEGORY:EYE:ALL:EXTREME_EMOTION]
        [CAN_DO_INTERACTION:PET_ANIMAL]
            [CDI:ADV_NAME:Pet animal]
            [CDI:USAGE_HINT:GREETING]
            [CDI:BP_REQUIRED:BY_TYPE:GRASP]
            [CDI:VERB:pet:pets:pets]
            [CDI:TARGET:A:SELF_ONLY]
            [CDI:TARGET:B:TOUCHABLE]
            [CDI:TARGET_RANGE:B:1]
            [CDI:MAX_TARGET_NUMBER:B:1]
            [CDI:WAIT_PERIOD:20]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:TOKEN:SPIT]
            [CDI:ADV_NAME:Spit]
            [CDI:USAGE_HINT:NEGATIVE_SOCIAL_RESPONSE]
            [CDI:USAGE_HINT:TORMENT]
            [CDI:BP_REQUIRED:BY_CATEGORY:MOUTH]
            [CDI:MATERIAL:LOCAL_CREATURE_MAT:SPIT:LIQUID_GLOB]
            [CDI:VERB:spit:spits:NA]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:15]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:30]
        [BODY_SIZE:0:0:3000]
        [BODY_SIZE:1:168:10000]
        [BODY_SIZE:20:0:50000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:110:150]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TUSK]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [BABY:1]
        [CHILD:12]
        [EQUIPS]
        [CANOPENDOORS]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [HOMEOTHERM:10040]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:2206:1692:1178:585:3400:4900] 15 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [SWIMS_LEARNED]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
            [BODY_DETAIL_PLAN:FACIAL_HAIR_TISSUE_LAYERS]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GOLDENROD:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_RED:1]
                    [TLCM_NOUN:eyes:PLURAL]
