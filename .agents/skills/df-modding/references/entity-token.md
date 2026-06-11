# Entity token

> Fonte: [Entity token](https://dwarffortresswiki.org/index.php/Entity_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\
**Entity tokens** define entities, or civilizations, in entity\_\*.txt files.

The `[OBJECT:ENTITY]` token begins the definition of an entity raw file. Each new entity definition that follows begins with the `[ENTITY:`*`entity_ID`*`]` token, where *entity_ID* is a unique identifier for that entity, and the entity's properties are then specified by the use of further entity tokens; or, tokens can be added to existing entities using `[SELECT_ENTITY:`*`entity_ID`*`]` instead.

All known entity tokens are listed below.

## Gameplay

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  ALL_MAIN_POPS_CONTROLLABLE |  | Allows adventure mode for entities with sites. |
|  SITE_CONTROLLABLE |  | Allows fortress mode. If multiple entities have the SITE_CONTROLLABLE token, then at embark the specific civs can be chosen on the civ list screen. At least one civilization must have this token. |
|  CREATURE | creature | The type of creature that will inhabit the civilization. If multiple creature types are specified, each civilization will randomly choose one of the creatures. In entities with multiple possible creatures, you can manipulate the chance of one creature being chosen by adding multiple identical creature tags. For instance adding \[CREATURE:DWARF\]\[CREATURE:DWARF\]\[CREATURE:DWARF\]\[CREATURE:ELF\] to the same entity will make the civs created about 75% dwarven, 25% elven. It should be noted that civilizations are in general weighted by this token: for example, if you have one entity with three \[CREATURE:DWARF\] tokens and another separate entity with a single \[CREATURE:ELF\] token, then you can expect to see three times as many of the former placed as the latter (assuming enough unclaimed \[START_BIOME:X\] space remains). Note that spawn rates are also limited by unclaimed biome space - if an entity can only spawn in a rarer set of biomes (only LAKE_TROPICAL_SALTWATER for example) then their spawn rate will end up being limited by the remaining unclaimed space in that biome type rather than the number of \[CREATURE:X\] tokens present in the entity raw. |
|  SOURCE_HFID | integer | Found on generated angel entities. Appears to draw from creatures with this HFID, which associates the entity with a historical figure of the same ID corresponding to a deity. |

## Placement

Entity spawning during world gen is influenced by several factors:

- The "Number of Civilizations" world gen setting places a hard limit on the total number of entities spawned.
- The "Playable Civilization Required" world gen setting forces at least one of each SITE_CONTROLLABLE entity to spawn (presumably still limited by "Number of Civilizations").
- The number of \[CREATURE:X\] tokens present in an entity modifies its chance of spawning. An entity containing more \[CREATURE:X\] tokens will spawn more often (assuming other requirements are met) and may even block entities with fewer \[CREATURE:X\] tokens from spawning altogether. You can use \[SELECT_ENTITY:VANILLA_ENTITY_X\] followed by any number of duplicate \[CREATURE:VANILLA_CREATURE_X\] tokens to attempt to balance the spawn rates of the existing vanilla entities with any custom multi-creature entities you may add.
- The number of unclaimed START_BIOME or EXCLUSIVE_START_BIOME tiles remaining in the world limits the spawn rate for an entity and allows entities to block each other's spawns. If there is no "starting" biome space left for an entity then it will not spawn and the game will try to spawn a different entity instead. This means that, on average, an entity that can start in ALL_MAIN biomes will spawn more frequently than one that can start only in LAKE_TROPICAL_SALTWATER biomes. This also means that entities whose starting biomes do not overlap will not block each other's spawns.

\

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  BIOME_SUPPORT | biome / frequency | Controls the expansion of the civilization's territory. The higher the number is relative to other BIOME_SUPPORT tokens in the entity, the faster it can spread through the biome. These numbers are evaluated relative to each other, i.e. if one biome is 1 and the other is 2, the spread will be the same as if one was 100 and the other was 200. Civs can spread out over biomes they cannot actually build in; for example, humans spread quickly over oceans but cannot actually build in them. / \[BIOME_SUPPORT:ANY_GRASSLAND:4\] / The first entry of biome support should be the Start biome, as mentioned in \[START_BIOME\] or \[EXCLUSIVE_START_BIOME\], otherwise no other settlements after the first one are founded. |
|  SETTLEMENT_BIOME | biome | If the civ's territory crosses over this biome, it can build settlements here. / \[SETTLEMENT_BIOME:ANY_GRASSLAND\] |
|  START_BIOME | biome | Combination of EXCLUSIVE_START_BIOME and SETTLEMENT_BIOME; allows the civ to start in and create settlements in the biome. Note that the civ's spawn rate may be limited if all of its START or EXCLUSIVE_START biome(s) are rare in the world or have already been fully occupied by other civ spawns. / \[START_BIOME:ANY_FOREST\] |
|  EXCLUSIVE_START_BIOME | biome | The birth of the civilization can occur in this biome, but cannot (necessarily) build in it. If the civ does not have SETTLEMENT_BIOME or START_BIOME for the biome in question, it will only construct a single settlement there. Note that the civ's spawn rate may be limited if all of its START or EXCLUSIVE_START biome(s) are rare in the world or have already been fully occupied by other civ spawns. / \[EXCLUSIVE_START_BIOME:MOUNTAIN\] |
|  DEFAULT_SITE_TYPE | site type | Valid site types are DARK_FORTRESS (π), CAVE (•), CAVE_DETAILED (Ω), TREE_CITY (î), and CITY (#). Also recognizes PLAYER_FORTRESS (creates a civ of hillocks only, that however do not contain any structures, when visited in adventure mode), and MONUMENT (creates a civ without visible sites (except tombs and castles), but may cause worldgen crashes). FORTRESS is no longer a valid entry, castles are currently controlled by BUILDS_OUTDOOR_FORTIFICATIONS. Defaults to CITY. Selecting CAVE causes the classic kobold behavior of not showing up on the "neighbors" section of the site selection screen. / Selecting DARK_FORTRESS also allows generation of / certain other structures / . It also gives the civ a / special overlord / . DARK_FORTRESS may cause crashes during world gen at "Placing civilizations... (0)" if it combined with entity tokens that the vanilla ENTITY:EVIL does not use (likely the POSITION related tokens see / this forum post / ). CAVE_DETAILED civilizations will create fortresses in mountainous regions and hillocks in non-mountainous regions. \[DEFAULT_SITE_TYPE:CAVE_DETAILED\] |
|  LIKES_SITE | site type | Most residents will try to move to this site type, unless already at one. / \[LIKES_SITE:CAVE_DETAILED\] |
|  TOLERATES_SITE | site type | Some residents will try to move to this site type, unless already at one. / \[TOLERATES_SITE:CITY\] |
|  WORLD_CONSTRUCTION | construction | Controls which constructions the civ will build on the world map. Valid constructions are ROAD, TUNNEL, BRIDGE, and WALL. / \[WORLD_CONSTRUCTION:BRIDGE\] \[WORLD_CONSTRUCTION:ROAD\] \[WORLD_CONSTRUCTION:TUNNEL\] \[WORLD_CONSTRUCTION:WALL\] |

## Population

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  MAX_POP_NUMBER | number | Max / historical / population / per entity / . Multiply this by max starting civ to get the total maximum historical population of the species. Defaults to 500, but all vanilla entities use 10,000, except skulking uses 2,000. Does not limit the / total / population, but it will prevent new settlements upon reaching the number. / \[MAX_POP_NUMBER:10000\] |
|  MAX_SITE_POP_NUMBER | number | Max historical population per individual site. Defaults to 50, but all the vanilla entities use 120. / \[MAX_SITE_POP_NUMBER:120\] |
|  MAX_STARTING_CIV_NUMBER | number | Max number of civilizations of this entity type to spawn at world generation, which picks entities in some sequential order from the raws, looping through the list as needed. This is a hard limit, if set to 1, only 1 civilization of this type will be placed. If all entities have reached their limit, world generation will not try to place any more, even if its own / total limit / has not been reached, and will continue on. Defaults to 3, but all vanilla entities use 100 (essentially unlimited). / \[MAX_STARTING_CIV_NUMBER:100\] |

## Flavor

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  PERMITTED_BUILDING | building name | The named, custom building can be built by a civilization in Fortress Mode. / \[PERMITTED_BUILDING:SOAP_MAKER\] |
|  PERMITTED_JOB | profession | Allows this job type to be selected. This applies to worldgen creatures, in the embark screen, and in play. Certain professions also influence the availability of materials for trade. / \[PERMITTED_JOB:MINER\] |
|  PERMITTED_REACTION | reaction name | Allows this reaction to be used by a civilization. It is used primarily in Fortress Mode, but also allows certain resources, such as / steel / , to be available to a race. When creating custom reactions, this token / must / be present or the player will not be able to use the reaction in Fortress Mode. / \[PERMITTED_REACTION:TAN_A_HIDE\] |
|  CURRENCY_BY_YEAR |  | Causes the civ's currency to be numbered with the year it was minted. |
|  CURRENCY | inorganic material / value | What kind of metals the civ uses for coin minting, as well as the value of the / coin / . Only effective in Adventurer mode due to lack of / dwarven economy / . / \[CURRENCY:SILVER:5\] |
|  ART_FACET_MODIFIER | type / number | OWN_RACE, FANCIFUL, EVIL, GOOD / Number goes from 0 to 25600 where 256 is the default. \[ART_FACET_MODIFIER:OWN_RACE:512\] |
|  ART_IMAGE_ELEMENT_MODIFIER | item / number | CREATURE, PLANT, TREE, SHAPE, ITEM / 0-25600 / Determines the chance of each image occurring in that entity's artwork, such as engravings and on artifacts, for default (non-historical) artwork. / \[ART_IMAGE_ELEMENT_MODIFIER:TREE:512\] |
|  ITEM_IMPROVEMENT_MODIFIER | item / number | ART_IMAGE, COVERED or GLAZED, RINGS_HANGING, BANDS, SPIKES, ITEMSPECIFIC, THREAD, CLOTH, SEWN_IMAGE. / Also available, but effect unknown: PAGES, ILLUSTRATION, INSTRUMENT_PIECE, WRITING, IMAGE_SET, COLORATION. / 0-25600 / Determines the chance of the entity using that particular artwork method, such as "encircled with bands" or "menaces with spikes". / \[ITEM_IMPROVEMENT_MODIFIER:SPIKES:0\] / This also seems to change the amount that the entity will pay for items that are improved in these ways in their tokens. |
|  TRANSLATION | language | What language raw the entity uses. / If an entity lacks this tag, translations are drawn randomly from all translation files. Multiple translation tags will only result in the last one being used. Migrants will sometimes arrive with no name. / If GEN_DIVINE is entered, the entity will use a generated divine language, that is, the same language that is used for the names of / angels / . / If the entity's main creature has / \[UTTERANCES\] / , then this token will be ignored (except when using the naming menu) in favor of procedural / kobold / -style / pseudolanguage / . / \[TRANSLATION:DWARF\] |
|  SELECT_SYMBOL | category / symbol | ALL, REMAINING, BATTLE, BRIDGE, CIV, CRAFT_GUILD, FESTIVAL (doesn't work, see below), HOSPITAL, LIBRARY, MERCHANT_COMPANY, MILITARY_UNIT, OTHER, RELIGION, ROAD, SIEGE, SITE, TEMPLE, TUNNEL, VESSEL, WALL, WAR / The entity will always use a word from the selected symbol(s) to generate names from that category. / OTHER applies the symbol selection to personal names and site names. REMAINING will apply the symbol selection to all categories that have not already been declared above it. / Specific to SELECT_SYMBOL, symbols selected this way will be used as "The X" in "The X of Y" names, and nouns from selected symbols can be used as first / names / . / FESTIVAL does not work. The game uses symbol NAME_FESTIVAL hardcoded. You may consider changing that symbol (with SELECT_SYMBOL), but then it's applied for all entities. / \[SELECT_SYMBOL:ALL:PEACE\] |
|  SUBSELECT_SYMBOL | category / symbol | As SELECT_SYMBOL, a word from the subselected symbol(s) will be used in names of that category, in addition to the word from SELECT_SYMBOL (if specified). Used in vanilla to put violent names in sieges and battles. / Words chosen with SUBSELECT_SYMBOL will appear as either adjectives or "of Y" in "The X of Y" names. / CULL_SYMBOL does not affect subselected symbols. / \[SELECT_SYMBOL:SIEGE:NAME_SIEGE\] / \[SUBSELECT_SYMBOL:SIEGE:VIOLENT\] |
|  CULL_SYMBOL | category / symbol | Causes the entity to not use the words in these SYM sets. / \[CULL_SYMBOL:ALL:UGLY\] |
|  FRIENDLY_COLOR | see color | The color of this entity's civilization settlements in the world gen and embark screens, also used when announcing arrival of their caravan. Defaults to 7:0:1. / \[FRIENDLY_COLOR:1:0:1\] |

## Religion

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  RELIGION | type | REGIONAL_FORCE: The creatures will worship a single force associated with the terrain of their initial biome. / PANTHEON: The creatures will worship a group of gods, each aligned with their spheres and other appropriate ones as well. / Can be specified multiple times, and will pick randomly from the assigned types. Additional instances of each type will weight the random choice, but unlike / \[CREATURE\] / , will not make the entity more likely to spawn. / \[RELIGION:PANTHEON\] |
|  RELIGION_SPHERE | sphere | Can be any available / sphere / - multiple entries are possible. Choosing a religious sphere will automatically make its opposing sphere not possible for the species to have: adding / WATER / , for example, means civs of this entity will never get / FIRE / as a religious sphere. Note that the / DEATH / sphere favours the appearance of necromancers (and therefore, towers) "in" the entity. / \[RELIGION_SPHERE:FORTRESSES\] |
|  SPHERE_ALIGNMENT | sphere / number | This token forces an entity to favor or disfavor particular religious spheres. Default is 256, minimum is 0, maximum is 25600. / Presently, this doesn't cause them to acquire those spheres more often when generating a pantheon. / PLANTS / and / ANIMALS / affect the prevalence of depicting / \[VEGETATION\] / and / \[NATURAL\] / creatures, respectively, in a similar fashion to / \[ART_FACET_MODIFIER\] / . / WAR / modifies the effective / item value / of / weapons / and / armor / to / traders / of this entity. The multiplier is SPHERE_ALIGNMENT / 256, though this only applies to equipment the entity's main creature can properly wield. / \[SPHERE_ALIGNMENT:TREES:512\] |

## Leadership

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  POSITION | string | Defines a leader/noble position for a civilization. These replace previous tags such as \[MAYOR\] and \[CAN_HAVE_SITE_LEADER\] and so on. To define a position further, see Position token. |
|  SITE_VARIABLE_POSITIONS | Position responsibility or ALL | Allows a site responsibility to be taken up by a dynamically generated position (lords, hearthpersons, etc.). Any defined positions holding a given responsibility will take precedence over generated positions for that responsibility. Also appears to cause site disputes.\[Verify\] See also: variable positions |
|  VARIABLE_POSITIONS | Position responsibility or ALL | Allows a responsibility to be taken up by a dynamically generated position (such as Law-maker). Any defined positions holding a given responsibility will take precedence over generated positions for that responsibility. See also: variable positions |

## Behavior

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  ETHIC | behavior / reaction | Sets the civ's view of / ethics / (certain behaviors), from capital punishment to completely acceptable. This also causes the civ to look upon opposing ethics with disfavor if their reaction to it is opposing, and when at extremes (one ACCEPTABLE, another civ UNTHINKABLE; for example) they will often go to war over it. / \[ETHIC:EAT_SAPIENT_KILL:ACCEPTABLE\] |
|  VALUE | value / number | Sets the civ's / cultural values / . Numbers range from -50 (complete anathema) to 0 (neutral) to 50 (highly valued). / \[VALUE:CRAFTSMANSHIP:50\] / Certain values must be set to 15 or more for civs to create structures and form entities during history gen: / 15+ KNOWLEDGE for libraries / 15+ COOPERATION / and / 15+ CRAFTSMANSHIP for craft guilds / Guilds also need guild-valid professions (see / PERMITTED_JOB / ) / If the positions of an entity are variable (and include the CUSTOM_OFFICIAL_1), then CUNNING \> 10 is needed for the CUSTOM_OFFICIAL_1 to have the espionage responsibility. / Also note that the values of a civ can deviate from the fixed values set in the raws, if the civ is able to make libraries. See / here / for more details. |
|  VARIABLE_VALUE | value or ALL / min / max | Makes values randomized rather than specified. / This tag overrides the VALUE tag. Using \[VARIABLE_VALUE:ALL:x:y\] and then overwriting single values with further \[VARIABLE_VALUE:value:x:y\] tags works. |
|  WILL_ACCEPT_TRIBUTE |  | Makes the civ's traders accept offered goods. |
|  WANDERER,  BEAST_HUNTER,  SCOUT,  MERCENARY |  | The civ will send out these sorts of adventurers in worldgen, which seems to increase Tracker skill. These types of adventurers will sometimes be seen leading a battle (instead of war leaders or generals) in remote locations during world-gen, in charge of the defenders. / Mercenaries and monster hunters from the civ may visit player's fortress and petition for residency there to enlist in the military or hunt monsters in caverns, respectively. |
|  ABUSE_BODIES |  | The civilization will mutilate bodies when they are the victors in history-gen warfare, such as hanging bodies from trees, putting them on spikes, and so forth. Adventurers killed in Adventurer mode will sometimes be impaled on spikes wherever they died, with or without this token, and regardless of whether they actually antagonized the townspeople. |
|  ACTIVE_SEASON | season | The season when the civ is most active: when they will trade, interact with you via diplomats, and / or invade you. Civs can have multiple season entries. Note: If multiple caravans arrive at the same time, you are able to select which civ to trade with at the depot menu. ACTIVE_SEASON tags may be changed for a currently active fort. / \[ACTIVE_SEASON:AUTUMN\] |
|  AMBUSHER |  | When invading, sneaks around and shoots at straggling members of your society. They will spawn on the edge of the map and will only be visible when one of their party are spotted; this can be quite dangerous to undefended trade depots. If the civilization also has the SIEGER token, they will eventually ramp it up to less subtle means of warfare. |
|  AT_PEACE_WITH_WILDLIFE |  | Will not attack wildlife, and will not be attacked by them, even if you have them in your party. This can be somewhat disconcerting when attacked by bears in the forest, and your elven ally sits back and does nothing. Additionally, this token determines if the entity can settle in savage biomes. |
|  BABYSNATCHER |  | Sends thieves to steal babies. Without this tag (or AMBUSHER, or ITEM_THIEF), enemy civs will only siege (if capable), and will siege as early as they would otherwise babysnatch. This can happen as early as the first year of the fort! In addition, babysnatcher civs will snatch children during worldgen, allowing them to become part of the civ if they do not escape. Also causes this civ to be hostile to any entity without this token. / Note: If the playable civ in fortress mode has this tag (e.g. you add BABYSNATCHER to the dwarf entity) then the roles will be reversed and elves and humans will siege and ambush and goblins will be friendly to you. However, animals traded away to one's own caravan will count as snatched, reported upon the animal leaving the map, and the animal will not count as having been exported. |
|  BUILDS_OUTDOOR_FORTIFICATIONS |  | Makes the civilization build castles from mead halls. Only functions when the type of site built is a hamlet/town. This, combined with the correct type of position associated with a site, is why adventurers can only lay claim to human sites. Bug:8001 |
|  BUILDS_OUTDOOR_TOMBS |  | Makes the civilization build tombs. |
|  BANDITRY | percentage | Sets a percentage of the entity population to be used as bandits. |
|  DIPLOMAT_BODYGUARDS |  | Visiting diplomats are accompanied by a pair of soldiers. |
|  GENERATED |  | Found on generated divine "HF Guardian Entities". Cannot be used in user-defined raws. |
|  INVADERS_IGNORE_NEUTRALS |  | Causes invaders to ignore visiting caravans and other neutral creatures.\[Verify\] |
|  ITEM_THIEF |  | Sends thieves to steal items. This will also occur in history generation, and thieves will have the "thief" profession. Items stolen in history gen will be scattered around that creature's home. Also causes that civ to be hostile to any entity without this token. Without this tag (or AMBUSHER, or BABYSNATCHER), enemy civs will only siege (if capable), and will siege as early as they would otherwise steal. / Note: If the playable civ in Fortress Mode has this tag (e.g. you add ITEM_THIEF to the Dwarf entity) then the roles will be reversed and elves and humans will siege and ambush and kobolds will be friendly to you. However, ALL items traded away to one's own caravan will count as stolen, reported when the items leave the map, and the stolen items will not count as exported. |
|  LOCAL_BANDITRY |  | Causes the entity to send out patrols that can ambush adventurers. Said patrols will be hostile to any adventurers they encounter, regardless of race or nationality. |
|  MERCHANT_BODYGUARDS |  | Caravan merchants are accompanied by soldiers. |
|  MERCHANT_NOBILITY |  | Merchants will engage in cross-civ trading and form companies. / In previous versions, this resulted in the civ having a Guild Representative / Merchant Baron / Merchant Prince, but now this is controlled solely by positions. |
|  PROGRESS_TRIGGER_POPULATION | level | 0 to 5, civ will come to site once population at site has reached that level. If multiple progress triggers exist for a civ, it will come when any one of them is fulfilled instead of waiting for all of them to be reached. A value of 0 disables the trigger. 1 corresponds to 20 dwarves, 2 to 50 dwarves, 3 to 80, 4 to 110, and 5 to 140. Progress triggers may be changed, added, or deleted for a currently active fort. Note: hostile civs require that this be fulfilled as well as at least one other non-siege trigger before visiting for non-siege activities. |
|  PROGRESS_TRIGGER_PRODUCTION | level | 0 to 5, civ will come to site once created wealth has reached that level. If multiple progress triggers exist for a civ, it will come when any one of them is fulfilled instead of waiting for all of them to be reached. A value of 0 disables the trigger. 1 corresponds to 5000☼ created wealth, 2 to 25000☼, 3 to 100000☼, 4 to 200000☼, and 5 to 300000☼. Progress triggers may be changed, added, or deleted for a currently active fort. |
|  PROGRESS_TRIGGER_TRADE | level | 0 to 5, civ will come to site once exported goods has reached that level. If multiple progress triggers exist for a civ, it will come when any one of them is fulfilled instead of waiting for all of them to be reached. A value of 0 disables the trigger. 1 corresponds to 500☼ exported wealth, 2 to 2500☼, 3 to 10000☼, 4 to 20000☼, and 5 to 30000☼. Progress triggers may be changed, added, or deleted for a currently active fort. |
|  PROGRESS_TRIGGER_POP_SIEGE | level | 0 to 5, civ will begin to send sieges against the player civ when this level is reached if it is hostile. / If multiple progress triggers exist for a civ, it will come when any one of them is fulfilled instead of waiting for all of them to be reached. A value of 0 disables the trigger. |
|  PROGRESS_TRIGGER_PROD_SIEGE | level | 0 to 5, civ will begin to send sieges against the player civ when this level is reached if it is hostile. |
|  PROGRESS_TRIGGER_TRADE_SIEGE | level | 0 to 5, civ will begin to send sieges against the player civ when this level is reached if it is hostile. |
|  SIEGER |  | Will start campfires and wait around at the edge of your map for a month or two before rushing in to attack. This will occur when the progress triggers for sieging are reached. If the civ lacks smaller methods of conflict (AMBUSHER, BABYSNATCHER, ITEM_THIEF), they will instead send smaller-scale sieges when their triggers for "first contact" are reached. |
|  SIEGE_SKILLED_MINERSv53.01 |  | Improves the skill of miner invaders by a factor of 5. Used for dwarves in vanilla. |
|  SITE_GUARDIAN |  | Guards certain special sites, such as a vault belonging to a demon allied with a deity. Used in generated divine entities. |
|  SKULKING |  | This makes the severity of attacks depend on the extent of item/baby thievery rather than the passage of time. Designed to go with ITEM_THIEF, may or may not work with BABYSNATCHER. Prevents the civ from engaging in diplomacy or ending up at war. |
|  TREE_CAP_DIPLOMACY |  | Visiting diplomats impose tree cutting quotas; without this, they will simply compliment your fortress and leave. Also causes the diplomat to make unannounced first contact at the very beginning of the first spring after your fortress becomes a land holder. |
|  LAYER_LINKED |  | Defines if a civilization is a hidden subterranean entity, such as bat man civilizations. May spawn in any of the three caverns; cavern dweller raids due to agitation will pull from these. If you embark as this civ, you have access to pets and trees from all three layers, not only the first. |
|  GENERATE_KEYBOARD_INSTRUMENTS,  GENERATE_PERCUSSION_INSTRUMENTS,  GENERATE_STRINGED_INSTRUMENTS,  GENERATE_WIND_INSTRUMENTS,  GENERATE_DANCE_FORMS,  GENERATE_MUSICAL_FORMS,  GENERATE_POETIC_FORMS |  | Makes civilizations generate the given instruments/forms. |
|  SCHOLAR | scholar type | ALL, ASTRONOMER, CHEMIST, DOCTOR, ENGINEER, GEOGRAPHER, HISTORIAN, MATHEMATICIAN, NATURALIST, PHILOSOPHER |
|  SET_SCHOLARS_ON_VALUES_AND_JOBS |  | Generates scholars based on the values generated with the VARIABLE_VALUE tag. |
|  NO_ARTIFACT_CLAIMS |  | Used for kobolds. |
|  MINING_UNDERWORLD_DISASTERS |  | The civilization can breach the Underworld during world generation, spawning a civilization of [`[EVIL]`](/index.php/Creature_token#EVIL "Creature token") creatures lead by a unique demon. |
|  MYTHICALv51.01-beta26 |  | Builds mysterious dungeons. |

## Available resources

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  AMMO | item token | Used after a ranged weapon type. / \[AMMO:ITEM_AMMO_BOLTS\] |
|  ARMOR | item token / rarity | Rarity is optional, and valid values are FORCED, COMMON, UNCOMMON, and RARE (anything else is treated as COMMON). FORCED items will be available 100% of the time, COMMON items 50%, UNCOMMON items 10%, and RARE items 1%. If certain armor types are lacking after performing one pass of randomised checks, the game will repeat random checks until an option is successfully chosen. / \[ARMOR:ITEM_ARMOR_PLATEMAIL:COMMON\] |
|  DIGGER | item token | Causes the selected weapon to fall under the "digging tools" section of the embark screen. Also forces the weapon to be made out of metal, which can cause issues if a modded entity has access to picks without access to metal - for those cases, listing the pick under the \[WEAPON\] token works just as well. Note that this tag is neither necessary nor sufficient to allow use of that item as a mining tool – for that, the item itself needs to be a weapon with / \[ / SKILL / :MINING\] / . / \[DIGGER:ITEM_WEAPON_PICK\] |
|  GLOVES | item token / rarity | Rarity is optional, and valid values are FORCED, COMMON, UNCOMMON, and RARE (anything else is treated as COMMON). Uses the same rarity values and methods as outlined in ARMOR. / \[GLOVES:ITEM_GLOVES_GLOVES:COMMON\] |
|  HELM | item token / rarity | Rarity is optional, and valid values are FORCED, COMMON, UNCOMMON, and RARE (anything else is treated as COMMON). Uses the same rarity values and methods as outlined in ARMOR. / \[HELM:ITEM_HELM_HELM:COMMON\] |
|  INSTRUMENT | item token | No longer used due to the ability to generate instruments in world generation. It is still usable if pre-defined instruments are modded in, and generated musical forms are capable of selecting pre-defined instruments to use. However, reactions for making instruments, instrument parts, and / or assembling such instruments need to be added as well, as this token no longer adds such instruments to the craftdwarf's workshop menu. / \[INSTRUMENT:ITEM_INSTRUMENT_FLUTE\] |
|  PANTS | item token / rarity | Rarity is optional, and valid values are FORCED, COMMON, UNCOMMON, and RARE (anything else is treated as COMMON). Uses the same rarity values and methods as outlined in ARMOR. / \[PANTS:ITEM_PANTS_PANTS:COMMON\] |
|  SHIELD | item token | \[SHIELD:ITEM_SHIELD_SHIELD\] |
|  SHOES | item token / rarity | Rarity is optional, and valid values are FORCED, COMMON, UNCOMMON, and RARE (anything else is treated as COMMON). Uses the same rarity values and methods as outlined in ARMOR. / \[SHOES:ITEM_SHOES_SHOES:COMMON\] |
|  SIEGEAMMO | item token | \[SIEGEAMMO:ITEM_SIEGEAMMO_BALLISTA\] |
|  TOOL | item token | \[TOOL:ITEM_TOOL_NEST_BOX\] |
|  TOY | item token | \[TOY:ITEM_TOY_PUZZLEBOX\] |
|  TRAPCOMP | item token | \[TRAPCOMP:ITEM_TRAPCOMP_GIANTAXEBLADE\] |
|  WEAPON | item token | While this does not accept a rarity value, something similar can be achieved by having multiple variations of a weapon type with small differences and specifying each of them. / \[1\] / \[WEAPON:ITEM_WEAPON_AXE_BATTLE\] |
|  USE_ANIMAL_PRODUCTS |  | Allows use of products made from animals. All relevant creatures will be able to provide wool, silk, and extracts (including milk and venom) for trade, and non-sentient creatures (unless ethics state otherwise) will be able to provide eggs, caught fish, meat, leather, bone, shell, pearl, horn, and ivory. |
|  USE_ANY_PET_RACE |  | Any creature in the civilization's list of usables (from the surrounding 7x7 or so of squares and map features in those squares) will be included in the initial usable creature list, which then gets pared down or otherwise considered. Without this, only common domestic and equipment creatures are added to the initial list. |
|  USE_CAVE_ANIMALS |  | If they don't have it, creatures with exclusively subterranean biomes are skipped. If they have it, cave creatures will be included in the initial usable creature list. |
|  USE_EVIL_ANIMALS |  | Without this, [`[EVIL]`](/index.php/Creature_token#EVIL "Creature token") creatures are skipped, otherwise, evil creatures with [`[SLOW_LEARNER]`](/index.php/Creature_token#SLOW_LEARNER "Creature token") or *without* [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") will be included in the initial usable creature list, even the normally untameable species. |
|  USE_EVIL_PLANTS |  | Same as USE_EVIL_ANIMALS for all uses of plants. |
|  USE_EVIL_WOOD |  | Same as USE_EVIL_ANIMALS for all uses of wood. |
|  USE_GOOD_ANIMALS |  | Without this, [`[GOOD]`](/index.php/Creature_token#GOOD "Creature token") creatures are skipped, otherwise, good creatures *without* [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") will be included in the initial usable creature list, even the normally untameable species. |
|  USE_GOOD_PLANTS |  | Same as USE_GOOD_ANIMALS for all uses of plants. |
|  USE_GOOD_WOOD |  | Same as USE_GOOD_ANIMALS for all uses of wood. |
|  USE_MISC_PROCESSED_WOOD_PRODUCTS |  | If the relevant professions are permitted, controls availability of lye ([`[LYE_MAKER]`](/index.php/Unit_type_token#LYE_MAKER "Unit type token")), charcoal ([`[WOOD_BURNER]`](/index.php/Unit_type_token#WOOD_BURNER "Unit type token")), and potash ([`[POTASH_MAKER]`](/index.php/Unit_type_token#POTASH_MAKER "Unit type token")). |
|  USE_NON_EXOTIC_PET_RACE |  | Makes the civilization use all locally available non-exotic pets. |
|  COMMON_DOMESTIC_MOUNT |  | Gives the civilization access to creatures with [`[COMMON_DOMESTIC]`](/index.php/Creature_token#COMMON_DOMESTIC "Creature token") and [`[MOUNT]`](/index.php/Creature_token#MOUNT "Creature token"). Additionally, all available (based on USE_ANY_PET_RACE, USE_CAVE_ANIMALS, USE_GOOD_ANIMALS, and USE_EVIL_ANIMALS) creature with [`[MOUNT]`](/index.php/Creature_token#MOUNT "Creature token") and [`[PET]`](/index.php/Creature_token#PET "Creature token") will be allowed for use as mounts during combat. |
|  COMMON_DOMESTIC_PACK |  | Gives the civilization access to creatures with [`[COMMON_DOMESTIC]`](/index.php/Creature_token#COMMON_DOMESTIC "Creature token") and [`[PACK_ANIMAL.]`](/index.php/Creature_token#PACK_ANIMAL. "Creature token") Additionally, all available (see above) creatures with [`[PACK_ANIMAL]`](/index.php/Creature_token#PACK_ANIMAL "Creature token") and [`[PET]`](/index.php/Creature_token#PET "Creature token") will be allowed for use during trade as pack animals. |
|  COMMON_DOMESTIC_PET |  | Gives the civilization access to creatures with [`[COMMON_DOMESTIC]`](/index.php/Creature_token#COMMON_DOMESTIC "Creature token") and [`[PET]`](/index.php/Creature_token#PET "Creature token"). Additionally, all available (see above) creatures with [`[PET]`](/index.php/Creature_token#PET "Creature token") will be allowed for use as pets. |
|  COMMON_DOMESTIC_PULL |  | Gives the civilization access to creatures with [`[COMMON_DOMESTIC]`](/index.php/Creature_token#COMMON_DOMESTIC "Creature token") and [`[WAGON_PULLER]`](/index.php/Creature_token#WAGON_PULLER "Creature token"). Additionally, all available (see above) creatures with [`[WAGON_PULLER]`](/index.php/Creature_token#WAGON_PULLER "Creature token") and [`[PET]`](/index.php/Creature_token#PET "Creature token") will be allowed for use during trade to pull wagons. |
|  RIVER_PRODUCTS |  | Allow use of river products in the goods available for trade. |
|  OCEAN_PRODUCTS |  | Allow use of ocean products (including amber and coral) in the goods available for trade. Without OCEAN_PRODUCTS, civilizations will not be able to trade ocean fish even if they are *also* available from other sources (e.g. sturgeons and stingrays). |
|  INDOOR_FARMING |  | Allow use of underground plant products in the goods available for trade. Lack of suitable vegetation in the caverns will cause worldgen rejections. According to Droseran: "Gives access to plants (structural material) and seeds. It only checks for [`[EDIBLE_RAW]`](/index.php/Material_definition_token#EDIBLE_RAW "Material definition token") or [`[EDIBLE_COOKED]`](/index.php/Material_definition_token#EDIBLE_COOKED "Material definition token") on the plant's structural material. It doesn't check if the plant can be used in a reaction to produce something edible, only if it can be eaten raw or cooked. If an entity with this token is placed in a biome that doesn't have at least one of these tokens on the structural material, the map is rejected. Due to the randomness of plant selection in biomes, this can happen a lot as only about half of the vanilla plants have edible structural materials. Removing either of these tokens from plants dramatically increases map rejections." |
|  OUTDOOR_FARMING |  | Allow use of outdoor plant products in the goods available for trade. Lack of suitable vegetation in this civilization's starting area will cause worldgen rejections. According to Droseran: "Gives access to plants (structural material) and seeds. It only checks for [`[EDIBLE_RAW]`](/index.php/Material_definition_token#EDIBLE_RAW "Material definition token") or [`[EDIBLE_COOKED]`](/index.php/Material_definition_token#EDIBLE_COOKED "Material definition token") on the plant's structural material. It doesn't check if the plant can be used in a reaction to produce something edible, only if it can be eaten raw or cooked. If an entity with this token is placed in a biome that doesn't have at least one of these tokens on the structural material, the map is rejected. Due to the randomness of plant selection in biomes, this can happen a lot as only about half of the vanilla plants have edible structural materials. Removing either of these tokens from plants dramatically increases map rejections." |
|  INDOOR_GARDENS |  | Allow use of underground plant growths (quarry bush leaves, in unmodded games) in the goods available for trade. According to Droseran: "Will never cause map rejections. It allows growths to be used, but doesn't care if none exist. If an entity doesn't have a farming token, they won't have seeds or plants available on embark/trade. But you can still farm in fortress mode with only this token, you just have to get the seeds manually or trading with another civ." |
|  OUTDOOR_GARDENS |  | Allow use of outdoor plant growths in the goods available for trade. According to Droseran: "Will never cause map rejections. It allows growths to be used, but doesn't care if none exist. If an entity doesn't have a farming token, they won't have seeds or plants available on embark/trade. But you can still farm in fortress mode with only this token, you just have to get the seeds manually or trading with another civ." |
|  INDOOR_ORCHARDS |  | Allows use of indoor tree growths in the goods available for trade. Not used in vanilla entities, as vanilla underground trees do not grow fruit. Needs INDOOR_WOOD to function. Will cause rejections, if growths are unavailable. According to Droseran: "Gives access to tree growths. It only checks for growths on trees that are [`[EDIBLE_RAW]`](/index.php/Material_definition_token#EDIBLE_RAW "Material definition token") or [`[EDIBLE_COOKED]`](/index.php/Material_definition_token#EDIBLE_COOKED "Material definition token"). If an entity with this token is placed in a biome that does not have a tree with a growth with at least one of these tokens, the map is rejected." |
|  OUTDOOR_ORCHARDS |  | Allows use of outdoor tree growths in the goods available for trade. Needs OUTDOOR_WOOD to function\[Verify\]. According to Droseran: "Gives access to tree growths. It only checks for growths on trees that are \[EDIBLE_RAW\] or \[EDIBLE_COOKED\]. If an entity with this token is placed in a biome that does not have a tree with a growth with at least one of these tokens, the map is rejected." |
|  CLOTHING |  | Civilization members will attempt to wear clothing. |
|  SUBTERRANEAN_CLOTHING |  | Will wear things made of spider silk and other subterranean materials. |
|  EQUIPMENT_IMPROVEMENTS |  | Adds decorations to equipment based on the level of the generated unit. Also improves item quality. |
|  IMPROVED_BOWS |  | Adds decorations to weapons generated for bowman and master bowman. |
|  METAL_PREF |  | Allows metal materials to be used to make cages (inexpensive metals only) and crafts. |
|  STONE_PREF |  | Allows the civilization to make use of nearby stone types. If the [`[FURNACE_OPERATOR]`](/index.php/Unit_type_token#FURNACE_OPERATOR "Unit type token") job is permitted, also allows ore-bearing stones to be smelted into metals. |
|  WOOD_WEAPONS |  | The civilization can make traditionally metallic weapons such as swords and spears from wood. |
|  WOOD_ARMOR |  | The civilization can make traditionally metallic armor such as mail shirts and helmets from wood. |
|  GEM_PREF |  | Enables creatures of this entity to bring gems in trade. |
|  INDOOR_WOOD |  | Allow use of subterranean wood types, such as tower-cap and fungiwood logs. |
|  OUTDOOR_WOOD |  | Allow use of outdoor wood types, such as mangrove and oak. |
|  GEM_SHAPE | shape | Precious gems cut by this civilization's jewelers can be of this shape. |
|  STONE_SHAPE | shape | Ordinary non-gem stones cut by this civilization's jewelers can be of this shape. |
|  DIVINE_MAT_CLOTHING |  | Allows use of materials with [`[DIVINE]`](/index.php/Inorganic_material_definition_token#DIVINE "Inorganic material definition token") for clothing. Used for generated divine entities. |
|  DIVINE_MAT_CRAFTS |  | Allows use of materials with [`[DIVINE]`](/index.php/Inorganic_material_definition_token#DIVINE "Inorganic material definition token") for crafts.\[Verify\] Used for generated divine entities. |
|  DIVINE_MAT_WEAPONS |  | Allows use of metals with [`[DIVINE]`](/index.php/Inorganic_material_definition_token#DIVINE "Inorganic material definition token") for weapons. Used for generated divine entities. |
|  DIVINE_MAT_ARMOR |  | Allows use of metals with [`[DIVINE]`](/index.php/Inorganic_material_definition_token#DIVINE "Inorganic material definition token") for armor. Used for generated divine entities. |

## Animal definitions

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  ANIMAL |  | Start an animal definition. |
|  ANIMAL_TOKEN | creature token | Select specific creature. |
|  ANIMAL_CASTE_TOKEN | creature caste token | Select specific creature caste (requires ANIMAL_TOKEN). Sites with animal populations will still include all castes, but only the selected ones will be used for specific roles. |
|  ANIMAL_CLASS | creature class | Select creature castes with this creature class (multiple uses allowed). |
|  ANIMAL_FORBIDDEN_CLASS | creature class | Forbid creature castes with this creature class (multiple uses allowed). |
|  ANIMAL_ALWAYS_PRESENT |  | Animal will be present even if it does not naturally occur in the entity's terrain. All creatures, including demons, night trolls and other generated ones will be used if no specific creature or class is selected. |
| ANIMAL_NEVER_MOUNT / , / ANIMAL_ALWAYS_MOUNT / ANIMAL_NEVER_WAGON_PULLER / , / ANIMAL_ALWAYS_WAGON_PULLER / ANIMAL_NEVER_SIEGE / , / ANIMAL_ALWAYS_SIEGE / ANIMAL_NEVER_PET / , / ANIMAL_ALWAYS_PET / ANIMAL_NEVER_PACK_ANIMAL / , / ANIMAL_ALWAYS_PACK_ANIMAL |  | Override creature usage tokens. Respectively: / MOUNT / and / MOUNT_EXOTIC / WAGON_PULLER / TRAINABLE_WAR / and not / CAN_LEARN / PET / and / PET_EXOTIC / PACK_ANIMAL / ALWAYS overrides NEVER if a caste is matched by more than one animal definition. |

## Tissue styling-related tokens

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  TISSUE_STYLE | tissue style unit ID | Select a tissue layer which has the ID attached using TISSUE_STYLE_UNIT token in unit raws. This allows setting further cultural style parameters for the selected tissue layer. |
|  TS_MAINTAIN_LENGTH | minimum length? / maximum length? | Presumably sets culturally preferred tissue length for selected tissue. Needs testing. / Dwarves have their beards set to 100:NONE by default. |
|  TS_PREFERRED_SHAPING | styling token | Valid tokens are NEATLY_COMBED, BRAIDED, DOUBLE_BRAIDS, PONY_TAILS, CLEAN_SHAVEN and STANDARD_HAIR / BEARD / MOUSTACHE / SIDEBURNS_SHAPINGS. / Presumably sets culturally preferred tissue shapings for selected tissue. Needs testing. |

## Examples

*Main articles: Entity examples*
