# Mysterious dungeon

> Fonte: [Mysterious dungeon](https://dwarffortresswiki.org/index.php/Mysterious_dungeon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

*"This place is dangerous. Steel yourself against ancient enemies. Try not to let yourself be surrounded, and remain standing. Enter and vanquish! Or slip in unseen. Securing the treasure is all that matters."*

— A deity's proclamation to their chosen.

**Mysterious lairs**, **dungeons** and **palaces** ( / ■) are **mythical sites**v51.01-beta26 that can be explored in adventurer mode. They are created in a time before time, with no known founder.

## Structure

All mythic sites have an aboveground room and an underground section. There are a number of common features, such as vertical bars activated by levers, trapped chests, and treasure on a raised floor.

The smallest of the mythic site types, lairs are square buildings with two floors and several floor plans. Dungeons are larger and deeper, often with multiple levers protecting the treasure room.

Palaces are even more elaborate, featuring several floors both above and below ground. The building is circular, like a dark fortress. Many of the inhabitants have a special dungeon guardian syndrome, and the strongest of them can wield a magic weapon: a legendary, masterwork item made from a primordial remnant. The rewards are greater, as pots and jugs filled with healing substances are scattered throughout.

 When inside a mythic site, the atmosphere is described as *"The area gives off a sickly light."*

## Inhabitants

Each site is lead by a dungeon guardian, an immortal historical figure with a unique title (such as "ancient of the trees" or "bark worshipper"). Currently, this guardian has no interactions throughout history, beyond being a member of a "mythic entity". They are equipped with high-quality weapons and armor, and good combat skills to wield them. They also have a waterskin filled with a mythical substance they can drink to heal.

Their title grants them immortality, immunity to blindness, fevers, exertion, and fear; removes their need to eat, sleep, and drink; and prevents their physical attributes from raising or rusting. They are sterile, and their personality is maximally loveless, hateful, violent, cruel, and non-altruistic. Visually, their skin is drawn with the same purple tone as a necromancer, or represented as a ÿ glyph.

A small squad of goblin soldiers (as evil creatures that don't need to eat or drink) also guard these sites. They are worse-equipped and less skilled than the aforementioned guardian.

Mythical sites also have animal populations, with access to "ancient" variants of predators. These creatures can potentially be drawn from the caverns. Mythical animals gain a special prefix inspired by their sphere, with the same effects as the dungeon guardian syndrome. They are tamed and loyal to the site's defenders.

All inhabitants speak the divine language.

## Treasure

Offering service to a religion will start a quest to collect a primordial remnant from a dungeon. The same sphere influences the name of both this object and the creature guarding it.

All types of armor and weapon can be found in chests. It will usually be of good quality, though any armor defaults to being sized for humans. Though the guardian's entity tokens suggest that they should be able to make use of divine metals and fabric, they do not have access to those materials.

Mysterious sites are the only known source of mythical substances and magic items made from primordial remnants.

## Gallery

-

  The floors of a lair.

-

  A simple lair's basement.

-

  Entering a dungeon.

-

  A dungeon's locked treasure room.

-

  Upper floors of a palace viewed in Fortress mode.

## See Also

- Dark fortress
- Vault

    Entity script

    entities
    .
    mythical_guardian
    .
    default
    =
    function
    (
    idx
    ,
    tok
    )

    local

    lines
    =
    {}

    for

    k
    ,
    v

    in

    ipairs
    ({
    "WEAPON"
    ,
    "AMMO"
    ,
    "SHIELD"
    ,
    "ARMOR"
    ,
    "HELM"
    ,
    "GLOVES"
    ,
    "SHOES"
    ,
    "PANTS"
    })

    do

    for

    kk
    ,
    vv

    in

    ipairs
    (
    world
    .
    itemdef
    [
    v
    :
    lower
    ()])

    do

    if

    not

    vv
    .
    generated

    then

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "["
    ..
    v
    ..
    ":"
    ..
    vv
    .
    token
    ..
    (
    rarityless_items
    [
    v
    ]

    and

    ""

    or

    ":COMMON"
    )
    ..
    "]"

    end

    end

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DIVINE_MAT_WEAPONS]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DIVINE_MAT_ARMOR]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DIVINE_MAT_CRAFTS]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DIVINE_MAT_CLOTHING]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CLOTHING]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[TRANSLATION:GEN_DIVINE]"

    return

    {
    entity
    =
    lines
    ,
    weight
    =
    1
    }

    end
