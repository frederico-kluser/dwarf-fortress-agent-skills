# Lua scripting

> Fonte: [Lua scripting](https://dwarffortresswiki.org/index.php/Lua_scripting) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

\

*This article is about procedural raw generation. Information on Utility:DFHack scripting can be found at https://docs.dfhack.org/en/stable/.*

**Lua scripting** is a feature of Dwarf Fortress's modding system. It is used to write definitions for procedurally-generated objects, with the stated goal of "supporting future magical endeavors." [1]

It was added as an experimental feature in version 51.06 [2] and incorporated into the 52.01 release. [3][4]

Inorganic materials, languages, creatures, interactions, items (currently excluding instruments), reactions, entities, and plants are open to this system.

Scripts are loaded from a mod's `scripts/init.lua` file, and can `require()` other files.

## Videos

Announcement video:

- More powerful mods coming to Dwarf Fortress via Lua

Tutorials:

- Generating raws with Lua
- Random creatures with Lua

## Structure

As of right now, Lua scripting is confined to generation of procedural objects. This is done by running the `generate()` function, a global function loaded in **`data/init/generators.lua`**. It runs unit tests, preprocess, do_once (or do_once_early), materials, items, languages, creatures, interactions, entities and postprocessing, in that order.

When random objects are first generated, the game populates two global tables, `world` and `random_object_parameters`.

- `world` contains info about the world currently being generated (or, in the future, played in). It contains worldgen parameters, raw object definitions, and a few other fields.

- `random_object_parameters` contains what the game expects to be generated in the current generation call.

You can print the contents of these tables to the log to see what data is available. The Runtime Dataminer mod includes a script to read these tables.

DFHack also has a version of df.world, though these tables are not necessarily equivalent. Headers and paths may differ, even when referencing the same data.

### Debugging

You can set the global `debug_level` variable to print some debug info. It's a number, but what numbers are there are completely arbitrary. If it's \>0, it'll run unit tests; if it's \>=0.5, it'll display what step of generation it's at, at every step. You can use `get_debug_logger(x)` to return a function that logs to `lualog.txt` if the debug level is at least `x`.

Unit tests are functions that return a table, containing `good`, which, if truthy, is considered passed, and `info`, which is a string that contains information on said pass or fail. These unit tests should have no side effects, i.e. they shouldn't muck with global state any. Here's an example unit test shipped with the generators:

    unittests.get_random_creature

    get_random_creature
    =
    function
    ()

    local

    cr
    =
    world
    .
    creature
    .
    get_random_creature
    ()

    local

    res
    =
    {}

    res
    .
    good
    =
    type
    (
    cr
    )
    ==
    'table'

    res
    .
    info
    =
    res
    .
    good

    and

    (
    "Got a random creature: "
    ..
    cr
    .
    token
    )

    or

    "No random creature could be gotten, even at most permissive!"

    return

    res

    end

### Object generation

When `generate()` is called, it uses `random_object_parameters` to determine what is generated.

Before the world map is generated, `random_object_parameters.pre_gen_randoms` is true for one generation. Once the map is finalized, `random_object_parameters.main_world_randoms` is true for one generation when "generating prehistory"; most of the initial randomization takes place here. Further generation calls, such as for experiments being created, do not set these variables to true.

If you're registering an entirely new procedural object type, you can generate it during these steps. The game includes a number of tables which you can add functions to, the game runs each function in them when generating raws.

- `do_once` only runs in the "main world randoms" generation call and is the safest option for adding new objects.
- `do_once_early` runs in the "pre-gen randoms" generation call, and can be used for objects that need to be placed in the map like minerals or surface animal populations.
- `preprocess` runs before either of the former tables, but is run during every `generate()` call and you cannot predict when this happens.
- `postprocess` runs at the end of each `generate()` call, after the other steps complete.

You can see examples of registering objects through these steps on the Lua script examples page.

If you want to use `preprocess` or `postprocess` to generate raws, you can check if it's the right generation step by reading the aforementioned `random_object_parameters`. The "adamantine alloys" example includes such a check.

You can also mess around with `random_object_parameters` in preprocessing. Vanilla demon types are assigned here, and you can change the proportions as an end user if you want.

#### Generation from list

After `preprocess` and `do_once`, the game then generates all of the individual objects that the `random_object_parameters` expects. The general procedure for this is that the game calls the `generate_from_list()` function on a table of functions, which calls every function and picks one of the resulting values at random depending on their weights.

For example, the `interactions.secrets` table contains one entry, that for necromancers; it returns a table containing three entries: `{raws=tbl,weight=1,spheres=spheres}`.

- `raws` is the full raw text of the interaction.
- `weight` is the random weight for the interaction, i.e. if you add another function which returns a table containing `weight=2`, that will be twice as likely as necromancers.
- `spheres` is some extra data the generator might be able to use. It actually doesn't, at this point, but one could override `generate_random_interactions()` with their own version that takes into account `spheres` and, say, tries to evenly distribute generated secrets over available spheres. (This didn't end up in vanilla primarily out of concerns of bug-like behavior cropping up).

