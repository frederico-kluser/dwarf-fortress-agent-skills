# Mythical substance

> Fonte: [Mythical substance](https://dwarffortresswiki.org/index.php/Mythical_substance) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

An adventurer about to eat a healing glob.\
*Art by Rumrusher.*

**Mythical substances** are procedurally-generated liquids and globs with magical properties. Each world has a number of differently-named substances, such as "odd jelly" or "peculiar broth," though currently all of them carry the same syndrome.

## Healing potion

A mysterious dungeon's guardian carries a waterskin filled with a restorative substance that they can consume in combat. Ingesting it grants a powerful syndrome that cures nearly all wounds, even regrowing limbs and healing nerve damage. It does not heal blood loss. However, it can allow you to live through Titan fire long enough to stop you from melting.

Creatures that are immune to poison (not `GENERAL_POISON`) do not benefit from this substance.

## See also

- Weather#Evil_weather

    Script

    mythical_healing_adjectives
    =
    {

    "curious"
    ,

    "weird"
    ,

    "odd"
    ,

    "strange"
    ,

    "unusual"
    ,

    "peculiar"

    }

    mythical_healing_liquids
    =
    {

    "liquid"
    ,

    "fluid"
    ,

    "broth"
    ,

    "juice"
    ,

    "goo"
    ,

    "liquor"
    ,

    "solution"

    }

    mythical_healing_alcohols
    =
    {

    liquor
    =
    true

    }

    mythical_healing_globs
    =
    {

    "jelly"
    ,

    "pulp"
    ,

    "wax"
    ,

    "jam"
    ,

    "dough"

    }

    materials
    .
    mythical_healing
    .
    default
    =
    function
    ()

    local

    name_str

    =

    pick_random
    (
    mythical_healing_adjectives
    )

    local

    noun
    =
    ""

    local

    lines
    =
    {}

    if

    one_in
    (
    2
    )

    then

    noun
    =
    pick_random
    (
    mythical_healing_liquids
    )

    name_str
    =
    name_str
    ..
    " "
    ..
    noun

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_NAME_ADJ:LIQUID:"
    ..
    name_str
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_NAME_ADJ:ALL_SOLID:frozen ]"
    ..
    name_str
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MELTING_POINT:9900]"

    else

    noun
    =
    pick_random
    (
    mythical_healing_globs
    )

    name_str
    =
    name_str
    ..
    " "
    ..
    noun

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_NAME_ADJ:LIQUID:molten "
    ..
    name_str
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_NAME_ADJ:ALL_SOLID:]"
    ..
    name_str
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MELTING_POINT:10200]"

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_NAME_ADJ:GAS:boiling "
    ..
    name_str
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BOILING_POINT:12000]"

    populate_monotone_color_pattern
    ()

    local

    col_pat
    =
    pick_random
    (
    monotone_color_pattern
    )

    if

    col_pat

    then

    local

    col

    =

    world
    .
    descriptor
    .
    color
    [
    col_pat
    .
    color
    ]

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_COLOR:ALL:"
    ..
    col
    .
    token
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DISPLAY_COLOR:"
    ..
    col
    .
    col_f
    ..
    ":0:"
    ..
    col
    .
    col_br

    else

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DISPLAY_COLOR:1:0:1]"

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_VALUE:1]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SPEC_HEAT:4181]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[IGNITE_POINT:NONE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[HEATDAM_POINT:NONE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[COLDDAM_POINT:NONE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MAT_FIXED_TEMP:NONE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MOLAR_MASS:1]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[EDIBLE_VERMIN]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[EDIBLE_RAW]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[EDIBLE_COOKED]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DO_NOT_CLEAN_GLOB]"

    if

    mythical_healing_alcohols
    [
    noun
    ]

    then

    -- i'm sure you can think of some alcoholic globs if you want

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ALCOHOL]"

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ENTERS_BLOOD]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [SYNDROME]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [SYN_NAME:"
    ..
    name_str
    ..
    " effect]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [SYN_AFFECTED_CLASS:GENERAL_POISON]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [SYN_INGESTED]"

    --[[ all of this was in a for loop with individual creature effects listed out but (I *think*) the design purpose for that is fulfilled

             by having it all out in Lua anyway, so I'm just going to hardcode it here and if users wanna mod it they can add their own function]]

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_REGROW_PARTS:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT:BP:BY_CATEGORY:ALL:ALL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_CLOSE_OPEN_WOUNDS:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT:BP:BY_CATEGORY:ALL:ALL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_HEAL_TISSUES:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT:BP:BY_CATEGORY:ALL:ALL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_HEAL_NERVES:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT:BP:BY_CATEGORY:ALL:ALL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_STOP_BLEEDING:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT:BP:BY_CATEGORY:ALL:ALL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_REDUCE_PAIN:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT:BP:BY_CATEGORY:ALL:ALL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_REDUCE_DIZZINESS:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_REDUCE_NAUSEA:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_REDUCE_SWELLING:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT:BP:BY_CATEGORY:ALL:ALL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_CURE_INFECTION:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT:BP:BY_CATEGORY:ALL:ALL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_REDUCE_PARALYSIS:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT:BP:BY_CATEGORY:ALL:ALL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "        [CE_REDUCE_FEVER:SEV:100:PROB:100:START:0:PEAK:0:END:12:ABRUPT]"

    return

    {
    mat
    =
    lines
    ,
    weight
    =
    1
    }

    end
