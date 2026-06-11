# Creature token (parte 2/3)

|  LAIR_HUNTER_SPEECH | Caste | speech file | What this creature says while hunting adventurers in its lair. |
|  LARGE_PREDATOR | Caste |  | Will attack other creatures that are smaller than it. Tamed large predators will still attack wildlife. In / fortress mode / , only one group of "large predators" (possibly two groups on "savage" maps) will appear on any given map. In / adventurer mode / , large predators will try to ambush and attack you (and your party will attack them back). When tamed, large predators tend to be much more aggressive to enemies than non-large predators, making them a good choice for an animal army. They may go on rampages in worldgen, and adventurers may receive quests to kill them. Also, they can be mentioned in the intro paragraph when starting a fortress e.g. "ere the wolves get hungry." / A single biome supports 7 large predator species, picking randomly and rolling a d100 under its / \[FREQUENCY\] / to add it until all 7 slots are filled. / Incompatible with / \[PACK_ANIMAL\] / on a technicality, if included: hauled items are likely to be dropped upon entering the map (even if / \[TRADE_CAPACITY\] / is present) in contrast to when the merchants depart. |
|  LARGE_ROAMING | Creature |  | This is the core requisite tag allowing the creature to spawn as a wild animal in the appropriate biomes. Requires specifying a / \[BIOME\] / in which the creature will spawn. Does not require specifying a frequency, population number, or cluster number. / This tag stacks with / \[MEGABEAST\] / , / \[SEMIMEGABEAST\] / , or / \[NIGHT_CREATURE_HUNTER\] / ; if used with one of these tags, the creature will spawn as both a boss and as a wild animal. This tag does not stack with / \[FEATURE_BEAST\] / and if both are used the creature will not spawn. This tag is unaffected by / \[DEMON\] / . Large roamers are not able to spawn in Pool biomes as they do not connect to the edge of the map and are too small, Lake biomes are a suitable alternative. |
|  LAYS_EGGS | Caste |  | Creature lays eggs instead of giving birth to live young. |
|  LAYS_UNUSUAL_EGGS | Caste | item token / material token | Creature lays the specified item instead of regular eggs. |
|  LIGAMENTS | Caste | material token / healing rate | The creature has ligaments in its [`[CONNECTIVE_TISSUE_ANCHOR]`](/index.php/Tissue_definition_token#CONNECTIVE_TISSUE_ANCHOR "Tissue definition token") tissues (bone or chitin by default). Cutting the bone/chitin tissue severs the ligaments, disabling motor function if the target is a limb. |
|  LIGHT_GEN | Caste |  | A vermin featuring this tag will remain visible to an adventurer even at night. / Subterranean vermin which feature this token will flicker in unexposed and unrevealed cavern layers while playing in Fortress Mode. |
|  LIKES_FIGHTING | Caste |  | The creature will attack enemies rather than flee from them. This tag has the same effect on player-controlled creatures - including modded dwarves. Retired as of v0.40.14 in favor of [`[LARGE_PREDATOR]`](/index.php/Creature_token#LARGE_PREDATOR "Creature token"). |
|  LISP | Caste |  | Creature uses "sssssnake talk" (multiplies 'S' when talking - "My name isss Recisssiz."). Used by serpent men and reptile men in the vanilla game. C's with the same pronunciation (depending on the word) are not affected by this token. |
|  LITTERSIZE | Caste | minimum / maximum | Determines the number of offspring per one birth; default 1-3, not used in vanilla raws. See also [`[MULTIPLE_LITTER_RARE]`](/index.php/Creature_token#MULTIPLE_LITTER_RARE "Creature token"). |
|  LOCAL_POPS_CONTROLLABLE | Creature |  | Allows you to play as a wild animal of this species in adventurer mode. Prevents trading of (tame) instances of this creature in caravans. |
|  LOCAL_POPS_PRODUCE_HEROES | Creature |  | Wild animals of this species may occasionally join a civilization. Prevents trading of (tame) instances of this creature in caravans. |
|  LOCKPICKER | Caste |  | Lets a creature open doors that are set to forbidden in fortress mode. |
|  LOOSE_CLUSTERS | Creature |  | The creatures will scatter if they have this tag, or form tight packs if they don't. |
|  LOW_LIGHT_VISION | Caste | number | Determines how well a creature can see in the dark - higher is better. Dwarves have 10000, which amounts to perfect nightvision. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## M

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  MAGICAL | Caste |  | According to Toady One, this is completely interchangeable with [`[AT_PEACE_WITH_WILDLIFE]`](/index.php/Creature_token#AT_PEACE_WITH_WILDLIFE "Creature token") and might have been used in very early versions of the game by wandering wizards or the ent-type tree creatures that used to be animated by elves. [2] |
|  MAGMA_VISION | Caste |  | The creature is able to see while submerged in magma. |
|  MALE | Caste |  | Makes the creature biologically male; usually declared inside a caste. |
|  MANNERISM\_\* | Caste | occasionally body part | Adds a possible mannerism to the creature's profile. See creature mannerism token for further info. |
|  MATERIAL | Creature | material id | Begins defining a new local material. Follow this with standard material definition tokens to define the material. A maximum of 200 materials can be defined on any given creature. |
|  MATERIAL_FORCE_MULTIPLIER | Caste | Material token / value A / value B | When struck with a weapon made of the specified material, the force exerted will be multiplied by A/B, thus making the creature more or less susceptible to this material. For example, if A is 2 and B is 1, the force exerted by the defined material will be doubled. If A is 1 and B is 2, it will be halved instead. See also [`[GENERAL_MATERIAL_FORCE_MULTIPLIER]`](/index.php/Creature_token#GENERAL_MATERIAL_FORCE_MULTIPLIER "Creature token"), which can be used to make this sort of effect applicable to all materials. |
|  MATUTINAL | Caste |  | When set, the creature will only appear at dawn (between 4:30 AM and 6:00 AM) in Adventurer mode. |
|  MAXAGE | Caste | min / max | Determines the creature's natural lifespan, using the specified minimum and maximum age values (in years). Each individual creature with this token is generated with a predetermined date (calculated down to the exact / tick / !) between these values, at which it is destined to die of old age, should it live long enough. Note that the probability of death at any given age does not increase as the creature gets older / \[3\] / . / Creatures which lack this token are naturally immortal. The / NO_AGING / syndrome tag will prevent death by old age from occurring. Also note that, among civilized creatures, castes which lack this token will refuse to marry others with it, and vice versa. |
|  MEANDERER | Caste |  | Makes the creature slowly stroll around, unless it's in combat or performing a job. If combined with [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token"), will severely impact their pathfinding and lead the creature to move extremely slowly when not performing any task. Problematically applies to animal people based on the animal, and war trained animalsBug:9588. |
|  MEGABEAST | Caste |  | A 'boss' creature; a small number of those are created during worldgen, their histories and descendants (if any) will be tracked in worldgen (as opposed to simply 'spawning'), and they will occasionally go on rampages, potentially leading to worship if they attack the same place multiple times. Their presence and number will also influence age names. When appearing in fortress mode, they will have a pop-up message announcing their arrival. They will remain hostile to the fortress military even after being tamed. / Bug / : / 10731 / See / megabeast / page for more details. / Requires specifying a / \[BIOME\] / in which the creature will live. Subterranean biomes appear to not be allowed. Does stack with / \[LARGE_ROAMING\] / and if both are used the creature will spawn as both historical bosses and as wild animals. |
|  MENT_ATT_CAP_PERC | Caste | ATTRIBUTE / Token / Cap % | Default is 200. This means you can increase your attribute to 200% of its starting value (or the average value + your starting value if that is higher). |
|  MENT_ATT_RANGE | Caste | ATTRIBUTE / lowest / lower / low / median / high / higher / highest | Sets up a mental attribute's range of values (0-5000). All mental attribute ranges default to 200:800:900:1000:1100:1300:2000. |
|  MENT_ATT_RATES | Caste | ATTRIBUTE / Token / cost to improve / unused counter rate / rust counter rate / demotion counter rate | Mental attribute gain/decay rates. Lower numbers in the last three slots make decay occur faster. Defaults are 500:4:5:4. |
|  MILKABLE | Caste | material token / frequency | Allows the creature to be milked in the farmer's workshop. The frequency is the amount of ticks the creature needs to "recharge" (i.e. how much time needs to pass before it can be milked again). Does not work on sentient creatures, regardless of ethics. |
|  MISCHIEVIOUS | Caste |  | Alias for [`[MISCHIEVOUS]`](/index.php/Creature_token#MISCHIEVOUS "Creature token"). |
|  MISCHIEVOUS | Caste |  | The creature spawns stealthed and will attempt to path into the fortress, pulling any levers it comes across. It will be invisible on the map and unit list until spotted by a citizen, at which point the game will pause and recenter on the creature. Used by gremlins in the vanilla game. "They go on little missions to mess with various fortress buildings, not just levers." |
|  MODVALUE | Caste |  | Seemingly no longer used. |
|  MOUNT | Caste |  | Creature may be used as a mount. No use for the player in fortress mode, but enemy sieging forces may arrive with cavalry. Mounts are usable in adventure mode. |
|  MOUNT_EXOTIC | Caste |  | Creature may be used as a mount, but civilizations cannot domesticate it in worldgen without certain exceptions. |
|  MULTIPART_FULL_VISION | Caste |  | Allows the creature to have all-around vision, as long as it has multiple heads that can see. |
|  MULTIPLE_LITTER_RARE | Caste |  | Makes the species usually produce a single offspring per birth, with a 1/500 chance of using the [`[LITTERSIZE]`](/index.php/Creature_token#LITTERSIZE "Creature token") as usual. Requires [`[FEMALE]`](/index.php/Creature_token#FEMALE "Creature token"). |
|  MUNDANE | Creature |  | Marks if the creature is an actual real-life creature. Only used for age-names at present. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## N

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  NAME | Creature | singular / plural / adjective | The generic name for any creature of this type - will be used for referring to the species in the abstract, such as the default material prefix. For labeling individual creatures, / \[CASTE_NAME\] / is necessary. If left undefined, the creature will be labeled as "nothing" by the game. / Some examples of adjective use: / "super / dwarven / strength" / "the / dwarven / hillocks of X" / Deity species as in " / feline / deity" / Megabeast attacks in worldgen. One with multiple dragons being a " / draconic / rampage" |
|  NATURAL | Caste |  | Animal is considered to be natural. NATURAL animals will not engage creatures tagged with [`[AT_PEACE_WITH_WILDLIFE]`](/index.php/Creature_token#AT_PEACE_WITH_WILDLIFE "Creature token") in combat unless they are members of a hostile entity and vice-versa. |
|  NATURAL_ANIMAL | Caste |  | Alias of [`[NATURAL]`](/index.php/Creature_token#NATURAL "Creature token"). |
|  NATURAL_SKILL | Caste | Skill token / value | The creature possesses the specified skill at this level inherently - that is, it begins with the skill at this level, and the skill may never rust below that. A value of 15 is legendary. |
|  NIGHT_CREATURE | Caste |  | Creatures with this token can appear as / experiments / . Causes the creature to count as / \[NOT_LIVING\] / . / Killing a creature featuring this token provides one point of "hero" reputation. Adds the creature's description as part of the initial summary of their historical figure in legends mode. People will react to creatures with this token as a night creature (natch). In adventure mode, ambushes involving these units will say "Night creature!" instead of "Ambush!" / Prevents creature behavior enabled by / \[LARGE_PREDATOR\] / . / Removes the high nature value check imposed by / \[LOCAL_POPS_PRODUCE_HEROES\] / . / Prevents the AI from using ANIMATE interactions, unless the newly-animated / \[OPPOSED_TO_LIFE\] / undead will not attack them. The check for this is specifically whether the unit is: / a ghost / an animated unit / a unit with the / \[NO_AGING\] / token added via / \[CE_ADD_TAG\] / . (This allows for the default exclusion of elves and goblins, unless raised as intelligent undead.) |
|  NIGHT_CREATURE_BOGEYMAN | Caste |  | Creatures with this token can appear in bogeyman ambushes in adventure mode, where they adopt classical bogeyman traits such as stalking the adventurer and vaporising when dawn breaks. Such traits do not manifest if the creature is encountered outside of a bogeyman ambush (for instance, as a megabeast or a civilised being). In addition, their corpses and severed body parts turn into smoke after a short while. Note that setting the "Number of Bogeyman Types" in advanced world generation to 0 will only remove randomly-generated bogeymen. |
|  NIGHT_CREATURE_EXPERIMENTER | Caste |  | Found on some necromancers. Creatures with this tag may periodically "perform horrible experiments" offscreen, during which they can use creature-targeting interactions with an [`[I_SOURCE:EXPERIMENT]`](/index.php/Interaction_token#I_SOURCE "Interaction token") tag on living creatures in their area. Worlds are generated with a list of procedurally-generated experiments, allowing necromancers to turn living people and animals into ghouls and other experimental creatures, and these will automatically be available to all experimenters; it does not appear possible to prevent this. You can mod in your own custom experiment interactions, but these are used very infrequently due to the large number of generated experiments. |
|  NIGHT_CREATURE_HUNTER | Caste |  | Found on / night trolls / and / werebeasts / . Implies that the creature is a / night creature / , and shows its description in / legends mode / entry. The creature is always hostile and will start / no quarter / combat with any nearby creatures, except for members of its own race. Note that this tag does not override the creature's normal behavior in / fortress mode / except for the aforementioned aggression, and doesn't prevent the creature from fleeing the battles it started. It also removes the creature's materials from stockpile settings list, making them be stored there regardless of settings. / Does stack with / \[LARGE_ROAMING\] / and if both are used the creature will spawn as both historical hunters and as wild animals; this requires specifying a / \[BIOME\] / in which the creature will live, and subterranean biomes are allowed. / This tag causes the usual behaviour of werebeasts in worldgen, that is, fleeing towns upon being cursed and conducting raids from a lair. If this tag is absent from a deity curse, the accursed will simply be driven out of towns in a similar manner to / vampires / . When paired with SPOUSE_CONVERTER, a very small population of the creature will be created during worldgen (sometimes only a single individual will be created), and their histories will be tracked (that is, they will not spawn spontaneously later, they must either have children or convert other creatures to increase their numbers). The creature will settle in a lair and go on rampages during worldgen. It will actively attempt to seek out potential conversion targets to abduct, convert, and have children with (if possible). |
|  NIGHT_CREATURE_NIGHTMARE | Caste |  | Found on nightmares. Corpses and severed body parts derived from creatures with this token turn into smoke after a short while. |
|  NO_AUTUMN | Caste |  | The creature caste does not appear in autumn. |
|  NO_CONNECTIONS_FOR_MOVEMENT | Caste |  | Creature doesn't require connected body parts to move\[Verify\]; generally used on undead creatures with connections that have rotted away. |
|  NO_DIZZINESS | Caste |  | Creature cannot become dizzy. |
|  NO_DRINK | Caste |  | Creature does not need to drink. |
|  NO_EAT | Caste |  | Creature does not need to eat. |
|  NO_FEVERS | Caste |  | Creature cannot suffer fevers. |
|  NO_GENDER | Caste |  | The creature is biologically sexless, making it unable to breed. |
|  NO_PHYS_ATT_GAIN | Caste |  | The creature cannot raise any physical attributes. |
|  NO_PHYS_ATT_RUST | Caste |  | The creature cannot lose any physical attributes. |
|  NO_SLEEP | Caste |  | Creature does not need to sleep, but can still be rendered unconscious by other means. |
|  NO_SPRING | Caste |  | The creature caste does not appear in spring. |
|  NO_SUMMER | Caste |  | The creature caste does not appear in summer. |
|  NO_THOUGHT_CENTER_FOR_MOVEMENT | Caste |  | The bodyparts of this creature don't need to be connected to an organ with the [`[THOUGHT]`](/index.php/Body_token#THOUGHT "Body token") tag in order to have motor function. Generally used on creatures that don't have brains. If a creature doesn't have a thought part and doesn't have this token, it will be unable to grasp or stand. Nautilus men experience this issue in vanilla. |
|  NO_UNIT_TYPE_COLOR | Caste |  | Prevents creature from selecting its color based on its profession (e.g. Miner, Hunter, Wrestler). |
|  NO_VEGETATION_PERTURB | Caste\[Verify\] |  | Likely prevents the creature from leaving broken vegetation tracks.\[Verify\] |
|  NO_WINTER | Caste |  | The creature caste does not appear in winter. |
|  NOBONES | Caste |  | Creature cannot be picked up for worldgen fell moods and cannot be made a skeleton deity. |
|  NOBREATHE | Caste |  | Creature doesn't need to breathe or have [`[BREATHE]`](/index.php/Body_token#BREATHE "Body token")parts in its body, nor can it drown or be strangled. Creatures living in magma must have this tag, otherwise they will drown. |
|  NOCTURNAL | Caste |  | When set, the creature will only appear at night (after 10:05 PM and before 4:30 AM) in Adventurer mode. |
|  NOEMOTION | Caste |  | Creature has no emotions, thus; it is immune to the effects of stress and unable to rage, and its needs cannot be fulfilled in any way. Used on undead in the vanilla game. |
|  NOEXERT | Caste |  | Creature can't become tired or over-exerted from taking too many combat actions, or moving at full speed for extended periods of time. |
|  NOFEAR | Caste |  | Creature doesn't feel fear and will never flee from battle, and will be immune to ghosts' attempts to 'scare it to death'. Additionally, it causes bogeymen and nightmares to become friendly towards the creature. |
|  NOMEAT | Caste |  | Creature will not be hunted or fed to wild beasts. |
|  NONAUSEA | Caste |  | Creature isn't nauseated by gut hits and cannot vomit. |
|  NOPAIN | Caste |  | Creature doesn't feel pain. |
|  NOSKIN | Caste |  | Creature will not drop a hide when butchered. |
|  NOSKULL | Caste |  | Creature will not drop a skull on butchering, rot, or decay of severed head. |
|  NOSMELLYROT | Caste |  | Does not produce miasma when rotting. |
|  NOSTUCKINS | Caste |  | Weapons can't get stuck in the creature. |
|  NOSTUN | Caste |  | Creature can't be stunned and knocked unconscious by pain or head injuries. Creatures with this tag never wake up from sleep in Fortress Mode. If this creature needs to sleep while playing, it **will** die. |
|  NOT_BUTCHERABLE | Caste |  | Corpses from this creature cannot be butchered. Does not prevent the creature from being slaughtered while alive, however. |
|  NOT_LIVING | Caste |  | Cannot be raised from the dead by necromancers or evil clouds. Implies the creature is not a normal living being. Used by vampires, mummies and inorganic creatures like the amethyst man and bronze colossus. Creatures who are [`[OPPOSED_TO_LIFE]`](/index.php/Creature_token#OPPOSED_TO_LIFE "Creature token") (undead) will be docile towards creatures with this token. |
|  NOTHOUGHT | Caste |  | Creature doesn't require a [`[THOUGHT]`](/index.php/Body_token#THOUGHT "Body token") body part to survive. Has the added effect of preventing speech, though directly controlling creatures that would otherwise be capable of speaking allows them to engage in conversation. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## O

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  ODOR_LEVEL | Caste | number | How easy the creature is to smell. The higher the number, the easier the creature is to sniff out. Defaults to 50. Vanilla creatures have values from 0 (undetectable) to 90 (noticeable by humans and dwarves). |
|  ODOR_STRING | Caste | string | What the creature smells like. If no odor string is defined, the creature name (not the caste name) is used. |
|  OPPOSED_TO_LIFE | Caste |  | Is hostile to all creatures except undead and other non-living ones and will show Opposed to life in the unit list. Used by undead in the vanilla game. Functions without the [`[NOT_LIVING]`](/index.php/Creature_token#NOT_LIVING "Creature token") token, and seems to imply said token as well. Undead will not be hostile to otherwise-living creatures given this token. Living creatures given this token will attack living creatures that lack it, while ignoring other living creatures that also have this token. |
|  ORIENTATION | Caste | MALE / FEMALE / disinterested chance / casual chance / strong chance | Determines caste's likelihood of having sexual attraction to certain sexes. Values default to 75:20:5 for the same sex and 5:20:75 for the opposite sex. The first value indicates how likely to be entirely uninterested in the sex, the second decides if the creature will be able to become lovers with that sex, the third decides whether they will be able to marry in worldgen and post-worldgen world activities (which implies being able to become lovers). Marriage seems to be able to happen in fort mode play regardless, as long as they are lovers first. |
|  OUTSIDER_CONTROLLABLE | Caste |  | Lets you play as an outsider of this species in adventure mode. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## P

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  PACK_ANIMAL | Caste |  | Allows the creature to be used as a pack animal. Used by / merchants / without wagons and adventurers. Also prevents creature from dropping hauled items on its own -- do / not / use for player-controllable creatures! May lead to the creature being domesticated during worldgen, even if it doesn't have / \[COMMON_DOMESTIC\] / . / Creatures with this tag but without / \[BENIGN\] / , and / or with / \[LARGE_PREDATOR\] / leads to hauled items being dropped. |
|  PARALYZEIMMUNE | Caste |  | The creature is immune to all paralyzing special attacks. |
|  PATTERNFLIER | Caste |  | Used to control the bat riders with paralyze-dart blowguns that flew through the 2D chasm. Doesn't do anything now. |
|  PCG_LAYERING | Creature | Layering type | Adds a layer to the current [`[PROCEDURAL_CREATURE_GRAPHICS]`](/index.php/Creature_token#PROCEDURAL_CREATURE_GRAPHICS "Creature token") definition. |
|  PEARL | Caste |  | Does nothing. |
|  PENETRATEPOWER | Caste | value | Controls the ability of / vermin / to find a way into containers when they are eating food from your stockpiles. / Objects made of most materials (e.g. metal) roll a number from 0-100, and if the resulting number is greater than the penetrate power, their contents escape for the time being. Objects made of / wood / , / leather / , / amber / , or / coral / roll 0-95, and items made of / cloth / roll 0-90. |
|  PERSONALITY | Caste | ATTRIBUTE / lowest / median / highest | Determines the range and chance of personality facets. Standard is 0:50:100. See personality facet for more info. |
|  PET | Caste |  | Allows the creature to be tamed in Fortress mode. Prerequisite for all other working animal roles. Civilizations that encounter it in worldgen will tame and domesticate it for their own use. Adding this to civilization members will classify them as pets instead of citizens, with all the problems that entails. However, you can solve these problems using the popular plugin Dwarf Therapist, which is completely unaffected by the tag. |
|  PET_EXOTIC | Caste |  | Allows the creature to be tamed in Fortress mode. Prequisite for all other working animal roles. Civilizations cannot domesticate it in worldgen, with certain exceptions. More difficult to tame?\[Verify\] Adding this to civilization members will classify them as pets instead of citizens, with all the problems that entails. (Example). |
|  PETVALUE | Caste | value | How valuable a tamed animal is. Actual cost in points in the embarking screen is 1+(PETVALUE/2) for an untrained animal, 1+PETVALUE for a war/hunting one. |
|  PETVALUE_DIVISOR | Caste | value | Divides the creature's [`[PETVALUE]`](/index.php/Creature_token#PETVALUE "Creature token") by the specified number. Used by honey bees to prevent a single hive from being worth a fortune. |
|  PHYS_ATT_CAP_PERC | Caste | ATTRIBUTE / Token / Cap % | Default is 200. This means you can increase your attribute to 200% of its starting value (or the average value + your starting value if that is higher). |
|  PHYS_ATT_RANGE | Caste | ATTRIBUTE / lowest / lower / low / median / high / higher / highest | Sets up a physical attribute's range of values (0-5000). All physical attribute ranges default to 200:700:900:1000:1100:1300:2000. |
|  PHYS_ATT_RATES | Caste | ATTRIBUTE / Token / cost to improve / unused counter rate / rust counter rate / demotion counter rate | Physical attribute gain/decay rates. Lower numbers in the last three slots make decay occur faster. Defaults for STRENGTH, AGILITY, TOUGHNESS, and ENDURANCE are 500:3:4:3, while RECUPERATION and DISEASE_RESISTANCE default to 500:NONE:NONE:NONE. |
|  PLUS_BP_GROUP | Caste | BY_TYPE, BY_CATEGORY, or BY_TOKEN / body type, category, or token | Adds a body part group to selected body part group. Presumably used immediately after [`[SET_BP_GROUP]`](/index.php/Creature_token#SET_BP_GROUP "Creature token"). |
|  PLUS_MATERIAL | Creature | material | Adds a material to selected materials. Used immediately after [`[SELECT_MATERIAL]`](/index.php/Creature_token#SELECT_MATERIAL "Creature token"). |
|  POP_RATIO | Caste | number (max 100000) | Weighted population of caste; Lower is rarer. Not to be confused with [`[FREQUENCY]`](/index.php/Creature_token#FREQUENCY "Creature token"). A weight of 0 willv51.06 experimental prevent a caste from spawning naturally. Regardless of pop ratio, Positions that only allow a certain caste can force it to spawn. |
|  POPULATION_NUMBER | Creature | min / max | The minimum/maximum numbers of how many of these creatures are present in each world map tile of the appropriate region. Defaults to 1:1 if not specified. If the creature's chosen [`[CLUSTER_NUMBER]`](/index.php/Creature_token#CLUSTER_NUMBER "Creature token") happens to be larger, it will be used instead. |
|  POWER | Caste |  | Allows the being to represent itself as a deity, allowing it to become the leader of a civilized group. Not used by any creatures in the vanilla game. Requires [`[CAN_SPEAK]`](/index.php/Creature_token#CAN_SPEAK "Creature token") to actually do anything more than settle at a location (e.g. write books, lead armies, profane temples). Doesn't appear to do anything for creatures that are already civilized. Once the creature ascends to a position of leadership, it will proceed to act as a standard ruler for their entity and fulfill the same functions (hold tournaments, tame creatures, etc.). |
|  PREFSTRING | Creature | string | Sets what other creatures prefer about this creature. "Urist likes dwarves for their beards." Multiple entries will be chosen from at random. Creatures lacking a PREFSTRING token will never appear under another's preferences. |
|  PROCEDURAL_CREATURE_GRAPHICS | Creature | Sprite type / or Caste then sprite type | Makes the creature have procedural graphics built for it, like forgotten beasts/demons/titans/experiments. Must be associated with PCG_LAYERING tokens. |
|  PROFESSION_NAME | Creature | Unit type token / (Profession) / singular / plural | The generic name for members of this profession, at the creature level. In order to give members of specific castes different names for professions, use [`[CASTE_PROFESSION_NAME]`](/index.php/Creature_token#CASTE_PROFESSION_NAME "Creature token") instead. |
|  PRONE_TO_RAGE | Caste | Chance | Creature has a percentage chance to flip out at visible non-friendly creatures. Enraged creatures attack anything regardless of timidity and get a strength bonus to their hits. This is what makes badgers so hardcore. |
|  PUS | Caste | \ / \ | The creature has pus. Specifies the stuff secreted by infected wounds. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## R

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  RELSIZE | Caste | BY_CATEGORY, BY_TYPE, BY_TOKEN / body category, type, or token / Relsize | Specifies a new relative size for a part than what is stated in the body plan. For example, dwarves have larger livers. |
|  REMAINS | Caste | singular / plural | What the creature's remains are called. |
|  REMAINS_COLOR | Caste |  | What color the creature's remains are. |
|  REMAINS_ON_VERMIN_BITE_DEATH | Caste |  | Goes with [`[VERMIN_BITE]`](/index.php/Creature_token#VERMIN_BITE "Creature token") and [`[DIE_WHEN_VERMIN_BITE]`](/index.php/Creature_token#DIE_WHEN_VERMIN_BITE "Creature token"), the vermin creature will leave remains on death when biting. Leaving this tag out will cause the creature to disappear entirely after it bites. |
|  REMAINS_UNDETERMINED | Caste |  | Nothing. |
|  REMOVE_MATERIAL | Creature | material token | Removes a material from the creature. |
|  REMOVE_TISSUE | Creature | tissue token | Removes a tissue from the creature. |
|  RETRACT_INTO_BP | Caste | BY_TYPE, BY_CATEGORY or BY_TOKEN / body type, / category / , or / token / Second person ("You") retract verb text / Third person ("The giant snail") retract verb text / Second person cancel retract text / Third person cancel retract text | The creature will retract into the specified body part(s) when threatened. It will be unable to move or attack, but enemies will only be able to attack the specified body part(s). When one of the specified body part is severed off, the creature automatically unretracts and cannot retract anymore. More than one body part can be selected by using BY_TYPE or BY_CATEGORY. / Second-person descriptions are used for adventurer mode natural ability. " / " can be used in the descriptions, being replaced with the proper pronoun (or lack thereof) in-game. / Undead curled up creatures are buggy, specifically those that retract into their upper bodies: / echidnas / , / hedgehogs / and / pangolins / . / Bug / : / 11463 / Bug / : / 10519 / The upper body is prevented from collapsing by a separate body part (the middle spine), which cannot be attacked when the creature is retracted. See / \[PREVENTS_PARENT_COLLAPSE\] / . Living creatures eventually succumb to blood loss, but undead creatures do not. Giant creatures also take a very long time to bleed out. |
|  RETURNS_VERMIN_KILLS_TO_OWNER | Creature |  | Cat behavior. If it kills a vermin creature and has an owner, it carries the remains in its mouth and drops them at their feet. Requires [`[HUNTS_VERMIN]`](/index.php/Creature_token#HUNTS_VERMIN "Creature token"). |
|  ROOT_AROUND | Caste | BY_TYPE, BY_CATEGORY or BY_TOKEN / body type, / category / , or / token / Second person ("You") verb text / Third person ("The hen") verb text | Creature will occasionally root around in the grass, looking for insects. Used for flavor in Adventurer Mode, spawns vermin edible for this creature in Fortress Mode. Creatures missing the specified body part will be unable to perform this action. The action produces a message (visible in adventure mode) in the form: / \[creature\] \[verb text\] the \[description of creature's location\]. / In adventure mode, the "rooting around" ability will be included in the "natural abilities" menu, represented by its second person verb text. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## S

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  SAVAGE | Creature |  | The creature will only show up in "savage" biomes. Has no effect on cavern creatures. Cannot be combined with [`[GOOD]`](/index.php/Creature_token#GOOD "Creature token") or [`[EVIL]`](/index.php/Creature_token#EVIL "Creature token"). |
|  SECRETION | Caste | \ / \ / BY_TOKEN / BY_CATEGORY / BY_TYPE / \ / \ or ALL / GRASP)\> / \ or ALL | Causes the specified tissue layer(s) of the indicated body part(s) to secrete the designated material. A size 100 ('covering') / contaminant / is created over the affected body part(s) in its specified material state (and at the temperature appropriate to this state) when the trigger condition is met, as long as one of the secretory tissue layers is still intact. Valid triggers are: / CONTINUOUS / Secretion occurs once every 40 / ticks / in / fortress mode / , and every tick in / adventurer mode / . / EXERTION / Secretion occurs continuously (at the rate described above) whilst the creature is at minimum / Tired / following physical exertion. Note that this cannot occur if the creature has / \[NOEXERT\] / . / EXTREME_EMOTION / Secretion occurs continuously (as above) whilst the creature is distressed. Cannot occur in creatures with / \[NOEMOTION\] / . |
|  SELECT_ADDITIONAL_CASTE | Creature |  | Adds an additional previously defined caste to the selection. Used after [`[SELECT_CASTE]`](/index.php/Creature_token#SELECT_CASTE "Creature token"). |
|  SELECT_CASTE | Creature | or ALL | Selects a previously defined caste |
|  SELECT_MATERIAL | Creature | \ | Selects a locally defined material. Can be ALL. |
|  SELECT_TISSUE | Creature | tissue token | Selects a tissue for editing. |
|  SEMIMEGABEAST | Caste |  | Essentially the same as [`[MEGABEAST]`](/index.php/Creature_token#MEGABEAST "Creature token"), but more of them are created during worldgen. See the semi-megabeast page for details. |
|  SENSE_CREATURE_CLASS | Caste | \ / : / : | Gives the creature the ability to sense creatures belonging to the specified creature class even when they lie far beyond line of sight, including through walls and floors. It also appears to reduce or negate the combat penalty of blind units when fighting creatures they can sense. In adventure mode, the specified tile will be used to represent sensed creatures when they cannot be seen directly. |
|  SET_BP_GROUP | Caste | selection criteria BY_TYPE, BY_CATEGORY, BY_TOKEN / category, type, or token | Begins a selection of body parts. |
|  SKILL_LEARN_RATE | Caste | \ | The rate at which this creature learns this skill. Requires [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") or [`[INTELLIGENT]`](/index.php/Creature_token#INTELLIGENT "Creature token") to function. |
|  SKILL_LEARN_RATES | Caste |  | The rate at which this creature learns all skills. Requires [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") or [`[INTELLIGENT]`](/index.php/Creature_token#INTELLIGENT "Creature token") to function. |
|  SKILL_RATE | Caste | skill_token / \ | Like [`[SKILL_RATES]`](/index.php/Creature_token#SKILL_RATES "Creature token"), but applies to individual skills instead. Requires [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") or [`[INTELLIGENT]`](/index.php/Creature_token#INTELLIGENT "Creature token") to function. |
|  SKILL_RATES | Caste | \ | Affects skill gain and decay. Lower numbers in the last three slots make decay occur faster (\[SKILL_RATES:100:1:1:1\] would cause rapid decay). The counter rates may also be replaced with NONE. / Default is \[SKILL_RATES:100:8:16:16\]. Requires / \[CAN_LEARN\] / or / \[INTELLIGENT\] / to function. |
|  SKILL_RUST_RATE | Caste | skill_token / value / value / value | The rate at which this skill decays. Lower values cause the skill to decay faster. Requires [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") or [`[INTELLIGENT]`](/index.php/Creature_token#INTELLIGENT "Creature token") to function. |
|  SKILL_RUST_RATES | Caste | value / value / value | The rate at which all skills decay. Lower values cause the skills to decay faster. Requires [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") or [`[INTELLIGENT]`](/index.php/Creature_token#INTELLIGENT "Creature token") to function. |
|  SLAIN_CASTE_SPEECH | Caste | text set | Caste-specific [`[SLAIN_SPEECH]`](/index.php/Creature_token#SLAIN_SPEECH "Creature token"). |
|  SLAIN_SPEECH | Creature | text set | Boasting speeches relating to killing this creature. Examples include text_dwarf.txt (`[SLAIN_SPEECH:SLAIN_DWARF]`) and text_elf.txt (`[SLAIN_SPEECH:SLAIN_ELF]`) in data\vanilla\vanilla_creatures\objects. |
|  SLOW_LEARNER | Caste |  | Shorthand for [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") + [`[SKILL_LEARN_RATES:50]`](/index.php/Creature_token#SKILL_LEARN_RATES "Creature token").\[Verify\] Used by a number of 'primitive' creatures (like ogres, giants and troglodytes) in the vanilla game. Applicable to player races. Prevents a player from recruiting nobility, even basic ones. Subterranean creatures with this token combined with [`[EVIL]`](/index.php/Creature_token#EVIL "Creature token") will become servants of goblins in their civilizations, in the style of trolls. |
|  SMALL_REMAINS | Caste |  | Creature leaves "remains" instead of a corpse. Used by vermin. |
|  SMELL_TRIGGER | Caste | value | Determines how keen a creature's sense of smell is - lower is better. At 10000, a creature cannot smell at all. |
|  SOLDIER_ALTTILE | Creature | 'character' or tile number | If this creature is active in its civilization's military, it will blink between its default tile and this one. |
|  SOUND | Caste | Sound application (currently accepts ALERT or PEACEFUL_INTERMITTENT) / Sound range (in tiles) / Sound delay (lower values = sound is produced more often) / VOCALIZATION or NONE (determines whether the sound requires breathing or not) / First-person description / Third-person description / Description when out of sight | Creature makes sounds periodically, which can be heard in Adventure mode. / First-person reads "You / bark / " / Third-person reads "The / capybara / barks / " / Out of sight reads "You hear / a loud bark / " / with the text in bold being the description arguments of the token. |
|  SOURCE_HFID | Creature | Integer | Found on generated angels. This is the historical figure ID of the deity with which the angel is associated. Since HFIDs are not predictable before worldgen, this isn't terribly usable in mods. |
|  SPECIFIC_FOOD | Caste | PLANT or CREATURE / Plant / creature ID | Creature will only appear in biomes with this plant or creature available. Grazers given a specific type of grass (such as pandas and bamboo) will only eat that grass and nothing else, risking starvation if there's none available. |
|  SPHERE | Creature | sphere | Sets what religious spheres the creature is aligned to, for purposes of being worshipped via the [`[POWER]`](/index.php/Creature_token#POWER "Creature token") token. Also affects the creature's name. |
|  SPOUSE_CONVERSION_TARGET | Caste |  | This creature can be converted by a night creature with [`[SPOUSE_CONVERTER]`](/index.php/Creature_token#SPOUSE_CONVERTER "Creature token"). |
|  SPOUSE_CONVERTER | Caste |  | If the creature has the [`[NIGHT_CREATURE_HUNTER]`](/index.php/Creature_token#NIGHT_CREATURE_HUNTER "Creature token") tag, it will kidnap [`[SPOUSE_CONVERSION_TARGET]`](/index.php/Creature_token#SPOUSE_CONVERSION_TARGET "Creature token")s and transform them into the caste of its species with the [`[CONVERTED_SPOUSE]`](/index.php/Creature_token#CONVERTED_SPOUSE "Creature token") tag during worldgen. It may also start families this way. |
|  SPREAD_EVIL_SPHERES_IF_RULER | Caste |  | If the creature rules over a site, it will cause the local landscape to be corrupted into evil surroundings associated with the creature's spheres. The creature must have at least one of the following spheres for this to take effect: BLIGHT, DEATH, DISEASE, DEFORMITY, NIGHTMARES. The first three kill vegetation, while the others sometimes do. The last two get evil plants and evil animals sometimes. NIGHTMARES gets bogeymen. [4] Used by demons in the vanilla game. |
|  STANCE_CLIMBER | Caste |  | Caste does not require [`[GRASP]`](/index.php/Body_token#GRASP "Body token") body parts to climb -- it can climb with [`[STANCE]`](/index.php/Body_token#STANCE "Body token") parts instead. |
|  STANDARD_GRAZER | Caste |  | Acts as [`[GRAZER]`](/index.php/Creature_token#GRAZER "Creature token") but set to 20000\*G\*(max size)^(-3/4), where G defaults to 100 but can be set in d_init, and the whole thing is trapped between 150 and 3 million. Used for all grazers in the default creature raws. |
|  STRANGE_MOODS | Caste |  | The creature will get strange moods in fortress mode and can produce artifacts. |
|  SUPERNATURAL | Caste |  | Gives the creature knowledge of any secrets with [`[SUPERNATURAL_LEARNING_POSSIBLE]`](/index.php/Interaction_token#IS_SECRET "Interaction token") that match its spheres and also prevents it from becoming a vampire or werebeast. Other effects are unknown. |
|  SWIMS_INNATE | Caste |  | The creature naturally knows how to swim perfectly and does not use the swimmer skill, as opposed to [`[SWIMS_LEARNED]`](/index.php/Creature_token#SWIMS_LEARNED "Creature token") below. However, Fortress mode AI never paths into water anyway, so it's less useful there. |
|  SWIMS_LEARNED | Caste |  | The creature swims only as well as their present swimming skill allows them to. |
|  SYNDROME_DILUTION_FACTOR | Caste | \: | Dilutes the effects of syndromes which have the specified identifier. A percentage of 100 is equal to the regular syndrome effect severity, higher percentages reduce severity. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## T

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  TENDONS | Caste | material token / healing rate | The creature has tendons in its [`[CONNECTIVE_TISSUE_ANCHOR]`](/index.php/Tissue_definition_token#CONNECTIVE_TISSUE_ANCHOR "Tissue definition token") tissues (bone or chitin by default). Cutting the bone/chitin tissue severs the tendons, disabling motor function if the target is a limb. |
|  THICKWEB | Caste |  | The creature's webs can catch larger creatures. |
|  TISSUE | Creature | name | Begins defining a tissue in the creature file. Follow this with standard tissue definition tokens to define the tissue properties. |
|  TISSUE_LAYER | Caste | BY_TYPE, BY_CATEGORY, BY_TOKEN / TYPE,CATEGORY, or TOKEN / TISSUE / LOCATION | Adds the tissue layer to wherever it is required. / Non-argument Locations can be FRONT, RIGHT, LEFT, TOP, BOTTOM. Argument locations are AROUND and CLEANS, requiring a further body part and a % of coverage / cleansing |
|  TISSUE_LAYER_OVER | Caste | BY_TYPE, BY_CATEGORY, BY_TOKEN / TYPE,CATEGORY, or TOKEN / TISSUE / LOCATION | Alias for TISSUE_LAYER |
|  TISSUE_LAYER_UNDER | Caste | BY_TYPE, BY_CATEGORY, BY_TOKEN / TYPE,CATEGORY, or TOKEN / TISSUE | Adds the tissue layer under a given part. / For example, an / iron man / has a gaseous poison within, and this tissue (GAS is its name) has the token \[TISSUE_LEAKS\] and its state is GAS, so when you puncture the iron outside and damage this tissue it leaks gas (can have a syndrome by using a previous one in the creature sample.) \[TISSUE_LAYER_UNDER:BY_CATEGORY:ALL:{tissue}\] {tissue} is what will be under the TISSUE_LAYER; here is an example Tissue from the Iron Man: / \[TISSUE:GAS\] \[TISSUE_NAME:gas:NP\] \[TISSUE_MATERIAL:LOCAL_CREATURE_MAT:GAS\] \[TISSUE_MAT_STATE:GAS\] \[RELATIVE_THICKNESS:50\] \[TISSUE_LEAKS\] \[TISSUE_SHAPE:LAYER\] |
|  TITAN | Caste |  | Found on titans. Cannot be specified in user-defined raws. |
|  TRADE_CAPACITY | Caste | number | How much the creature can carry when used by merchants. 1000 by default. Completely ignored if the animal does not also have PACK_ANIMAL or WAGON, instead using BODY_SIZE^(2/3)/20, even if they're a pack animal due to ANIMAL_ALWAYS_PACK_ANIMAL. |
|  TRAINABLE | Caste |  | Shortcut for [`[TRAINABLE_HUNTING]`](/index.php/Creature_token#TRAINABLE_HUNTING "Creature token") + [`[TRAINABLE_WAR]`](/index.php/Creature_token#TRAINABLE_WAR "Creature token"). |
|  TRAINABLE_HUNTING | Caste |  | Can be trained as a hunting beast, increasing speed. |
|  TRAINABLE_WAR | Caste |  | Can be trained as a war beast, increasing strength and endurance. |
|  TRANCES | Caste |  | Allows the creature to go into martial trances. Used by dwarves in the vanilla game. |
|  TRAPAVOID | Caste |  | The creature will never trigger traps it steps on. Used by a number of creatures. Doesn't make the creature immune to remotely activated traps (like retractable spikes being triggered while the creature is standing over them). TRAPAVOID creatures lose this power if they're immobilized while standing in a trap, be it by stepping on thick web, being paralyzed or being knocked unconscious. |
|  TRIGGERABLE_GROUP | Creature | min / max | A large swarm of vermin can be disturbed, usually in adventurer mode. |
|  TSU_NOUN | Caste | noun / SINGULAR or PLURAL | Noun for the [`[TISSUE_STYLE_UNIT]`](/index.php/Creature_token#TISSUE_STYLE_UNIT "Creature token"), used in the description of the tissue layer's style. |

|  |
|----|
| **Contents** A B C D E F G H I J K L M N O P Q R S T U V W X Y Z top |

## U

|  |  |  |  |
|----|----|----|----|
| Token | Type | Arguments | Description |
|  UBIQUITOUS | Creature |  | Creature will occur in every region with the correct biome. Does not apply to [`[EVIL]`](/index.php/Creature_token#EVIL "Creature token")/[`[GOOD]`](/index.php/Creature_token#GOOD "Creature token") tags. Supersedes [`[FREQUENCY]`](/index.php/Creature_token#FREQUENCY "Creature token") for the purposes of distributing populations through the map, they are present in every part of the valid biome. Respects [`[FREQUENCY]`](/index.php/Creature_token#FREQUENCY "Creature token") for the frequency of unit cluster spawns being of this species. |

---
*Parte 2 de 3 de «Creature token». Demais partes em arquivos `...-part-{1..3}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Creature_token*
