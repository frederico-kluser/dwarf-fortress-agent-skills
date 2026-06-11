# Entity examples

> Fonte: [Entity examples](https://dwarffortresswiki.org/index.php/Entity_examples) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

This page was created to aid those looking to create new civilizations. Those familiar with entity design should feel free to add helpful/obscure information to the lists below to help less-experienced members of the community with their entities.

## Example Animal Person Civilization

The various Animal People (with the exception of those based on creatures with the \[AQUATIC\] token) already have all the parts they need to join civilized society. They just need to be given an ENTITY that will allow them to create civilizations of their own. The following example creates water-themed otter people civilizations based on the vanilla human civilizations.

    entity_example
                                                        -- make sure the file name starts with "entity_" and matches the first line in the file --
    [OBJECT:ENTITY]                                      -- make sure the file has an [OBJECT:ENTITY] tag before the new ENTITY --

    [ENTITY:OTTER_PEOPLE]                                -- pick any animal person based on a non-AQUATIC creature --
        [CREATURE:OTTER_MAN]                         note that OTTER_MAN is based on RIVER OTTER, not SEA OTTER so they'll prefer fresh water over salt water

                                                        -- give them some appropriate starting biomes --
        [START_BIOME:RIVER_TROPICAL_FRESHWATER]          starts in temperate and tropical, fresh or brackish water biomes
        [START_BIOME:RIVER_TEMPERATE_FRESHWATER]
        [START_BIOME:RIVER_TROPICAL_BRACKISHWATER]
        [START_BIOME:RIVER_TEMPERATE_BRACKISHWATER]
        [START_BIOME:LAKE_TROPICAL_FRESHWATER]
        [START_BIOME:LAKE_TEMPERATE_FRESHWATER]          you can also use "EXCLUSIVE_START_BIOME:X" to create a biome that the entity can start from,
        [START_BIOME:LAKE_TROPICAL_BRACKISHWATER]            but not create any further settlements in (unless explicitly added as a "SETTLEMENT_BIOME")
        [START_BIOME:LAKE_TEMPERATE_BRACKISHWATER]
        [START_BIOME:POOL_TROPICAL_FRESHWATER]
        [START_BIOME:POOL_TEMPERATE_FRESHWATER]
        [START_BIOME:POOL_TROPICAL_BRACKISHWATER]
        [START_BIOME:POOL_TEMPERATE_BRACKISHWATER]       note that entities CAN originate and build functioning settlements in the middle of the ocean
        [START_BIOME:SWAMP_TROPICAL_FRESHWATER]              they just need to be given ocean biomes (like "ANY_OCEAN") for either their START_BIOMEs or SETTLEMENT_BIOMEs
        [START_BIOME:SWAMP_TEMPERATE_FRESHWATER]         !!ocean-based settlements appear to behave properly during world gen, but are likely buggy if visited in adventure mode!!
        [START_BIOME:MARSH_TROPICAL_FRESHWATER]
        [START_BIOME:MARSH_TEMPERATE_FRESHWATER]

                                                        -- list any additional biomes they can settle in --
        [SETTLEMENT_BIOME:ANY_FOREST]                    can settle in all non-ocean water biomes (+ forests in case there aren't enough wet areas for them)
        [SETTLEMENT_BIOME:ANY_LAKE]
        [SETTLEMENT_BIOME:ANY_RIVER]
        [SETTLEMENT_BIOME:ANY_POOL]
        [SETTLEMENT_BIOME:SWAMP_TROPICAL_SALTWATER]
        [SETTLEMENT_BIOME:SWAMP_TEMPERATE_SALTWATER]
        [SETTLEMENT_BIOME:MARSH_TROPICAL_SALTWATER]
        [SETTLEMENT_BIOME:MARSH_TEMPERATE_SALTWATER]

                                                        -- list the biomes they can expand their borders through and the expansion rates --
        [BIOME_SUPPORT:ANY_FOREST:1]
        [BIOME_SUPPORT:ANY_SHRUBLAND:1]                  can expand across shrubland and ocean, but cannot settle in them because they are neither START nor SETTLEMENT biomes
        [BIOME_SUPPORT:OCEAN_TEMPERATE:3]
        [BIOME_SUPPORT:OCEAN_TROPICAL:3]
        [BIOME_SUPPORT:OCEAN_ARCTIC:1]
        [BIOME_SUPPORT:SWAMP_TROPICAL_SALTWATER:1]       prefers fresh water, but can use salt water
        [BIOME_SUPPORT:SWAMP_TEMPERATE_SALTWATER:1]
        [BIOME_SUPPORT:SWAMP_TROPICAL_FRESHWATER:5]
        [BIOME_SUPPORT:SWAMP_TEMPERATE_FRESHWATER:5]
        [BIOME_SUPPORT:MARSH_TROPICAL_SALTWATER:1]
        [BIOME_SUPPORT:MARSH_TEMPERATE_SALTWATER:1]
        [BIOME_SUPPORT:MARSH_TROPICAL_FRESHWATER:5]
        [BIOME_SUPPORT:MARSH_TEMPERATE_FRESHWATER:5]
        [BIOME_SUPPORT:RIVER_TROPICAL_SALTWATER:1]
        [BIOME_SUPPORT:RIVER_TEMPERATE_SALTWATER:1]
        [BIOME_SUPPORT:RIVER_TROPICAL_BRACKISHWATER:2]
        [BIOME_SUPPORT:RIVER_TEMPERATE_BRACKISHWATER:2]
        [BIOME_SUPPORT:RIVER_TROPICAL_FRESHWATER:5]
        [BIOME_SUPPORT:RIVER_TEMPERATE_FRESHWATER:5]
        [BIOME_SUPPORT:LAKE_TROPICAL_SALTWATER:1]
        [BIOME_SUPPORT:LAKE_TEMPERATE_SALTWATER:1]
        [BIOME_SUPPORT:LAKE_TROPICAL_BRACKISHWATER:2]
        [BIOME_SUPPORT:LAKE_TEMPERATE_BRACKISHWATER:2]
        [BIOME_SUPPORT:LAKE_TROPICAL_FRESHWATER:5]
        [BIOME_SUPPORT:LAKE_TEMPERATE_FRESHWATER:5]
        [BIOME_SUPPORT:POOL_TROPICAL_SALTWATER:1]
        [BIOME_SUPPORT:POOL_TEMPERATE_SALTWATER:1]
        [BIOME_SUPPORT:POOL_TROPICAL_BRACKISHWATER:2]
        [BIOME_SUPPORT:POOL_TEMPERATE_BRACKISHWATER:2]
        [BIOME_SUPPORT:POOL_TROPICAL_FRESHWATER:5]
        [BIOME_SUPPORT:POOL_TEMPERATE_FRESHWATER:5]

                                                        -- set the civ settings --

        [FRIENDLY_COLOR:7:0:1]                           color of civ (same as vanilla humans)

        [MAX_STARTING_CIV_NUMBER:100]                    civ limits (same as vanilla humans)
        [MAX_POP_NUMBER:10000]
        [MAX_SITE_POP_NUMBER:120]

        [ALL_MAIN_POPS_CONTROLLABLE]                 they are playable in adventure mode (same as vanilla humans)

        [DEFAULT_SITE_TYPE:CITY]                     they will build and prefer cities, but can live in elven or dwarven settlements (same as vanilla humans)
        [LIKES_SITE:CITY]
        [TOLERATES_SITE:CITY]
        [TOLERATES_SITE:TREE_CITY]
        [TOLERATES_SITE:CAVE_DETAILED]

        [BUILDS_OUTDOOR_FORTIFICATIONS]                  they will build castles and tombs (same as vanilla humans)
        [BUILDS_OUTDOOR_TOMBS]

        [WORLD_CONSTRUCTION:WALL]                        they will build walls, bridges, and roads (same as vanilla humans)
        [WORLD_CONSTRUCTION:BRIDGE]
        [WORLD_CONSTRUCTION:ROAD]

        [BANDITRY:10]                                    they will have bandits (10% of population, same as vanilla humans)

                                                        -- set some religious biases --

        [RELIGION:PANTHEON]                              they will use multiple gods (same as vanilla humans)
        [RELIGION_SPHERE:WATER]                          they will use a water god (picking a sphere prevents them from using the opposing sphere(s), in this case FIRE)
        [SPHERE_ALIGNMENT:LAKES:5120]                    they are 20x more likely to use gods from these particular spheres
        [SPHERE_ALIGNMENT:RIVERS:5120]                   default value is 256, range is 0 to 25600
        [SPHERE_ALIGNMENT:RAIN:5120]
        [SPHERE_ALIGNMENT:FISH:5120]
        [SPHERE_ALIGNMENT:FISHING:5120]
        [SPHERE_ALIGNMENT:COASTS:5120]
        [SPHERE_ALIGNMENT:SEASONS:5120]
        [SPHERE_ALIGNMENT:CHAOS:5120]
        [SPHERE_ALIGNMENT:YOUTH:5120]

                                                        -- set up their language --

        [TRANSLATION:HUMAN]                              they will use the human language

        [SELECT_SYMBOL:ALL:WILD]                     they will prefer using these word groups (symbols) when naming anything
        [SELECT_SYMBOL:ALL:AQUATIC]
        [SELECT_SYMBOL:ALL:GAMES]
        [SELECT_SYMBOL:ALL:NATURE]

        [CULL_SYMBOL:ALL:EARTH]                          they will not use these word groups when naming anything
        [CULL_SYMBOL:ALL:FIRE]
        [CULL_SYMBOL:ALL:SKY]
        [CULL_SYMBOL:ALL:RESTRAIN]
        [CULL_SYMBOL:ALL:SUBORDINATE]
        [CULL_SYMBOL:ALL:EVIL]
        [CULL_SYMBOL:ALL:NEGATIVE]
        [CULL_SYMBOL:ALL:UGLY]
        [CULL_SYMBOL:ALL:NEGATOR]

        [SELECT_SYMBOL:WAR:NAME_WAR]                 they will use these specific word groups for specific things (this section is unchanged from vanilla humans)
            [SUBSELECT_SYMBOL:WAR:VIOLENT]
        [SELECT_SYMBOL:BATTLE:NAME_BATTLE]
            [SUBSELECT_SYMBOL:BATTLE:VIOLENT]            SUBSELECT_SYMBOL chooses descriptors for the previous symbol (this SELECT/SUBSELECT pair will create battles named like "Battle of Carnage")
        [SELECT_SYMBOL:SIEGE:NAME_SIEGE]
            [SUBSELECT_SYMBOL:SIEGE:VIOLENT]
        [SELECT_SYMBOL:ROAD:NAME_ROAD]
        [SELECT_SYMBOL:TUNNEL:NAME_TUNNEL]
        [SELECT_SYMBOL:BRIDGE:NAME_BRIDGE]
        [SELECT_SYMBOL:WALL:NAME_WALL]
        [SELECT_SYMBOL:TEMPLE:NAME_BUILDING_TEMPLE]
        [SELECT_SYMBOL:LIBRARY:NAME_BUILDING_LIBRARY]
        [SELECT_SYMBOL:MERCHANT_COMPANY:NAME_ENTITY_MERCHANT_COMPANY]
        [SELECT_SYMBOL:CRAFT_GUILD:NAME_ENTITY_MERCHANT_COMPANY]
        [SELECT_SYMBOL:HOSPITAL:NAME_BUILDING_HOSPITAL]
        [SELECT_SYMBOL:CIV:NAME_ENTITY_KINGDOM]
        [SELECT_SYMBOL:SITE:NAME_ENTITY_TOWN_FOUNDER]

                                                        -- set up their values --

        [VARIABLE_VALUE:LAW:-40:40]                      they randomly choose from a diverse value range just like humans, but with a bit more wild variance
        [VARIABLE_VALUE:LOYALTY:-40:40]                  (vanilla humans use -30 to +30 for all values)
        [VARIABLE_VALUE:FAMILY:-40:40]                   the max possible range is -50 to +50
        [VARIABLE_VALUE:FRIENDSHIP:-40:40]
        [VARIABLE_VALUE:POWER:-40:40]
        [VARIABLE_VALUE:TRUTH:-40:40]
        [VARIABLE_VALUE:CUNNING:-40:40]
        [VARIABLE_VALUE:ELOQUENCE:-40:40]                you could instead use the format "VALUE:ELOQUENCE:X" to make how much they value ELOQUENCE to be a constant
        [VARIABLE_VALUE:FAIRNESS:-40:40]                 and you can also use "ALL" to target all values at once
        [VARIABLE_VALUE:DECORUM:-40:40]                      (vanilla humans shorten their entire values section to "VARIABLE_VALUE:ALL:-30:30")
        [VARIABLE_VALUE:TRADITION:-40:40]
        [VARIABLE_VALUE:ARTWORK:-40:40]
        [VARIABLE_VALUE:COOPERATION:15:40]               !!a min of 15 COOPERATION (and CRAFTSMANSHIP) is needed for craft guilds to form!!
        [VARIABLE_VALUE:INDEPENDENCE:-40:40]
        [VARIABLE_VALUE:INTROSPECTION:-40:40]
        [VARIABLE_VALUE:SELF_CONTROL:-40:40]
        [VARIABLE_VALUE:TRANQUILITY:-40:40]
        [VARIABLE_VALUE:HARMONY:-40:40]
        [VARIABLE_VALUE:MERRIMENT:-40:40]
        [VARIABLE_VALUE:CRAFTSMANSHIP:15:40]         !!a min of 15 CRAFTSMANSHIP (and COOPERATION) is needed for craft guilds to form!!
        [VARIABLE_VALUE:MARTIAL_PROWESS:-40:40]
        [VARIABLE_VALUE:SKILL:-40:40]
        [VARIABLE_VALUE:HARD_WORK:-40:40]
        [VARIABLE_VALUE:SACRIFICE:-40:40]
        [VARIABLE_VALUE:COMPETITION:-40:40]
        [VARIABLE_VALUE:PERSEVERANCE:-40:40]
        [VARIABLE_VALUE:LEISURE_TIME:20:40]              they are playful (Urist likes otter people for their playfulness) and will always value LEISURE_TIME (+20 to +40)
        [VARIABLE_VALUE:COMMERCE:-40:40]
        [VARIABLE_VALUE:ROMANCE:-40:40]
        [VARIABLE_VALUE:NATURE:20:50]                    they will always value NATURE (+20 to +50)
        [VARIABLE_VALUE:PEACE:-40:40]
        [VARIABLE_VALUE:KNOWLEDGE:15:40]             !!a min of 15 KNOWLEDGE is needed for libraries to form!!

        [SET_SCHOLARS_ON_VALUES_AND_JOBS]                scholar types will be based on the values picked and the jobs allowed (same as vanilla humans)

                                                        -- set up their ethics --

        [ETHIC:KILL_ENTITY_MEMBER:JUSTIFIED_IF_GOOD_REASON]  same as vanilla humans
        [ETHIC:KILL_NEUTRAL:JUSTIFIED_IF_NO_REPERCUSSIONS]
        [ETHIC:KILL_ENEMY:ACCEPTABLE]
        [ETHIC:KILL_ANIMAL:ACCEPTABLE]
        [ETHIC:KILL_PLANT:ACCEPTABLE]
        [ETHIC:TORTURE_AS_EXAMPLE:ACCEPTABLE]
        [ETHIC:TORTURE_FOR_INFORMATION:ACCEPTABLE]
        [ETHIC:TORTURE_FOR_FUN:APPALLING]
        [ETHIC:TORTURE_ANIMALS:SHUN]
        [ETHIC:TREASON:PUNISH_CAPITAL]
        [ETHIC:OATH_BREAKING:PUNISH_CAPITAL]
        [ETHIC:LYING:PERSONAL_MATTER]
        [ETHIC:VANDALISM:PUNISH_SERIOUS]
        [ETHIC:TRESPASSING:PUNISH_SERIOUS]
        [ETHIC:THEFT:PUNISH_SERIOUS]
        [ETHIC:ASSAULT:PUNISH_SERIOUS]
        [ETHIC:SLAVERY:ACCEPTABLE]
        [ETHIC:EAT_SAPIENT_OTHER:UNTHINKABLE]
        [ETHIC:EAT_SAPIENT_KILL:UNTHINKABLE]
        [ETHIC:MAKE_TROPHY_SAME_RACE:ACCEPTABLE]
        [ETHIC:MAKE_TROPHY_SAPIENT:ACCEPTABLE]
        [ETHIC:MAKE_TROPHY_ANIMAL:ACCEPTABLE]

                                                        -- set up their culture --

        [GENERATE_STRINGED_INSTRUMENTS]                  same as vanilla humans
        [GENERATE_WIND_INSTRUMENTS]
        [GENERATE_PERCUSSION_INSTRUMENTS]
        [GENERATE_POETIC_FORMS]
        [GENERATE_MUSICAL_FORMS]
        [GENERATE_DANCE_FORMS]

        [POSITION:FLOW_READER]                           create some special noble positions for them (these are copies of the vanilla elf positions with some name changes)
            [NAME:reader of the flow:readers of the flow]      (same as elf druid)
            [NUMBER:1]
            [RESPONSIBILITY:RELIGION]
            [SUCCESSION:BY_POSITION:WAVE_WATCHER]
            [MENIAL_WORK_EXEMPTION]
            [PUNISHMENT_EXEMPTION]
            [ELECTED]
            [DETERMINES_COIN_DESIGN]
            [PRECEDENCE:1]
            [FLASHES]
            [BRAG_ON_KILL]
            [CHAT_WORTHY]
            [DO_NOT_CULL]
            [KILL_QUEST]
            [EXPORTED_IN_LEGENDS]
            [COLOR:2:0:1]
            [DUTY_BOUND]
        [POSITION:WAVE_WATCHER]
            [NAME:watcher of the waves:watchers of the waves]  (same as elf acolyte)
            [NUMBER:1]
            [MENIAL_WORK_EXEMPTION]
            [PUNISHMENT_EXEMPTION]
            [APPOINTED_BY:FLOW_READER]
            [PRECEDENCE:100]
            [FLASHES]
            [BRAG_ON_KILL]
            [CHAT_WORTHY]
            [DO_NOT_CULL]
            [COLOR:2:0:0]
            [DUTY_BOUND]
        [POSITION:FAMILY_SUCCESSOR]                              (same as elf princess without the GENDER:FEMALE restriction)
            [NAME:family successor:family successors]  the collective noun for a group of otters is a "family" of otters
            [NUMBER:1]
            [RESPONSIBILITY:MILITARY_GOALS]
            [RESPONSIBILITY:MILITARY_STRATEGY]
            [RESPONSIBILITY:ESPIONAGE]
            [COMMANDER:FAR_SWIMMER_CAPTAIN:ALL]
            [MENIAL_WORK_EXEMPTION]
            [PUNISHMENT_EXEMPTION]
            [APPOINTED_BY:FLOW_READER]
            [PRECEDENCE:3]
            [FLASHES]
            [BRAG_ON_KILL]
            [CHAT_WORTHY]
            [DO_NOT_CULL]
            [KILL_QUEST]
            [EXPORTED_IN_LEGENDS]
            [COLOR:3:0:1]
            [DUTY_BOUND]
        [POSITION:FAMILY_LEADER]                                 (same as elf queen without the GENDER:FEMALE restriction)
            [NAME:family leader:family leaders]
            [NUMBER:1]
            [RULES_FROM_LOCATION]
            [SUCCESSION:BY_POSITION:FAMILY_SUCCESSOR]
            [MENIAL_WORK_EXEMPTION]
            [PUNISHMENT_EXEMPTION]
            [APPOINTED_BY:FLOW_READER]
            [RESPONSIBILITY:LAW_MAKING]
            [RESPONSIBILITY:RECEIVE_DIPLOMATS]
            [RESPONSIBILITY:MILITARY_GOALS]
            [PRECEDENCE:2]
            [FLASHES]
            [BRAG_ON_KILL]
            [CHAT_WORTHY]
            [DO_NOT_CULL]
            [KILL_QUEST]
            [EXPORTED_IN_LEGENDS]
            [COLOR:7:0:1]
            [DUTY_BOUND]
        [POSITION:DIPLOMAT]                                      (same as elf diplomat)
            [NAME:diplomat:diplomats]
            [NUMBER:1]
            [RESPONSIBILITY:MAKE_INTRODUCTIONS]
            [RESPONSIBILITY:MAKE_PEACE_AGREEMENTS]
            [RESPONSIBILITY:MAKE_TOPIC_AGREEMENTS]
            [APPOINTED_BY:FAMILY_LEADER]
            [PRECEDENCE:70]
            [DO_NOT_CULL]
            [COLOR:7:0:1]
            [MENIAL_WORK_EXEMPTION]
            [SLEEP_PRETENSION]
            [PUNISHMENT_EXEMPTION]
            [ACCOUNT_EXEMPT]
            [DUTY_BOUND]
        [POSITION:FAR_SWIMMER_CAPTAIN]                           (same as elf ranger captain)
            [NAME:far swimmer captain:far swimmer captains]
            [NUMBER:AS_NEEDED]
            [SQUAD:10:far swimmer:far swimmers]
            [RESPONSIBILITY:ATTACK_ENEMIES]
            [RESPONSIBILITY:PATROL_TERRITORY]
            [APPOINTED_BY:FAMILY_SUCCESSOR]
            [PRECEDENCE:200]
            [DO_NOT_CULL]
            [DUTY_BOUND]

        [VARIABLE_POSITIONS:ALL]                     dynamically generate other positions as needed (same as vanilla humans)
        [SITE_VARIABLE_POSITIONS:ALL]

                                                        -- set trade and quest behavior --

        [RIVER_PRODUCTS]                             give them access to products from rivers and oceans (same as vanilla humans)
        [OCEAN_PRODUCTS]

        [WANDERER]                                       they will send out these types of adventurers (same as vanilla humans)
        [BEAST_HUNTER]
        [SCOUT]
        [MERCENARY]

        [CLOTHING]                                       they will make and wear clothing (same as vanilla humans)

        [MERCHANT_NOBILITY]                              they will have merchants
        [MERCHANT_BODYGUARDS]                                and guards for their merchants
        [DIPLOMAT_BODYGUARDS]                                and for their diplomats (all the same as vanilla humans)

        [METAL_PREF]                                 they use metal, gems, and stone (same as vanilla humans)
        [GEM_PREF]
        [STONE_PREF]

        [OUTDOOR_WOOD]                                   they use above-ground wood and plant products (same as vanilla humans)
        [OUTDOOR_FARMING]
        [OUTDOOR_GARDENS]
        [OUTDOOR_ORCHARDS]                               they can use fruits (vanilla humans do not have this)

        [USE_ANIMAL_PRODUCTS]                            they can use animal-based products (same as vanilla humans)
        [USE_MISC_PROCESSED_WOOD_PRODUCTS]               they can use lye, potash, charcoal (same as vanilla humans)

        [COMMON_DOMESTIC_PACK]                           they can tame and use domestic animals (same as vanilla humans)
        [COMMON_DOMESTIC_PULL]
        [COMMON_DOMESTIC_MOUNT]
        [COMMON_DOMESTIC_PET]

        [USE_NON_EXOTIC_PET_RACE]                        they can tame and use any local creatures (same as vanilla humans)

        [ACTIVE_SEASON:SUMMER]                           trade season and thresholds, siege thresholds (same as vanilla humans)
        [PROGRESS_TRIGGER_TRADE:1]
        [SIEGER]
        [PROGRESS_TRIGGER_POP_SIEGE:3]
        [PROGRESS_TRIGGER_PROD_SIEGE:0]
        [PROGRESS_TRIGGER_TRADE_SIEGE:0]

        [WILL_ACCEPT_TRIBUTE]                            their traders will accept offered goods (same as vanilla humans)

        [CURRENCY:COPPER:1]                              their currency metals and values (same as vanilla humans)
        [CURRENCY:SILVER:5]
        [CURRENCY:GOLD:15]

        [EQUIPMENT_IMPROVEMENTS]                     they can decorate items (same as vanilla humans)

        [ART_FACET_MODIFIER:FANCIFUL:640]                they prefer art of fanciful creatures or themselves (same as vanilla humans)
        [ART_FACET_MODIFIER:OWN_RACE:512]                default value is 256, range is 0 to 25600. types are OWN_RACE, FANCIFUL, EVIL, or GOOD

        [ART_IMAGE_ELEMENT_MODIFIER:CREATURE:512]        they prefer art of creatures. default value is 256, range is 0 to 25600. types are CREATURE, PLANT, TREE, SHAPE, or ITEM

        [ITEM_IMPROVEMENT_MODIFIER:ART_IMAGE:512]        they prefer adorning items with images
        [ITEM_IMPROVEMENT_MODIFIER:SEWN_IMAGE:512]       default value is 256, range is 0 to 25600. types are ART_IMAGE, COVERED, RINGS_HANGING, BANDS, SPIKES, ITEMSPECIFIC, THREAD, CLOTH, or SEWN_IMAGE

                                                        -- finally, give them the same items, jobs, reactions, and buildings as vanilla humans (this continues to the end of the example) --
        [DIGGER:ITEM_WEAPON_PICK]

        [WEAPON:ITEM_WEAPON_WHIP]
        [WEAPON:ITEM_WEAPON_AXE_BATTLE]
        [WEAPON:ITEM_WEAPON_HAMMER_WAR]
        [WEAPON:ITEM_WEAPON_SWORD_SHORT]
        [WEAPON:ITEM_WEAPON_SPEAR]
        [WEAPON:ITEM_WEAPON_MACE]
        [WEAPON:ITEM_WEAPON_CROSSBOW]
            [AMMO:ITEM_AMMO_BOLTS]
        [WEAPON:ITEM_WEAPON_BOW]
            [AMMO:ITEM_AMMO_ARROWS]
        [WEAPON:ITEM_WEAPON_PIKE]
        [WEAPON:ITEM_WEAPON_HALBERD]
        [WEAPON:ITEM_WEAPON_SWORD_2H]
        [WEAPON:ITEM_WEAPON_SWORD_LONG]
        [WEAPON:ITEM_WEAPON_MAUL]
        [WEAPON:ITEM_WEAPON_AXE_GREAT]
        [WEAPON:ITEM_WEAPON_FLAIL]
        [WEAPON:ITEM_WEAPON_MORNINGSTAR]
        [WEAPON:ITEM_WEAPON_SCIMITAR]
        [WEAPON:ITEM_WEAPON_AXE_TRAINING]
        [WEAPON:ITEM_WEAPON_SWORD_SHORT_TRAINING]
        [WEAPON:ITEM_WEAPON_SPEAR_TRAINING]

        [ARMOR:ITEM_ARMOR_BREASTPLATE:COMMON]
        [ARMOR:ITEM_ARMOR_MAIL_SHIRT:COMMON]
        [ARMOR:ITEM_ARMOR_LEATHER:COMMON]
        [ARMOR:ITEM_ARMOR_COAT:COMMON]
        [ARMOR:ITEM_ARMOR_SHIRT:COMMON]
        [ARMOR:ITEM_ARMOR_CLOAK:COMMON]
        [ARMOR:ITEM_ARMOR_TUNIC:COMMON]
        [ARMOR:ITEM_ARMOR_TOGA:UNCOMMON]
        [ARMOR:ITEM_ARMOR_CAPE:COMMON]
        [ARMOR:ITEM_ARMOR_VEST:COMMON]
        [ARMOR:ITEM_ARMOR_DRESS:COMMON]
        [ARMOR:ITEM_ARMOR_ROBE:COMMON]

        [HELM:ITEM_HELM_HELM:COMMON]
        [HELM:ITEM_HELM_CAP:COMMON]
        [HELM:ITEM_HELM_HOOD:COMMON]
        [HELM:ITEM_HELM_TURBAN:UNCOMMON]
        [HELM:ITEM_HELM_MASK:RARE]
        [HELM:ITEM_HELM_VEIL_HEAD:UNCOMMON]
        [HELM:ITEM_HELM_VEIL_FACE:RARE]
        [HELM:ITEM_HELM_SCARF_HEAD:UNCOMMON]

        [GLOVES:ITEM_GLOVES_GAUNTLETS:COMMON]
        [GLOVES:ITEM_GLOVES_GLOVES:COMMON]
        [GLOVES:ITEM_GLOVES_MITTENS:COMMON]

        [SHOES:ITEM_SHOES_SHOES:COMMON]
        [SHOES:ITEM_SHOES_BOOTS:COMMON]
        [SHOES:ITEM_SHOES_BOOTS_LOW:COMMON]
        [SHOES:ITEM_SHOES_SANDAL:COMMON]
        [SHOES:ITEM_SHOES_CHAUSSE:UNCOMMON]
        [SHOES:ITEM_SHOES_SOCKS:COMMON]

        [PANTS:ITEM_PANTS_PANTS:COMMON]
        [PANTS:ITEM_PANTS_GREAVES:COMMON]
        [PANTS:ITEM_PANTS_LEGGINGS:COMMON]
        [PANTS:ITEM_PANTS_LOINCLOTH:COMMON]
        [PANTS:ITEM_PANTS_THONG:UNCOMMON]
        [PANTS:ITEM_PANTS_SKIRT:COMMON]
        [PANTS:ITEM_PANTS_SKIRT_SHORT:COMMON]
        [PANTS:ITEM_PANTS_SKIRT_LONG:COMMON]
        [PANTS:ITEM_PANTS_BRAIES:UNCOMMON]

        [SHIELD:ITEM_SHIELD_SHIELD]
        [SHIELD:ITEM_SHIELD_BUCKLER]

        [SIEGEAMMO:ITEM_SIEGEAMMO_BALLISTA]

        [TRAPCOMP:ITEM_TRAPCOMP_GIANTAXEBLADE]
        [TRAPCOMP:ITEM_TRAPCOMP_ENORMOUSCORKSCREW]
        [TRAPCOMP:ITEM_TRAPCOMP_SPIKEDBALL]
        [TRAPCOMP:ITEM_TRAPCOMP_LARGESERRATEDDISC]
        [TRAPCOMP:ITEM_TRAPCOMP_MENACINGSPIKE]

        [TOY:ITEM_TOY_PUZZLEBOX]
        [TOY:ITEM_TOY_BOAT]
        [TOY:ITEM_TOY_HAMMER]
        [TOY:ITEM_TOY_AXE]

        [TOOL:ITEM_TOOL_CAULDRON]
        [TOOL:ITEM_TOOL_LADLE]
        [TOOL:ITEM_TOOL_BOWL]
        [TOOL:ITEM_TOOL_MORTAR]
        [TOOL:ITEM_TOOL_PESTLE]
        [TOOL:ITEM_TOOL_KNIFE_CARVING]
        [TOOL:ITEM_TOOL_KNIFE_BONING]
        [TOOL:ITEM_TOOL_KNIFE_SLICING]
        [TOOL:ITEM_TOOL_KNIFE_MEAT_CLEAVER]
        [TOOL:ITEM_TOOL_FORK_CARVING]
        [TOOL:ITEM_TOOL_NEST_BOX]
        [TOOL:ITEM_TOOL_JUG]
        [TOOL:ITEM_TOOL_LARGE_POT]
        [TOOL:ITEM_TOOL_HIVE]
        [TOOL:ITEM_TOOL_POUCH]
        [TOOL:ITEM_TOOL_WHEELBARROW]
        [TOOL:ITEM_TOOL_SCROLL_ROLLERS]
        [TOOL:ITEM_TOOL_BOOK_BINDING]
        [TOOL:ITEM_TOOL_SCROLL]
        [TOOL:ITEM_TOOL_QUIRE]
        [TOOL:ITEM_TOOL_BOOKCASE]
        [TOOL:ITEM_TOOL_PEDESTAL]
        [TOOL:ITEM_TOOL_ALTAR]
        [TOOL:ITEM_TOOL_DIE]

        [STONE_SHAPE:OVAL_CABOCHON]
        [STONE_SHAPE:ROUND_CABOCHON]
        [STONE_SHAPE:CUSHION_CABOCHON]
        [STONE_SHAPE:RECTANGULAR_CABOCHON]

        [GEM_SHAPE:OVAL_CABOCHON]
        [GEM_SHAPE:ROUND_CABOCHON]
        [GEM_SHAPE:CUSHION_CABOCHON]
        [GEM_SHAPE:RECTANGULAR_CABOCHON]
        [GEM_SHAPE:POINT_CUT_GEM]
        [GEM_SHAPE:TABLE_CUT_GEM]
        [GEM_SHAPE:SINGLE_CUT_GEM]
        [GEM_SHAPE:ROSE_CUT_GEM]
        [GEM_SHAPE:BRIOLETTE_CUT_GEM]

        [PERMITTED_JOB:MINER]
        [PERMITTED_JOB:CARPENTER]
        [PERMITTED_JOB:BOWYER]
        [PERMITTED_JOB:WOODCUTTER]
        [PERMITTED_JOB:ENGRAVER]
        [PERMITTED_JOB:MASON]
        [PERMITTED_JOB:ANIMAL_CARETAKER]
        [PERMITTED_JOB:ANIMAL_TRAINER]
        [PERMITTED_JOB:HUNTER]
        [PERMITTED_JOB:TRAPPER]
        [PERMITTED_JOB:ANIMAL_DISSECTOR]
        [PERMITTED_JOB:FURNACE_OPERATOR]
        [PERMITTED_JOB:WEAPONSMITH]
        [PERMITTED_JOB:ARMORER]
        [PERMITTED_JOB:BLACKSMITH]
        [PERMITTED_JOB:METALCRAFTER]
        [PERMITTED_JOB:GEM_CUTTER]
        [PERMITTED_JOB:GEM_SETTER]
        [PERMITTED_JOB:WOODCRAFTER]
        [PERMITTED_JOB:STONECRAFTER]
        [PERMITTED_JOB:LEATHERWORKER]
        [PERMITTED_JOB:BONE_CARVER]
        [PERMITTED_JOB:WEAVER]
        [PERMITTED_JOB:CLOTHIER]
        [PERMITTED_JOB:GLASSMAKER]
        [PERMITTED_JOB:FISHERMAN]
        [PERMITTED_JOB:FISH_DISSECTOR]
        [PERMITTED_JOB:FISH_CLEANER]
        [PERMITTED_JOB:CHEESE_MAKER]
        [PERMITTED_JOB:MILKER]
        [PERMITTED_JOB:SHEARER]
        [PERMITTED_JOB:SPINNER]
        [PERMITTED_JOB:GELDER]
        [PERMITTED_JOB:COOK]
        [PERMITTED_JOB:THRESHER]
        [PERMITTED_JOB:MILLER]
        [PERMITTED_JOB:BUTCHER]
        [PERMITTED_JOB:TANNER]
        [PERMITTED_JOB:DYER]
        [PERMITTED_JOB:PLANTER]
        [PERMITTED_JOB:HERBALIST]
        [PERMITTED_JOB:BREWER]
        [PERMITTED_JOB:SOAP_MAKER]
        [PERMITTED_JOB:POTASH_MAKER]
        [PERMITTED_JOB:LYE_MAKER]
        [PERMITTED_JOB:WOOD_BURNER]
        [PERMITTED_JOB:MECHANIC]
        [PERMITTED_JOB:SIEGE_ENGINEER]
        [PERMITTED_JOB:SIEGE_OPERATOR]
        [PERMITTED_JOB:PUMP_OPERATOR]
        [PERMITTED_JOB:CLERK]
        [PERMITTED_JOB:ADMINISTRATOR]
        [PERMITTED_JOB:TRADER]
        [PERMITTED_JOB:DIAGNOSER]
        [PERMITTED_JOB:BONE_SETTER]
        [PERMITTED_JOB:SUTURER]
        [PERMITTED_JOB:SURGEON]
        [PERMITTED_JOB:GLAZER]
        [PERMITTED_JOB:POTTER]
        [PERMITTED_JOB:PRESSER]
        [PERMITTED_JOB:BEEKEEPER]
        [PERMITTED_JOB:WAX_WORKER]
        [PERMITTED_JOB:PAPERMAKER]
        [PERMITTED_JOB:BOOKBINDER]

        [PERMITTED_BUILDING:SOAP_MAKER]
        [PERMITTED_BUILDING:SCREW_PRESS]

        [PERMITTED_REACTION:TAN_A_HIDE]
        [PERMITTED_REACTION:RENDER_FAT]
        [PERMITTED_REACTION:MAKE_SOAP_FROM_TALLOW]
        [PERMITTED_REACTION:MAKE_SOAP_FROM_OIL]
        [PERMITTED_REACTION:MILL_SEEDS_NUTS_TO_PASTE]
        [PERMITTED_REACTION:MAKE_CLAY_JUG]
        [PERMITTED_REACTION:MAKE_CLAY_BRICKS]
        [PERMITTED_REACTION:MAKE_CLAY_STATUE]
        [PERMITTED_REACTION:MAKE_LARGE_CLAY_POT]
        [PERMITTED_REACTION:MAKE_CLAY_CRAFTS]
        [PERMITTED_REACTION:MAKE_QUICKLIME]
        [PERMITTED_REACTION:MAKE_MILK_OF_LIME]
        [PERMITTED_REACTION:MAKE_PARCHMENT]
        [PERMITTED_REACTION:MAKE_SCROLL]
        [PERMITTED_REACTION:MAKE_QUIRE]
        [PERMITTED_REACTION:MAKE_SHEET_FROM_PLANT]
        [PERMITTED_REACTION:MAKE_SLURRY_FROM_PLANT]
        [PERMITTED_REACTION:PRESS_PLANT_PAPER]
        [PERMITTED_REACTION:BIND_BOOK]
        [PERMITTED_REACTION:GLAZE_JUG]
        [PERMITTED_REACTION:GLAZE_STATUE]
        [PERMITTED_REACTION:GLAZE_LARGE_POT]
        [PERMITTED_REACTION:GLAZE_CRAFT]
        [PERMITTED_REACTION:PRESS_OIL]
        [PERMITTED_REACTION:PRESS_OIL_FRUIT]
        [PERMITTED_REACTION:MAKE_CLAY_HIVE]
        [PERMITTED_REACTION:PRESS_HONEYCOMB]
        [PERMITTED_REACTION:MAKE_WAX_CRAFTS]
        [PERMITTED_REACTION:BREW_DRINK_FROM_PLANT]
        [PERMITTED_REACTION:BREW_DRINK_FROM_PLANT_GROWTH]
        [PERMITTED_REACTION:MAKE_MEAD]
        [PERMITTED_REACTION:PROCESS_PLANT_TO_BAG]
        [PERMITTED_REACTION:BRASS_MAKING]
        [PERMITTED_REACTION:BRASS_MAKING2]
        [PERMITTED_REACTION:BRONZE_MAKING]
        [PERMITTED_REACTION:BRONZE_MAKING2]
        [PERMITTED_REACTION:ELECTRUM_MAKING]
        [PERMITTED_REACTION:ELECTRUM_MAKING2]
        [PERMITTED_REACTION:BILLON_MAKING]
        [PERMITTED_REACTION:BILLON_MAKING2]
        [PERMITTED_REACTION:PEWTER_FINE_MAKING]
        [PERMITTED_REACTION:PEWTER_FINE_MAKING2]
        [PERMITTED_REACTION:PEWTER_TRIFLE_MAKING]
        [PERMITTED_REACTION:PEWTER_TRIFLE_MAKING2]
        [PERMITTED_REACTION:PEWTER_LAY_MAKING]
        [PERMITTED_REACTION:BLACK_BRONZE_MAKING]
        [PERMITTED_REACTION:STERLING_SILVER_MAKING]
        [PERMITTED_REACTION:ROSE_GOLD_MAKING]

Now after this example you might be thinking "*Why not make a generic animal person civilization and stuff all 175+ existing \[CREATURE:ANIMAL_MAN\] tokens into it?*". This works, but the trick is it works far too well. The number of \[CREATURE:X\] tags changes the civ's spawn rate, so adding every \[CREATURE:ANIMAL_MAN\] to one entity will likely cause their civ to spawn so often that it blocks all the elves, humans, goblins, kobolds, and dwarves from spawning and will lead to world gen rejections. To balance the spawn rates for the vanilla civs you would need to add \[SELECT_ENTITY:VANILLA_ENTITY_X\] followed by the same number (175+) of duplicate \[CREATURE:VANILLA_CREATURE_X\] tokens for each vanilla civ. See entity placement for more info on this.

## General Tips
