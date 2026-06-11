# Dark gnome

> Fonte: [Dark gnome](https://dwarffortresswiki.org/index.php/Dark_gnome) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes dark gnomes for their ability to hold liquor.**
- **Biome**
- **Mountain**
- **Attributes**
- **Alignment:** Evil
- **Steals drink · Learns · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,500 cm 3
- **Mid:** 7,500 cm 3
- **Max:** 15,000 cm 3
- **Age**
- **Child at:** 1
- **Adult at:** 20
- **Max age:** 230-250
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A tiny, foul-tempered humanoid creature that dwells in the evil mountains. They are known to enjoy drinking liquor and will take any unguarded supplies of booze.*

**Dark gnomes** are small humanoid creatures who inhabit evil mountains. Their intelligence is on par with dwarves and other sentient creatures, but they lack the ability to communicate verbally, one possible reason they haven't formed a civilized society. They have teal skin, yellow eyes and a wonderful variety of beards. They're a rather long-lived race, with the oldest ones living up to 250 years. In adventurer mode, they're only active during the night.

If you leave booze out in the open, they'll come in groups of five to ten to drink it all and scare the poop out of any civilians they encounter. If they reach your alcohol, they'll guzzle it with such efficient speed that your dwarves will soon be dying of thirst unless you have steady access to plants or water. They are even capable of stealing alcohol directly from your dwarves: If, say, an axedwarf is busy fighting a goblin ~~liberator~~ child-snatcher, the dark gnome will walk right up and drink their personal supply of booze (if they have one). They have even been seen swarming caravans and chugging booze between getting hacked to bits by the caravan guards.

Despite their apparent malice, dark gnomes are not particularly violent and will run in terror when chased. They're able to equip weapons and armor that are appropriately sized for them, but this is rarely seen. Any dwarf or dog can easily hurt them, but be wary of fighting on mountainsides, where a dwarf may charge the gnome, miss, and fall a very long distance. Gnomeblight is extremely toxic to dark gnomes, causing necrosis if somehow applied to them.

Their good counterparts are the mountain gnomes.

Some dwarves like dark gnomes for their *ability to hold liquor*. They have an inebriation dilution factor of 500, allowing them to drink more than creatures ten times their size.

## Gallery

-

  *Art by Fault.*

-

  *Art by Jeff Agudelo.*

    [CREATURE:GNOME_DARK]
        [DESCRIPTION:A tiny, foul-tempered humanoid creature that dwells in the evil mountains.  They are known to enjoy drinking liquor and will take any unguarded supplies of booze.]
        [NAME:dark gnome:dark gnomes:dark gnome]
        [CASTE_NAME:dark gnome:dark gnomes:dark gnome]
        [CREATURE_TILE:'g'][COLOR:3:0:0]
        [CREATURE_CLASS:MAMMAL]
        [GRASSTRAMPLE:0][EVIL]
        [BIOME:MOUNTAIN]
        [LARGE_ROAMING][FREQUENCY:10]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:5:10][LOOSE_CLUSTERS]
        [CURIOUSBEAST_GUZZLER]
        [BENIGN]
        [CAN_LEARN]
        [PREFSTRING:ability to hold liquor]
        [BODY:HUMANOID_NECK:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:5FINGERS:5TOES:MOUTH:TONGUE:FACIAL_FEATURES:TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:HEAD_HAIR_TISSUE_LAYERS]
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
        [BODY_SIZE:0:0:1500]
        [BODY_SIZE:1:168:7500]
        [BODY_SIZE:20:0:15000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
            [APP_MOD_IMPORTANCE:500]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
            [APP_MOD_IMPORTANCE:500]

        [SET_BP_GROUP:BY_CATEGORY:EYE]
            [BP_APPEARANCE_MODIFIER:CLOSE_SET:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
            [BP_APPEARANCE_MODIFIER:DEEP_SET:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
            [BP_APPEARANCE_MODIFIER:ROUND_VS_NARROW:0:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
            [BP_APPEARANCE_MODIFIER:LARGE_IRIS:25:70:90:100:110:130:200]
                [APP_MOD_NOUN:eyes:PLURAL]
                [APP_MOD_DESC_RANGE:30:60:90:110:150:190]

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

        [MAXAGE:230:250]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_EDGE]
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
        [CHILD:20]
        [EQUIPS]
        [NOCTURNAL]
        [HOMEOTHERM:10067]
        [SYNDROME_DILUTION_FACTOR:INEBRIATION:500]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:750:600:439:1900:2900] 20 kph
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
            [BODY_DETAIL_PLAN:FACIAL_HAIR_TISSUE_LAYERS]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:CHEEK:CHEEK_WHISKERS]
             [PLUS_TL_GROUP:BY_CATEGORY:HEAD:CHIN_WHISKERS]
             [PLUS_TL_GROUP:BY_CATEGORY:HEAD:MOUSTACHE]
             [PLUS_TL_GROUP:BY_CATEGORY:HEAD:SIDEBURNS]
             [PLUS_TL_GROUP:BY_CATEGORY:HEAD:EYEBROW]
             [PLUS_TL_GROUP:BY_CATEGORY:EYELID:EYELASH]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:hair:SINGULAR]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:hair:SINGULAR]
                    [TLCM_TIMING:ROOT:80:0:130:0]
                [TL_COLOR_MODIFIER:WHITE:1]
                    [TLCM_NOUN:hair:SINGULAR]
                    [TLCM_TIMING:ROOT:130:0:150:0]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:EYEBROW]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:LENGTH:50:80:90:100:110:120:150]
                    [APP_MOD_NOUN:eyebrows:PLURAL]
                    [APP_MOD_DESC_RANGE:55:70:90:110:130:145]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:DENSE:50:80:90:100:110:120:150]
                    [APP_MOD_NOUN:eyebrows:PLURAL]
                    [APP_MOD_DESC_RANGE:55:70:90:110:130:145]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:HIGH_POSITION:0:70:90:100:110:130:200]
                    [APP_MOD_NOUN:eyebrows:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:EYELID:EYELASH]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:LENGTH:50:80:90:100:110:120:150]
                    [APP_MOD_NOUN:eyelashes:PLURAL]
                    [APP_MOD_DESC_RANGE:55:70:90:110:130:145]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:CHEEK:CHEEK_WHISKERS]
             [PLUS_TL_GROUP:BY_CATEGORY:HEAD:CHIN_WHISKERS]
             [PLUS_TL_GROUP:BY_CATEGORY:HEAD:MOUSTACHE]
             [PLUS_TL_GROUP:BY_CATEGORY:HEAD:SIDEBURNS]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:LENGTH:0:0:0:0:0:0:0]
                    [APP_MOD_NOUN:hair:SINGULAR]
                    [APP_MOD_RATE:1:DAILY:0:1000:0:0:NO_END]
                    [APP_MOD_DESC_RANGE:10:25:75:125:200:300]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:CURLY:0:70:90:100:110:130:200]
                    [APP_MOD_NOUN:hair:SINGULAR]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:GREASY:0:70:90:100:110:130:200]
                    [APP_MOD_NOUN:hair:SINGULAR]
                [TISSUE_LAYER_APPEARANCE_MODIFIER:DENSE:50:80:90:100:110:120:150]
                    [APP_MOD_NOUN:hair:SINGULAR]
                    [APP_MOD_DESC_RANGE:55:70:90:110:130:145]
            SET_TL_GROUP:BY_CATEGORY:FINGER:NAIL]
             PLUS_TL_GROUP:BY_CATEGORY:TOE:NAIL]
                TISSUE_LAYER_APPEARANCE_MODIFIER:LENGTH:100:100:100:100:100:100:100]
                    APP_MOD_RATE:1:DAILY:0:1000:0:0:NO_END]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:TEAL:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_YELLOW:1]
                    [TLCM_NOUN:eyes:PLURAL]
