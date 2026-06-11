# Foul blendec

> Fonte: [Foul blendec](https://dwarffortresswiki.org/index.php/Foul_blendec) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes foul blendecs for their goat heads.**
- **Biome**
- **Temperate Broadleaf Forest Tropical Coniferous Forest Tropical Dry Broadleaf Forest**
- **Attributes**
- **Alignment:** Evil
- **Learns · Horn · Horn · Humanoid**
- **Cannot be tamed**
- **Size**
- **Birth:** 6,000 cm 3
- **Mid:** 30,000 cm 3
- **Max:** 60,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Cannot be butchered**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A man-shaped creature with the legs of a goat and the empty-eyed skull of a goat.*

**Foul blendecs** are fanciful, intelligent creatures found in certain evil-aligned forests. Standing as the size of a dwarf, these skull-headed creatures spawn rarely, in groups of 3 to 5 individuals who will menace everything smaller than themselves. They will attack dwarves who provoke them and may cause great injury unless countered by a military squad. They are a male-only race - no female foul blendecs exist - and are also immortal, only dying to violence and disease.

Foul blendecs are sapient and can open unlocked doors, though they're unlikely to enter a fortress unless chasing dwarves inside. As described, they're completely eye-less, but can still see through [`[EXTRAVISION]`](/index.php/Creature_token#EXTRAVISION "Creature token") (meaning it's impossible to blind them). They possess a pet value of 250, but lack the necessary tokens to be trainable (and even if modded to be trainable, the fact they are intelligent creatures will lead to strange behavior). Due to the aforementioned intelligence, dwarves will not butcher, eat or use products made from foul blendecs, limiting their use to occupying space in your refuse stockpile, live training or putting them somewhere more to your liking if you capture one in a cage trap.

Their good counterparts are the satyrs.

Some dwarves like foul blendecs for their *goat heads*, their *goat legs* and their *rotten eye sockets*.

-

  A foul blendec, drawn in crayon by Bay 12 Games

-

  A more detailed version of the foul creature.\
  *Art by kough_noises*

-

  Another detailed view of the foul creature.\
  *Art by Salasti*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Foul blendecs are quite reminiscent of another goat-skull-headed monster. Dwarves who witness them carrying machetes and using dogs are recommended to kill the dogs first.

## Trivia

-

  Initially, the premium version had a sprite for a child foul blendec. It was later removed from the game, because foul blendecs are adults at birth.

- ThreeToe's story "Forest Befouled" represents a potential origin story for foul blendecs being corrupted from satyrs.

\

    [CREATURE:BLENDEC_FOUL]
        [DESCRIPTION:A man-shaped creature with the legs of a goat and the empty-eyed skull of a goat.]
        [NAME:foul blendec:foul blendecs:foul blendec]
        [CASTE_NAME:foul blendec:foul blendecs:foul blendec]
        [CREATURE_TILE:'b'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:3:5]
        [CANOPENDOORS]
        [LARGE_PREDATOR][EVIL]
        [BONECARN]
        [GRASSTRAMPLE:0]
        [PETVALUE:250]
        [LARGE_ROAMING][FREQUENCY:5]
        [BIOME:FOREST_TEMPERATE_BROADLEAF]
        [BIOME:FOREST_TROPICAL_CONIFER]
        [BIOME:FOREST_TROPICAL_DRY_BROADLEAF]
        [PREFSTRING:goat heads]
        [PREFSTRING:goat legs]
        [PREFSTRING:rotten eye sockets]
        [BODY:HUMANOID_NECK_HOOF:TAIL:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:2HEAD_HORN:HUMANOID_JOINTS:5FINGERS:MOUTH:TONGUE:TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [USE_MATERIAL_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_MATERIAL_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [USE_TISSUE_TEMPLATE:HOOF:HOOF_TEMPLATE]
            [USE_TISSUE_TEMPLATE:HORN:HORN_TEMPLATE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [TISSUE_LAYER:BY_CATEGORY:LEG_LOWER:HAIR:NORMAL]
        [TISSUE_LAYER:BY_CATEGORY:LEG_UPPER:HAIR:NORMAL]
        [TISSUE_LAYER:BY_CATEGORY:BODY_LOWER:HAIR:BOTTOM]
        [EXTRAVISION]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
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
        [BODY_SIZE:0:0:6000]
        [BODY_SIZE:1:168:30000]
        [BODY_SIZE:12:0:60000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
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
        [ATTACK:GORE:BODYPART:BY_CATEGORY:HORN]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:gore:gores]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
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
        [CAN_LEARN]
        [CAN_SPEAK]
        [EQUIPS]
        [ALL_ACTIVE]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:5341:4723:4112:1254:6433:7900] 7 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
        [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
            [SET_TL_GROUP:BY_CATEGORY:BODY_LOWER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_UPPER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_LOWER:HAIR]
        [TL_COLOR_MODIFIER:AMBER:1:AUBURN:1:BLACK:1:BROWN:1:BUFF:1:BURNT_SIENNA:1:BURNT_UMBER:1:CHARCOAL:1:CHESTNUT:1:CHOCOLATE:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_CHESTNUT:1:DARK_TAN:1:ECRU:1:FLAX:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:LIGHT_BROWN:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:PALE_CHESTNUT:1:PUMPKIN:1:RAW_UMBER:1:RUSSET:1:SAFFRON:1:SEPIA:1:TAN:1:TAUPE_DARK:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
