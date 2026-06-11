# Graphics token

> Fonte: [Graphics token](https://dwarffortresswiki.org/index.php/Graphics_token) — Dwarf Fortress Wiki (GFDL/MIT)

The `[OBJECT:GRAPHICS]` token defines the use of various tile-based graphics in the game. As of version 50.01, graphics tokens have been greatly expanded to accommodate the release of the Steam & Itch premium version. These tokens, and explanations on how to use them, are listed below; the list will expand as the tokens are discovered and understood.

## Creature Graphics

Creature graphics are found within graphics_creature_x files (such as graphics_creature_domestic or graphics_creature_layered). All graphics files must begin with the file name, followed by the `[OBJECT:GRAPHICS]` type that tells the game that the file contains graphics definitions. A more detailed explanation on how to use these can be found in creature graphics.

### Types

[TABLE]

### Basic Conditions

Different graphics can be defined for the same creature based on some properties about it. Below is a list of all conditions that can be used for creature graphics that accept a *condition* token.

[TABLE]

### Layered Conditions

Layers aren't very useful on their own, so they come with a set of conditions to define how when they are displayed and how they interact.

[TABLE]

### Vermin Conditions

Special Conditions for creature graphics:

[TABLE]

## Item Graphics

Item graphics can also be defined, but are mostly hardcoded. This section of the wiki needs to be fleshed out. Descriptions of the token functions is provisional.

Item graphics currently do not support LARGE_IMAGE.

[TABLE]

## World Map Graphics

World map graphics are defined in `Dwarf Fortress``\data\vanilla\vanilla_world_map\graphics\graphics_world_map.txt` Tokens that accept variants have 5 of them:

`   [TILE_GRAPHICS:::::1]`\
`   [TILE_GRAPHICS:::::2]`\
`   [TILE_GRAPHICS:::::3]`\
`   [TILE_GRAPHICS:::::4]`\
`   [TILE_GRAPHICS:::::5]`

Otherwise:

`  [TILE_GRAPHICS::::]`

## See Also

- Creature token
- Syndrome
- Creature examples
