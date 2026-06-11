# Item definition token

> Fonte: [Item definition token](https://dwarffortresswiki.org/index.php/Item_definition_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\
**Item definition tokens** are used in item definitions in the raws.

Item types:

- ITEM_AMMO - ammo token
- ITEM_ARMOR - armor-type armor token
- ITEM_FOOD - see below
- ITEM_GLOVES - gloves-type armor token
- ITEM_HELM - helm-type armor token
- ITEM_INSTRUMENT - instrument token
- ITEM_PANTS - pants-type armor token
- ITEM_SHIELD - shield-type armor token
- ITEM_SHOES - shoes-type armor token
- ITEM_SIEGEAMMO - see below
- ITEM_TOOL - tool token
- ITEM_TOY - see below
- ITEM_TRAPCOMP - trap component token
- ITEM_WEAPON - weapon token

## Toy tokens

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  NAME | singular:plural | What this item will be called in-game. |
|  HARD_MAT |  | Presumably prevents the item from being made from cloth, silk, or leather, present on everything but puzzleboxes and drums. Appears to work backwards for strange moods. |

## Siege ammo tokens

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  NAME | singular:plural | What this item will be called in-game. |
|  CLASS |  | Specifies what type of siege engine uses this ammunition. Currently, only BALLISTA is permitted. |

## Food tokens

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  NAME | singular:plural | What this item will be called in-game. |
|  LEVEL |  | Specifies the number of ingredients that are used in this type of prepared meal - 2 for Easy, 3 for Fine, 4 for Lavish. Defaults to 2. |

For example, see item_food.txt

## See Also

- Item token
