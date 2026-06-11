# Interaction token

> Fonte: [Interaction token](https://dwarffortresswiki.org/index.php/Interaction_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

The following tokens can be used to define and use interactions. (*It appears that, at least in order to make the big list make a little more sense, some examples of those may be necessary.*)

## Definitions

|  |  |  |  |
|----|----|----|----|
| Token | Context | Arguments | Description |
|  INTERACTION | Global | ID | Used to start defining a new interaction. The term "interaction ID" refers to the text specified within this token; this is used to make reference to the interaction in various other places. |
|  EXPERIMENT_ONLY | Global |  | Disallows use of the interaction in play, but if the interaction animates or resurrects corpses, or has an I_SOURCE:EXPERIMENT tag, it can be used in worldgen. Animation and resurrection interactions do not need I_SOURCE:EXPERIMENT to work in worldgen. |
|  I_SOURCE | Global | type | Defines what things are capable of triggering this interaction - multiple sources may be specified. Valid values: / CREATURE_ACTION / - Specifies that the interaction may be used in conjunction with / \[CAN_DO_INTERACTION\] / and / \[CE_CAN_DO_INTERACTION\] / , but it isn't actually necessary for this. It might exist simply to allow for the inclusion of IS\_ tokens (detailed below) to be applied when the interaction is used in this context. / ATTACK / - Allows the interaction to be used in conjunction with / \[SPECIALATTACK_INTERACTION\] / and / \[CE_SPECIAL_ATTACK_INTERACTION\] / . / INGESTION / - Allows the interaction to be used in conjunction with / \[CE_BODY_MAT_INTERACTION\] / . / DEITY / - Allows the interaction to be inflicted upon mortals by the gods, for reasons dictated by / \[IS_USAGE_HINT\] / . / SECRET / - Allows the interaction to act as a secret which can be learnt and passed on to others, as specified via / \[IS_SECRET\] / . Appropriate / interaction effects / with a / creature target / will be applied to individuals who learn the secret. It is possible to set restrictions on who may learn the secret by using creature target tokens as described below. Also see / \[IS_SECRET_GOAL\] / and / \[IS_SPHERE\] / . / REGION / - Allows the interaction to take place spontaneously in regions specified using / \[IS_REGION\] / . Also see / \[IS_FREQUENCY\] / and / \[IE_INTERMITTENT\] / . / DISTURBANCE / - Allows the interaction to take place spontaneously in disturbed / tombs / ; generated interactions with this token are used to create / mummies / . / UNDERGROUND_SPECIAL / - Allows the interaction to take place spontaneously in / curious underground structures / (which no longer generate); generated interactions with this token used to be used to produce / zombies / when creating the structure's inhabitants. / EXPERIMENT / - This can be used by NIGHT_CREATURE_EXPERIMENTERs while "performing horrible experiments" in worldgen. Only seems relevant for interactions that target living creatures. Note that all NIGHT_CREATURE_EXPERIMENTERs have access to generated experiments, and due to the large number of generated experiments available custom experiment interactions will tend to show up very rarely. / MYTHICAL / - Presumably used to upgrade creatures guarding a / mysterious dungeon / . / ITEM_POWER / - Granted by a ◄ / magic / item►. Currently can only be found on / remnant weapons / , which chooses a random interaction with this source. |
|  IS_HIST_STRING_1 | Within I_SOURCE | text | Describes what the interaction did to a historical figure; this is displayed in legends mode following the name of the historical figure who performed the interaction and preceding the name of the targeted historical figure (or, in the case of / \[I_SOURCE:INGESTION\] / , the historical figure from whom the consumed material was extracted). / \[IS_HIST_STRING_1: cursed\] |
|  IS_HIST_STRING_2 | Within I_SOURCE | text | Describes what the interaction did to a historical figure; this is displayed in legends mode after the name of the historical figure who was targeted by the interaction. In the case of / \[I_SOURCE:INGESTION\] / , it is displayed after the name of the historical figure from whom the consumed material was extracted. / \[IS_HIST_STRING_2: to assume the form of a lizard-like monster every full moon\] |
|  IS_TRIGGER_STRING | Within I_SOURCE | text | Displayed as an announcement when the interaction is carried out during play. The text follows the name of the target unit, and is preceded by / IS_TRIGGER_STRING_SECOND / or / IS_TRIGGER_STRING_THIRD / . May be limited to / \[I_SOURCE:DEITY\] / and / \[I_SOURCE:EXPERIMENT\] / interactions at present; this still needs to be tested. / \[IS_TRIGGER_STRING: been infected with a contagious ghoulish condition\] |
|  IS_TRIGGER_STRING_SECOND | Within I_SOURCE | text | Presented before the / IS_TRIGGER_STRING / when describing the event in the second person. / \[IS_TRIGGER_STRING_SECOND: have\] |
|  IS_TRIGGER_STRING_THIRD | Within I_SOURCE | text | Presented before the / IS_TRIGGER_STRING / when describing the event in the third person. / \[IS_TRIGGER_STRING_THIRD: has\] |
|  IS_NAME | Within I_SOURCE | string | Generally used with / \[I_SOURCE:SECRET\] / interactions to describe what the secret is about (though it may be used to name any I_SOURCE). This name is engraved onto the appropriate secret-containing slabs from worldgen, and is used in legends mode when describing the secret being learnt by historical figures. / \[IS_NAME:the secrets of life and death\] |
|  IS_SPHERE | Within I_SOURCE:SECRET | sphere | Indicates the sphere to which this secret pertains. Only one sphere can be defined for each \[I_SOURCE:SECRET\] token, so several \[I_SOURCE:SECRET\] tokens are required to make a secret belong to multiple spheres. |
|  IS_SECRET_GOAL | Within I_SOURCE:SECRET | Secret Goal token | Indicates why somebody would want to learn the secret. Valid values: / STAY_ALIVE / MAINTAIN_ENTITY_STATUS / START_A_FAMILY / RULE_THE_WORLD / CREATE_A_GREAT_WORK_OF_ART / CRAFT_A_MASTERWORK / BRING_PEACE_TO_THE_WORLD / BECOME_A_LEGENDARY_WARRIOR / MASTER_A_SKILL / FALL_IN_LOVE / SEE_THE_GREAT_NATURAL_SITES / IMMORTALITY / MAKE_A_GREAT_DISCOVERY / ATTAIN_RANK_IN_SOCIETY / BATHE_WORLD_IN_CHAOS / However, currently only IMMORTALITY will result in a secret being pursued during worldgen. |
|  IS_SECRET | Within I_SOURCE:SECRET | Secret Flag | Indicates how the secret can be learned. Valid values: / SUPERNATURAL_LEARNING_POSSIBLE / - gods may gift the secret to their worshippers. Secrets with / \[IS_SPHERE\] / specified may only be granted by gods who have at least one matching sphere. / MUNDANE_RESEARCH_POSSIBLE / - the secret can be researched by mundane means. This doesn't do anything at present. / \[1\] / . / MUNDANE_TEACHING_POSSIBLE / - the secret can be taught to apprentices / MUNDANE_RECORDING_POSSIBLE:TITLE_SET:NAME_SET / - the secret can be written in books whose title and name are taken from the specified text sets. If this tag is present, a slab will be created upon learning the secret by supernatural means. |
|  IS_USAGE_HINT | Within I_SOURCE:DEITY | Usage Hint token | Indicates why a deity would choose to perform this interaction. See CDI:USAGE_HINT below for valid values - in this context, **MINOR_BLESSING**, **MEDIUM_BLESSING**, **MINOR_CURSE**, **MEDIUM_CURSE**, and **MAJOR_CURSE** are the only values that make sense. |
|  IS_REGION | Within I_SOURCE:REGION | Region type | Indicates what types of regions are capable of performing this interaction. This token may be specified several times per I_SOURCE to permit multiple terrain / alignment types. Valid values: / ANY / permits the interaction to occur in all regions, regardless of terrain or alignment / Terrain / : / DESERT / FOREST / GLACIER / GRASSLAND / HILLS / LAKE / MOUNTAINS / OCEAN / SWAMP / TUNDRA / ANY_TERRAIN / permits the interaction to occur in all regions which meet alignment specifications / Alignment / : / NORMAL_ALLOWED / EVIL_ALLOWED / GOOD_ALLOWED / SAVAGE_ALLOWED / EVIL_ONLY / GOOD_ONLY / SAVAGE_ONLY |
|  IS_FREQUENCY | Within I_SOURCE | Probability | When used with / \[I_SOURCE:REGION\] / , determines how likely it is for the region(s) specified via / \[IS_REGION\] / to possess this interaction. / Note: it appears that regions aren't allowed to possess more than a single regional interaction at present. |
|  IS_POWER_LEVEL | Within I_SOURCE:MYTHICAL | 1-3 | Corresponds to the three tiers of mysterious dungeon. |
|  IS_DESCRIPTION | Within I_SOURCE:ITEM_POWER | string | Adds the given string to the affected item's description. |
|  IS_CDI | Within I_SOURCE:ITEM_POWER | CDI token | Details the interaction that the item grants. Comparable to [`[CAN_DO_INTERACTION]`](/index.php/Creature_token#CAN_DO_INTERACTION "Creature token"). |
|  I_TARGET | Global | ID, type | Defines the targets available for subsequent use with / \[I_EFFECT\] / tokens. Multiple targets may be specified; the precise target(s) used with each interaction effect are indicated via their ID (see / \[IE_TARGET\] / ). Valid values: / CORPSE / - The target is a / CORPSE / or / CORPSEPIECE / item. / CREATURE / - The target is a / unit / . / MATERIAL / - This is a valid target for use in / \[I_EFFECT:MATERIAL_EMISSION\] / interaction effects, and is used to set the material or flow type of the emission. This information, in turn, is either obtained from an / \[IT_MATERIAL\] / token or by using / \[IT_LOCATION:CONTEXT_MATERIAL\] / . Using the latter implies that the precise emission info will be provided when defining / how an interaction user can use the interaction in question via CDI tokens / , enabling one to create 'template' material emission interactions such as the MATERIAL_EMISSION and MATERIAL_EMISSION_WITH_HIDE interactions included in the vanilla raws. / LOCATION / - The target is a / local map tile / . If used with / \[IT_LOCATION:CONTEXT_CREATURE_OR_LOCATION\] / , creatures at the target tile are also valid targets. |
|  IT_LOCATION | Within I_TARGET | Location | This is often included after / \[I_TARGET\] / token to add more detail about the target. Valid values: / CONTEXT_CREATURE / - Used with CREATURE to target the whole unit. / CONTEXT_BP / - Used with CREATURE to target the body part specified in / \[CDI:BP_REQUIRED\] / . / CONTEXT_LOCATION / - Used with LOCATION to target only a tile. / CONTEXT_CREATURE_OR_LOCATION / - Used with LOCATION to allow for targetting of both creatures and tiles. / CONTEXT_ITEM / - Used with CORPSE. / CONTEXT_REGION / - Can only be used by / \[I_SOURCE:REGION\] / interactions. / CONTEXT_MATERIAL / - Used with MATERIAL if you want an / \[I_EFFECT:MATERIAL_EMISSION\] / to obtain the emission material / flow type from / \[CDI:MATERIAL\] / or / \[CDI:FLOW\] / . / RANDOM_NEARBY_LOCATION / - Used with LOCATION. Targets a location from somewhere random within a number of squares from another LOCATION target specified by its target ID. For example, \[I_TARGET:B:LOCATION\] with \[IT_LOCATION:RANDOM_NEARBY_LOCATION:A:5\] will randomly select a tile lying somewhere within a radius of 5 tiles from \[I_TARGET:A:LOCATION\]. A walkable path between the two locations must exist. |
|  IT_MANUAL_INPUT | Within I_TARGET | text | Tells the adventure mode player what they should be selecting. If not specified, the player will only be able to target themselves. |
|  IT_AFFECTED_CREATURE | Within I_TARGET:CORPSE or I_TARGET:CREATURE | CREATURE:CASTE | Specifies specific creatures the interaction can target. |
|  IT_AFFECTED_CLASS | Within I_TARGET:CORPSE or I_TARGET:CREATURE | Creature class | Specifies creature classes the interaction can target. |
|  IT_IMMUNE_CREATURE | Within I_TARGET:CORPSE or I_TARGET:CREATURE | CREATURE:CASTE | Specifies specific creatures the interaction cannot target. |
|  IT_IMMUNE_CLASS | Within I_TARGET:CORPSE or I_TARGET:CREATURE | Creature class | Specifies creature classes the interaction cannot target. |
|  IT_REQUIRES | Within I_TARGET:CORPSE or I_TARGET:CREATURE | Creature token or property | Indicates that the target must have the specified property. Valid values: / FIT_FOR_ANIMATION / - Any corpse or body part that can become a zombie (heads, hands, etc.) / FIT_FOR_RESURRECTION / - The target corpse's UPPERBODY must be attached. / HAS_BLOOD / MORTAL / NO_AGING / STERILE / Creature token: / BLOODSUCKER, CAN_LEARN, CAN_SPEAK, CRAZED, EXTRAVISION, MISCHIEVOUS / (or / MISCHIEVIOUS / ), / NO_CONNECTIONS_FOR_MOVEMENT, NO_DIZZINESS, NO_DRINK, NO_EAT, NO_FEVERS, NO_PHYS_ATT_GAIN, NO_PHYS_ATT_RUST, NO_SLEEP, NO_THOUGHT_CENTER_FOR_MOVEMENT, NOBREATHE, NOEMOTION, NOEXERT, NOFEAR, NONAUSEA, NOPAIN, NOSTUN, NOT_LIVING, NOTHOUGHT, OPPOSED_TO_LIFE, PARALYZEIMMUNE, SUPERNATURAL, TRANCES, UTTERANCES |
|  IT_FORBIDDEN | Within I_TARGET:CORPSE or I_TARGET:CREATURE | Creature token or property | Indicates that the target must not have the specified property. Valid values are the same as for IT_REQUIRES. |
|  IT_CANNOT_TARGET_IF_ALREADY_AFFECTED | Within I_TARGET:CORPSE or I_TARGET:CREATURE |  | Prevents the interaction from targeting a creature that's already under the effect of the same interaction. |
|  IT_CANNOT_HAVE_SYNDROME_CLASS | Within I_TARGET:CORPSE or I_TARGET:CREATURE | Syndrome class | Prevents the interaction from targeting a creature under the effects of a syndrome having the specified SYN_CLASS value. |
|  IT_MATERIAL | Within I_TARGET:MATERIAL | type | Specifies the type of material the interaction targets; currently only used for / MATERIAL_EMISSION / interaction effects. See / Breath Attack Types / . Valid values: / FLOW / :Breath attack token - The emission will consist of the specified special flow type. / MATERIAL / : / Material token / :Breath attack token - The emission will consist of the specified material dispersed in the specified manner. / CONTEXT_MATERIAL / - Indicates the emission details should be obtained from / \[CDI:MATERIAL\] / or / \[CDI:FLOW\] / . |
|  I_EFFECT | Global | type | Specifies what the interaction does to the targets. Multiple \[I_EFFECT\]s may be specified in a single interaction, and the same type may be used more than once. Valid values: / ADD_SYNDROME / - Adds one or more syndromes to a valid creature target. You must specify the syndrome details just below this interaction effect using the / \[SYNDROME\] / tag followed by the relevant syndrome tokens. See / here / for more information. / ANIMATE / - Raises the target corpse / bodypart as an / undead / unit. The zombie will always be hostile to life and will retain no information about its original personality / loyalties. Syndromes can also be specified within this tag. If a regional interaction contains this effect, affected regions will have undead wildlife. / RESURRECT / - Takes a target corpse and returns the creature to life. This can be used on parts that are not FIT_FOR_RESURRECTION, but only the main part (with an UPPERBODY attached) will remain loyal to its original faction. Syndromes can also be specified within this tag. / CLEAN / - Removes / contaminants / from a valid creature target. See / \[IE_GRIME_LEVEL\] / and / \[IE_SYNDROME_TAG\] / . / CONTACT / - Causes the creatures to touch. / MATERIAL_EMISSION / - Causes a particular material to be emitted. Used by / evil weather / and the MATERIAL_EMISSION interaction. / HIDE / - Allows the creature to / hide / even if another creature can see it. / CREATE_ITEM / - Creates an item as described by / \[IE_ITEM\] / and / \[IE_ITEM_QUALITY\] / . / CHANGE_ITEM_QUALITY / - Alters an item's quality level as indicated by either / \[IE_CHANGE_QUALITY\] / or / \[IE_SET_QUALITY\] / . When targeting a unit, all items equipped by that unit will be affected. / SUMMON_UNIT / - Creates a new unit at the target. The type of unit can either be specified using the / \[CREATURE\] / token, or made to be randomly selected as indicated by a variety of flag-based tokens: / \[IE_CREATURE_FLAG\] / , / \[IE_FORBIDDEN_CREATURE_FLAG\] / , / \[IE_CREATURE_CASTE_FLAG\] / , / \[IE_FORBIDDEN_CREATURE_CASTE_FLAG\] / , / \[IE_HAVE_FAST_EFFORTLESS_GAIT_SPEED\] / and / or / \[IE_ALL_SLOW_EFFORTLESS_GAIT_SPEED\] / . See also / \[IE_TIME_RANGE\] / and / \[IE_MAKE_PET_IF_POSSIBLE\] / . / PROPEL_UNIT / - Applies a force specified using / \[IE_PROPEL_FORCE\] / to a unit to knock it back. / CHANGE_WEATHER / - Changes the weather as specified by / \[IE_ADD_WEATHER\] / and / or / \[IE_REMOVE_WEATHER\] / . / RAISE_GHOST / - Present in version 0.47.01 and accepted as a valid I_EFFECT token, but does not have an effect currently. |
|  IE_ARENA_NAME | Within I_EFFECT | text | Allows the interaction effect to be applied directly to newly spawned creatures in arena mode. The specified name is used to represent it within the creature creation effects list. |
|  IE_TARGET | Within I_EFFECT | ID | Specifies which I_TARGET a particular interaction effect will be applied to. For example, in an interaction with the token \[I_TARGET:B:CREATURE\], 'B' is the ID used to indicate this target option. \[I_EFFECT:ADD_SYNDROME\] followed by \[IE_TARGET:B\] would therefore apply the syndrome to this target. Certain types of interaction effects require multiple IE_TARGET tokens in a specific order to function properly. A few effects do not require a target at all. |
|  IE_INTERMITTENT | Within I_EFFECT | Frequency | Only appears to work with \[I_SOURCE:REGION\] interactions. Indicates that the effect happens intermittently and specifies roughly how often. Regional interactions aren't able to use effects which lack this token. Valid values: / WEEKLY / Note: DAILY, MONTHLY and YEARLY also exist in the string dump but don't appear to work at present. |
|  IE_IMMEDIATE | Within I_EFFECT |  | Indicates that the effect happens immediately. |
|  IE_LOCATION | Within I_EFFECT | Location Hint | Prevents the interaction effect from manifesting unless the target is in a location which meets the specified criteria. / Valid values: / IN_WATER / IN_MAGMA / NO_WATER / NO_MAGMA / NO_THICK_FOG / OUTSIDE / A / depth / of 1 / 7 is sufficient for IN_WATER and IN_MAGMA. / Note: NO_THICK_FOG and OUTSIDE are accepted as valid location hints when specified with IE_LOCATION, but don't appear to work. It's possible that they're currently only implemented for use with / \[CDI:LOCATION_HINT\] / . |
|  IE_ADD_WEATHER | Within I_EFFECT:CHANGE_WEATHER | type | Indicates what type of weather is added. Valid values: / FOG_MIST / FOG_NORMAL / FOG_THICK / FRONT_WARM / FRONT_COLD / FRONT_OCCLUDED / STRATUS_ALTO / STRATUS_PROPER / STRATUS_NIMBUS / CUMULUS_MED / CUMULUS_MULTI / CUMULUS_NIMBUS / CIRRUS |
|  IE_REMOVE_WEATHER | Within I_EFFECT:CHANGE_WEATHER | type | Indicates what type of weather is removed. See above for a list of valid weather types. |
|  IE_GRIME_LEVEL | Within I_EFFECT:CLEAN | amount? | \[IE_GRIME_LEVEL:2\] appears in the default cleaning interaction, and may indicate amount of grime cleaned. |
|  IE_SYNDROME_TAG | Within I_EFFECT:CLEAN | syndrome trigger flag | When a creature cleans off a contaminant which is associated with a syndrome, the syndrome will be contracted if it has a matching trigger flag. This is what enables cats to become slightly inebriated when licking off alcohol. **SYN_INGESTED** appears to be the only syndrome trigger flag that works in this context. |
|  IE_PROPEL_FORCE | Within I_EFFECT:PROPEL_UNIT | amount | Indicates the amount of force that the target will be propelled with. |
|  IE_ITEM | Within I_EFFECT:CREATE_ITEM | ::item token:material token | Defines what item will be created. |
|  IE_ITEM_QUALITY | Within I_EFFECT:CREATE_ITEM | \ OR quality\>:quality\> | Defines what / quality / the created item shall have. Can either be specified in the form of a single, fixed quality (it seems that ARTIFACT can only be used in this manner), or a minimum and maximum level (in which case the quality is selected randomly). Valid values (numerals only except for ARTIFACT): / 0 / = ordinary / 1 / = well-crafted / 2 / = finely crafted / 3 / = superior quality / 4 / = exceptional / 5 / = masterwork / ARTIFACT |
|  IE_SET_QUALITY | Within I_EFFECT:CHANGE_ITEM_QUALITY | quality level | Defines a fixed quality level which the affected item(s) will be set to (decreasing or increasing in quality as necessary). See above for a list of valid quality levels (but note that ARTIFACT cannot be used in this effect). |
|  IE_CHANGE_QUALITY | Within I_EFFECT:CHANGE_ITEM_QUALITY | amount | Determines how much the quality of the item(s) will be changed. For instance, improving a well-crafted -item- (quality level 1) by 2 will turn it into a superior-quality \*item\* (quality level 3). A negative value can be used to decrease quality. Quality cannot be increased beyond level 5 (masterwork) or decreased below level 0 (ordinary). |
|  CREATURE | Within I_EFFECT:SUMMON_UNIT | : | Indicates which specific creature will be created when using this interaction. ANY can be used in place of a specific caste token. Only one \[CREATURE\] may currently be specified per interaction effect. |
|  IE_CREATURE_FLAG | Within I_EFFECT:SUMMON_UNIT | \ | When this token is added to a random creature summoning effect, it narrows down the selection to creatures which have the specified creature flag. This token may be used multiple times per interaction effect; creatures which lack any of the indicated flags will never be summoned. |
|  IE_FORBIDDEN_CREATURE_FLAG | Within I_EFFECT:SUMMON_UNIT | \ | When this token is added to a random creature summoning effect, any creature with the specified creature flag will be excluded from the selection. This token may be used multiple times per interaction effect; creatures which possess any of the indicated flags will never be summoned. |
|  IE_CREATURE_CASTE_FLAG | Within I_EFFECT:SUMMON_UNIT | \ | When this token is added to a random creature summoning effect, it narrows down the selection to creatures which have the specified caste flag. This token may be used multiple times per interaction effect; creatures which lack any of the indicated flags will never be summoned. |
|  IE_FORBIDDEN_CREATURE_CASTE_FLAG | Within I_EFFECT:SUMMON_UNIT | \ | When this token is added to a random creature summoning effect, it excludes any creature with the specified caste flag. This token may be used multiple times per interaction effect; creatures which possess any of the indicated flags will never be summoned. |
|  IE_HAVE_FAST_EFFORTLESS_GAIT_SPEED | Within I_EFFECT:SUMMON_UNIT | gait speed\> | When this token is added to a random creature summoning effect, it narrows down the selection to creatures which have at least one gait with an [](/index.php/Creature_token#GAIT "Creature token") of 0 and a [](/index.php/Creature_token#GAIT "Creature token") less than or equal to the specified ("less than" because lower is faster in the scale used for gait speed). [2] |
|  IE_ALL_SLOW_EFFORTLESS_GAIT_SPEED | Within I_EFFECT:SUMMON_UNIT | gait speed\> | When this token is added to a random creature summoning effect, it excludes any creatures which have at least one gait with an [](/index.php/Creature_token#GAIT "Creature token") of 0 and a [](/index.php/Creature_token#GAIT "Creature token") value less than or equal to the specified (note that larger values are slower in the scale used for gait speed). [3] |
|  IE_TIME_RANGE | Within I_EFFECT:SUMMON_UNIT | ticks\>:ticks\> | The summoned unit vanishes in a puff of smoke once a certain amount of time has elapsed. The time limit is a randomly selected number of ticks within the specified minimum-maximum time range. The unit will persist indefinitely if this token is omitted. |
|  IE_MAKE_PET_IF_POSSIBLE | Within I_EFFECT:SUMMON_UNIT |  | Makes the summoned unit behave as a pet of the unit who performed the summoning interaction. |
|  GENERATED | Global |  | Indicates that this is a generated interaction. Cannot be specified in user-defined raws. |

## Usage

To enable a particular type of creature to use an interaction directly, the creature token [`[CAN_DO_INTERACTION:]`](/index.php/Creature_token#CAN_DO_INTERACTION "Creature token") should be added to its creature raws (replacing '' with the ID of the desired interaction; for an interaction called `[INTERACTION:CLEANING]` in the raws, the ID would be "CLEANING"), followed by a series of \[CDI:...\] tokens as detailed below.

Interactions can also be granted to individual creatures via syndromes using the syndrome effect token [`[CE_CAN_DO_INTERACTION]`](/index.php/Syndrome#CE_CAN_DO_INTERACTION "Syndrome") followed by [`[CDI:INTERACTION:]`](/index.php/Interaction_token#INTERACTION "Interaction token") and additional CDI tokens as required.

The following is a list of valid CDI tokens. Precede them with "CDI:" in the style of `[CDI:ADV_NAME:Clean]`, for example.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  INTERACTION | ID | Specifies which interaction can be performed. This is only needed following CE_CAN_DO_INTERACTION; there's no need to include this after CAN_DO_INTERACTION as the latter allows you to specify the interaction directly (as explained above). |
|  ADV_NAME | text | Specifies the name of the interaction as it will appear on the adventure mode 'powers/abilities' menu. |
|  TOKEN | ID | Specifies a reference for the interaction graphics icon as it will appear on the adventure mode 'powers/abilities' menu\[Verify\]. |
|  TARGET | target ID, target types | Specifies how the creature chooses what to target. Target ID refers to an I_TARGET defined in the interaction itself. Multiple target types can be specified. If no target is specified, creature will target any available target within range, even through walls. Valid target types: / LINE_OF_SIGHT / - the source needs to be able to see the target / TOUCHABLE / - the source needs to be able to touch the target / DISTURBER_ONLY / - the target must be whoever disturbed the source (this is currently only relevant to / mummies / , allowing them to curse solely the unit who disturbed their / resting place / ) / SELF_ALLOWED / - the target can be the source / SELF_ONLY / - the target / must / be the source |
|  TARGET_RANGE | target ID, range | Determines the maximum distance from the interaction user (in tiles) at which something can be considered a valid target. For SOLID_GLOB, SHARP_ROCK, LIQUID_GLOB and FIREBALL breath attacks, also determines how far the projectiles can fly before falling to the ground. |
|  MAX_TARGET_NUMBER | ID, number | Specifies the maximum number of things that can be selected for a particular I_TARGET. |
|  LOCATION_HINT | Location Hint | Prevents CPU-controlled creatures from using the interaction unless they are in a location which meets the specified criteria. See above for a list of valid location hint values. |
|  USAGE_HINT | Usage hint token | Indicates when and how CPU-controlled creatures will use the interaction. If no hint is specified in fortress mode, the interaction will be performed at every opportunity in combat. Multiple usage hints may be specified. Valid values: / GREETING / - Creatures will target 'friendly' creatures, usually at random. / ATTACK / - Targets enemy creatures in combat. If the interaction specifies SELF_ONLY, CPU-controlled creatures will never use it. / DEFEND / - Used in combat. Creature will target itself. / FLEEING / - Used when fleeing an enemy. Creature will target itself. / CLEAN_SELF / - Creature targets itself when its body is covered with / contaminants / . / CLEAN_FRIEND / - As above, but targets other friendly units instead. / NEGATIVE_SOCIAL_RESPONSE / - Used when a creature is expressing contempt (for example, to a murderer). This is used in the default spitting interaction, for example. / TORMENT / - This is also used in the default spitting interaction, and is presumably used in a similar context. / MINOR_BLESSING / - Used in divination dice blessings. Targets the roller. / MEDIUM_BLESSING / - Used in divination dice blessings. Targets the roller. / MINOR_CURSE / - Used in divination dice curses. Targets the roller. / MEDIUM_CURSE / - Used in divination dice curses. Targets the roller. / MAJOR_CURSE / - Used in disturbance and deity curses. Targets the tomb disturber / temple defiler. |
|  WAIT_PERIOD | number | The creature must wait the specified number of / ticks / before being able to use the interaction again. The delay defaults to 20 ticks if this is omitted. Setting it to 0 removes the delay altogether. / Note: A WAIT_PERIOD of 10 is 10 ticks long in / fortress mode / , but only 1 tick long in / adventurer mode / . |
|  FREE_ACTION |  | Indicates that performing the interaction doesn't take any time. |
|  BP_REQUIRED | Body part criteria | Indicates that a particular body part must be present in order to perform the interaction. Criteria are **BY_CATEGORY:**category, **BY_TYPE:**type (GRASP, for example), or **BY_TOKEN:**token (uses the body part ID). See body token. |
|  VERBAL |  | Only creatures that can speak will be able to use the interaction. Might also be needed for VERBAL_SPEECH. |
|  VERBAL_SPEECH | text set | Specifies what the creature says when they perform the interaction. Text sets are defined in text\_\* raws. |
|  CAN_BE_MUTUAL |  | Presumably allows two creatures with the same interaction to use it on each other simultaneously, for example, cats cleaning each other. |
|  VERB | self:other:mutual | When a creature uses the interaction, a combat report message will be displayed in the form: / \[interaction user(s)\] \[VERB text\] \[target creature (if applicable)\] / The 'self' text is presented when describing the interaction in the second person (that is, when the interaction is carried out by the player character in / adventure mode / ), the 'other' text is presented when describing it in the third person, and the 'mutual' text is presented when the interaction is carried out in a / mutual / fashion. / \[CDI:VERB:lick:licks:lick each other\] / \[CDI:VERB:gesture:gestures:NA\] |
|  VERB_REVERSE | ? | ? |
|  TARGET_VERB | self:other | When a creature uses the interaction, a message will display, describing the target as doing this. / \[CDI:TARGET_VERB:shudder and begin to move:shudders and begins to move\] |
|  FLOW | Breath attack token | Can be used with interactions that have / \[I_EFFECT:MATERIAL_EMISSION\] / and / \[IT_LOCATION:CONTEXT_MATERIAL\] / (or / \[IT_MATERIAL:CONTEXT_MATERIAL\] / ) to make the interaction emit a special flow type. Valid values: / FIREBALL / FIREJET / DRAGONFIRE / . |
|  MATERIAL | Material token:Breath attack token | Can be used with interactions that have [\[I_EFFECT:MATERIAL_EMISSION\]](/index.php/Interaction_token#I_EFFECT "Interaction token") and [\[IT_LOCATION:CONTEXT_MATERIAL\]](/index.php/Interaction_token#IT_LOCATION "Interaction token") (or [\[IT_MATERIAL:CONTEXT_MATERIAL\]](/index.php/Interaction_token#IT_MATERIAL "Interaction token")) to make the interaction emit the specified material in the manner described by the breath attack token used. |

## Breath attacks

Breath attacks are controlled by the MATERIAL_EMISSION interaction, like so:

     [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:ADV_NAME:Breath custom material]
            [CDI:USAGE_HINT:ATTACK]
            [CDI:BP_REQUIRED:BY_CATEGORY:MOUTH]
            [CDI:MATERIAL:LOCAL_CREATURE_MAT:CUSTOMMATERIAL:TRAILING_VAPOR_FLOW]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:15]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:50]

The most important part is this line:

     [CDI:MATERIAL:LOCAL_CREATURE_MAT:CUSTOMMATERIAL:TRAILING_VAPOR_FLOW]

The CDI refers to CAN_DO_INTERACTION; the MATERIAL states that this line shows what the material is. LOCAL_CREATURE_MAT:CUSTOMMATERIAL is your material, and TRAILING_VAPOR_FLOW refers to the breath attack type. Other types are seen below. Also important is this line:

     [CDI:TARGET:C:LINE_OF_SIGHT]

LINE_OF_SIGHT refers to where the target C may be; others include SELF_ALLOWED (presumably like LINE_OF_SIGHT, but with the creature allowed to target itself), SELF_ONLY (preferable for undirected attacks) and TOUCHABLE (for up-close attacks, as trailing flows tend to be).

### Breath Attack Types

       [CDI:MATERIAL::]

Is used to emit a specific material in a specific manner. A list of valid emission types can be found below.

Examples:

       [CDI:MATERIAL:INORGANIC:GABBRO:SHARP_ROCK]

shoots a sharp gabbro rock

       [CDI:MATERIAL:PLANT_MAT:GRASS_CAVE_WHEAT:MILL:UNDIRECTED_DUST]

releases a cloud of dwarven wheat flour

       [CDI:MATERIAL:CREATURE_MAT:DWARF:TEARS:SPATTER_LIQUID]

creates a pool of dwarven tears

\

       [CDI:FLOW:]

Is used to emit one of the special hardcoded flow types (FIREBALL, FIREJET or DRAGONFIRE).

Example:

       [CDI:FLOW:DRAGONFIRE]

\

|  |  |  |
|----|----|----|
| Token | Usage Type | Description |
|  TRAILING_DUST_FLOW | MATERIAL | Shoots a trail of solid dust at the target. Appears to use cave-in dust physics, as the dust cloud will fling around anything it comes in contact with (including the creature who emitted it), making it capable of smashing creatures into the ground and flinging them over walls. Creatures caught in the dust cloud will be covered with dust; this will trigger any associated contact syndromes. |
|  TRAILING_VAPOR_FLOW | MATERIAL | Shoots a trail of liquid mist at the target. Creatures caught in the vapor will be covered with the condensed liquid; this will trigger any associated contact syndromes. |
|  TRAILING_GAS_FLOW | MATERIAL | Shoots a trail of gaseous substance at the target. This can be inhaled, triggering any associated inhalation syndromes. |
|  TRAILING_ITEM_FLOW:item token | MATERIAL | Shoots a "cloud" of items at the target, leaving piles of this item on the floor. Note that this does *not* create the actual items or use falling item mechanics (meaning no flying daggers or Touhou-style barrages, unfortunately). Instead, this token acts as TRAILING_GAS_FLOW, except that the material will use its *normal* temperature - for example, a breath attack of steel anvils will envelop the target in a "burst of steel". |
|  UNDIRECTED_DUST | MATERIAL | The creature releases a cloud of solid dust which spreads and dissipates. Similar to TRAILING_DUST_FLOW, but undirected, thus affecting a larger area but losing the distance - range is roughly the same as that of a cave-in. Creature will attack as normal. ~~DO NOT USE THIS TAG UNLESS YOU WANT TO KILL THE CREATURE AND EVERYTHING NEAR IT AND SEND PEOPLE FLYING.~~ You know you want to. |
|  UNDIRECTED_VAPOR | MATERIAL | The creature releases a cloud of liquid mist which spreads and dissipates. Similar to TRAILING_VAPOR_FLOW, but undirected, thus affecting a larger area but losing the distance. |
|  UNDIRECTED_GAS | MATERIAL | The creature releases a cloud of gaseous material which spreads and dissipates. Similar to TRAILING_GAS_FLOW, but undirected, thus affecting a larger area but losing the distance. |
|  UNDIRECTED_ITEM_CLOUD:item token | MATERIAL | The creature releases a "cloud" of items at the target, leaving piles of this item on the floor. The same comments apply as TRAILING_ITEM_FLOW. |
|  WEATHER_CREEPING_DUST | MATERIAL | Creates a cloud of creeping dust. Not usable by creatures. |
|  WEATHER_CREEPING_VAPOR | MATERIAL | Creates a cloud of creeping vapor. Not usable by creatures. |
|  WEATHER_CREEPING_GAS | MATERIAL | Creates a cloud of gas that appears at the edge of the map and slowly creeps across the map. Not usable by creatures. |
|  WEATHER_FALLING_MATERIAL | MATERIAL | Causes it to start raining a particular material. If the material is solid at the outdoor temperatures, it will snow the material instead. Can transfer contact syndromes. Regardless of the nature of the material, being caught in it will give dwarves the negative thought of being 'caught in freakish weather lately'. Not usable by creatures. |
|  SOLID_GLOB | MATERIAL | Shoots a solid glob of spinning substance at the target, leaving a symbol similar to broken arrows, if it misses. Essentially a projectile weapon. If the cooldown rate is short enough, some creatures with this breath attack will not move, preferring instead to hold position and shoot globs at their enemies, even when they are right next to them. |
|  SHARP_ROCK | MATERIAL | Just like SOLID_GLOB, but more harmful, as it shoots a sharpened solid chunk of material instead. |
|  LIQUID_GLOB | MATERIAL | Shoots a liquid glob of substance at the target. Contact syndromes will take effect if the glob hits the target's exposed skin. |
|  SPATTER_POWDER | MATERIAL | Creates a pile of powder at the specified location. |
|  SPATTER_LIQUID | MATERIAL | Creates a pool of liquid at the specified location. |
|  WEB_SPRAY | MATERIAL | Emits a burst of webs that entangle target creatures. |
|  DRAGONFIRE | FLOW | Emits a wide cone of dragon fire that burns target creatures at a scorching 50000 °U  . |
|  FIREJET | FLOW | Emits a narrow cone of fire that burns target creatures at 11000 °U  . |
|  FIREBALL | FLOW | Emits a fireball that burns the target creature. |

Keep in mind that you can give a creature multiple breath attacks, which appears to make the creature choose between them at random. Creatures cannot use the WEATHER effects, these being reserved for regional interactions.

One major difference between GAS, VAPOR, and DUST is that if the material cannot exist in the specified state at the current temperature, it will automatically be created at a temperature allowing it to exist. So if you create a vapor spray that uses rock or metal as a material, that spray will be created at the material's melting point, setting everything it touches on fire. You can also create a freezing spray by using a custom material that has extremely low melting and/or boiling points.

If you give a creature a material breath attack, be aware that it will be caught in the attack more frequently than its targets. Make sure to make your creatures immune to their own breath weapons!

## Creature and Caste Flags

Certain interaction and syndrome effects (currently limited to [\[IE_SUMMON_UNIT\]](/index.php/Interaction_token#I_EFFECT "Interaction token") and [\[CE_BODY_TRANSFORMATION\]](/index.php/Syndrome#CE_BODY_TRANSFORMATION "Syndrome")) permit modders to specify the required/forbidden creature and caste flags of the desired creature(s). These are a collection of internal flags which are derived from creature tokens but are not necessarily identical to them. The following lists contain creature and caste flag names as provided by Toady One in a FotF reply [4] (valid as of 0.47.04).

    Creature Flags

    ALL_CASTES_ALIVE
    ARTIFICIAL_HIVEABLE
    BIOME_DESERT_BADLAND
    BIOME_DESERT_ROCK
    BIOME_DESERT_SAND
    BIOME_FOREST_TAIGA
    BIOME_FOREST_TEMPERATE_BROADLEAF
    BIOME_FOREST_TEMPERATE_CONIFER
    BIOME_FOREST_TROPICAL_CONIFER
    BIOME_FOREST_TROPICAL_DRY_BROADLEAF
    BIOME_FOREST_TROPICAL_MOIST_BROADLEAF
    BIOME_GLACIER
    BIOME_GRASSLAND_TEMPERATE
    BIOME_GRASSLAND_TROPICAL
    BIOME_LAKE_TEMPERATE_BRACKISHWATER
    BIOME_LAKE_TEMPERATE_FRESHWATER
    BIOME_LAKE_TEMPERATE_SALTWATER
    BIOME_LAKE_TROPICAL_BRACKISHWATER
    BIOME_LAKE_TROPICAL_FRESHWATER
    BIOME_LAKE_TROPICAL_SALTWATER
    BIOME_MARSH_TEMPERATE_FRESHWATER
    BIOME_MARSH_TEMPERATE_SALTWATER
    BIOME_MARSH_TROPICAL_FRESHWATER
    BIOME_MARSH_TROPICAL_SALTWATER
    BIOME_MOUNTAIN
    BIOME_OCEAN_ARCTIC
    BIOME_OCEAN_TEMPERATE
    BIOME_OCEAN_TROPICAL
    BIOME_POOL_TEMPERATE_BRACKISHWATER
    BIOME_POOL_TEMPERATE_FRESHWATER
    BIOME_POOL_TEMPERATE_SALTWATER
    BIOME_POOL_TROPICAL_BRACKISHWATER
    BIOME_POOL_TROPICAL_FRESHWATER
    BIOME_POOL_TROPICAL_SALTWATER
    BIOME_RIVER_TEMPERATE_BRACKISHWATER
    BIOME_RIVER_TEMPERATE_FRESHWATER
    BIOME_RIVER_TEMPERATE_SALTWATER
    BIOME_RIVER_TROPICAL_BRACKISHWATER
    BIOME_RIVER_TROPICAL_FRESHWATER
    BIOME_RIVER_TROPICAL_SALTWATER
    BIOME_SAVANNA_TEMPERATE
    BIOME_SAVANNA_TROPICAL
    BIOME_SHRUBLAND_TEMPERATE
    BIOME_SHRUBLAND_TROPICAL
    BIOME_SUBTERRANEAN_CHASM
    BIOME_SUBTERRANEAN_LAVA
    BIOME_SUBTERRANEAN_WATER
    BIOME_SWAMP_MANGROVE
    BIOME_SWAMP_TEMPERATE_FRESHWATER
    BIOME_SWAMP_TEMPERATE_SALTWATER
    BIOME_SWAMP_TROPICAL_FRESHWATER
    BIOME_SWAMP_TROPICAL_SALTWATER
    BIOME_TUNDRA
    DOES_NOT_EXIST
    EQUIPMENT
    EQUIPMENT_WAGON
    EVIL
    FANCIFUL
    GENERATED
    GOOD
    HAS_ANY_BENIGN
    HAS_ANY_CANNOT_BREATHE_AIR
    HAS_ANY_CANNOT_BREATHE_WATER
    HAS_ANY_CAN_SWIM
    HAS_ANY_CARNIVORE
    HAS_ANY_COMMON_DOMESTIC
    HAS_ANY_CURIOUS_BEAST
    HAS_ANY_DEMON
    HAS_ANY_FEATURE_BEAST
    HAS_ANY_FLIER
    HAS_ANY_FLY_RACE_GAIT
    HAS_ANY_GRASP
    HAS_ANY_GRAZER
    HAS_ANY_HAS_BLOOD
    HAS_ANY_IMMOBILE
    HAS_ANY_INTELLIGENT_LEARNS
    HAS_ANY_INTELLIGENT_SPEAKS
    HAS_ANY_LARGE_PREDATOR
    HAS_ANY_LOCAL_POPS_CONTROLLABLE
    HAS_ANY_LOCAL_POPS_PRODUCE_HEROES
    HAS_ANY_MEGABEAST
    HAS_ANY_MISCHIEVIOUS
    HAS_ANY_NATURAL_ANIMAL
    HAS_ANY_NIGHT_CREATURE
    HAS_ANY_NIGHT_CREATURE_BOGEYMAN
    HAS_ANY_NIGHT_CREATURE_EXPERIMENTER
    HAS_ANY_NIGHT_CREATURE_HUNTER
    HAS_ANY_NIGHT_CREATURE_NIGHTMARE
    HAS_ANY_NOT_FIREIMMUNE
    HAS_ANY_NOT_FLIER
    HAS_ANY_NOT_LIVING
    HAS_ANY_OUTSIDER_CONTROLLABLE
    HAS_ANY_POWER
    HAS_ANY_RACE_GAIT
    HAS_ANY_SEMIMEGABEAST
    HAS_ANY_SLOW_LEARNER
    HAS_ANY_SUPERNATURAL
    HAS_ANY_TITAN
    HAS_ANY_UNIQUE_DEMON
    HAS_ANY_UTTERANCES
    HAS_ANY_VERMIN_HATEABLE
    HAS_ANY_VERMIN_MICRO
    HAS_FEMALE
    HAS_MALE
    LARGE_ROAMING
    LOOSE_CLUSTERS
    MATES_TO_BREED
    MUNDANE
    OCCURS_AS_ENTITY_RACE
    SAVAGE
    SMALL_RACE - applies to any vermin creature
    TWO_GENDERS
    UBIQUITOUS
    VERMIN_EATER
    VERMIN_FISH
    VERMIN_GROUNDER
    VERMIN_ROTTER
    VERMIN_SOIL
    VERMIN_SOIL_COLONY

    Caste Flags

    ADOPTS_OWNER
    ALCOHOL_DEPENDENT
    ALL_ACTIVE
    AMBUSHPREDATOR
    AQUATIC_UNDERSWIM
    ARENA_RESTRICTED
    AT_PEACE_WITH_WILDLIFE
    BENIGN
    BLOODSUCKER
    BONECARN
    CANNOT_BREATHE_AIR
    CANNOT_CLIMB
    CANNOT_JUMP
    CANOPENDOORS
    CAN_BREATHE_WATER
    CAN_LEARN / INTELLIGENT_LEARNS
    CAN_SPEAK / INTELLIGENT_SPEAKS
    CAN_SWIM
    CAN_SWIM_INNATE
    CARNIVORE
    CAVE_ADAPT
    COLONY_EXTERNAL
    COMMON_DOMESTIC
    CONVERTED_SPOUSE
    COOKABLE_LIVE
    CRAZED
    CREPUSCULAR
    CURIOUS_BEAST
    CURIOUS_BEAST_EATER
    CURIOUS_BEAST_GUZZLER
    CURIOUS_BEAST_ITEM
    DEMON
    DIE_WHEN_VERMIN_BITE
    DIURNAL
    DIVE_HUNTS_VERMIN
    EQUIPS
    EXTRAVISION
    FEATURE_ATTACK_GROUP
    FEATURE_BEAST
    FIREIMMUNE
    FIREIMMUNE_SUPER
    FISHITEM
    FLEEQUICK
    FLIER
    GELDABLE
    GETS_INFECTIONS_FROM_ROT
    GETS_WOUND_INFECTIONS
    GNAWER
    GRAZER
    HASSHELL
    HAS_BABYSTATE
    HAS_BLOOD
    HAS_CHILDSTATE
    HAS_COLOR
    HAS_FLY_RACE_GAIT
    HAS_GLOW_COLOR
    HAS_GLOW_TILE
    HAS_GRASP
    HAS_NERVES
    HAS_PUS
    HAS_RACE_GAIT
    HAS_ROTTABLE
    HAS_SECRETION
    HAS_SOLDIER_TILE
    HAS_SOUND_ALERT
    HAS_SOUND_PEACEFUL_INTERMITTENT
    HAS_TILE
    HUNTS_VERMIN
    IMMOBILE
    IMMOBILE_LAND
    IMMOLATE
    ITEMCORPSE
    LAIR_HUNTER
    LARGE_PREDATOR
    LAYS_EGGS
    LAYS_UNUSUAL_EGGS
    LIGAMENTS
    LIGHT_GEN
    LISP
    LOCAL_POPS_CONTROLLABLE
    LOCAL_POPS_PRODUCE_HEROES
    LOCKPICKER
    MAGICAL
    MAGMA_VISION
    MANNERISM_BREATH
    MANNERISM_EYELIDS
    MANNERISM_LAUGH
    MANNERISM_POSTURE
    MANNERISM_SIT
    MANNERISM_SMILE
    MANNERISM_STRETCH
    MANNERISM_WALK
    MATUTINAL
    MEANDERER
    MEGABEAST
    MILKABLE
    MISCHIEVIOUS
    MOUNT
    MOUNT_EXOTIC
    MULTIPART_FULL_VISION
    MULTIPLE_LITTER_RARE
    NATURAL_ANIMAL
    NIGHT_CREATURE
    NIGHT_CREATURE_BOGEYMAN
    NIGHT_CREATURE_EXPERIMENTER
    NIGHT_CREATURE_HUNTER
    NIGHT_CREATURE_NIGHTMARE
    NOBONES
    NOBREATHE
    NOCTURNAL
    NOEMOTION
    NOEXERT
    NOFEAR
    NOMEAT
    NONAUSEA
    NOPAIN
    NOSKIN
    NOSKULL
    NOSMELLYROT
    NOSTUCKINS
    NOSTUN
    NOTHOUGHT
    NOT_BUTCHERABLE
    NOT_LIVING
    NO_AUTUMN
    NO_CONNECTIONS_FOR_MOVEMENT
    NO_DIZZINESS
    NO_DRINK
    NO_EAT
    NO_FEVERS
    NO_PHYS_ATT_GAIN
    NO_PHYS_ATT_RUST
    NO_SLEEP
    NO_SPRING
    NO_SUMMER
    NO_THOUGHT_CENTER_FOR_MOVEMENT
    NO_UNIT_TYPE_COLOR
    NO_VEGETATION_PERTURB
    NO_WINTER
    OPPOSED_TO_LIFE
    OUTSIDER_CONTROLLABLE
    PACK_ANIMAL
    PARALYZEIMMUNE
    PATTERNFLIER
    PEARL
    PET
    PET_EXOTIC
    POWER
    REMAINS_ON_VERMIN_BITE_DEATH
    REMAINS_UNDETERMINED
    RETURNS_VERMIN_KILLS_TO_OWNER
    SEMIMEGABEAST
    SLOW_LEARNER
    SPOUSE_CONVERSION_TARGET
    SPOUSE_CONVERTER
    SPREAD_EVIL_SPHERES_IF_RULER
    STANCE_CLIMBER
    STRANGE_MOODS
    SUPERNATURAL
    TENDONS
    THICKWEB
    TITAN
    TRAINABLE_HUNTING
    TRAINABLE_WAR
    TRANCES
    TRAPAVOID
    UNIQUE_DEMON
    UTTERANCES
    VEGETATION
    VERMIN_GOBBLER
    VERMIN_HATEABLE
    VERMIN_MICRO
    VERMIN_NOFISH
    VERMIN_NOROAM
    VERMIN_NOTRAP
    VESPERTINE
    WAGON_PULLER
    WEBBER
    WEBIMMUNE

## See Also

- Syndrome
- Interaction examples
