# Descriptor color token

> Fonte: [Descriptor color token](https://dwarffortresswiki.org/index.php/Descriptor_color_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

Tokens used to define the descriptive colors used in the game, by dyes, materials and tissues. Not to be confused with the game's color scheme that defines what colors are graphically shown in-game.

## Tokens

|  |  |  |  |
|----|----|----|----|
| Token | Arguments | Usage | Description |
|  NAME | string | Required | What this color will be called in-game. |
|  WORD | tag | Required | Associates the color with any number of words. Historical figures can be named after the color of their TL_COLOR_MODIFIER. Seems to be more notable if that description can only be a single color. |
|  RGB | red:green:blue | Required | Decides the exact color value of the color using the additive RGB system. This color is not shown in-game, but when a randomly generated beast uses this color, their tile color is defined by an approximation of this\[Verify\]. Each value can range from 0-255. |