#### Languages

Languages are special, though; as can be seen in the Divine language/script or identity language. The `languages` table just expects to return table containing translations, e.g. `tbl["ABBEY"]="abbey"`. If you want to procedurally add words or symbols (and yes, these are both doable), you can do so with `raws.register_languages()` in another function table.

## Creatures

Creatures have a lot more to them than other procedural objects. Forgotten beasts are, in a sense, the simplest of them:

    creatures.fb.default

    creatures
    .
    fb
    .
    default
    =
    function
    (
    layer_type
    ,
    tok
    )

    local

    tbl
    =
    {}

    local

    options
    =
    {

    strong_attack_tweak
    =
    true
    ,

    spheres
    =
    {
    CAVERNS
    =
    true
    },

    is_evil
    =
    true
    ,

    sickness_name
    =
    "beast sickness"
    ,

    token
    =
    tok

    }

    tbl
    =
    split_to_lines
    (
    tbl
    ,
    [[

        [FEATURE_BEAST]

        [ATTACK_TRIGGER:0:0:2]

        [NAME:forgotten beast:forgotten beasts:forgotten beast]

        [CASTE_NAME:forgotten beast:forgotten beasts:forgotten beast]

        [NO_GENDER]

        [CARNIVORE]

        [DIFFICULTY:10]

        [NATURAL_SKILL:WRESTLING:6]

        [NATURAL_SKILL:BITE:6]

        [NATURAL_SKILL:GRASP_STRIKE:6]

        [NATURAL_SKILL:STANCE_STRIKE:6]

        [NATURAL_SKILL:MELEE_COMBAT:6]

        [NATURAL_SKILL:DODGING:6]

        [NATURAL_SKILL:SITUATIONAL_AWARENESS:6]

        [LARGE_PREDATOR]

        ]]
    )

    add_regular_tokens
    (
    tbl
    ,
    options
    )

    tbl
    [
    #
    tbl
    +
    1
    ]
    =
    layer_type
    ==
    0

    and

    "[BIOME:SUBTERRANEAN_WATER]"

    or

    "[BIOME:SUBTERRANEAN_CHASM]"

    if

    layer_type
    ==
    0

    then

    options
    .
    spheres
    .
    WATER
    =
    true

    end

    options
    .
    spheres
    [
    pick_random
    (
    evil_spheres
    )]
    =
    true

    options
    .
    do_water
    =
    layer_type
    ==
    0

    populate_sphere_info
    (
    tbl
    ,
    options
    )

    local

    rcp
    =
    get_random_creature_profile
    (
    options
    )

    add_body_size
    (
    tbl
    ,
    math.max
    (
    10000000
    ,
    rcp
    .
    min_size
    ),
    options
    )

    tbl
    [
    #
    tbl
    +
    1
    ]
    =
    "[CREATURE_TILE:"
    ..
    tile_string
    (
    rcp
    .
    tile
    )
    ..
    "]"

    build_procgen_creature
    (
    rcp
    ,
    tbl
    ,
    options
    )

    return

    {
    creature
    =
    tbl
    ,
    weight
    =
    1
    }

    end

This is a lot of info! First, you build an `options` table; it's possible to make a full list of options used in vanilla, but other mods can also use arbitrary options. It then adds all the usual special-to-forgotten-beast tokens, in a big string, followed by calling `add_regular_tokens(tbl,options)`, which adds some stuff common to all (vanilla) procedural creatures, based on the options given.

It sets `do_water` and the WATER sphere if the FB is in a water cavern, an option which whitelists certain random creature profiles, as well as adding a random evil sphere.

