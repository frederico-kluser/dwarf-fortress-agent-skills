# Position token

> Fonte: [Position token](https://dwarffortresswiki.org/index.php/Position_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\
Position tokens define noble positions for civilizations and site governments, inside entity tokens. In the vanilla game, position token definitions can be found in `\data\vanilla\vanilla_entities\objects\entity_default.txt`.

## Code

A position is defined with a position 'code', as an argument in the \[POSITION\]-tag. The same code may be used multiple times, they don't have to be unique. This code is used as reference by APPOINTED_BY, SUCCESSION:BY_POSITION, REPLACE_BY and COMMANDER. 'MONARCH' is an example of this code.

## Position tokens

These tokens belong in an entity definition, applying to a position (such as monarch) and should follow the \[POSITION:POSITION_NAME\] token.

Token
Arguments
Description

 ACCOUNT_EXEMPT

The position holder is not subjected to the economy. Less than relevant right now.

 ALLOWED_CLASS
[CREATURE_CLASS] token
ALLOWED_CLASS: Only creatures with the specified [CREATURE_CLASS] token may be appointed to this position. Multiple entries are allowed. / ALLOWED_CREATURE: Restricts the position to the specified creature and caste. Multiple entries are allowed. / These tokens only apply within the entity’s own race (including its castes). / In world generation, they limit which units may be assigned to the position, but they do not prevent other creature types from acquiring the position through alternative means (for example, via a coup). In fortress mode, these tokens are enforced during manual appointment and succession. During world generation, if all allowed castes have a POP_RATIO of 0, a unit of an allowed caste will still be generated to fill the position.

 ALLOWED_CREATURE
CREATURE:CASTE

 APPOINTED_BY
position
This position can only be chosen for the task from the nobles screen, and is available only if there is an *argument* present. For example, the GENERAL is [APPOINTED_BY:MONARCH]. Contrast [ELECTED]. Being appointed by a MONARCH seems to handle a lot of worldgen stuff, and interferes with fort mode titles. Multiple entries are allowed. If you have neither an ELECTED-token nor a APPOINTED_BY-token, the holder may always be changed (like the expedition leader). / Read more: / Advanced_Entity_Position_Mechanics#Appointment

 BRAG_ON_KILL

A creature that kills a member of this position will be sure to talk/brag about it a lot.

 CHAT_WORTHY

In adventure mode, when referencing locations, an NPC may mention this position holder living there or having done some deed there; it also means that the position exists in world-gen, rather than being created only at the end of world-gen.

 COLOR
Color
Creatures of this position will have this color, instead of their profession color, e.g. [COLOR:5:0:1]. It is also applied to the name of the citizen in the units screen.

 COMMANDER
position:ALL
This position will act as a commander of the specified position / [ / Verify / ] / . E.g. GENERAL is [COMMANDER:LIEUTENANT:ALL]. Unknown if values other than ALL work. Multiple entries are allowed. / Read more: / Army

 CONQUERED_SITE

This position is a puppet ruler, left behind at a conquered site.

 DEMAND_MAX
number (0-100)
How many demands the position can make of the population at one time.

 DESCRIPTION
string. Readable up to 470 characters in the nobles' screen.
description of this position in the nobles screen.

 DETERMINES_COIN_DESIGN

The site's (or civ's) minted coins, if any, will have images that reflect the personality of this position holder.

 DO_NOT_CULL

The position won't be culled from Legends as "unimportant" during world generation.

 DUTY_BOUND

Members of this position will never agree to 'join' your character during adventure mode. They also don't settle anywhere else but in the capital, and will not emigrate from their site. If they are not DUTY_BOUND, they will live anywhere as they like.

 ELECTED

The population will periodically select the most skill-eligible creature to fill this position for site-level positions at the player's fort. For responsibilities or positions that use more than one skill, no skill takes priority in electing a creature: an accomplished comedian is more qualified for the TRADE responsibility than a skilled appraiser. A creature may be elected to multiple positions at the same time. Contrast [APPOINTED_BY]. / More info: / Elections / Read more: / Advanced_Entity_Position_Mechanics#Elections

 EXECUTION_SKILL
