# Lua functions

> Fonte: [Lua functions](https://dwarffortresswiki.org/index.php/Lua_functions) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

\

Dwarf Fortress defines a number of functions in addition to those standard for Lua 5.4.

## C++ function calls

|  |  |
|----|----|
| Function | Description |
| *int*  trandom(*int* n) | Returns a 32-bit integer from 0 to n-1. Uses DF's internal RNG system instead of `math.random()`. |
| *str*  capitalize_string_words(*str* s) | Capitalizes every word in a string. |
| *str*  capitalize_string_first_word(*str* s) | Capitalizes the first word in a string. |
| *str*  utterance() | Returns a word from the kobold language. |
| *void*  lua_log(*str* s) | Prints a string to `Dwarf Fortress/lualog.txt`. The `log()` function is more robust and should be used instead. |
| void / raws.register_reactions / ( / table / lines) / void / raws.register_creatures / ( / table / lines) / void / raws.register_entities / ( / table / lines) / void / raws.register_items / ( / table / lines) / void / raws.register_inorganics / ( / table / lines) / void / raws.register_interactions / ( / table / lines) / void / raws.register_languages / ( / table / lines) / void / raws.register_plants / ( / table / lines) | Takes a table of tokens and reads them as that type of raw file. It is not necessary to add a header. |

## Globals

Helper functions are defined in `init/globals.lua`, and can be accessed by any script even if `vanilla_procedural` is not loaded.

### Generation

This function is defined in `init/generators.lua`.

|  |  |
|----|----|
| Function | Description |
| *table*  add_generated_info(*table* tbl) | Adds [`[GENERATED]`](/index.php/Creature_token#GENERATED "Creature token") to the input table, and [`[SOURCE_HFID]`](/index.php/Creature_token#SOURCE_HFID "Creature token")/[`[SOURCE_ENID]`](/index.php/Creature_token#SOURCE_ENID "Creature token") if IDs are defined. Necessary for generated raws to be saved properly. |

### Randomization

|  |  |
|----|----|
| Function | Description |
| *value*  pick_random(*table* t) | Returns a random value from a table. |
| *value*  pick_random_no_replace(*table* t) | Returns a random value from a table, then removes it from the table. |
| *value*  pick_random_conditional(*table* t, *function* cond,...) | Returns a random value from a table that satisfies `cond(...)`. |
| *bool*  one_in(*num* x) | Returns true with a one in x chance. |
| *value*  pick_random_pairs(*table* tbl) | Returns a random key from a table. For example, `pick_random_pairs( {WATER = true} )` returns "WATER". |
| *value*  pick_weighted_from_table(*table* tbl) | Requires a table of tables with / weight / keys. Returns a weighted random value. / At debug level \>=4, logs the roll. |
| *value*  generate_from_list(*table* tbl,...) | Requires a table of functions that return a `weight` key. Runs each function and returns a weighted random output. Used by werebeasts to generate an interaction and link to options from it. |

### Tables

|  |  |
|----|----|
| Function | Description |
| *table*  split_to_lines(*table* tbl,*string* str) | Adds a string into a table, with each line being a separate key. |
| *table*  map_merge(*table* tbl1, *table* tbl2) | Combines two tables. If `tbl1` already has a value for a given key, it will not be overwritten. Used for sets such as `{ WATER = true }`. |
| *table*  table_merge(*table* tbl1, *table* tbl2) | Adds each value from `tbl2` onto the end of `tbl1`. |
| *bool*  find_in_array_part(*table* tbl, *value* item) | Returns true if `item` is a value in `tbl`. |
| *void*  convert_array_to_set(*table* tbl) | Makes a set from an array, e.g. takes {"a","b","c"} and makes it {a=true,b=true,c=true} so that it can be indexed. |
| *void*  add_unique(*table* tbl, *value* item) | Adds `item` to the end of `tbl` if not already present. |
| *void*  remove_item(*table* tbl, *value* item) | Removes all instances of `item` from `tbl`. |
| *table*  shallow_copy(*table* tbl) | Returns a table copied from all values in the input table. |
| *table*  deep_copy(*table* tbl) | Returns a table recursively copied from all values in the input table. |

### Debug

|  |  |
|----|----|
| Function | Description |
| *void*  log(...) | Logs the input to `Dwarf Fortress/lualog.txt`. Used for most cases. |
| *string*  get_caller_loc_string() | Returns the debug source info and the current line. |
| *string*  get_debug_logger(*num* level=1,...) | Logs `get_caller_loc_string()` and any overloads if the `debug_level` is at least `level`. `debug_level` is a global variable that defaults to 0. |
| *function*  partial_function(*function* f, arg,...) | Returns `f(arg,...)`. |
| *function*  log_table(*table* tbl, *num* debug_level=0, *num* nest_level=0, *num* added_debug_from_nest=0) | Logs a table if the global `debug_level` is at least the input `debug_level`. `nest_level` starts at 0 and adds `added_debug_from_nest` for each nesting to the input debug level. |
| *function*  print_table(*table* tbl, *num* nest_level=0) | Logs a table, regardless of debug level. |

### Spheres

|  |  |
|----|----|
| Function | Description |
| *string*  get_random_sphere_adjective(*string* sphere) | Returns a random string from global table `random_sphere_adjective[sph]`. |
| *table*  get_random_sphere_noun(*string* sphere) | Returns a random table / tbl / from global table / random_sphere_nouns\[sphere\] / . / tbl / has two members: / tbl.str / , which is a string; and / tbl.flags / , which defaults to / {OF=true,PREPOS=true,PRE=true} / , for grammar. |
| *table*  add_sphere_mpp(*table* sphere_list, *string* new_s, *table* available_sphere, *table* available_sphere_cur) | Adds / new_s / to / sphere_list / and all parents and children. Sets the added spheres in / available_sphere / and / available_sphere_cur / to false, and sets all enemies in / available_sphere_cur / to false. / At debug level \>= 2, will be logged. |

## Generation tables

The `generate()` function is defined in `init/generators.lua`, and is called to generate objects.

Each type of random object is defined through a function that generates a table of raws. To generate objects for specific purposes, `generate()` can call functions from a table and provide inputs such as `tok` (unique token string). For example, forgotten beasts are unique and generated for each cave region. If multiple functions are defined in `creatures.fb`, such as both `creatures.fb.default` and a modded forgotten beast, the game uses the `weight` output to influence which one will be randomly chosen.

By default, objects are generated in this order: unittests\*, preprocess, do_once, materials, items, languages, creatures, interactions, entities, and postprocess. Do note that you can register raws at any step. For example, each vault entity generates a set of divine equipment during the entity step, and werebeasts generate a curse interaction during the creature step.

### Custom

When the game uses `generate()` to generate objects, all functions in the following tables are run in sequence.

`random_object_parameters.pre_gen_randoms` and `random_object_parameters.main_world_randoms` are only ever true for one generation call each, at the start of world generation in that order.

You cannot predict when `generate()` is called. Raws registered through `preprocess` and `postprocess` should check for either variable so that further calls do not endlessly register raws.

Functions stored and called through these tables are not supplied with arguments.

|  |  |
|----|----|
| Table | Description |
| preprocess | Run at the start of each / generate() / call, after unit testing. / Includes two functions by default: / preprocess.demon() / , which populates the distribution of / demon_type / string inputs / preprocess.bogeyman_polymorph() / , which generates the / bogeyman / 's polymorph / interactions / if bogeymen exist |
| do_once_early | As / do_once / , but only runs if / random_object_parameters.pre_gen_randoms == true / (before the map exists) / Recommended for generating custom objects that need to be placed in the map; ie: animal populations, / minerals / . |
| do_once | Runs immediately after all functions in preprocess, and before all other generation steps. Only runs if / random_object_parameters.main_world_randoms == true / (in prehistory once the map is finalized) / Recommended for generating most custom objects. / Includes one function by default: / do_once.rcp_mat_emission() / , adds the / RCP_MATERIAL_EMISSION / interaction |
| postprocess | Runs after all other generation steps are finished. |
| unittests | Runs before preprocess if the global `debug_level` is greater than 0. Expects a boolean output. |
| languages | For each function in this table, registers a language. Expects table of key-value pairs where the key is the word token and the value is the translated string. Initial generation call only. |

### Creatures

|  |  |  |
|----|----|----|
| Table | Inputs | Article |
| creatures.angel.great_beast / creatures.angel.humanoid_generic / creatures.angel.humanoid_warrior | function(tok) | Angel (see types) |
| creatures.demon | function(demon_type, difficulty, tok) | Demon |
| creatures.experiment.beast_large / creatures.experiment.beast_small / creatures.experiment.failed_large / creatures.experiment.failed_small / creatures.experiment.humanoid_giant / creatures.experiment.humanoid | function(tok) | Experiment |
| creatures.fb | function(layer_type, tok) | Forgotten beast |
| creatures.night_creature.bogeyman | function(tok) | Bogeyman |
| creatures.night_creature.nightmare | function(tok) | Nightmare |
| creatures.night_creature.troll | function(tok) | Night troll |
| creatures.night_creature.werebeast / werebeast_origin_interactions / \* | function(tok) / function(tok, name, options) | Werebeast |
| creatures.titan | function(subregion, tok) | Titan |

#### Creature patching

While `SELECT_CREATURE` cannot target generated objects, there are global tables set up to append data when building a creature. These tables contain functions which have access to tokens, options, and local functions from `build_body_from_rcp()`. All functions in these tables are run at corresponding stages in the build function.

`lines`, `options` and `rcp` are the creature's raw lines and data, which can be read or modified in these functions.

|  |  |  |
|----|----|----|
| Table | Inputs | Timing |
| btc1_tweaks | function(lines, options, add_to_body, add_to_body_unique, add_tweak_candidate) | Before `options.btc` (the first tweak) is determined. |
| feature_tweaks | function(rcp, options, add_to_body, add_to_body_unique, add_tweak_candidate) | After `options.btc2` is set. `add_tweak_candidate()` is unused in vanilla at this stage. |
| post_attack_tweaks | function(lines, options, is_in_body) | After `options.attack_tweak` is set. By default, runs functions to add [`[ATTACK]`](/index.php/Creature_token#ATTACK "Creature token")s for body parts. |
| post_gait_tweaks | function(lines, options) | This is the last operation in the build function. / Includes the / bogey_polymorph() / function by default, which checks / options.can_bogey_polymorph / to add the interaction. |

|  |  |
|----|----|
| Local Function | Effect |
| *void* add_to_body(str) | Adds the input body token to the `options.body_string` table. |
| *void* add_to_body_unique(str) | As `add_to_body()` and `add_unique()`, only adds if not already present. |
| *void* add_tweak_candidate(str) | Adds the input to `options.body_tweak_candidate`, pointing to a key in the `tweaks` table. |
| *bool* is_in_body(str) | Checks if the input body token is in `options.body_string`. |

### Entities

Generated entities are supplied with the `idx` parameter, which is a number that starts at 1 and increments by 1 for each entity of that type. It can be used to give a unique ID to divine equipment.

|  |  |  |
|----|----|----|
| Table | Inputs | Articles |
| entities.vault_guardian | function(idx,tok) | Vault (angels) |
| entities.mythical_guardian | function(idx,tok) | Mysterious dungeon (dungeon guardians) |

### Interactions

#### World

World interactions are generated in the `generate_random_interactions()` step of `generators.lua`.

|  |  |  |
|----|----|----|
| Table | Inputs | Examples |
| interactions.blessing.minor / interactions.blessing.medium | function(idx) | Die roll effects: luck, holy item, healing, etc |
| interactions.curse.minor / interactions.curse.medium | function(idx) | Die roll effects: week of curse |
| interactions.curse.major | function(idx,tok) | Vampire |
| interactions.disturbance | function(idx) | Mummy |
| interactions.mythical | function(idx,power_level,sphere) | Dungeon guardian |
| interactions.mythical_item_power | spheres={}, interaction=function() | Primordial remnant#List of powers |
| interactions.regional | function(idx) | Reanimating evil biomes |
| interactions.secrets | function(idx,sphere) | Necromancer |

#### Powers

Powers are stored in the `interactions.powers` table and can be generated by other interactions. The structure of each power entry contains several keys that determine how it can be added to an interaction's syndrome.

|  |  |  |
|----|----|----|
| Key | Inputs | Notes |
| tags | *table* | A table of user-defined values that can be checked by other functions. |
| tags.lieutenant | *bool* | If true, available to intelligent undead. |
| rarity | *number* n | Higher is rarer. An intelligent undead has a 1 in n chance to receive this power. |
| gen | *table* `tbl`, *table* `end_tbl` function(name) | Generates and returns lines of raws. / tbl / consists of / syndrome / lines comprising / \[CE_CAN_DO_INTERACTION\] / and / CDI / . / end_tbl / consists of lines that define the / interaction / . |

#### Interaction helpers

Interaction helpers are defined by `vanilla_procedural`.

|  |  |
|----|----|
| Function | Notes |
| *table* `tbl`, *table* `end_tbl` basic_lieutenant(*string* name, *string* name_plural, *string* token) | Generates an interaction that raises an intelligent undead and calls `basic_lieutenant_powers(token)`. |
| *table* `tbl`, *table* `end_tbl` basic_lieutenant_powers(*string* token) | Adds any number of powers (chosen from among `interaction.powers`) and 0-5 sicken effects (from `add_curses()`) to the current definition. |
| *table* `tbl`, *table* `end_tbl`, *int* `idx` add_curses(*table* tbl, *table* end_tbl, *string* token, *int* num, *int* start_idx, *int* sev, *table* good_effects) | Adds `num` curses/afflictions to the current definition. `good_effects` lists the possible curses that can be chosen from `default_curse_effects`, and `sev` is the syndrome's severity. Basic lieutenants use a `sev` of 500. |
| *string* get_abstract_gesture() | Returns a random string from either `gestures` or `gestures_abstract`, used for [`[VERB]`](/index.php/Interaction_token#VERB "Interaction token"). |
| populate_monotone_color_pattern() | Writes all / MONOTONE color patterns / from / world.descriptor.color_pattern / to the global table / monotone_color_pattern / , if not already populated. / Not to be confused with / world.descriptor.color / , which has the same keys as a color rather than a pattern. |
| add_base_poison_effects(mat, good_effects, sev, max_eff, min_start, max_start, min_peak, max_peak, min_end, max_end, terminal_chance, resist_chance, size_delay_chance, size_dilute_chance) | Writes 1 to `max_eff` syndrome effects from `good_effects` to `mat`, a table of raw lines. Has a one in `terminal_chance` to not end. If the effect [`[RESISTABLE]`](/index.php/Creature_token#RESISTABLE "Creature token") |

### Items

#### Instruments

The default instrument system is not currently open to Lua, but `generators.lua` defines tables for each token.

|  |  |  |
|----|----|----|
| Table | Inputs | Token |
| items.instruments.keyboard | N/A | [`[GENERATE_KEYBOARD_INSTRUMENTS]`](/index.php/Entity_token#GENERATE_KEYBOARD_INSTRUMENTS "Entity token") |
| items.instruments.stringed | N/A | [`[GENERATE_STRINGED_INSTRUMENTS]`](/index.php/Entity_token#GENERATE_STRINGED_INSTRUMENTS "Entity token") |
| items.instruments.wind | N/A | [`[GENERATE_WIND_INSTRUMENTS]`](/index.php/Entity_token#GENERATE_WIND_INSTRUMENTS "Entity token") |
| items.instruments.percussion | N/A | [`[GENERATE_PERCUSSION_INSTRUMENTS]`](/index.php/Entity_token#GENERATE_PERCUSSION_INSTRUMENTS "Entity token") |

#### Divine equipment

`entities.vault_guardian.default` generates from the list `angel_item_gens`, the default function of which then calls functions from `angel_item_info`. Unless otherwise stated, the **Behavior** column refers to the behavior of how `angel_item_gens.default` generates from these lists.

|  |  |  |
|----|----|----|
| Table | Inputs | Behavior |
| angel_item_gens | function(prefix,tokens) | Called by `entities.vault_guardian.default`, which supplies a unique `prefix` and doesn't provide `tokens`. |
| angel_item_info.armor.pants.gen / angel_item_info.armor.armor.gen / angel_item_info.armor.helm.gen / angel_item_info.armor.gloves.gen / angel_item_info.armor.shoes.gen / angel_item_info.shield.gen | function(i,prefix) | Generates 1 piece of armor for each slot and 1 shield. |
| angel_item_info.clothing.pants.gen / angel_item_info.clothing.armor.gen / angel_item_info.clothing.helm.gen / angel_item_info.clothing.gloves.gen / angel_item_info.clothing.shoes.gen | function(i,prefix) | Generates 1 piece of clothing for each slot. |
| angel_item_info.weapon.PIKE.gen / angel_item_info.weapon.WHIP.gen / angel_item_info.weapon.BOW.gen / angel_item_info.weapon.BLOWGUN.gen / angel_item_info.weapon.AXE.gen / angel_item_info.weapon.SWORD.gen / angel_item_info.weapon.DAGGER.gen / angel_item_info.weapon.MACE.gen / angel_item_info.weapon.HAMMER.gen / angel_item_info.weapon.SPEAR.gen / angel_item_info.weapon.CROSSBOW.gen | function(i,prefix) | Generates 5 weapons. The tables correspond to combat skills, and are not repeated. For example, a vault can't generate two types of swords. |
| angel_item_info.ammo.ARROW / angel_item_info.ammo.BOLT / angel_item_info.ammo.BLOWDART | function() | When a ranged weapon is generated, it will also generate a random subtype of the proper ammunition. |

### Materials

|  |  |  |  |
|----|----|----|----|
| Table | Inputs | Article | Notes |
| materials.clouds / materials.rain | function() | Evil weather | Associated regional interactions are automatically written by `init/generators.lua`. |
| materials.divine.metal / materials.divine.silk | function(sphere) | Divine metal / Divine fabric | The list of potential spheres is determined by the individual function. See / Lua script examples#New divine metal / . / \[DIVINE\] / and / \[SPHERE\] / are added by / generators.lua / rather than in the individual function. |
| materials.mythical_remnant | function(sphere) | Primordial remnant | Possible spheres are determined by `random_object_parameters.mythical_sphere`. |
| materials.mythical_healing | function() | Mythical substance |  |

## Random creatures

Creatures generated by `vanilla_procedural` use a number of shared functions to determine their attributes. The local `options` table stores most of the data used by these steps.

### rcp functions

The random creature profile determines the basic body of a generated creature, such as "humanoid" or "toad", and provides options and data to later build the proper creature definition.

|  |  |
|----|----|
| Function | Notes |
| *table* get_random_creature_profile(options,blacklist) | Makes a weighted random choice of options from / random_creature_types / that satisfy arguments set in / options / ( / options.do_water / , etc) and / blacklist / . Falls back to / random_creature_types.GENERAL_BLOB / . / At debug_level \>= 3, will log failures. At debug_level \>= 4, will also log successes. |
| *bool* is_valid_random_creature(*string* creature, *bool* do_water, *bool* humanoidable_only, *bool* is_good, *bool* beast_only) | Checks if / creature / is a valid key in certain tables depending on the arguments: aquatic ( / do_water / ), can be "twisted into humanoid form" ( / humanoidable_only / ), isn't an "evil" species ( / is_good / ), and is an animal species ( / beast_only / ) / At debug_level \>= 3, will be logged. |
| *void* finalize_random_creature_types() | If `random_creature_types_finalized` is false: sets it to true and iterates over `random_creature_types` to sanitize certain inputs. |

### Shared functions

Default creatures use `add_regular_tokens()`, `populate_sphere_info()`, `get_random_creature_profile()`, `add_body_size()` and `build_procgen_creature()` as the main steps in generating raws.

|  |  |
|----|----|
| Function | Notes |
| add_regular_tokens(tbl,options) | Adds tokens to `tbl`. Sets [`[PETVALUE]`](/index.php/Creature_token#PETVALUE "Creature token"), calculates material weaknesses (if `options.material_weakness`), and adds a few immunity tokens depending on `options.normal_biological`. |
| tile_string(arg) | Returns a string usable for [`[CREATURE_TILE]`](/index.php/Creature_token#CREATURE_TILE "Creature token"). Encloses number arguments in `'` characters. |
| add_body_size(tbl,size,options) | Adds [`[BODY_SIZE]`](/index.php/Creature_token#BODY_SIZE "Creature token") and sets `options.body_size`. Calls `body_size_properties()`. |
| body_size_properties(tbl,size,options) | Adds [`[BUILDINGDESTROYER]`](/index.php/Creature_token#BUILDINGDESTROYER "Creature token") if size \> 80,000; adds [`[GRASSTRAMPLE]`](/index.php/Creature_token#GRASSTRAMPLE "Creature token") and [`[TRAPAVOID]`](/index.php/Creature_token#TRAPAVOID "Creature token") if size \> 100,000. |
| populate_sphere_info(tbl,options) | Adds [`[SPHERE]`](/index.php/Creature_token#SPHERE "Creature token") tokens from `options.spheres`. If `options.do_sphere_rcm`, 1/2 chance to set `options.sphere_rcm`. |
| add_poison_bits(tbl,options) | Generates a poison material based on `options.poison_state` and `options.sickness_name`. |
| build_procgen_creature(rcp,tbl,options) | Calls `build_body_from_rcp()`, `build_description()`, and `build_pcg_graphics()`. |
| build_body_from_rcp(rcp,tbl,options) | Generates based on `rcp` and `options`, assigns tweaks (mutations from the base body), tissues, organs, special attacks. |
| build_description(tbl,options) | Writes the [`[DESCRIPTION]`](/index.php/Creature_token#DESCRIPTION "Creature token") and any [`[PREFSTRING]`](/index.php/Creature_token#PREFSTRING "Creature token")s. |
| build_pcg_graphics(tbl,options) | Assigns procedural graphics layers based on `options.pcg_layering` keys set by `build_body_from_rcp()`. |

### Options

|  |  |  |
|----|----|----|
| Key | Usage | Notes |
| token | add_poison_bits() / build_body_from_rcp() | The creature's token. |
| do_water | get_random_creature_profile() | Use an aquatic rcp (`water_based_random_creature`) |
| humanoidable_only | get_random_creature_profile() / build_body_from_rcp() | Use a rcp that can be turned into a humanoid form (`humanoidable_random_creature`), and automatically applies the `MAKE_HUMANOID` tweak. Will apply the tweak even if the body is already humanoid. |
| beast_only | get_random_creature_profile() | Forbids generic humanoid/blob/quadruped rcps (`not_beast_random_creature`). |
| normal_biological | add_regular_tokens() | If untrue, adds [`[AMPHIBIOUS]`](/index.php/Creature_token#AMPHIBIOUS "Creature token"), [`[SWIMS_INNATE]`](/index.php/Creature_token#SWIMS_INNATE "Creature token"), [`[NONAUSEA]`](/index.php/Creature_token#NONAUSEA "Creature token"), [`[NOEXERT]`](/index.php/Creature_token#NOEXERT "Creature token"), [`[NO_DIZZINESS]`](/index.php/Creature_token#NO_DIZZINESS "Creature token"), [`[NOPAIN]`](/index.php/Creature_token#NOPAIN "Creature token"), [`[NOSTUN]`](/index.php/Creature_token#NOSTUN "Creature token"). Used by experiments. |
| always_nobreathe | build_body_from_rcp() | Adds [`[NOBREATHE]`](/index.php/Creature_token#NOBREATHE "Creature token"), even if not uniform. |
| no_general_poison | build_body_from_rcp() | If untrue and the creature has blood or ichor, adds `[``CREATURE_CLASS``:GENERAL_POISON]`. |
| fire_immune | build_body_from_rcp() | Adds [`[FIREIMMUNE]`](/index.php/Creature_token#FIREIMMUNE "Creature token"). Does not affect materials. Set if the creature has a fire interaction. |
| material_weakness | add_regular_tokens() | Will gain a 10x [`[MATERIAL_FORCE_MULTIPLIER]`](/index.php/Creature_token#MATERIAL_FORCE_MULTIPLIER "Creature token") to a random weapon metal and a `[``GENERAL_MATERIAL_FORCE_MULTIPLIER``:1:2]`. |
| is_good | get_random_creature_profile() / build_body_from_rcp() / build_description() | Forbids "evil" rcps ( / cannot_be_good_random_creature / ). / Affects options for materials, tweaks, description. Cannot have attack tweaks unless the rcp forces it. |
| is_evil | build_body_from_rcp() / build_description() | Affects options for materials, tweaks, description. |
| spheres | populate_sphere_info() / color_picker_functions / build_description() | A set of the creature's spheres. |
| do_sphere_rcm | populate_sphere_info() | Adds a 1/2 chance to set `options.sphere_rcm` to a material relevant to their spheres. |
| pick_sphere_rcm | random_creature_class.UNIFORM.body_fun() | If uniform, adds an additional 1/2 chance to use a material relevant to their spheres. |
| pos_sphere_rcm | populate_sphere_info() | Temporary data storage for possible sphere RCM during `populate_sphere_info()`. |
| sphere_rcm | build_body_from_rcp() | Forces the creature to be uniform and made of that `random_creature_material`. |
| always_insubstantial | build_body_from_rcp() | If uniform, will always choose an insubstantial material from `insubstantial_materials`. |
| never_uniform | build_body_from_rcp() | If `options.r_class` is UNIFORM, change it to FLESHY. |
| always_make_uniform | build_body_from_rcp() | Changes `options.r_class` to UNIFORM. |
| do_not_make_uniform | build_body_from_rcp() | Do not randomly change `options.r_class` to UNIFORM (normally there is a 1/20 chance), unless `options.sphere_rcm` is set. |
| walk_var | build_body_from_rcp() | A string for [`[APPLY_CREATURE_VARIATION]`](/index.php/Creature_token#APPLY_CREATURE_VARIATION "Creature token"), ex: "STANDARD_WALKING_GAITS". Usually set by `rcp.body_base`. |
| walk_speed / special_walk_speed | build_body_from_rcp() | The basic walking speed in a creature's / gait / . / options.special_walk_speed / will be used instead of / options.walk_speed / if both are present. / Crawling bodies use a / options.walk_speed / of 2900, walking bodies use 900. |
| add_fly_gaits | build_body_from_rcp() | Creature has a flying gait even if wings aren't added. `local add_fly_gaits` is used for creatures with wings. |
| intangible_flier | build_body_from_rcp() | If `options.intangible` (set by certain uniform materials), sets `options.add_fly_gaits` and adds [`[FILER]`](/index.php/Creature_token#FILER "Creature token"). |
| cannot_swim | build_body_from_rcp() | Will not add a swimming gait. |
| no_tweak | build_body_from_rcp() | Will not add any random tweaks (such as body parts or attacks) to the basic creature that aren't specified by the rcp. |
| always_glowing_eyes | build_body_from_rcp() | Will always add glowing eyes if the creature has `options.eyes`. |
| no_glowing_eyes / cannot_have_antennae / cannot_have_mandibles | build_body_from_rcp() | Will not add the listed body tweaks. |
| no_random_attack_tweak | build_body_from_rcp() | Will not add attack tweaks (or body parts that grant them) that aren't specified by the rcp. |
| strong_attack_tweak | build_body_from_rcp() | Enables access to attack tweaks. Will always gain an attack tweak, unless the rcp already specifies it. |
| experiment_attack_tweak | build_body_from_rcp() | Enables access to a limited set of attack tweaks 1/4 of the time. |
| sickness_name | add_poison_bits() | Determines the name of syndromes caused by this creature. |
| poison_state | add_poison_bits() / build_body_from_rcp() | Accepts "LIQUID" (default), "GAS", or "SOLID_POWDER". Determines the state of this creature's venom. |
| prioritize_bite | post_attack_tweaks | If true, non-bite attacks will have `[``PRIORITY``:SECOND]`. If untrue, non-bite attacks will have `[``PRIORITY``:MAIN]`. |
| bite_interaction | post_attack_tweaks | Adds [`[SPECIALATTACK_INTERACTION]`](/index.php/Creature_token#SPECIALATTACK_INTERACTION "Creature token") to bite attacks. |
| can_bogey_polymorph | post_gait_tweaks | Allows the creature to use the bogeyman polymorph interaction. |
| rcp | build_body_from_rcp() / build_description() | Set in / build_body_from_rcp() / from the / rcp / argument. / Usually derived from / random_creature_types / , passes information from the random creature profile. |
| r_class | build_body_from_rcp() | Set to a table in `random_creature_class`. Describes the basic tissues/features a creature has, such as FLESHY, CHITIN_EXO, or UNIFORM. |
| surface | build_body_from_rcp() | The creature's exterior tissue. Set based on its `random_creature_class` and any tweaks. |
| rcm | random_creature_class.UNIFORM.body_fun() | Set by / random_creature_class.UNIFORM.body_fun() / . / If / options.sphere_rcm / is supplied, will use that, otherwise will be randomly chosen based on / options.is_evil / , / options.is_good / , / options.pick_sphere_rcm / , / options.rcp.requires_flexible_material / , and / options.always_insubstantial / . |
| post_mat_adj | build_description() | A string that says "composed of X", etc. Normally supplied by `random_creature_material`. |
| matgloss | random_creature_class.UNIFORM.body_fun() | Temporary data storage when calling inorganic materials from `random_creature_material`. |
| tok1 / tok2 | random_creature_class.UNIFORM.body_fun() | A uniform creature's / \[ / TISSUE_MATERIAL / :options.tok1:options.tok2\] / . / Must be supplied by / random_creature_material / . |
| mat_temp1 / mat_temp2 | random_creature_class.UNIFORM.body_fun() | A uniform creature's / \[ / USE_MATERIAL_TEMPLATE / :options.tok1:options.tok2\] / . / Can be supplied by / random_creature_material / to add an organic material. |
| st_tok | random_creature_class.UNIFORM.body_fun() | A uniform creature's [`[TISSUE_MAT_STATE]`](/index.php/Tissue_definition_token#TISSUE_MAT_STATE "Tissue definition token"). Must be supplied by `random_creature_material`. |
| fixed_temp | random_creature_class.UNIFORM.body_fun() | A uniform creature's / \[FIXED_TEMP\] / . / Can be supplied by / random_creature_material / . If a material template is used, adds / \[MAT_FIXED_TEMP\] / . |
| intangible | build_body_from_rcp() | Flag normally supplied by `random_creature_material`. Creature is non-solid, serves as the condition for `options.intangible_flier`. Limits access to attack tweak. |
| fire_mat | build_body_from_rcp() | Flag normally supplied by `random_creature_material`. Prevents a fire breath attack. |
| body_string | build_body_from_rcp() | An array of all [`[BODY]`](/index.php/Creature_token#BODY "Creature token") tokens used. |
| body_size | build_description() / build_pcg_graphics() | Set by `body_size_properties()`. Stores the creature's volume for later use. |
| body_tweak_candidate | build_body_from_rcp() | Temporary data storage for assigning tweaks. |
| tweak | *quadruped_function_curry()* | Temporary data storage for quadruped leg tweaks. |
| attack_tweak / btc / btc2 | build_body_from_rcp() / build_description() | Strings used as a key to retrieve information about the chosen tweaks. Set by `build_body_from_rcp()` |
| eyes / beak / brain / cheeks / eyelids / guts / heart / lips / lungs / mouth / neck / nose / ribs / skull / spine / teeth / throat / tongue | build_body_from_rcp() | Normally set by the creature's / random_creature_class / (MAMMAL, CHITIN_EXO, etc). / Adds the listed parts to the creature's body plan. |
| blood / ichor / goo | build_body_from_rcp() | Normally set by the creature's / random_creature_class / (MAMMAL, CHITIN_EXO, etc). / Sets the creature's default / \[BLOOD\] / type. |
| force_goo / force_ichor | build_body_from_rcp() | If the creature is not uniform, overwrites the creature's default [`[BLOOD]`](/index.php/Creature_token#BLOOD "Creature token") type. |
| blood_color | build_body_from_rcp() | Expects a function that takes a color's HSV values and returns a boolean. Sets the creature's blood color to any color that returns true for this function. / Only works with standard / blood / from / options.blood / . |
| glowing_eyes / fingers / toes / finger_claws / toe_claws / finger_nails / toe_nails / finger_talons / toe_talons / bat_wings / lacy_wings / feathered_wings / has_proboscis / do_webs | build_procgen_creature() | Set when building the body if the creature has those traits. Can be called by the description and when building graphics. / Nails / , claws, and talons are given attacks. |
| eye_count | build_procgen_creature() | The number of eyes the creature has. Set when building the body. |
| tail_count | build_procgen_creature() | The number of tails the creature has. Can be set before building the body. |
| clp | build_procgen_creature() | The creature's body color. Chosen randomly or based on material unless `rcp.cannot_have_color` is true. |
| eye_clp | build_procgen_creature() | The creature's eye color. Set when building the body. |
| color_f / color_b / color_br | build_body_from_rcp() | Set based on `options.clp` unless `options.forced_color` is supplied. Adds `[``COLOR``:options.color_f:options.color_b:options.color_br]`. |
| forced_color | build_body_from_rcp() | Adds `[``COLOR``:options.forced_color.f:options.forced_color.b:options.forced_color.br]` and [`[NO_UNIT_TYPE_COLOR]`](/index.php/Creature_token#NO_UNIT_TYPE_COLOR "Creature token"). |
| animal_coloring_allowed | build_body_from_rcp() | Color must be a shade of brown. |
| experiment_colors | build_body_from_rcp() | Uses the set of colors assigned to experiments. |
| exp_proc_surface_color | build_pcg_graphics | Stores the index of an experiment's color, for portraits. |
| name_mat / flavor_adj / potential_end_phrase | Custom names | An array of names for a creature's material. Can be supplied by `random_creature_material`. |
| feature_flavor_adj | Custom names | When `build_description()` is run, populates `options.flavor_adj` with strings based on the creature's tweaks and color. |
| can_learn | build_description() | Enables certain description strings, such as "it knows and intones the names of all it encounters". Used by default intelligent creatures. |
| no_extra_description | build_description() | Will not add strings from `default_desc_adds`/`good_desc_adds`/`evil_desc_adds` to the end of the description. |
| custom_desc_func | build_description() | Adds the output of a string instead of `default_desc_adds`/etc. Cannot have `options.no_extra_description.` |
| end_phrase | build_description() | Adds a phrase after all other generated description pieces, such as "Now you know why you fear the night." |
| and_add | build_description() | Temporary storage for description grammar. |
| pref_str | build_description() | A table of possible [`[PREFSTRING]`](/index.php/Creature_token#PREFSTRING "Creature token")s. |
| fallback_pref_str | build_description() | A string that is added to `options.pref_str` it is empty. |
| odor_string / odor_level | build_body_from_rcp() | Sets [`[ODOR_STRING]`](/index.php/Creature_token#ODOR_STRING "Creature token") and [`[ODOR_LEVEL]`](/index.php/Creature_token#ODOR_LEVEL "Creature token") respectively. Can be supplied by `random_creature_material`. |
| forced_odor_string / forced_odor_level forced_odor_chance | build_body_from_rcp() | Sets [`[ODOR_STRING]`](/index.php/Creature_token#ODOR_STRING "Creature token") and [`[ODOR_LEVEL]`](/index.php/Creature_token#ODOR_LEVEL "Creature token") (defaults to 90), 1 in `options.forced_odor_chance` of the time. |
| always_odor | build_body_from_rcp() | Can use the `options.forced_odor_string` even if creature is uniform. |
| pcg_layering | build_pcg_graphics() | A set of procedural graphics layers. Set by `build_pcg_graphics()`. |
| pcg_layering_base | build_pcg_graphics() | The basic PCG layer-set string, concatenated to form `options.pcg_layering` keys. Set by `build_body_from_rcp()`. |
| pcg_layering_modifier | build_pcg_graphics() | A set of extra info for PCG layering, such as experiment skin types. Set by `build_body_from_rcp()`. |
| use_werebeast_pcg | build_pcg_graphics() | If true, use the layers for werebeasts. |
| experiment_layering | build_pcg_graphics() | If true, use the layers for humanoid experiments. Expects `options.experiment_colors` to be true. |
| is_male_version night_creature_strength_pref night_creature_agile_pref night_creature_strength_agile_pref | night_troll_names | Flags used by Night trolls. |
| no_default_werebeast_curse | werebeast_origin_interactions.default() | If this is true for a custom function in creatures.night_creature.werebeast, `generate_from_list(werebeast_origin_interactions,tok,rcp.name_string,options)` will not be able to use werebeast_origin_interactions.default. This allows mods to better control access to werebeast curses. |
| amalgam_experiment / failed_experiment | *experiment_description()* | Flags used for default / experiments / . |
| experiment_name_type | *experiment_name_token* | Array of nouns used instead of `ropar.making_experiment` for naming experiments. |
| is_large | *make_failed_rcp()* | Used for large failed experiments. Capitalizes the creature tile. |
| eadj / fadj | Custom names | Temporary data storage for complex name generation. |

### rcp parameters
