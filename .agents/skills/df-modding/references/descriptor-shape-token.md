# Descriptor shape token

> Fonte: [Descriptor shape token](https://dwarffortresswiki.org/index.php/Descriptor_shape_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\
These tokens are used to describe various shapes used in the game. All vanilla shapes are found in `descriptor_shape_standard.txt`.

## Tokens

|  |  |  |  |
|----|----|----|----|
| Token | Arguments | Usage | Description |
|  ADJ | string |  | An adjective to be paired with the name. Can be used multiple times, allowing for variants of the same shape e.g. "thin cross", "tall cross". |
|  CATEGORY | category name |  | A category the shape belongs to, which can be used by the tool token SHAPE_CATEGORY. Vanilla categories are SIMPLE, PLATONIC, and DICE, but any arbitrary category name is allowed. |
|  SIDES | number | dice | The amount of sides of the dice. |
|  GEMS_USE_ADJ |  | gems | Makes gems in this shape use the syntax 'ADJ + material' e.g. "conglomerate gizzard stone". This, GEMS_USE_NOUN or GEMS_USE_ADJ_NOUN must be used for the name of a gem in this shape to show up. |
|  GEMS_USE_ADJ_NOUN |  | gems | Makes gems in this shape use the syntax 'ADJ + material + NAME' e.g. "smooth conglomerate cabochon". This, GEMS_USE_ADJ or GEMS_USE_ADJ_NOUN must be used for the name of a gem in this shape to show up. |
|  GEMS_USE_NOUN |  | gems | Makes gems in this shape use the syntax 'material + NAME' e.g. "point cut conglomerate". This, GEMS_USE_ADJ or GEMS_USE_ADJ_NOUN must be used for the name of a gem in this shape to show up. |
|  NAME | string:plural | Required | The name of the shape. Is not always strictly used, see GEMS_USE_ADJ. |
|  TILE | 'character' or tile number | Required | The tile the shape uses, as an engraving or as an item (gem, die). |
|  WORD | word |  | Effect unknown. |
