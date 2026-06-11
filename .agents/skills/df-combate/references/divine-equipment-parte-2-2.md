# Divine equipment (parte 2/2)

    ]
    =
    "[ITEM_AMMO:"
    ..
    prefix
    ..
    "WP_A"
    ..
    tostring
    (
    i
    )
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    ammo
    .
    BOLT
    ).
    item
    )

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    ammo
    .
    BLOWDART
    .
    narrow
    =
    function
    ()

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:blowdart:blowdarts]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:narrow]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CLASS:BLOWDART]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:20]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:1:50:stick:sticks:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    ammo
    .
    BLOWDART
    .
    thick
    =
    function
    ()

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:blowdart:blowdarts]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:thick]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CLASS:BLOWDART]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:40]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:2:50:stick:sticks:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    ammo
    .
    BLOWDART
    .
    tapered
    =
    function
    ()

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:blowdart:blowdarts]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:narrow]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CLASS:BLOWDART]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:30]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:1:50:stick:sticks:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    ammo
    .
    BLOWDART
    .
    double
    =
    function
    ()

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:blowdart:blowdarts]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:double-tipped]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CLASS:BLOWDART]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:25]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:2:50:stick:sticks:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    BLOWGUN
    .
    gen
    .
    blowgun
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:blowgun:blowguns]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    BOW
    .
    adj
    )
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
    "[SIZE:150]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:SWORD]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[RANGED:BLOWGUN:BLOWDART]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SHOOT_FORCE:100]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SHOOT_MAXVEL:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:2]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:10000:4000:bash:bashes:NO_SUB:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_AMMO:"
    ..
    prefix
    ..
    "WP_A"
    ..
    tostring
    (
    i
    )
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    ammo
    .
    BLOWDART
    ).
    item
    )

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    AXE
    .
    gen
    .
    battle
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:battle axe:battle axes]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:800]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:AXE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:47500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:42500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:4]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:40000:6000:hack:hacks:NO_SUB:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:40000:6000:slap:slaps:flat:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    AXE
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    AXE
    .
    gen
    .
    halberd
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:halberd:halberds]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:1200]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:AXE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:77500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:62500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:5]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:20000:8000:slash:slashes:NO_SUB:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:50:2000:stab:stabs:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:20000:6000:bash:bashes:shaft:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    AXE
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    AXE
    .
    gen
    .
    great
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:great axe:great axes]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:1300]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:AXE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:77500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:62500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:5]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:60000:8000:hack:hacks:NO_SUB:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:60000:8000:slap:slaps:flat:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    AXE
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    gen
    .
    dagger
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:dagger:daggers]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:200]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:DAGGER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:27500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:1]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:1000:800:slash:slashes:NO_SUB:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:5:1000:stab:stabs:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:20:600:strike:strikes:pommel:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    gen
    .
    knife
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:knife:knives]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:200]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:DAGGER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:27500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:1]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:1000:800:slash:slashes:NO_SUB:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:5:1000:stab:stabs:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    gen
    .
    nail
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:nail:nails]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:200]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:DAGGER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:27500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:1]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:5:1000:stab:stabs:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    gen
    .
    spike
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:spike:spikes]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:200]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:DAGGER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:27500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:1]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:5:1000:stab:stabs:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    gen
    .
    prong
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:prong:prongs]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:200]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:DAGGER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:27500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:1]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:5:1000:stab:stabs:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    DAGGER
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    MACE
    .
    gen
    .
    mace
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:mace:maces]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:800]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:MACE]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:37500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:32500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:20:200:bash:bashes:NO_SUB:2000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    MACE
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    HAMMER
    .
    gen
    .
    war_hammer
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:war hammer:war hammers]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:400]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:HAMMER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:37500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:32500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:10:200:bash:bashes:NO_SUB:2000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    HAMMER
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    HAMMER
    .
    gen
    .
    maul
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:maul:mauls]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:1300]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:HAMMER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:77500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:62500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:5]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:100:6000:bash:bashes:NO_SUB:2000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    HAMMER
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    weapon
    .
    SPEAR
    .
    gen
    .
    spear
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:spear:spears]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SIZE:400]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SKILL:SPEAR]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TWO_HANDED:47500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MINIMUM_SIZE:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:EDGE:20:10000:stab:stabs:NO_SUB:1000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ATTACK:BLUNT:10000:6000:bash:bashes:shaft:1250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "    [ATTACK_PREPARE_AND_RECOVER:3:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    weapon
    .
    SPEAR
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_info
    .
    shield
    .
    gen
    .
    shield
    =
    function
    (
    i
    ,
    prefix
    )

    local

    lines
    =
    {}

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:shield:shields]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ARMORLEVEL:2]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BLOCKCHANCE:20]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[UPSTEP:2]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_SIZE:4]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    shield
    .
    adj
    )
    ..
    "]"

    return

    {
    item
    =
    lines
    ,
    weight
    =
    1
    }

    end

    angel_item_gens
    =
    {}

    angel_item_gens
    .
    default
    =
    function
    (
    prefix
    ,
    tokens
    )

    local

    weapon_num
    =
    5

    local

    shield_num
    =
    1

    local

    a_pants_num
    =
    1

    local

    c_pants_num
    =
    1

    local

    a_armor_num
    =
    1

    local

    c_armor_num
    =
    1

    local

    a_helm_num
    =
    1

    local

    c_helm_num
    =
    1

    local

    a_gloves_num
    =
    1

    local

    c_gloves_num
    =
    1

    local

    a_shoes_num
    =
    1

    local

    c_shoes_num
    =
    1

    local

    lines
    =
    {}

    local

    tokens
    =
    {

    WEAPON
    =
    {},

    AMMO
    =
    {},

    SHIELD
    =
    {},

    ARMOR
    =
    {},

    HELM
    =
    {},

    GLOVES
    =
    {},

    SHOES
    =
    {},

    PANTS
    =
    {}

    }

    for

    i
    =
    1
    ,
    a_pants_num

    do

    local

    tok
    =
    prefix
    ..
    "APN"
    ..
    tostring
    (
    i
    )

    tokens
    .
    PANTS
    [
    #
    tokens
    .
    PANTS
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_PANTS:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    armor
    .
    pants
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    armor
    .
    pants
    .
    adj
    )
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
    "[METAL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[HARD]"

    end

    for

    i
    =
    1
    ,
    c_pants_num

    do

    local

    tok
    =
    prefix
    ..
    "CPN"
    ..
    tostring
    (
    i
    )

    tokens
    .
    PANTS
    [
    #
    tokens
    .
    PANTS
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_PANTS:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    clothing
    .
    pants
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    clothing
    .
    pants
    .
    adj
    )
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
    "[SOFT]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STRUCTURAL_ELASTICITY_WOVEN_THREAD]"

    end

    for

    i
    =
    1
    ,
    a_armor_num

    do

    local

    tok
    =
    prefix
    ..
    "AAR"
    ..
    tostring
    (
    i
    )

    tokens
    .
    ARMOR
    [
    #
    tokens
    .
    ARMOR
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_ARMOR:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    armor
    .
    armor
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    armor
    .
    armor
    .
    adj
    )
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
    "[HARD]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[METAL]"

    end

    for

    i
    =
    1
    ,
    c_armor_num

    do

    local

    tok
    =
    prefix
    ..
    "CAR"
    ..
    tostring
    (
    i
    )

    tokens
    .
    ARMOR
    [
    #
    tokens
    .
    ARMOR
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_ARMOR:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    clothing
    .
    armor
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    clothing
    .
    armor
    .
    adj
    )
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
    "[SOFT]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STRUCTURAL_ELASTICITY_WOVEN_THREAD]"

    end

    for

    i
    =
    1
    ,
    a_helm_num

    do

    local

    tok
    =
    prefix
    ..
    "AHM"
    ..
    tostring
    (
    i
    )

    tokens
    .
    HELM
    [
    #
    tokens
    .
    HELM
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_HELM:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    armor
    .
    helm
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    armor
    .
    helm
    .
    adj
    )
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
    "[HARD]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[METAL]"

    end

    for

    i
    =
    1
    ,
    c_helm_num

    do

    local

    tok
    =
    prefix
    ..
    "CHM"
    ..
    tostring
    (
    i
    )

    tokens
    .
    HELM
    [
    #
    tokens
    .
    HELM
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_HELM:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    clothing
    .
    helm
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    clothing
    .
    helm
    .
    adj
    )
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
    "[SOFT]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STRUCTURAL_ELASTICITY_WOVEN_THREAD]"

    end

    for

    i
    =
    1
    ,
    a_gloves_num

    do

    local

    tok
    =
    prefix
    ..
    "AGL"
    ..
    tostring
    (
    i
    )

    tokens
    .
    GLOVES
    [
    #
    tokens
    .
    GLOVES
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_GLOVES:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    armor
    .
    gloves
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    armor
    .
    gloves
    .
    adj
    )
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
    "[METAL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[HARD]"

    end

    for

    i
    =
    1
    ,
    c_gloves_num

    do

    local

    tok
    =
    prefix
    ..
    "CGL"
    ..
    tostring
    (
    i
    )

    tokens
    .
    GLOVES
    [
    #
    tokens
    .
    GLOVES
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_GLOVES:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    clothing
    .
    gloves
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    clothing
    .
    gloves
    .
    adj
    )
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
    "[SOFT]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STRUCTURAL_ELASTICITY_WOVEN_THREAD]"

    end

    for

    i
    =
    1
    ,
    a_shoes_num

    do

    local

    tok
    =
    prefix
    ..
    "ASH"
    ..
    tostring
    (
    i
    )

    tokens
    .
    SHOES
    [
    #
    tokens
    .
    SHOES
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_SHOES:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    armor
    .
    shoes
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    armor
    .
    shoes
    .
    adj
    )
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
    "[METAL]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[HARD]"

    end

    for

    i
    =
    1
    ,
    c_shoes_num

    do

    local

    tok
    =
    prefix
    ..
    "CSH"
    ..
    tostring
    (
    i
    )

    tokens
    .
    SHOES
    [
    #
    tokens
    .
    SHOES
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_SHOES:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    clothing
    .
    shoes
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ADJECTIVE:"
    ..
    pick_random
    (
    angel_item_info
    .
    clothing
    .
    shoes
    .
    adj
    )
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
    "[SOFT]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STRUCTURAL_ELASTICITY_WOVEN_THREAD]"

    end

    local

    available_skills
    =
    {

    "PIKE"
    ,

    "WHIP"
    ,

    "BOW"
    ,

    "BLOWGUN"
    ,

    "AXE"
    ,

    "SWORD"
    ,

    "DAGGER"
    ,

    "MACE"
    ,

    "HAMMER"
    ,

    "SPEAR"
    ,

    "CROSSBOW"

    }

    for

    i
    =
    1
    ,
    weapon_num

    do

    local

    tok
    =
    prefix
    ..
    "WP"
    ..
    tostring
    (
    i
    )

    tokens
    .
    WEAPON
    [
    #
    tokens
    .
    WEAPON
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_WEAPON:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    local

    skill
    =
    pick_random_no_replace
    (
    available_skills
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    weapon
    [
    skill
    ].
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    end

    for

    i
    =
    1
    ,
    shield_num

    do

    local

    tok
    =
    prefix
    ..
    "SH"
    ..
    tostring
    (
    i
    )

    tokens
    .
    SHIELD
    [
    #
    tokens
    .
    SHIELD
    +
    1
    ]
    =
    tok

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEM_SHIELD:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    table_merge
    (
    lines
    ,
    generate_from_list
    (
    angel_item_info
    .
    shield
    .
    gen
    ,
    i
    ,
    prefix
    ).
    item
    )

    end

    return

    {
    lines
    =
    lines
    ,
    weight
    =
    1
    ,
    tokens
    =
    tokens
    }

    end


---
*Parte 2 de 2 de «Divine equipment». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Divine_equipment*
