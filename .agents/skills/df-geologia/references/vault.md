# Vault

> Fonte: [Vault](https://dwarffortresswiki.org/index.php/Vault) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|  |  |
|:--:|----|
|  | This article contains **massive spoilers**. If you do not wish to have your game experience spoiled, **do not scroll down**! |

\

\

A **vault** ( / ■) is a site that constitutes the ultimate challenge for any adventurer. Vaults are created by demons during world generation as part of the process of escaping into the world, so disabling demons in advanced world generation also disables vaults. After constructing the vault and a slab, demons enlist the help of a deity with a relevant sphere, and the deity performs a ritual at the vault to bring the demon physically into the world (for example, a god associated with Fortresses may release a demon associated with Fortresses). The slab used in the ritual is then stored in the vault, and various guardian angels make it their duty to defend the vault and the slab against adventurers.

After the demon has been brought into the world, it returns to the underworld spire from which it originally emerged. When history begins, goblin civilizations build a dark fortress around the spire and make it their capital, with the demon their leader. It is not known for certain whether there are always the same number of goblin civilizations as escaped demons.\[Verify\]

Vaults are large cylindrical structures constructed from slade, descending many Z-levels into the ground and filled with a mostly linear chain of rooms (similar to those found in sewers and tombs) occupied by the angelic guardians and containing occasional parkour-esque climbing challenges. Along the way can be found several levers linked to vertical bars which must be raised in order to progress further. At the bottom of the vault is a giant slab inscribed with the demon's true name, and this knowledge allows you to track it down and either banish it or compel it to join you as a companion.

There are three types of angels that can be found in vaults: assistants (bestial creatures with random features and low combat skills), soldiers (sentient humanoids with weapons and armor made of divine materials and Talented-level combat skills), and the archangels (gigantic creatures with size comparable to that of forgotten beasts that possess Grand Master combat skills). Every vault has exactly 50 assistants, 25 soldiers, and one archangel. Vaults will actively replenish themselves with new angels after each visit, meaning the angels must be defeated in one go, without any rest. However, the Archangel will keep the wounds received between runs, so it's possible to defeat it eventually.

### Finding a vault

A discovered vault icon. This particular one was found via DFHack's reveal-hidden-sites script.

In fortress mode, vaults can be found by pressing Y to head to the World Map, then searching under Artifacts for a slab that reads This is a \[stone/metal name\] slab. All craftmanship is of the highest quality. The slab reads "I am \[demon name\],\[translated name\], once of the Underworld. By the fated, I bind myself to this place.

In adventure mode, vaults can be found by repeatedly asking a member of a nearby civilization about the surrounding area, where they will tell you about the nearest sites including the vault, saying The Farmer Urist: \[vault name\] is in \[location\]. In a time before time, the \[demon name\] created \[vault name\]. The size of the radius in which site will be mentioned is limited, its range is still unknown, with the farthest known being 9 tiles away from the map. If the demon is killed during world generation, the vault is likely never mentioned.\
Furthermore, if all civilizations are extinct, you will only be a human outsider in adventure mode, and since you have to start from *some* site, it *can* be a vault.

Attempting to conquer a vault and retrieve its slab will be a difficult challenge for even the best-equipped and skilled adventurer. It is recommended to have at least high physical attributes, mastery of at least one weapon skill, and a breadth of capability in others. The rewards will be worth the effort and risk; knowledge of the slab and the divine armor and weapons from felling angel soldiers will tremendously improve your adventurer.

Conquering a vault in fortress mode through raids is marginally easier due to the more abstract way combat is treated, and if you demand surrender you may sometimes win without a fight. Once you have conquered a vault, some specific types of angels become a playable race in adventure mode.

## Gallery

-

  Artwork of a vault, but the slab spawned elsewhere.\
  *Art by 000Fesbra000*

-

  The slab.

-

  A vault room in the premium version.

## Bugs

|  |
|----|
| "Vault" in other / Languages / Dwarven / : / ubbul / Elven / : / thenaca / Goblin / : / ötak / Human / : / pamnot |

- The slab may not load, or certain rooms may not be connected, preventing players from accessing the final chamber. DFHack may be used to reveal the local map (which will unreveal once the player character moves) and then teleport the player character to the inaccessible area (the player character's id is given by cprobe).
- Alternatively, the "flashstep" command may be used to teleport the player directly to the cursor(from the \[L\]ook key, for example).
- Unlike discovering a river, the vault is only possible to be discovered by fast travel, if you know the location is on a mountain (assume you're using Legends Viewer), you cannot use fast travel to discover it by yourself, unless you ask the nearest civilization from the vault.
- Some entities belonging in the vault might spawn in the wall.
- The slab might spawn on the floor, not on a one tile higher floor surrounded by ramps.
- The slab is not even included in the vault at all. It might be somewhere outside.

    Entity script

    entities
    .
    vault_guardian
    .
    default
    =
    function
    (
    idx
    ,
    tok
    )

    -- first, we have to generate their weird items

    local

    item_token_prefix
    =
    random_object_parameters
    .
    token_prefix
    ..
    "EI"
    ..
    tostring
    (
    idx
    )

    local

    item_info
    =
    generate_from_list
    (
    angel_item_gens
    ,
    item_token_prefix
    )

    raws
    .
    register_items
    (
    item_info
    .
    lines
    )

    local

    lines
    =
    {}

    -- put the weird items into the entity

    for

    k
    ,
    v

    in

    pairs
    (
    item_info
    .
    tokens
    )

    do

    for

    kk
    ,
    vv

    in

    ipairs
    (
    v
    )

    do

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
    k
    ..
    ":"
    ..
    vv
    ..
    (
    rarityless_items
    [
    k
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
