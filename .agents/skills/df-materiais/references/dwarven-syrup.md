# Dwarven syrup

> Fonte: [Dwarven syrup](https://dwarffortresswiki.org/index.php/Dwarven_syrup) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Dwarven syrup** is a cooking ingredient made from sweet pods at a farmer's workshop using the "process plants (barrel)" order and the plant processing labor. Five units of dwarven syrup are made from each sweet pod, and one seed per sweet pod will be left over. Dwarven syrup cannot be eaten in its raw state, but can be made into edible food using cooking.

## Bugs

Cooks will only cook syrup and other fluids as a last resort, instead preferring to cook solid foods with solid foods. Bug:2393 For more information, see the kitchen page.

    [USE_MATERIAL_TEMPLATE:EXTRACT:PLANT_EXTRACT_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:frozen dwarven syrup]
        [STATE_NAME_ADJ:LIQUID:dwarven syrup]
        [STATE_NAME_ADJ:GAS:boiling dwarven syrup]
        [MATERIAL_VALUE:20]
        [DISPLAY_COLOR:6:0:0]
        [EDIBLE_RAW]
        [EDIBLE_COOKED]
        [EXTRACT_STORAGE:BARREL]
        [PREFIX:NONE]
