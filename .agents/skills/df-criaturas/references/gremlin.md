# Gremlin

> Fonte: [Gremlin](https://dwarffortresswiki.org/index.php/Gremlin) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes gremlins for their mischief.**
- **Biome**
- **Underground Depth: 1-3**
- **Attributes**
- **Trapavoid · Mischievous · Learns · Humanoid**
- **Tamed Attributes**
- **Pet value:** 0
- **Not hunting/war trainable**
- **Size**
- **Birth:** 500 cm 3
- **Mid:** 2,500 cm 3
- **Max:** 10,000 cm 3
- **Age**
- **Child at:** 1
- **Adult at:** 18
- **Max age:** 800-1000
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small humanoid creature with a mischievous, toothy grin.*

**Gremlins** are intelligent cavern creatures who are invisible until spotted, and cause various kinds of fun in your fortress by stepping on pressure plates, pulling levers, opening cages, picking locks and opening forbidden doors - it is recommended to not have gremlins and easily-accessible self destruct levers in the same fortress. One way of exploiting their lever-pulling behaviour is to have a lever that triggers a trap to kill the user when pulled, and leaving it in an area likely to see gremlins visiting. All gremlins are born with Competent skill in ambusher.

When a gremlin is discovered, the game pauses and centers on it, with the message: "A gremlin! Drive it away!".

Despite being intelligent creatures, gremlins possess the [`[PET_EXOTIC]`](/index.php/Creature_token#PET_EXOTIC "Creature token") token and can in fact be trained by your dwarves, provided you can bypass their natural immunity to most traps. They don't possess a pet value, which theoretically makes them worthless for keeping around your fort, but if you do manage to capture and train a gremlin, it could actually become your mayor. In fact, this is quite likely because the gremlin is not able to work, so it will spend all its time in your meeting hall making friends. After a certain period of time a trained adult gremlin will turn into a gremlin hunter and will then hunt alongside your hunters. This is because gremlins have natural skill in ambushing, which is associated with the hunting labor.

Note that a trained gremlin will not pull levers mischievously anymore. As explained by Toady One, the reason they are tamable is roughly that they are supposed to be only pretending to listen to your dwarves so they can mess with your levers and then run away, though trained gremlins currently do not perform this function at all and simply act as regular (albeit buggy) pets.Source

In the current version, a stray gremlin will claim a bed in the inn and become a long-term resident, eventually petitioning for citizenship. This can be mortally annoying, because they will then perform labors and ignore requests to be trained, resulting in trainers dying of starvation and thirst if you aren't careful. A solution to this is to make them exclusively soldiers, or assign them to a small burrow with a workshop exclusive to them, and make the area a training ground, which you can also order them to station in. Being trained isn't a job for the gremlin and it just has to be there; the trainer will eventually finish the job if the gremlin is in the same area. This no longer occurs with their tame offspring. This method can also work for other trained intelligent creatures if you've modded them to be pets.

Gremlins are carnivorous due to having the [`[BONECARN]`](/index.php/Creature_token#BONECARN "Creature token") tag, and are notably long-lived, with some living up to 1000 years. Due to their minuscule size, they are terrible at handling alcohol, and cannot wear any other creatures' clothes or armor, nor can clothes or armor be ordered to fit them\[Verify\].

Some dwarves like gremlins for their *mischief*.

Acts as bad as he looks.

## Trivia

Gremlins can talk, and be recruited in adventurer mode, which is useful if one is trapped in a cave and cannot find animal people. Also, because they both inhabit the first cavern layer and are trainable, the dwarven caravan will offer their bodily fluids for sale, including gremlin blood, sweat and tears.\[Verify\]

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Don't expose them to bright light. Don't feed them after midnight. Don't get them wet.

They are not very good at making wagons.

    [CREATURE:GREMLIN]
        [DESCRIPTION:A small humanoid creature with a mischievous, toothy grin.]
        [NAME:gremlin:gremlins:gremlin]
        [CASTE_NAME:gremlin:gremlins:gremlin]
        [CREATURE_TILE:'g'][COLOR:2:0:1]
        [LARGE_ROAMING][BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:1:3]
        [POPULATION_NUMBER:1:1]
        [CAN_LEARN][CAN_SPEAK]
        [PET_EXOTIC]
        [LOCKPICKER][TRAPAVOID][MISCHIEVOUS]
        [NATURAL_SKILL:SNEAK:3]
        [CANOPENDOORS]
        [BONECARN]
        [PREFSTRING:mischief]
        [PERSONALITY:EXCITEMENT_SEEKING:50:75:100]
        [PERSONALITY:CURIOUS:50:75:100]
        [PERSONALITY:HUMOR:50:75:100]
        [PERSONALITY:CRUELTY:50:75:100]
        [PERSONALITY:DISCORD:50:75:100]
        [PERSONALITY:ORDERLINESS:0:25:50]
        [PERSONALITY:DUTIFULNESS:0:25:50]
        [BODY:HUMANOID_NECK:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:5FINGERS:5TOES:MOUTH:TONGUE:FACIAL_FEATURES:TEETH:RIBCAGE]
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
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
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
        [BODY_SIZE:0:0:500]
        [BODY_SIZE:1:168:2500]
        [BODY_SIZE:12:0:10000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:75:95:98:100:102:105:125]
            [APP_MOD_IMPORTANCE:500]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:75:95:98:100:102:105:125]
            [APP_MOD_IMPORTANCE:500]
        [SET_BP_GROUP:BY_CATEGORY:EYE]
            [BP_APPEARANCE_MODIFIER:CLOSE_SET:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
            [BP_APPEARANCE_MODIFIER:DEEP_SET:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
            [BP_APPEARANCE_MODIFIER:ROUND_VS_NARROW:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
        [SET_BP_GROUP:BY_CATEGORY:LIP]
            [BP_APPEARANCE_MODIFIER:THICKNESS:50:70:90:100:110:130:200]
                [APP_MOD_NOUN:lips:PLURAL]
                [APP_MOD_DESC_RANGE:55:70:90:110:150:190]
        [SET_BP_GROUP:BY_CATEGORY:NOSE]
            [BP_APPEARANCE_MODIFIER:BROADNESS:25:70:90:100:110:130:200]
                [APP_MOD_DESC_RANGE:30:60:90:110:150:190]
            [BP_APPEARANCE_MODIFIER:LENGTH:25:70:90:100:110:130:200]
                [APP_MOD_DESC_RANGE:30:60:90:110:150:190]
            [BP_APPEARANCE_MODIFIER:UPTURNED:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:CONVEX:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:nose bridge:SINGULAR]
        [SET_BP_GROUP:BY_CATEGORY:EAR]
            [BP_APPEARANCE_MODIFIER:SPLAYED_OUT:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:ears:PLURAL]
            [BP_APPEARANCE_MODIFIER:HANGING_LOBES:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:ears:PLURAL]
            [BP_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
                [APP_MOD_IMPORTANCE:700]
                [APP_MOD_NOUN:ears:PLURAL]
                [APP_MOD_DESC_RANGE:91:94:98:102:106:109]
            [BP_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
                [APP_MOD_IMPORTANCE:700]
                [APP_MOD_NOUN:ears:PLURAL]
                [APP_MOD_DESC_RANGE:91:94:98:102:106:109]
        [SET_BP_GROUP:BY_CATEGORY:TOOTH]
            [BP_APPEARANCE_MODIFIER:GAPS:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:teeth:PLURAL]
            [BP_APPEARANCE_MODIFIER:LENGTH:100:100:100:100:100:100:100] for vampires
                [APP_MOD_IMPORTANCE:1000]
                [APP_MOD_NOUN:teeth:PLURAL]
                [APP_MOD_DESC_RANGE:30:60:90:110:150:190]
        [SET_BP_GROUP:BY_CATEGORY:SKULL]
            [BP_APPEARANCE_MODIFIER:HIGH_CHEEKBONES:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:BROAD_CHIN:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:JUTTING_CHIN:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:SQUARE_CHIN:0:70:90:100:110:130:200]
        [SET_BP_GROUP:BY_CATEGORY:THROAT]
            [BP_APPEARANCE_MODIFIER:DEEP_VOICE:0:70:90:100:110:130:200]
            [BP_APPEARANCE_MODIFIER:RASPY_VOICE:0:70:90:100:110:130:200]
        [SET_BP_GROUP:BY_CATEGORY:HEAD]
            [BP_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
                [APP_MOD_IMPORTANCE:700]
                [APP_MOD_DESC_RANGE:91:94:98:102:106:109]
            [BP_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
                [APP_MOD_IMPORTANCE:700]
                [APP_MOD_DESC_RANGE:91:94:98:102:106:109]
        [MAXAGE:800:1000]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_CANLATCH]
        [BABY:1]
        [CHILD:18]
        [EQUIPS]
        [ALL_ACTIVE]
        [SMELL_TRIGGER:10]
        [LOW_LIGHT_VISION:10000]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_LEARNED]
        [CASTE:FEMALE]
            [FEMALE]
            [MULTIPLE_LITTER_RARE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GREEN:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:PUPIL_EYE_YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