weapon skill
A mandatory sub-tag of [RESPONSIBILITY:EXECUTIONS]. Determines the weapon chosen by the executioner for their work.

 EXPORTED_IN_LEGENDS

The various members who have filled this role will be listed in the civilisation's history.

 FLASHES

The creature holding this position will visibly flash, like legendary citizens. Represents a properly noble station by default.

 GENDER
male/female
The position can only be held by the specified gender. Currently bugged Bug:2714

 KILL_QUEST

The position can assign quests to adventurers.

 LAND_HOLDER
importance tier (1-10)
This is an alternative to SITE, allowing positions to be created at civ-level 'as needed' for all sites that meet the requirements to have them, which are the values set in / land holder difficulty / settings / . The character is tied permanently to a particular site, but also operates at the civ-level. / Read more: / Advanced_Entity_Position_Mechanics#land holders

 LAND_NAME
string. Readable up to 21 characters in the nobles' screen.
The name the area takes on when under the control of a LAND_HOLDER. E.g. for the DUKE, [LAND_NAME:a duchy]. If the position is not a LAND_HOLDER, the land_name is still displayed left of the position in the nobles menu.

 MANDATE_MAX
number (0-100)
The maximum number of mandates the position can make at once.

 MENIAL_WORK_EXEMPTION

The position holder cannot be assigned labors. It only works for [SITE]-positions.

 MENIAL_WORK_EXEMPTION_SPOUSE

The spouse of the position holder doesn't have to work, either - see above.

 MILITARY_SCREEN_ONLY

This position cannot be appointed from the nobles screen. Intended for militia captains and other squad leaders to reduce clutter. Currently nonfunctionalBug:8965

 NAME
singular:plural. Readable up to 21 characters in the nobles' screen and up to 30 in the unit list.
The name of the position.

 NAME_MALE
singular:plural. Readable up to 21 characters in the nobles' screen and up to 30 in the unit list.
If the creature holding the position is male, this is the position's name. E.g. for MONARCH, [NAME_MALE:king:kings]

 NAME_FEMALE
singular:plural. Readable up to 21 characters in the nobles' screen and up to 30 in the unit list.
If the creature holding the position is female, this is the position's name. E.g. for MONARCH, [NAME_FEMALE:queen:queens]

 NUMBER
number / AS_NEEDED
How many of the position there should be. If the [SITE] token exists, this is per site, otherwise this is per civilisation. AS_NEEDED applies mainly to positions involved with the military command chain; this is used to allow armies to expand to whatever size they need to be. Other non-military positions like the land_holders or the / messenger / with NUMBER:AS_NEEDED will also be appointed. / The problem with / Lieutenants / and / Captains / not being created, is their AS_NEEDED number. They are only then created when they're needed, and that has some pretty unusual conditions. When a fixed number is used, they are appointed with the creation of the civ. If the NUMBER is set at a fixed value higher than 1, the position is always filled up full. If the position is available on embark, it is completely filled up with only the first dwarf.

 PRECEDENCE
number (0-30000)/NONE
How important the position is in society; a lower number is more important and displayed higher in the Nobles menu. For MONARCH it's 1, for MILITIA_CAPTAIN it's 200. / The game marks the first non-[SITE] position with [PRECEDENCE:1] as the ruler, for both embark screen and mountainhome purposes. When it is empty, [REPLACED_BY] another position, or not yet created because of [REQUIRES_POPULATION], the screen just says 'None' as the holders' name. / Landholders can become the ruler, if they are the first defined position with precedence of 1. civ-position can also be created without precedence. Positions may have the same precedence and will be appointed, although the effect is unknown. Precedence has no effect on who's doing the job, if both positions have the same responsibilities.

 PUNISHMENT_EXEMPTION

