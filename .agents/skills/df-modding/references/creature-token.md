# Creature token

> Fonte: [Creature token](https://dwarffortresswiki.org/index.php/Creature_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

The `[OBJECT:CREATURE]` token begins the definition of a *Dwarf Fortress* creature raw file. Each creature definition that follows begins with the `[``CREATURE``:creature ID]` token, and the creature's exact properties and behavior are then specified by the use of further creature tokens. All known creature tokens are listed below.

Vanilla creature definitions can be found in `\data\vanilla\vanilla_creatures\`. Creature ID is also used with graphics tokens to make customizable graphics sets.

The caste tokens allow defining sub-species within the broader creature definition, including true biological castes and lesser variations, such as sexes. Creature tokens can either be 'Creature' or 'CASTE-only' type which can only be applied to creature or caste respectively, or 'CASTE' which can be applied to both. In the table bellow, creature type distinguishes tokens that can be applied to creature only, caste only, and both ('creature', 'CASTE-only', and 'CASTE' respectively)

\

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## A

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  ADOPTS_OWNER | Caste |  | Prevents the tamed creature from being made available for adoption, instead allowing it to automatically adopt whoever it wants. The basic requirements for adoption are intact, and the creature will only adopt individuals who have a preference for their species. Used by cats in the vanilla game. When viewing a tame creature with this token, the message "This animal isn't interested in your wishes" will appear instead of "This \[adorable\] animal can't work" or "This animal is waiting to be trained". |
|  ALCOHOL_DEPENDENT | Caste |  | Makes the creature need alcohol to get through the working day; it will choose to drink booze instead of water if possible. Going sober for too long reduces speed. |
|  ALL_ACTIVE | Caste |  | When set, the creature will appear at any time of day. Overrides [`[DIURNAL]`](/index.php/Creature_token#DIURNAL "Creature token"), [`[NOCTURNAL]`](/index.php/Creature_token#NOCTURNAL "Creature token"), [`[CREPUSCULAR]`](/index.php/Creature_token#CREPUSCULAR "Creature token"), [`[MATUTINAL]`](/index.php/Creature_token#MATUTINAL "Creature token"), and [`[VESPERTINE]`](/index.php/Creature_token#VESPERTINE "Creature token"). |
|  ALTTILE | Creature | 'character' or tile number | If set, the creature will blink between its [`[TILE]`](/index.php/Creature_token#TILE "Creature token") and its ALTTILE. |
|  AMBUSHPREDATOR | Caste |  | Makes the creature start out hidden and remain near its original location until its prey draws near. When combined with [`[WEBBER]`](/index.php/Creature_token#WEBBER "Creature token"), causes them to lay gigantic webs near their spawn location, though only for creatures present during embark. |
|  AMPHIBIOUS | Caste |  | Allows a creature to breathe both in and out of water (unlike [`[AQUATIC]`](/index.php/Creature_token#AQUATIC "Creature token")) - does not prevent drowning in magma. |
|  APP_MOD_DESC_RANGE | Appearance Modifier | Range (6 values, low to high) | Based on info from / Wannabehero on the forums / : When used with an appearance modifier token (BP_APPEARANCE_MODIFIER or BODY_APPEARANCE_MODIFIER), tells the game what numeric ranges to map to which descriptors. / The game uses 7 descriptor levels for each modifier, with the center one generally being to omit the thing from the creature description entirely. The six values in APP_MOD_DESC_RANGE define the boundaries between each described range. If this is not specified it uses the numbers 10:50:95:105:150:190. |
|  APP_MOD_GENETIC_MODEL | Appearance Modifier | Model (Accepts DOMINANT_MORE, DOMINANT_LESS, and MIX) | Defines a genetic model for the relevant appearance modifier(s). May or may not do anything significant at present. |
|  APP_MOD_IMPORTANCE | Appearance Modifier | number | Determines how important the appearance modifier is, for determining whether it shows up in the creature description.\[Verify\] |
|  APP_MOD_NOUN | Appearance Modifier | noun / SINGULAR or PLURAL | Creates a noun for the appearance, and whether it is singular or plural. |
|  APP_MOD_RATE | Appearance Modifier | Rate (integer) / Scale (DAILY, YEARLY) / min (growth) / max (growth) / start year / start day / end year / end day | Setting the growth rate of the modifier. The last two tokens can be replaced by NO_END to have growth continue indefinitely. |
|  APPLY_CREATURE_VARIATION | Caste | creature variation ID / (optional) any amount of arbitrary arguments | Applies the specified creature variation. See Creature_variation_token#Arguments_and_conditional_tokens for how the subsequent arguments may be used. |
|  APPLY_CURRENT_CREATURE_VARIATION | Special |  | Applies the effects of all pending [`[CV_ADD_TAG]`](/index.php/Creature_token#CV_ADD_TAG "Creature token") and [`[CV_REMOVE_TAG]`](/index.php/Creature_token#CV_REMOVE_TAG "Creature token") tokens that have been defined in the current creature. |
|  AQUATIC | Caste |  | Enables the creature to breathe in water, but causes it to air-drown on dry land. |
|  ARENA_RESTRICTED | Caste |  | Causes the creature to be excluded from the object testing arena's creature spawning list. Typically applied to spoileriffic creatures. |
|  ARTIFICIAL_HIVEABLE | Creature |  | Enables the creature to be kept in artificial hives by beekeepers. |
|  AT_PEACE_WITH_WILDLIFE | Caste |  | Prevents the creature from attacking or frightening creatures with the [`[NATURAL]`](/index.php/Creature_token#NATURAL "Creature token") tag. |
|  ATTACK | Caste | token / selection criteria (it's complicated) | Defines the attack name, and the body part used. See / below / for valid subtokens / Example: / \[ATTACK:GORE:BODYPART:BY_CATEGORY:HORN\] / GORE / = name of the attack / BODYPART:BY_CATEGORY:HORN / = the horn is used to attack (presuming the creature has one) |
|  ATTACK_TRIGGER | Caste | population / exported wealth / created wealth | Specifies when a megabeast or semi-megabeast will attack the fortress. The attacks will start occurring when all of the requirements are met. Setting a value to 0 disables the trigger. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## B

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  BABY | Caste | integer | Age at which creature is considered a child, the default is zero. One can think of this as the duration of the baby stage. |
|  BABYNAME | Caste | singular / plural | Defines a new name for a creature in baby state at the caste level. For non-caste-specific baby names, see [`[GENERAL_BABY_NAME]`](/index.php/Creature_token#GENERAL_BABY_NAME "Creature token"). |
|  BEACH_FREQUENCY | Caste | integer | Creature may be subject to beaching, becoming stranded on shores, where they will eventually air-drown. The number indicates the frequency of the occurrence. Presumably requires the creature to be [`[AQUATIC]`](/index.php/Creature_token#AQUATIC "Creature token"). Used by orcas, sperm whales and sea nettle jellyfish in the vanilla game. |
|  BENIGN | Caste |  | The creature is non-aggressive by default, and will never automatically be engaged by companions or soldiers, running away from any creatures that are not friendly to it, and will only defend itself if it becomes enraged. Can be thought of as the counterpoint of the / \[LARGE_PREDATOR\] / tag. When tamed, animals with this tag will be useless for fortress defense. / This and / \[TRADE_CAPACITY\] / are required for / \[PACK_ANIMAL\] / to function properly, if an animal contains the aforementioned requirements without this tag: items loaded by the merchants will be dropped upon departure. |
|  BIOME | Creature | biome token | Select a biome the creature may appear in. |
|  BLOOD | Caste | \ / \ | Specifies what the creature's blood is made of. |
|  BLOODSUCKER | Caste |  | Causes vampire-like behaviour; the creature will suck the blood of unconscious victims when its thirst for blood grows sufficiently large. When controlling the creature in adventure mode, this can be done at will. Seems to be required to make the creature denouncable (in-world) as a creature of the night. |
|  BODY | Caste | body parts | Draws body parts from OBJECT:BODY files (such as body_default.txt) / Example: / \[BODY:BODY_WITH_HEAD_FLAG:HEART:GUTS:BRAIN:MOUTH\] / This is the body from a / purring maggot / . It creates a body with head, a heart, some guts, a brain, and a mouth. That's all a maggot needs. / The body parts need to be listed in an order such that any parent part appears before its connected children. For example \[BODY:HEART:BODY_WITH_HEAD_FLAG\] produces a "Body Token Recognized But Could Not Connect: HEART" error because HEART can't find any UPPERBODY(s) to connect to. Switching the order to \[BODY:BODY_WITH_HEAD_FLAG:HEART\] fixes the problem because now the UPPERBODY is created before the HEART tries to connect to it. / If the body is left undefined, the creature (or caste) will be tagged as \[DOES_NOT_EXIST\]. / \[ / Verify / \] |
|  BODY_APPEARANCE_MODIFIER | Caste | ATTRIBUTE / lowest / lower / low / median / high / higher / highest | These body modifiers give individual creatures different characteristics. In the case of HEIGHT, BROADNESS and LENGTH, the modifier is also a percentage change to the BODY_SIZE of the individual creature. The seven numbers afterward give a distribution of ranges. Each interval has an equal chance of occurring. / Example: / \[BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110\] / HEIGHT / : marks the height to be changed / 90:95:98:100:102:105:110 / : sets the range from the shortest (90% of the average height) to the tallest (110% of the average height) creature variation. |
|  BODY_DETAIL_PLAN | Caste | PlanName / Arguments | Loads a plan from listed OBJECT:BODY_DETAIL_PLAN files, such as b_detail_plan_default.txt. Mass applies USE_MATERIAL_TEMPLATE, mass alters RELSIZE, alters body part positions, and will allow tissue layers to be defined. Tissue layers are defined in order of skin to bone here. / Example: / \[BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE\] / This creates the detailed body of a / fox / , the skin, fat, muscle, bones and cartilage out of the vertebrate tissues. / A / maggot / would only need: / \[BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:SKIN:FAT:MUSCLE\] |
|  BODY_SIZE | Caste | years / days / size | Sets size at a given age. Size is in cubic centimeters, and for normal body materials, is roughly equal to the creature's average weight in grams. / Example: / \[BODY_SIZE:0:0:10000\] / \[BODY_SIZE:1:168:50000\] / \[BODY_SIZE:12:0:220000\] / This describes the size of a / minotaur / . Its birth size would be 10,000 cm / 3 / (~10 kg). At 1 year and 168 days old it would be 50,000 cm / 3 / (~50 kg). And as an adult (at 12 years old) it would be 220,000 cm / 3 / and weigh roughly 220 kg. |
|  BODYGLOSS | Caste | gloss | Substitutes body part text with replacement text. Draws gloss information from OBJECT:BODY files (such as body_default.txt) |
|  BONECARN | Caste |  | Creature eats bones. Implies [`[CARNIVORE]`](/index.php/Creature_token#CARNIVORE "Creature token"). Currently does not work due to a bug (Bug:11069). |
|  BP_ADD_TYPE | Caste |  | Adds a type to a body part - used with [`[SET_BP_GROUP]`](/index.php/Creature_token#SET_BP_GROUP "Creature token"). In vanilla DF, this is used for adding the type 'GELDABLE' to the lower body of certain creatures. |
|  BP_APPEARANCE_MODIFIER | Caste | QUALITY / lowest / lower / low / median / high / higher / highest | Sets up the breadth of possibilities for appearance qualities for a selected BP group. EG. Eyes (CLOSE_SET, DEEP_SET, ROUND_VS_NARROW, LARGE_IRIS),Lips (THICKNESS), Nose (BROADNESS, LENGTH, UPTURNED, CONVEX), Ear (SPLAYED_OUT, HANGING_LOBES, BROADNESS, HEIGHT), Tooth (GAPS), Skull (HIGH_CHEEKBONES, BROAD_CHIN, JUTTING CHIN, SQUARE_CHIN), Neck (DEEP_VOICE, RASPY_VOICE), Head (BROADNESS, HEIGHT) |
|  BP_REMOVE_TYPE | Caste |  | Removes a type from a body part. Used with [`[SET_BP_GROUP]`](/index.php/Creature_token#SET_BP_GROUP "Creature token"). |
|  BUILDINGDESTROYER | Caste | 1 or 2 | Allows a creature to destroy furniture and buildings. Value \[1\] targets mostly doors, hatches, furniture and the like. Value \[2\] targets anything not made with the b + C commands. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## C

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  CAN_DO_INTERACTION | Caste | interaction token | The creature can perform an interaction. See interaction token. |
|  CAN_LEARN | Caste |  | The creature gains skills and can have professions. If a member of a civilization (even a pet) has this token, it'll need to eat, drink and sleep. Note that this token makes the creature unable to be eaten by an adventurer, so it is not recommended for uncivilized monsters. Adventurers lacking this token can allocate but not increase attributes and skills. Skills allocated will disappear on start. A creature with at least this token or the [`[CAN_SPEAK]`](/index.php/Creature_token#CAN_SPEAK "Creature token") token will be able to have values and goals. |
|  CAN_SPEAK | Caste |  | Can talk. Note that this is not necessary for a creature to gain social skills but to make friends in fortress mode. A creature with at least this token or the [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") token will be able to have values and goals. |
|  CANNOT_CLIMB | Caste |  | Creature cannot climb, even if it has free grasp parts. |
|  CANNOT_JUMP | Caste |  | Creature cannot jump. |
|  CANNOT_UNDEAD | Caste |  | Acts like [`[NOT_LIVING]`](/index.php/Creature_token#NOT_LIVING "Creature token"), except that [`[OPPOSED_TO_LIFE]`](/index.php/Creature_token#OPPOSED_TO_LIFE "Creature token") creatures will attack them. |
|  CANOPENDOORS | Caste |  | Defunct, as doors cannot be set as tightly closed anymore. |
|  CARNIVORE | Caste |  | Creature *only* eats meat. If the creature goes on rampages in worldgen, it will often devour the people/animals it kills. |
|  CASTE | Creature | name | Defines a caste. |
|  CASTE_ALTTILE | Caste | tile number or "letter" | Caste-specific [`[ALTTILE]`](/index.php/Creature_token#ALTTILE "Creature token"). Requires [`[CASTE_TILE]`](/index.php/Creature_token#CASTE_TILE "Creature token"). |
|  CASTE_COLOR | Caste | fg / bg / brightness | Caste-specific [`[COLOR]`](/index.php/Creature_token#COLOR "Creature token"). |
|  CASTE_GLOWCOLOR | Caste | fg / bg / brightness | Caste-specific [`[GLOWCOLOR]`](/index.php/Creature_token#GLOWCOLOR "Creature token"). |
|  CASTE_GLOWTILE | Caste | tile value or "letter" | Caste-specific [`[GLOWTILE]`](/index.php/Creature_token#GLOWTILE "Creature token"). |
|  CASTE_NAME | Caste | singular / plural / adjective | While [`[NAME]`](/index.php/Creature_token#NAME "Creature token") describes the name of the species, [`[CASTE_NAME]`](/index.php/Creature_token#CASTE_NAME "Creature token") names individuals of the species. Unlike other caste-specific descriptions, this token is required, even for creatures without separate castes. If left undefined, the creature will not show up in the arena and members of the species will be labeled as "nothing". |
|  CASTE_PROFESSION_NAME | Caste | Unit type token / (Profession) / singular / plural | Caste-specific [`[PROFESSION_NAME]`](/index.php/Creature_token#PROFESSION_NAME "Creature token"). |
|  CASTE_SOLDIER_ALTTILE | Caste | 'character' or tile number | Caste-specific [`[SOLDIER_ALTTILE]`](/index.php/Creature_token#SOLDIER_ALTTILE "Creature token"). Requires [`[CASTE_SOLDIER_TILE]`](/index.php/Creature_token#CASTE_SOLDIER_TILE "Creature token"). |
|  CASTE_SOLDIER_TILE | Caste | 'character' or tile number | Caste-specific [`[CREATURE_SOLDIER_TILE]`](/index.php/Creature_token#CREATURE_SOLDIER_TILE "Creature token"). |
|  CASTE_TILE | Caste | tile number or "letter" | Caste-specific [`[CREATURE_TILE]`](/index.php/Creature_token#CREATURE_TILE "Creature token"). |
|  CAVE_ADAPT | Caste |  | Causes the creature to develop / cave adaptation / . / Allows for creature's race to be involved in jokes that end in "And the \[race\] saw the sun and vomited on the spot!" |
|  CDI | Caste | Varies | Specifies interaction details following a [`[CAN_DO_INTERACTION]`](/index.php/Creature_token#CAN_DO_INTERACTION "Creature token") token. See interaction token. |
|  CHANGE_BODY_SIZE_PERC | Caste | integer | Multiplies body size by a factor of (integer)%. 50 halves size, 200 doubles. |
|  CHANGE_FREQUENCY_PERC | Creature | integer | Multiplies frequency by a factor of (integer)%. |
|  CHILD | Caste | integer | Age at which creature is considered an adult - one can think of this as the duration of the child stage. Allows the creature's offspring to be rendered fully tame if trained during their childhood. |
|  CHILDNAME | Caste | singular / plural | Defines a new name for a creature in the child state at the caste level. For non-caste-specific child names, see [`[GENERAL_CHILD_NAME]`](/index.php/Creature_token#GENERAL_CHILD_NAME "Creature token"). |
|  CLUSTER_NUMBER | Creature | min / max | The minimum/maximum numbers of how many creatures per spawned cluster. Vermin fish with this token in combination with temperate ocean and river biome tokens will perform seasonal migrations. Defaults to 1:1 if not specified. |
|  CLUTCH_SIZE | Caste | min / max | Number of eggs laid in one sitting. |
|  COLONY_EXTERNAL | Caste |  | Caste hovers around colony. |
|  COLOR | Creature | foreground / background / brightness | Color of the creature's tile. (See Color for usage.) |
|  COMMON_DOMESTIC | Caste |  | When combined with any of [`[PET]`](/index.php/Creature_token#PET "Creature token"), [`[PACK_ANIMAL]`](/index.php/Creature_token#PACK_ANIMAL "Creature token"), [`[WAGON_PULLER]`](/index.php/Creature_token#WAGON_PULLER "Creature token") and/or [`[MOUNT]`](/index.php/Creature_token#MOUNT "Creature token"), the creature is guaranteed to be domesticated by any civilization with [`[COMMON_DOMESTIC_PET]`](/index.php/Entity_token#COMMON_DOMESTIC_PET "Entity token"), [`[COMMON_DOMESTIC_PACK]`](/index.php/Entity_token#COMMON_DOMESTIC_PACK "Entity token"), [`[COMMON_DOMESTIC_PULL]`](/index.php/Entity_token#COMMON_DOMESTIC_PULL "Entity token") and/or [`[COMMON_DOMESTIC_MOUNT]`](/index.php/Entity_token#COMMON_DOMESTIC_MOUNT "Entity token") respectively. Such civilizations will always have access to the creature, even in the absence of wild populations. This token is invalid on [`[FANCIFUL]`](/index.php/Creature_token#FANCIFUL "Creature token") creatures. |
|  CONVERTED_SPOUSE | Caste |  | Creatures of this caste's species with the [`[SPOUSE_CONVERTER]`](/index.php/Creature_token#SPOUSE_CONVERTER "Creature token") and [`[NIGHT_CREATURE_HUNTER]`](/index.php/Creature_token#NIGHT_CREATURE_HUNTER "Creature token") tokens will kidnap [`[SPOUSE_CONVERSION_TARGET]`](/index.php/Creature_token#SPOUSE_CONVERSION_TARGET "Creature token")s of an appropriate sex and convert them into castes with CONVERTED_SPOUSE. |
|  COOKABLE_LIVE | Caste |  | Set this to allow the creature to be cooked in meals while it is still alive, as well as when it's dead but not yet cleaned. Used by some water-dwelling vermin such as mussels, nautiluses and oysters. Currently does not work correctly when applied to non-[`[FISHITEM]`](/index.php/Creature_token#FISHITEM "Creature token") vermin.Bug:13200 |
|  CRAZED | Caste |  | Creature is 'berserk' and will attack all other creatures, except members of its own species that **also** have the CRAZED tag. It will show Berserk in the unit list. Berserk creatures go on rampages during worldgen much more frequently than non-berserk ones. |
|  COPY_TAGS_FROM | Special | creature ID | Copies another specified creature. This will override any definitions made before it; essentially, it makes this creature identical to the other one, which can then be modified. Often used in combination with [`[APPLY_CREATURE_VARIATION]`](/index.php/Creature_token#APPLY_CREATURE_VARIATION "Creature token") to import standard variations from a file. The vanilla giant animals and animal peoples are examples of this token combination. |
|  CREATURE | Creature | creature ID | A unique, arbitrary identifier that begins the definition of each new creature, and is used to reference the creature in other tokens and raws. |
|  CREATURE_CLASS | Caste | classname | An arbitrary creature classification. Can be set to anything, but the only vanilla uses are GENERAL_POISON (used in syndromes), EDIBLE_GROUND_BUG (used as targets for / \[GOBBLE_VERMIN_CLASS\] / ), MAMMAL, and POISONOUS (both used for kobold pet eligibility). A single creature can have multiple classes. / The full list of tokens that use creature classes is: / Creature tokens: / \[GOBBLE_VERMIN_CLASS\] / , / \[GOBBLE_VERMIN_CLASS\] / Interaction tokens: / \[IT_AFFECTED_CLASS\] / , / \[IT_IMMUNE_CLASS\] / Animal definition (Entity) tokens: / \[ANIMAL_CLASS\] / , / \[ANIMAL_FORBIDDEN_CLASS\] / Position (Entity) token: / \[ALLOWED_CLASS\] / Syndrome tokens: / \[SYN_AFFECTED_CLASS\] / , / \[SYN_IMMUNE_CLASS\] / , / \[CE_SENSE_CREATURE_CLASS\] |
|  CREATURE_SOLDIER_TILE | Creature | 'character' or tile number | Creatures active in their civilization's military will use this tile instead. |
|  CREATURE_TILE | Creature | 'character' or tile number | The symbol of the creature in ASCII mode. |
|  CREPUSCULAR | Caste |  | When set, the creature will appear at dawn (between 4:30 AM and 6:00 AM) and in the evening (between 8:00 PM and 10:05 PM) in Adventurer mode. |
|  CURIOUSBEAST_EATER | Caste |  | Allows a creature to steal and eat edible items from a site. It will attempt to grab a food item and immediately make its way to the map's edge, where it will disappear with it. If the creature goes on rampages during worldgen, it will often steal food instead of attacking. Trained and tame instances of the creature will no longer display this behavior. |
|  CURIOUSBEAST_GUZZLER | Caste |  | Allows a creature to (very quickly) drink your alcohol. Or spill the barrel to the ground. Also affects undead versions of the creature. Unlike food or item thieves, drink thieves will consume your alcohol on the spot rather than run away with one piece of it. Trained and tame instances of the creature will no longer display this behavior. |
|  CURIOUSBEAST_ITEM | Caste |  | Allows a creature to steal things (apparently, of the highest value it can find). It will attempt to grab an item of value and immediately make its way to the map's edge, where it will disappear with it. If a creature with any of the CURIOUSBEAST tokens carries anything off the map, even if it is a caravan's pack animal, it will be reported as stealing everything it carries. If the creature goes on rampages in worldgen, it will often steal items instead of attacking - kea birds are infamous for this. Trained and tame instances of the creature will no longer display this behavior. Also, makes the creature unable to drop hauled items until it enters combat. |
|  CV_ADD_TAG | Special | TAG NAME | Adds a tag. Used in conjunction with creature variation templates. |
|  CV_REMOVE_TAG | Special | TAG NAME | Removes a tag. Used in conjunction with creature variation templates. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## D

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  DEMON | Caste |  | Found on generated / demons / . / At least 1 demon generated, or custom must have the / \[FLIER\] / token in order for the / horrifying screams / event to trigger. |
|  DESCRIPTION | Caste | text | A brief description of the creature type, as displayed when viewing the creature's description/thoughts & preferences screen. |
|  DIE_WHEN_VERMIN_BITE | Caste |  | Causes the creature to die upon attacking. Used by honey bees to simulate them dying after using their stingers. |
|  DIFFICULTY | Caste | integer | Increases experience gain during adventure mode. Creatures with a difficulty of 11 or higher are not assigned for quests in adventure mode. |
|  DIURNAL | Caste |  | When set, the creature will only appear during the day (between 6:00 AM and 8:00 PM) in Adventurer mode. |
|  DIVE_HUNTS_VERMIN | Caste |  | The creature hunts vermin by diving from the air. On tame creatures, it has the same effect as [`[HUNTS_VERMIN]`](/index.php/Creature_token#HUNTS_VERMIN "Creature token"). Found on peregrine falcons. |
|  DOES_NOT_EXIST | Creature |  | Adding this token to a creature prevents it from appearing in generated worlds (unless it's marked as / always present / for a particular civilisation). For example, adding it to / dogs / will lead to worlds being generated without dogs in them. Also removes the creature from the / object testing arena / 's spawn list. If combined with / \[FANCIFUL\] / , artistic depictions of the creature will occur regardless. Used by / centaurs / , / chimeras / and / griffons / in the vanilla game. / Note: a creature tagged as DOES_NOT_EXIST can still be / summoned / successfully, as long as it has a body defined in its raws / \[1\] / , or, another creature can / transform / into it. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## E

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  EBO_ITEM | Caste | item token / material token / (ANY_HARD_STONE can be used for the material) | Defines the item that the creature drops upon being butchered. Used with [`[EXTRA_BUTCHER_OBJECT]`](/index.php/Creature_token#EXTRA_BUTCHER_OBJECT "Creature token"). |
|  EBO_SHAPE | Caste | gem shape | The shape of the creature's extra butchering drop. Used with [`[EXTRA_BUTCHER_OBJECT]`](/index.php/Creature_token#EXTRA_BUTCHER_OBJECT "Creature token"). |
|  EGG_MATERIAL | Caste | \ / \ | Defines the material composition of eggs laid by the creature. Egg-laying creatures in the default game define this 3 times, using LOCAL_CREATURE_MAT:EGGSHELL, LOCAL_CREATURE_MAT:EGG_WHITE, and then LOCAL_CREATURE_MAT:EGG_YOLK. Eggs will be made out of eggshell. Edibility is determined by tags on whites or yolk, but they otherwise do not exist. |
|  EGG_SIZE | Caste | size | Determines the size of laid eggs. Doesn't affect hatching or cooking, but bigger eggs will be heavier, and may take longer to be hauled depending on the hauler's strength. |
|  EQUIPMENT_WAGON | Creature |  | Makes the creature appear as a large 3×3 wagon responsible for carrying trade goods, pulled by two [`[WAGON_PULLER]`](/index.php/Creature_token#WAGON_PULLER "Creature token") creatures and driven by a merchant. |
|  EQUIPS | Caste |  | Allows the creature to wear or wield items. |
|  EVIL | Creature |  | The creature is considered evil and will only show up in evil biomes. Civilizations with / \[USE_EVIL_ANIMALS\] / can domesticate them regardless of exotic status. Has no effect on cavern creatures except to restrict taming. A civilization with evil creatures can colonize evil areas. / Civilizations which list evil creatures as one of their main population options will potentially emerge following an underworld mining disaster, with the added caveat that a demon will be in charge of the civ. The rules which govern which noble position the demon in charge adopts however, are unclear. It either picks one of the predefined positions, or simply makes its own. |
|  EXTRA_BUTCHER_OBJECT | Caste | BY_CATEGORY / or / BY_TYPE / or / BY_TOKEN / TYPE, CATEGORY, or TOKEN | The creature drops an additional object when butchered, as defined by [`[EBO_ITEM]`](/index.php/Creature_token#EBO_ITEM "Creature token") and [`[EBO_SHAPE]`](/index.php/Creature_token#EBO_SHAPE "Creature token"). Used for gizzard stones in default creatures. For some materials, needs to be defined after caste definitions with SELECT_CASTE:ALLBug:6355 |
|  EXTRACT | Caste | material token | Defines a creature extract which can be obtained via small animal dissection. |
|  EXTRAVISION | Caste |  | The creature can see regardless of whether it has working eyes and has full 360 degree vision, making it impossible to strike the creature from a blind spot in combat. Invisible creatures will also be seen, namely intelligent undead using a "vanish" power. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## F

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  FANCIFUL | Creature |  | The creature is a thing of legend and known to all civilizations. Its materials cannot be requested or preferred. The tag also adds some art value modifiers. Used by a number of creatures. Conflicts with [`[COMMON_DOMESTIC]`](/index.php/Creature_token#COMMON_DOMESTIC "Creature token"). |
|  FEATURE_ATTACK_GROUP | Caste |  | Found on subterranean animal-man tribals. Currently defunct. In previous versions\[Verify\], it caused these creatures to crawl out of chasms and underground rivers. |
|  FEATURE_BEAST | Caste |  | Found on / forgotten beasts / . Presumably makes it act as such, initiating underground attacks on fortresses, or leads to the pop-up message upon encountering one / \[ / Verify / \] / . Displays the creature's / \[DESCRIPTION\] / in its / legends mode / entry and hides the creature from displaying in a world_sites_and_pops file. Does not create historical figures like generated forgotten beasts do. / Requires specifying a / \[BIOME\] / in which the creature will live, and both surface and subterranean biomes are allowed. Does not stack with / \[LARGE_ROAMING\] / and if both are used the creature will not spawn. Appears to be incompatible with / \[DEMON\] / even if used in separate castes. |
|  FEMALE | Caste |  | Makes the creature biologically female, enabling her to bear young. Usually specified inside a caste. |
|  FIREIMMUNE | Caste |  | Makes the creature immune to FIREBALL and FIREJET attacks, and allows it to path through high temperature zones, like lava or fires. Does not, by itself, make the creature immune to the damaging effects of burning in fire, and does not prevent general heat damage or melting on its own (this would require adjustments to be made to the creature's body materials - see the dragon raws for an example). |
|  FIREIMMUNE_SUPER | Caste |  | Like [`[FIREIMMUNE]`](/index.php/Creature_token#FIREIMMUNE "Creature token"), but also renders the creature immune to DRAGONFIRE attacks. |
|  FISHITEM | Caste |  | The creature's corpse is a single / FISH_RAW / food item that needs to be cleaned (into a / FISH / item) at a / fishery / to become edible. Before being cleaned the item is referred to as "raw". The food item is categorized under "fish" on the food and stocks screens, and when uncleaned it is sorted under "raw fish" in the stocks (but does not show up on the food screen). / Without this or / \[COOKABLE_LIVE\] / , / fished / vermin will turn into food the same way as non-vermin creatures, resulting in multiple units of food (meat, brain, lungs, eyes, spleen etc.) from a single fished vermin. These units of food are categorized as meat by the game. |
|  FIXED_TEMP | Caste | temperature | The creature's body is constantly at this temperature, heating up or cooling the surrounding area. Alters the temperature of the creature's inventory and all adjacent tiles, / with all the effects that this implies / - may trigger wildfires at high enough values. Also makes the creature immune to extreme heat or cold, as long as the temperature set is not harmful to the materials that the creature is made from. Corpses and body parts of creatures with a fixed temperature maintain their temperature even after death. / Note that temperatures of 12000 and higher may cause / pathfinding / issues in fortress mode. |
|  FLEEQUICK | Caste |  | If engaged in combat, the creature will flee at the first sign of resistance. Used by kobolds in the vanilla game. |
|  FLIER | Caste |  | Allows a creature to fly, independent of it having wings or not. Fortress Mode pathfinding only partially incorporates flying - flying creatures need a land path to exist between them and an area in order to access it, but as long as one such path exists, they do not need to use it, instead being able to fly over intervening obstacles. Winged creatures with this token can lose their ability to fly if their wings are crippled or severed. Winged creatures without this token will be unable to fly. (A 'wing' in this context refers to any body part with its own / FLIER / token). / At least 1 / Demon / must have the flier token in order for the / horrifying screams / event to trigger. |
|  FREQUENCY | Creature | number, max 100 | The / \[FREQUENCY\] / value plays two separate roles. The first is in determining the initial distribution of creatures across the world map. Each creature is randomly assigned a single x, y co-ordinate on the world map, which act as the epicenter for that creature's distribution. A square is drawn around that x, y co-ordinate with a Manhattan radius equal to the / \[FREQUENCY\] / value divided by 100 times the world map size. For example, in a 256 by 256 size world map, the / lion / might be assigned 14, 112. The / lion / has / \[FREQUENCY:5\] / , and so a square is drawn by moving 13 tiles in each direction from the / lion / 's x, y co-ordinate. This is the / lion / 's "territory". / Each sub-region in the world will attempt to fill lists of wildlife. There are five lists - / \[VERMIN_GROUNDER\] / , / \[VERMIN_SOIL\] / , / \[VERMIN_SOIL_COLONY\] / , / \[LARGE_ROAMING\] / , and / \[LARGE_PREDATOR\] / , corresponding with the relevant tokens. The game will attempt to place seven creatures in each list for each sub-region. The game will select the seven nearest valid creatures. Creatures are valid for sub-region's list if they have the requisite token for that list, if they have the valid token for that sub-region's biome (for example, the \[lion\] can only be selected for / \[BIOME:SAVANNA_TROPICAL\] / , / \[BIOME:GRASSLAND_TROPICAL\] / , and / \[BIOME:SHRUBLAND_TROPICAL\] / , and if their "territory" as defined by their random epicenter and / \[FREQUENCY\] / radius overlaps with that sub-region. These lists then determine the creatures that can actually appear within that sub-region during gameplay. / There are some exceptions to the above. If the game was not capable of filling all seven entries in a list, it will drop the overlapping territory requirement, and simply pull the nearest creature which has the correct token and biome availability. Conversely, if a creature has an epicenter but has not appeared on any of the list for any of the world map's sub-regions, the creature will be assigned to the relevant list for the nearest appropriate sub-region - meaning it is occasionally possible to have lists of eight creatures or more. This is more common in smaller worlds where there are less possible sub-regions to be assigned towards. Creatures with the / \[GOOD\] / and / \[EVIL\] / tokens ignore the epicenter distribution system altogether. They are always capable of appearing in appropriate biomes which are / \[GOOD\] / or / \[EVIL\] / respectively. This is not true for / \[SAVAGE\] / , which acts more like the biome tokens. Creatures with / \[UBIQUITOUS\] / have a "territory" which covers the entire map, regardless of their epicenter (although they can still fail to be chosen if there are 7 creatures which are eligible and have nearer epicenters to the sub-region in question). / The second use for / \[FREQUENCY\] / is to determine how often a creature actually appears on map. In Fortress Mode, the game will try and spawn large wildlife (creatures with / \[LARGE_ROAMING\] / or / \[LARGE_PREDATOR\] / in fairly regular waves. These waves include / \[LARGE_ROAMING\] / , / \[LARGE_ROAMING\] / combined with / \[FLIER\] / , / \[LARGE_PREDATOR\] / , and / \[CURIOUS_BEAST\] / - so a / lion / does not compete for selection with a / gazelle / . When the game decides it needs to spawn in a fresh wave of e.g. / \[LARGE_ROAMING\] / creatures, it will select one of the creatures available to it from the lists for that sub-region at random, with all creatures weighted equally. Once it has selected a creature, it then effectively rolls a d100 against the relevant creature's / \[FREQUENCY\] / . If the d100 is equal to the creature's / \[FREQUENCY\] / or less, that creature is then spawned in. If the d100 is above the creature's / \[FREQUENCY\] / , the game returns to the relevant list and selects again. / \[UBIQUITOUS\] / acts as / \[FREQUENCY:100\] / for these purposes - in other words, the creature cannot fail the d100 check and will always be spawned in if it is selected from the list. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## G

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  GAIT | Caste | speed\> / speed\> / speed\> | Defines a gait by which the creature can move. See / Gait / for more information. Specifically, you likely want to use one of the existing STANDARD_X_GAITS creature variations, as described in / this subsection / . / indicates the maximum / speed / achievable by a creature using this gait / indicates the creature's speed when it starts moving using this gait / indicates how long it will take for a creature using this gait to go from / to / . For example, a value of 10 means that it should be able to reach the maximum speed by moving 10 / tiles / in a straight line over even terrain. / indicates the maximum speed permissible when the creature suddenly changes its direction of motion. The creature's speed will be reduced to / if travelling at a higher speed than this before turning. / indicates how energy-consuming the gait is. Higher values cause the creature to tire out faster. Persistent usage of a high-intensity gait will eventually lead to exhaustion and / collapse / . / NO_BUILD_UP / can be specified instead of a / value to make the / instantly achievable upon initiating movement (this is equivalent to a / of 0). Note that / and / are both ignored if specified alongside this (as NO_BUILD_UP trumps / and preserves / whilst turning, and / cannot exceed / ) so it is permissible to omit them so long as they are / both / omitted together. / It's possible to specify a / greater than the / ; the moving creature will decelerate towards its / in this case. / valid gait types: / WALK / Used for moving normally over ground tiles. / CRAWL / Used for moving over ground tiles whilst / prone / . / SWIM / Used for moving through tiles containing / water / or / magma / at a / depth / of at least 4 / 7. / FLY / Used for moving through / open space / . / CLIMB / Used for moving whilst / climbing / . / valid gait flags: / AGILITY / Speeds / slows movement depending on the creature's / Agility / stat. / STRENGTH / Speeds / slows movement depending on the creature's / Strength / stat. / LAYERS_SLOW / Makes / THICKENS_ON_ENERGY_STORAGE / and / THICKENS_ON_STRENGTH / tissue layers slow movement depending on how thick they are. Adding the STRENGTH gait flag counteracts the impact of the latter layer. / STEALTH_SLOWS: / Slows movement by the specified percentage when the creature is / sneaking / . |
|  GENERAL_BABY_NAME | Creature | singular / plural | Like [`[BABYNAME]`](/index.php/Creature_token#BABYNAME "Creature token"), but applied regardless of caste. |
|  GENERAL_CHILD_NAME | Creature | singular / plural | Like [`[CHILDNAME]`](/index.php/Creature_token#CHILDNAME "Creature token"), but applied regardless of caste. |
|  GENERAL_MATERIAL_FORCE_MULTIPLIER | Caste | value A / value B | Has the same function as [`[MATERIAL_FORCE_MULTIPLIER]`](/index.php/Creature_token#MATERIAL_FORCE_MULTIPLIER "Creature token"), but applies to all attacks instead of just those involving a specific material. Appears to be overridden by MATERIAL_FORCE_MULTIPLIER (werebeasts, for example, use both tokens to provide resistance to all materials, with one exception to which they are especially vulnerable). |
|  GENERATED | Creature |  | Found on procedurally generated creatures like forgotten beasts, titans, demons, angels, and night creatures. Cannot be specified in user-defined raws. |
|  GETS_INFECTIONS_FROM_ROT | Caste |  | Makes the creature get infections from necrotic tissue. |
|  GETS_WOUND_INFECTIONS | Caste |  | Makes the creature's wounds become infected if left untreated for too long. |
|  GLOWCOLOR | Creature | foreground / background / brightness | The colour of the creature's [`[GLOWTILE]`](/index.php/Creature_token#GLOWTILE "Creature token"). |
|  GLOWTILE | Creature | ascii character | If present, the being glows in the dark (generally used for Adventurer Mode). The tile is what replaces the being's current tile when it is obscured from your sight by darkness. The default setting for kobolds (a yellow quotation mark) provides a nice "glowing eyes" effect. The game is also hardcoded to automatically convert quotation mark GLOWTILES into apostrophes if the creature has lost one eye. This works at the generic creature level - for caste-specific glow tiles, use [`[CASTE_GLOWTILE]`](/index.php/Creature_token#CASTE_GLOWTILE "Creature token") instead. |
|  GNAWER | Caste | verb | The creature can and will gnaw its way out of animal traps and cages using the specified verb, depending on the material from which it is made (normally wood). |
|  GOBBLE_VERMIN_CLASS | Caste | class | The creature eats vermin of the specified class. |
|  GOBBLE_VERMIN_CREATURE | Caste | creature / caste | The creature eats a specified vermin. |
|  GO_TO_END | Special |  | When using tags from an existing creature, inserts new tags at the end of the creature. |
|  GO_TO_START | Special |  | When using tags from an existing creature, inserts new tags at the beginning of the creature. |
|  GO_TO_TAG | Special |  | When using tags from an existing creature, inserts new tags *before* the specified tag. |
|  GOOD | Creature |  | Creature is considered good and will only show up in good biomes - unicorns, for example. Civilizations with [`[USE_GOOD_ANIMALS]`](/index.php/Entity_token#USE_GOOD_ANIMALS "Entity token") can domesticate them regardless of exotic status. Has no effect on cavern creatures except to restrict taming. A civilization that has good creatures can colonise good areas in world-gen. |
|  GRASSTRAMPLE | Caste | value | The value determines how rapidly grass is trampled when a creature steps on it - a value of 0 causes the creature to never damage grass, while a value of 100 causes grass to be trampled as rapidly as possible. Defaults to 5. |
|  GRAVITATE_BODY_SIZE | Caste | target value | Used in Creature Variants. This token changes the adult body size to the average of the old adult body size and the target value and scales all intermediate growth stages by the same factor. |
|  GRAZER | Caste | number | The creature is a grazer - if tamed in fortress mode, it needs a pasture to survive. The higher the number, the less frequently it needs to eat in order to live. Not used since 0.40.12, replaced by [`[STANDARD_GRAZER]`](/index.php/Creature_token#STANDARD_GRAZER "Creature token") to fix Bug 4113. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## H

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  HABIT | Caste | type / probability | Defines certain behaviors for the creature. The habit types are: / COLLECT_TROPHIES / COOK_PEOPLE / COOK_VERMIN / GRIND_VERMIN / COOK_BLOOD / GRIND_BONE_MEAL / EAT_BONE_PORRIDGE / USE_ANY_MELEE_WEAPON / GIANT_NEST / COLLECT_WEALTH. / These require the creature to have a / \[LAIR\] / to work properly, and also don't seem to work on creatures who are not a / \[SEMIMEGABEAST\] / , / \[MEGABEAST\] / , or / \[NIGHT_CREATURE_HUNTER\] / . |
|  HABIT_NUM | Caste | number or TEST_ALL | "If you set HABIT_NUM to a number, it should give you that exact number of habits according to the weights.".[1] All lists of HABITs are preceded by \[HABIT_NUM:TEST_ALL\] |
|  HAS_NERVES | Caste |  | The creature has nerves in its muscles. Cutting the muscle tissue can sever motor and sensory nerves, disabling the limb. |
|  HASSHELL | Caste |  | The creature has a shell. Seemingly no longer used - holdover from previous versions. |
|  HIVE_PRODUCT | Creature | number / time / item tokens | What product is harvested from beekeeping. |
|  HOMEOTHERM | Caste | number or NONE | Default 'NONE'. The creature's normal body temperature. Creature ceases maintaining temperature on death unlike fixed material temperatures. Provides minor protection from environmental temperature to the creature. |
|  HUNTS_VERMIN | Caste |  | Creature hunts and kills nearby vermin, randomly walking between places with food laying on the ground or in stockpiles, to check for possible \[VERMIN_EATER\] vermin, but they'll kill any other vermin too. Do not include this creature token on an intelligent entity that you intend to play as in fortress mode because it will prevent them from feeding themselves. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## I

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  IMMOBILE | Caste |  | The creature cannot move. Found on sponges. Will also stop a creature from breeding in fortress mode (MALE and FEMALE are affected, if one is IMMOBILE; no breeding will happen). |
|  IMMOBILE_LAND | Caste |  | The creature is immobile while on land. Only works on [`[AQUATIC]`](/index.php/Creature_token#AQUATIC "Creature token") creatures which can't breathe on land. |
|  IMMOLATE | Caste |  | The creature radiates fire. It will ignite, and potentially completely destroy, items the creature is standing on. Also gives the vermin a high chance of escaping from animal traps and cages made of any flammable materials (specifically ones that could be ignited by magma). |
|  INTELLIGENT | Caste |  | Alias for [`[CAN_SPEAK]`](/index.php/Creature_token#CAN_SPEAK "Creature token") + [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token"). |
|  ITEMCORPSE | Caste | item token / material token | Determines if the creature leaves behind a non-standard corpse (i.e. wood, statue, bars, stone, pool of liquid, etc.). Ethics may prevent actually using the item in jobs or reactions. |
|  ITEMCORPSE_QUALITY | Caste | number | The quality of an item-type corpse left behind. Valid values are: 0 for ordinary, 1 for well-crafted, 2 for finely-crafted, 3 for superior, 4 for exceptional, 5 for masterpiece. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## L

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  LAIR | Caste | type / probability | Found on megabeasts, semimegabeasts, and night creatures. The creature will seek out sites of this type and take them as lairs. The lair types are: / SIMPLE_BURROW / SIMPLE_MOUND / WILDERNESS_LOCATION / SHRINE / LABYRINTH |
|  LAIR_CHARACTERISTIC | Caste | characteristic / probability | Defines certain features of the creature's lair. The only valid characteristic is HAS_DOORS. |
|  LAIR_HUNTER | Caste |  | This creature will actively hunt adventurers in its lair. |

---
*Parte 1 de 3 de «Creature token». Demais partes em arquivos `...-part-{1..3}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Creature_token*
