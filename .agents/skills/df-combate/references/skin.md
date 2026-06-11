# Skin

> Fonte: [Skin](https://dwarffortresswiki.org/index.php/Skin) — Dwarf Fortress Wiki (GFDL/MIT)

*This article refers to "hide" in terms of the skin of a creature, for the article on hiding items and buildings, see .*

**Skin** is a tissue layer common to most creatures. Different types of creatures have different types of skin.

- Most mundane creatures have raw hide, which displays in-game as **skin**. This is the only type that can be tanned into leather.
- Arthropod creatures have untannable **chitin**. Much tougher than normal skin, chitin serves as the skeleton of most creatures that have it, meaning damage immediately affects structural function.
- Reptilian creatures and fish generally have untannable **scales**. Somewhat tougher than ordinary skin, scales slightly reduce damage from weaker sources.

Skins (both fresh and rotten) are stored in a refuse stockpile under the names "fresh raw hide" and "rotten raw hide" respectively in the stockpile menu. Each butchering job produces a single skin, but tanning a hide may produce multiple pieces of leather, depending on the creature's size.

## Skin uses

Raw skin can be processed at a tanner's shop by a dwarf with the tanning labor enabled in order to produce leather, or a dwarf with the tanner labor enabled can bring a skin and a bucket of milk of lime to a tanner's shop to produce a sheet of parchment. Skins are automatically tanned if the "Auto tan" order is enabled. If skins are not tanned automatically, you can use your manager to automatically queue "Tan a Hide" jobs, or manually queue jobs from a tanner's shop. Scales and chitin cannot be tanned (aside from shenanigans being done).

## Leather

Leather is used to make low-grade armor and clothing. Leather is also used to make bags, quivers, backpacks, waterskins, clothing, shields, armor, crafts and decorations. The process of making and using leather is part of the meat industry, rather than the clothing industry.

## Modding scales to be usable in leatherworking

If you want to make items out of scale or chitin, add these tokens to SCALE_TEMPLATE or CHITIN_TEMPLATE in material_template_default.txt in the game raws:

        [LEATHER]
        [ITEMS_LEATHER]
        [BUTCHER_SPECIAL:SKIN_TANNED:NONE]

This will make butchering yield several sheets of the creature's scale that are usable in leatherworking, instead of regular unusable scales.

## See also

- Leather
- Meat industry
- Armor
- Paper industry