The position holder will not be held accountable for his or her crimes. Currently nonfunctional.Bug:4589[Verify]

 QUEST_GIVER

The position holder can give quests in Adventure mode. Functionality in 0.31.13 and later is uncertain.

 REJECTED_CLASS
CREATURE_CLASS Token
Creatures of the specified class cannot be appointed to this position. Multiple entries are allowed

 REJECTED_CREATURE
CREATURE:CASTE
Restricts position holders by CREATURE type. Multiple entries are allowed. It doesn't seem to work in world-gen. When checking Legends mode, units are seen assigned this position regardless of their creature-type or caste. It does work in Fortress mode.

 REPLACED_BY
position
This position is absorbed by another down the line. For example, expedition leader is [REPLACED_BY:MAYOR]. Only a single entry is allowed. / It can work with both [REQUIRES_POPULATION] and [REQUIRES_MARKET]. / The tag differs in function for landholders, see / Advanced_entity_position_mechanics

 REQUIRED_BEDROOM
number (0-1000000)
The position holder requires a bedroom with at least this value.

 REQUIRED_BOXES
number (0-100)
The position holder requires at least this many boxes.

 REQUIRED_CABINETS
number (0-100)
The position holder requires at least this many cabinets.

 REQUIRED_DINING
number (0-1000000)
The position holder requires a dining room with at least this value.

 REQUIRED_OFFICE
number (0-1000000)
The position holder requires an office with at least this value.

 REQUIRED_RACKS
number (0-100)
The position holder requires at least this many weapon racks.

 REQUIRED_STANDS
number (0-100)
The position holder requires at least this many armour stands.

 REQUIRED_TOMB
number (0-1000000)
The position holder requires a tomb with at least this value.

 REQUIRES_MARKET

Does not have anything directly to do with trade depots. It means that in minor sites (such as hillocks) the position will not appear, while in major sites (such as dwarf fortresses) it will. Depending on its economical position in the region, a hamlet may build a market and develop into a Town eventually. That is when this position becomes available. It only works in combination with the [SITE]-token.

 REQUIRES_POPULATION
number
The position requires the population to be at least this number before it becomes available, or before the position holder will move in.

 RESPONSIBILITY
responsibility
The position holder does something - see the Responsibilities table below for suitable arguments. A position does not need to have a responsibility.

 RULES_FROM_LOCATION

If there is a special location set aside for rulers, such as a human castle/mead hall, the position holder will always be found at that particular location. Does nothing for dwarven nobles, because at present, dwarves have no such special locations.

 SITE

Every site government will have the defined number of this position instead of the whole civilization; provided that other criteria (if any) are met. Unless LAND_HOLDER is present instead, the defined number of the position will be created only for the civilization as a whole.

 SLEEP_PRETENSION

The position holder will get upset if someone with a higher PRECEDENCE holds quarters with a greater value than their own.

 SPECIAL_BURIAL

The civilization will inter the corpse of the position holder in a special grave, either in catacombs or in monuments. If that grave is disturbed, the position holder can return as a mummy.[Verify]

 SPOUSE
singular:plural. Readable up to 30 characters in the unit list.
The name of the position holder's spouse.

 SPOUSE_FEMALE
singular:plural. Readable up to 30 characters in the unit list.
If the spouse of the creature holding the position is female, this is the spouse's position name.

 SPOUSE_MALE
singular:plural. Readable up to 30 characters in the unit list.
If the spouse of the creature holding the position is male, this is the spouse's position name.

 SQUAD
number:singular:plural
The position holder is authorized to form a military squad, led by themselves using the leader and military tactics skills. The number denotes the maximum headcount. The noun used to describe the subordinates (e.g. royal guard) is used in adventure mode for the adventurer. This token is used together with [RESPONSIBILITY:LAW_ENFORCEMENT] for giving quests to adventurers as hearthpeople. Further details: Advanced_entity_position_mechanics#Military

 SUCCESSION
