# Cat

> Fonte: [Cat](https://dwarffortresswiki.org/index.php/Cat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cats for their aloofness.**
- **Biome**
- **Domesticated**
- **Tamed Attributes**
- **Pet value:** 20
- **Not hunting/war trainable**
- **Size**
- **Birth:** 500 cm 3
- **Mid:** 2,000 cm 3
- **Max:** 5,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 0-7
- **Fat:** 0-7
- **Intestines:** 0-1
- **Raw materials**
- **Bones:** 0-4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small mammalian carnivore. It is usually domestic and hunts vermin.*

**Cats** are domestic animals, and one of the most common creatures in a typical dwarven fortress. They spend their time hunting vermin, creating messes for their owners to dispose of, and also seem to want to wander every room, hall and mineshaft at least once, perhaps due to some modeling of curiosity. They do not require any food. All cats are born with Legendary skill in climbing, with their newborns being known as *kittens*.

Cats are infamous for the phenomenon known as a catsplosion: If you are not careful, your cat population may explode, causing your FPS to plummet. This can be hard to resolve, due to the fact that killing pets causes a strong unhappy thought to their owners, though male cats can be assigned to gelding in order to prevent them from breeding.

Some dwarves like cats for their *aloofness*.

## Mechanics

### Cats as pets

Cats possess a number of mechanics not found in other domestic animals. They are unique among all other creatures in that they cannot be assigned as pets; instead, cats choose dwarves as owners. The mechanics for pet adoption are still in place, so cats will only choose dwarves who have preference for them. If a cat is caged, it will not adopt; however, it may adopt the moment it is taken from the cage (even if assigned for immediate butchering). In adventurer mode, cats can be witnessed bumping their heads on friendly creatures to greet them.

Cats are tiny and benign, making them extremely weak in combat and unable to defend themselves outside of very lucky hits. Avoid leaving cats in dangerous areas, lest they fall prey to dangerous creatures and create unhappy thoughts to their adopted dwarves. Thanks to their [`[AT_PEACE_WITH_WILDLIFE]`](/index.php/Creature_token#AT_PEACE_WITH_WILDLIFE "Creature token") token, cats will not perturb natural creatures, but are still prone to being killed by things like cavern monsters.

Inspecting a cat with v reveals a unique message: This animal isn't interested in your wishes.

### Cats as pest control

Cats (both pets and strays) will hunt and kill most vermin they come across, creating remains along the way. This makes them useful for dealing with vermin eating at your food stockpiles or causing rot; a cat placed over your food stock with a pasture will keep it free of troublesome vermin. The only other animal with vermin-hunting abilities are trained peregrine falcons, which are significantly harder to obtain.

Cats, by nature, will attempt to haul vermin to their adopted dwarves. The dwarf will then dismiss the cat, at which point the cat will drop the remains for a dwarf with refuse hauling enabled to clean up. Cats with any contaminant on their fur will clean themselves with their tongue, exposing themselves to any ingestion-induced syndromes the contaminant may carry.

### Cats as food

Cats are useful around the fort to prevent the unhappy thoughts produced by vermin, and also for producing large numbers of kittens. If you can resist their cuteness and charm, and get to them before they adopt a dwarf, cats can be butchered to provide a small, never-ending trickle of leather, bones and meat for your fort. As a breeding pair of cats only costs 22 embark points, this is well worth considering - just cage and/or butcher the kittens as they are born, lest the kittens grow to adopt a dwarf before their last voyage (see Breeding).

Kittens cannot be butchered for bones: only skulls will be created. Immature adult cats (less than 2 years old) may return about 2 meat, fat and bone, 1 skin, and 1 skull, or may only return a skull, while full adults (\> 2 yrs) consistently return about 6-7 meat and fat. Unfortunately there is no in-game way to tell for sure whether a particular animal is an immature or full adult. (Note that other animals also have smaller immature sizes and butchering returns, but most other immature domestics return a more reasonable percentage of adult returns; for example, immature dogs consistently return about 50% of adult returns and include byproducts (e.g. bones and skin), compared to cats' 0-30% and sometimes no byproducts but the skull.) If you have a bunch of unwanted kittens, there are many uses for them. For example, use them as bait for a forgotten beast if it has some sort of poison, in order to determine what the poison does. If there's a desperate need to maximize cat-butchering returns, one can partly work around the lack of age info by slaughtering one-by-one the first-listed (therefore, usually, oldest) cats in the unit or animal screen until the returns drop to immature-sized returns, then waiting some months or a year for the remaining kitties to ~~stew~~ mature for a while.

|  |
|----|
| "Cat" in other / Languages / Dwarven / : / kun / Elven / : / linì / Goblin / : / sest / Human / : / usa |

Admired for its *aloofness*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Abnormally large cats "C" can easily be mixed up with a bronze colossus "C", whose effects on a fortress are a lot more "Fun" than a catsplosion.

    [CREATURE:CAT]
        [DESCRIPTION:A small mammalian carnivore.  It is usually domestic and hunts vermin.]
        [NAME:cat:cats:feline]
        [CASTE_NAME:cat:cats:feline]
        [CREATURE_TILE:'c'][COLOR:0:0:1]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:20]
        [LARGE_ROAMING]
        [AT_PEACE_WITH_WILDLIFE]
        [HUNTS_VERMIN]
        [RETURNS_VERMIN_KILLS_TO_OWNER]
        [ADOPTS_OWNER]
        [COMMON_DOMESTIC][BENIGN]
        [CARNIVORE][NATURAL][PET]
        [PREFSTRING:aloofness]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:5TOES_FQ_REG:4TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:CLAW:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:CLAW:CLAW_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:CLAW:FRONT]
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
        [BODY_SIZE:0:0:500]
        [BODY_SIZE:1:0:2000]
        [BODY_SIZE:2:0:5000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:CLAW]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [CHILD:1]
        [GENERAL_CHILD_NAME:kitten:kittens]
        [DIURNAL]
        [HOMEOTHERM:10070]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [STANCE_CLIMBER][NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_REAR:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EAR:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:ears:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:TAIL:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:tail:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:head:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:FOOT_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RFTOE1:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RFTOE2:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RFTOE3:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RFTOE4:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RFTOE5:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LFTOE1:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LFTOE2:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LFTOE3:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LFTOE4:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LFTOE5:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:front paws:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:FOOT_REAR:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RRTOE1:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RRTOE2:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RRTOE3:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RRTOE4:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LRTOE1:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LRTOE2:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LRTOE3:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LRTOE4:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:rear paws:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_AMBER:1:IRIS_EYE_AQUA:1:IRIS_EYE_AQUAMARINE:1:IRIS_EYE_ASH_GRAY:1:IRIS_EYE_AUBURN:1:IRIS_EYE_AZURE:1:IRIS_EYE_BLUE:1:IRIS_EYE_BRASS:1:IRIS_EYE_BRONZE:1:IRIS_EYE_BROWN:1:IRIS_EYE_CERULEAN:1:IRIS_EYE_CHESTNUT:1:IRIS_EYE_CHOCOLATE:1:IRIS_EYE_CINNAMON:1:IRIS_EYE_COPPER:1:IRIS_EYE_DARK_BLUE:1:IRIS_EYE_DARK_BROWN:1:IRIS_EYE_DARK_CHESTNUT:1:IRIS_EYE_DARK_GREEN:1:IRIS_EYE_DARK_OLIVE:1:IRIS_EYE_DARK_TAN:1:IRIS_EYE_ECRU:1:IRIS_EYE_EMERALD:1:IRIS_EYE_FERN_GREEN:1:IRIS_EYE_GRAY:1:IRIS_EYE_GREEN:1:IRIS_EYE_JADE:1:IRIS_EYE_LIGHT_BLUE:1:IRIS_EYE_LIGHT_BROWN:1:IRIS_EYE_MAHOGANY:1:IRIS_EYE_MIDNIGHT_BLUE:1:IRIS_EYE_OCHRE:1:IRIS_EYE_OLIVE:1:IRIS_EYE_PALE_BLUE:1:IRIS_EYE_PALE_BROWN:1:IRIS_EYE_PALE_CHESTNUT:1:IRIS_EYE_PERIWINKLE:1:IRIS_EYE_PINE_GREEN:1:IRIS_EYE_RAW_UMBER:1:IRIS_EYE_RUSSET:1:IRIS_EYE_SEA_GREEN:1:IRIS_EYE_SEPIA:1:IRIS_EYE_SKY_BLUE:1:IRIS_EYE_SLATE_GRAY:1:IRIS_EYE_SPRING_GREEN:1:IRIS_EYE_TAN:1:IRIS_EYE_TAUPE_DARK:1:IRIS_EYE_TAUPE_GRAY:1:IRIS_EYE_TAUPE_MEDIUM:1:IRIS_EYE_TAUPE_PALE:1:IRIS_EYE_TAUPE_SANDY:1:IRIS_EYE_TEAL:1:IRIS_EYE_TURQUOISE:1]
                    [TLCM_NOUN:eyes:PLURAL]
        [CAN_DO_INTERACTION:CLEANING]
            [CDI:ADV_NAME:Clean]
            [CDI:USAGE_HINT:CLEAN_SELF]
            [CDI:USAGE_HINT:CLEAN_FRIEND]
            [CDI:BP_REQUIRED:BY_CATEGORY:TONGUE]
            [CDI:VERB:lick:licks:lick each other]
            [CDI:CAN_BE_MUTUAL]
            [CDI:TARGET:A:SELF_ALLOWED:TOUCHABLE]
            [CDI:TARGET_RANGE:A:1]
            [CDI:MAX_TARGET_NUMBER:A:1]
            [CDI:WAIT_PERIOD:10]
        [CAN_DO_INTERACTION:BP_BUMP]
            [CDI:ADV_NAME:Head bump]
            [CDI:USAGE_HINT:GREETING]
            [CDI:BP_REQUIRED:BY_CATEGORY:HEAD]
            [CDI:VERB:head-bump:head-bumps:bump heads]
            [CDI:CAN_BE_MUTUAL]
            [CDI:TARGET:A:SELF_ONLY]
            [CDI:TARGET:B:TOUCHABLE]
            [CDI:TARGET_RANGE:B:1]
            [CDI:MAX_TARGET_NUMBER:B:1]
            [CDI:WAIT_PERIOD:20]