`populate_sphere_info()` is similar to `add_regular_tokens()`; it adds all of the spheres in `options.spheres` to the creature, using the [`[SPHERE]`](/index.php/Creature_token#SPHERE "Creature token") token, then, if certain options are set, does more.

Then, it gets a random creature profile using `get_random_creature_profile()` and the options, uses `add_body_size()` to set the BODY_SIZE tokens and attendant things that come with it, sets the creature tile, and finally runs the Big Function, `build_procgen_creature()`, which creates the description, body, tissues, et cetera.

### Random Creature Profiles

A random creature profile is a type of "thing" a generated creature can be. For example:

    random_creature_types.GENERAL_QUADRUPED

    GENERAL_QUADRUPED
    =
    {

    name_string
    =
    "quadruped"
    ,

    tile
    =
    'Q'
    ,

    body_base
    =
    "QUADRUPED"
    ,

    c_class
    =
    "UNIFORM"
    ,

    cannot_have_get_more_legs
    =
    true
    ,

    min_size
    =
    70000
    ,

    weight
    =
    1000

    },

Of these, only `cannot_have_get_more_legs` is optional. `build_procgen_creature()` has direct access to the rcp, as the first argument, and thus extra table entries can be used however you like.

`body_base` points to a key in `body_base_fun`, which is used to set creature options (walking and PCG layering are set this way) and returns a list of body tokens. Quadrupeds use a special function to vary the sprite, so here's the body base function for a humanoid.

    body_base_fun.HUMANOID

    HUMANOID
    =
    function
    (
    rcp
    ,
    options
    )

    options
    .
    pcg_layering_base
    =
    "BEAST_HUMANOID"

    options
    .
    walk_var
    =
    "STANDARD_BIPED_GAITS"

    options
    .
    walk_speed
    =
    900

    return

    {
    "RCP_UPPER_BODY"
    ,
    "RCP_LOWER_BODY"
    ,
    "RCP_NECK"
    ,
    "RCP_HEAD"
    ,
    "RCP_TWO_PART_ARMS"
    ,
    "RCP_TWO_PART_LEGS"
    }

    end

`c_class` also refers to another determines the kind of tissue layers the creature has. "FLESHY", "MAMMAL", "CHITIN_EXO", etc imply a biological creature with sinew, blood, different organs, nerves, and so on. "UNIFORM" describes a creature made of a single material, the choice influenced by its options. The `random_creature_class` and `random_creature_material` tables store the info for these traits.

Organic creatures can be tweaked to alter their surfaces, such as becoming skinless, hairy, or even uniform.

### Tweaks

In the broadest sense, a tweak is any deviation from the creature profile. The aforementioned surface changes, new body parts, and attack interactions are all examples of tweaks.

A number of options change the available tweaks or force one to happen, for example:

- `options.no_tweak` disables random tweaks.
- `options.strong_attack_tweak` allows the creature to always pick from the `attack_tweaks` table; ie: "Beware its webs!"
- `options.humanoidable_only` makes the creature "twisted into humanoid form" (if evil), or "a in humanoid form" (if otherwise).

One potential use of `btc1_tweaks` (see Lua functions#Creature patching) is to add custom tweak candidates, pointing to keys in `tweaks`.

### Color pickers

Color picker functions can give more fitting color choices based on the options, instead of the default full spectrum. There are color pickers for certain malevolent spheres, giving them a dark appearance. Werebeasts use a flag to only have natural brown or black colors.

If the creature matches `cond` and a given descriptor color matches `color`, then it is added to the list of candidates. Colors have h,s,v and r,g,b values ranging from 0-1 (except hue, which ranges 0-360 degrees).

    color_picker_functions

    color_picker_functions
    =
    {

    death_misery
    =
    {

    cond
    =
    function
    (
    options
    )

    return

    options
    .
    spheres
    .
    DEATH

    or

    options
    .
    spheres
    .
    MISERY

    end
    ,

    color
    =
    function
    (
    color
    )

    -- GRAY TO BLACK/BLUEISH GREEN THAT ARE SOMEWHAT GRAYISH AND MORE BLUE

    return

    (
    color
    .
    v
    <=
    0.75

    and

    color
    .
    s
    <=
    0.001
    )

    or

    (
    color
    .
    v
    ==
    color
    .
    b

    and

    color
    .
    s
    <=
    0.25
    )

    end

    },

    darkness_night
    =
    {

    cond
    =
    function
    (
    options
    )

    return

    options
    .
    spheres
    .
    DARKNESS

    or

    options
    .
    spheres
    .
    NIGHT

    end
    ,

    color
    =
    function
    (
    color
    )

    -- GRAY TO BLACK OR DARK BLUISH

    return

    color
    .
    v
    <=
    0.4

    and

    (
    color
    .
    s

    <

    0.001

    or

    (
    color
    .
    h
    >
    180

    and

    color
    .
    h
    <=
    240
    ))

    end

    },

    werebeast
    =
    {

    cond
    =
    function
    (
    options
    )

    -- werebeasts only, in vanilla

    return

    options
    .
    animal_coloring_allowed

    end
    ,

    color
    =
    function
    (
    color
    )

    --BROWN OKAY TOO

    return

    color
    .
    h
    >=
    30

    and

    color
    .
    h
    <=
    48

    and

    color
    .
    b
    <=
    0.15

    and

    color
    .
    v
    <=
    0.75

    and

    color
    .
    v

    >

    0

    end

    }

    }

`options.blood_color` works like a color picker function. If any colors match its function, then its blood will be colored like one of them. Bogeymen and nightmares have a function that gives them magenta blood, for example, but you can create your own blood color functions.

Creatures with other blood types, such as ichor, are unaffected.

    options.blood_color (Bogeyman)

    blood_color
    =
    function
    (
    cl
    )

    -- DARKER MAGENTA COLORS

    return

    cl
    .
    h
    >=
    260

    and

    cl
    .
    h

    <=

    340

    and

    cl
    .
    v

    <=

    0.5

    and

    cl
    .
    v

    >=

    0.1

    end