BY_HEIR / BY_POSITION:position
How a new position holder is chosen. A single position can have multiple BY_POSITION tokens. See / Noble / for more information on how succession is handled in the game. / The SUCCESSION-Tag is also considered when a new positions opens up, for example when a required population number is reached. If a valid successor is available, they will be the one taking that position initially, without appointment or election.

## Responsibilities

|  |  |  |
|----|----|----|
| Argument | Description |  |
|  ACCOUNTING | Found on bookkeeper. The position will use the record keeper skill to keep track of stocks. |  |
|  ADVISE_LEADERS |  |  |
|  ATTACK_ENEMIES | Found on elven ranger captain and human warrior. Effect unknown.\[Verify\] |  |
|  BUILD_MORALE | Found on champion. Citizens get a special thought for "talking to a pillar of society" when speaking to this noble. |  |
|  BUILDING_SAFETY |  |  |
|  COLLECT_TAXES | Currently unused - was originally assigned to the tax collector. |  |
|  CONSTRUCTION_PERMITS |  |  |
|  DELIVER_MESSAGES | Found on messenger. The position travels to other sites and uses social skills. |  |
|  EQUIPMENT_MANIFESTS | Currently unused - was originally assigned to the arsenal dwarf. |  |
|  ESCORT_TAX_COLLECTOR | Currently unused - was originally assigned to the Royal Guards (squad members beneath the Hammerer). |  |
|  ESPIONAGE | Found on dungeon master and the elven princess and uses the schemer skill. |  |
|  ESTABLISH_COLONY_TRADE_AGREEMENTS | Found on outpost liaison. Position travels with the caravan and uses social skills to make trade agreements with any settlements that it visits, provided they are domestic, report the news and promote [`[LAND_HOLDER]`](/index.php/Entity_token#LAND_HOLDER "Entity token") positions. Also reports recent news. Presumably has no effect at site level. Crucially, it does not visit foreign settlements, but the civ-level TRADE position does the exact same thing in its position. They arrive the same time as the caravan arrives, and this can thus be modded by setting [`[ACTIVE_SEASON]`](/index.php/Entity_token#ACTIVE_SEASON "Entity token") |  |
|  EXECUTIONS | Found on hammerer. Position executes death penalty judgements with a weapon of the appropriate skill. Cannot be combined with LAW_ENFORCEMENT, resulting in the "Invalid Officer"-error. |  |
|  FIRE_SAFETY |  |  |
|  FOOD_SUPPLY |  |  |
|  HEALTH_MANAGEMENT | Found on chief medical dwarf. Position will use diagnostician skill to evaluate wounds and schedule treatment, reported in each citizen's Health tab. |  |
|  JUDGE |  |  |
|  LAW_ENFORCEMENT | Found on sheriff/captain of the guard. Position and its subordinates are in charge of punishing criminals. A [`[SITE]`](/index.php/Position_token#SITE "Position token") position holding this responsibility plus the [`[SQUAD]`](/index.php/Position_token#SQUAD "Position token") token (or allowing the entity to have a [`[SITE_VARIABLE_POSITIONS]`](/index.php/Entity_token#SITE_VARIABLE_POSITIONS "Entity token") with this responsibility) is required for an adventurer from a given civilization to start as a hearthperson, fortress guard, etc. Cannot be combined with EXECUTIONS, resulting in the "Invalid Officer"-error. |  |
|  LAW_MAKING | Found on monarchs and nobles. Will be referred to as the leader of the site in adventure mode and they may designate the site as being the capital city for civ-level positions. This position is in charge of creating procedural positions, corresponding to either [`[VARIABLE_POSITIONS]`](/index.php/Entity_token#VARIABLE_POSITIONS "Entity token") or [`[SITE_VARIABLE_POSITIONS]`](/index.php/Entity_token#SITE_VARIABLE_POSITIONS "Entity token"). Position-holders that have attained immortality may issue oppressive edicts to protect themselves against suspicion. |  |
|  MAINTAIN_BRIDGES |  |  |
|  MAINTAIN_ROADS |  |  |
|  MAINTAIN_SEWERS |  |  |
|  MAINTAIN_TUNNELS |  |  |
|  MAKE_INTRODUCTIONS | Position will make a 'social call' to an established foreign settlement, complimenting or insulting them depending on relations and reporting the news. |  |
|  MAKE_PEACE_AGREEMENTS | Found on diplomat. Position negotiates peace treaties in order to end wars. |  |
|  MAKE_TOPIC_AGREEMENTS | Found on diplomat. Position negotiates special agreements, such as tree cutting quotas. Used when elevating a settlement in the [`[LAND_HOLDER]`](/index.php/Position_token#LAND_HOLDER "Position token") chain up from level 1. |  |
|  MANAGE_ANIMALS | Found on dungeon master. |  |
|  MANAGE_LEADER_HOUSEHOLD_CLEANLINESS |  |  |
|  MANAGE_LEADER_HOUSEHOLD_DRINKS |  |  |
|  MANAGE_LEADER_HOUSEHOLD_FOOD |  |  |
|  MANAGE_PRODUCTION | Found on manager. Position enables the use of workshop profiles and uses the organizer skill to process work orders entered in the job manager after the fortress population reaches 20. |  |
|  MEET_WORKERS | Found on expedition leader/mayor. Position uses the various social skills to hold meetings with unhappy citizens and try to pacify them with happy thoughts. In adventure mode, \[SITE\] positions with this responsibility handle petitions to make the player a performer for the local government. |  |
|  MILITARY_GOALS | Found on monarch/landholder/leaders. Character is in charge of going to war and making peace for the government they work for. Without a position with this responsibility at civ level the civilization will not be able to make peace and its sites will wage war on each other constantly, and as a result, all viable civilizations must have one leader with this tag at civ level. This appears not to be a problem for kobolds, presumably due to the [`[SKULKING]`](/index.php/Entity_token#SKULKING "Entity token"). If no position has this responsibility in fortress mode, players are unable to start missions. |  |
|  MILITARY_STRATEGY | Found on general/militia commander. Means that they will command the armies of their site or civilization. Issues the orders for the teams conducting raids or other operations away from the fortress. During worldgen, positions (of a civilization) will go on expeditions to tame exotic creatures (but this only yields a pet, not any training knowledge, and only of a race for which the civilization has already some training knowledge). Counterintuitively not by the TAME_EXOTICS-position. The destinations of these expeditions are determined by the entities USE\_(...)\_ANIMALS-tokens. |  |
|  OVERSEE_LEADER_HOUSEHOLD |  |  |
|  PATROL_TERRITORY | Found on elven ranger captain. Effect unknown.\[Verify\] |  |
|  PREPARE_LEADER_MEALS |  |  |
|  RECEIVE_DIPLOMATS | Found on monarch/landholder/leaders. Position uses the various social skills to hold meetings with incoming diplomats and liaisons. |  |
|  RELIGION | Found on elven druid and uses social skills. Position informs you about worship cults\[Verify\] |  |
|  SORT_AMMUNITION | Currently unused - was originally assigned to the arsenal dwarf. |  |
|  TAME_EXOTICS | Position will tame animals with the [`[PET_EXOTIC]`](/index.php/Creature_token#PET_EXOTIC "Creature token") token. Currently unused - was originally assigned to the dungeon master. Expeditions to tame exotic creatures will be done by the MILITARY_STRATEGY-position |  |
|  TRADE | Found on broker. Position will use Appraisal skill to display value estimates and the various Social skills to trade at the depot. When applied to other civilizations, this position will arrive with the caravan to make trade agreements (like the Human Guild Representative from older versions) and behaves otherwise like the civ's own ESTABLISH_COLONY_TRADE_AGREEMENTS position holder. They arrive the same time as the caravan arrive and this can thus be modded by setting [`[ACTIVE_SEASON]`](/index.php/Entity_token#ACTIVE_SEASON "Entity token") |  |
|  UPGRADE_SQUAD_EQUIPMENT | Currently unused - was originally assigned to the arsenal dwarf. |  |

## Related tokens

The following two entity tokens are not actually position tokens, but bear mentioning on this page because they can modify the way that a civilization's positions behave:

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
| [`[VARIABLE_POSITIONS]`](/index.php/Entity_token#VARIABLE_POSITIONS "Entity token") | Position responsibility or ALL | Allows a responsibility to be taken up by a dynamically generated position (such as Law-maker). |
| [`[SITE_VARIABLE_POSITIONS]`](/index.php/Entity_token#SITE_VARIABLE_POSITIONS "Entity token") | Position responsibility or ALL | Allows a responsibility to be taken up by a dynamically generated position (such as Law-maker). |

## Why won't my positions appear?

The way DF determines what positions will actually *appear* in your fortress is somewhat counter-intuitive and fairly limiting. This guide should help you understand what you can do to actually get your positions working properly.

There are five tokens governing which positions appear in your fortress - LAND_HOLDER, REQUIRES_POPULATION, APPOINTED_BY, ELECTED, and REPLACED_BY. The first two determine when your fortress is eligible for a new position, the next two determine how a new position for which your fortress is eligible can be added, and the fifth allows you to clear up obsolete positions. Unfortunately, they also interact in some strange ways that makes creating interesting position structures difficult.

When you start a new fortress, DF compiles a list of your initial positions. To do this, it looks at the requirements for each position - any position whose only requirement is less than seven dwarves (either because they have no requirement tokens, or because their only requirement tokens are \[REQUIRES_POPULATION: =\< 7\] or \[LAND_HOLDER:some trigger whose only requirement is some number of dwarves equal to or less than 7\]). Most importantly, *any* position whose only requirement is a LAND_HOLDER requirement, regardless of what the trigger for that requirement is, will be added if another eligible starting position is REPLACED_BY it. **A non-LAND_HOLDER position that is REPLACED_BY a LAND_HOLDER position will never appear.** With this list compiled, the game culls all positions that are REPLACED_BY another eligible position, and then culls all positions that have the APPOINTED_BY token. **You may not embark with any appointed positions.** Any remaining positions are then filled by a dwarf chosen at random.

**Positions do not automatically appear when you reach their requirements.** For example, if you remove the ELECTED token from the Mayor, then the Mayor will never appear, even once you reach their required number of dwarves. **For a position that does not appear at embark to appear in your fortress, it must be APPOINTED_BY another position or ELECTED.**

Naturally, this is more complicated than it looks. **APPOINTED_BY positions must be appointed by another position already in your fortress, or a civ-level position. Only LAND_HOLDER positions may be appointed by civ-level positions.** LAND_HOLDER positions that are APPOINTED_BY civ-level positions are inherently tied to civ-level tokens with the ESTABLISH_COLONY_TRADE_AGREEMENTS responsibility. If a fortress meets the LAND_HOLDER_TRIGGER for a new LAND_HOLDER tier when a caravan leaves, then the next time the outpost liaison or equivalent arrives, they will offer to make you an official colony, which will allow you to select all positions for that LAND_HOLDER level. **Each time they appear, the outpost liaison will only promote your fortress one tier up the LAND_HOLDER track.** The biggest problem with this system is that you may set your LAND_HOLDER_TRIGGERS such that you are eligible for the first tier of LAND_HOLDER positions at embark. **If you are eligible for the first tier of LAND_HOLDER positions at embark, then all first-tier positions will appear twice - once at embark, and again when the outpost liaison comes to appoint you to the first tier.**

If civ-positions are neither APPOINTED_BY nor ELECTED, they still will be filled.

Read more: Advanced Entity Position Mechanics
