# Royal jelly

> Fonte: [Royal jelly](https://dwarffortresswiki.org/index.php/Royal_jelly) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Royal jelly** is a product of the beekeeping industry collected from an artificial bee hive. Royal jelly is stored in jugs, and can only be used as a liquid ingredient in prepared meals. Due to a bug, dwarves may store royal jelly jugs as finished goods; combined with a cook's aversion to liquid ingredients, it is very rare to see royal jelly cooked at all. That isn't necessarily a bad thing, though, since royal jelly is only available in single-unit stacks and has the same base value as most other foods.

The contents of a hive with a colony of honey bees that is toggled to "gather any products" will be harvested as part of the beekeeping industry. In order to collect the royal jelly, you must have a dwarf with the beekeeping labor active and empty jugs. A honeycomb will also be produced.

Royal jelly and honey are the edible products of bees. In real life, it is used as a nutritional substance for larvae.

Nutrition for larvae.

## Bugs

- Jugs of royal jelly may be stored in bins as finished goods, preventing its use in the food industry.Bug:4229
- Collecting royal jelly may require more than 1 jug in storage to begin.
- Cooks will only cook jelly and other fluids as a last resort, instead preferring to cook solid foods with solid foods.Bug:2393 For more information, see the kitchen page.

    [USE_MATERIAL_TEMPLATE:ROYAL_JELLY:CREATURE_EXTRACT_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:frozen honey bee royal jelly]
        [STATE_NAME_ADJ:LIQUID:honey bee royal jelly]
        [STATE_NAME_ADJ:GAS:boiling honey bee royal jelly]
        [STATE_COLOR:ALL:WHITE]
        [DISPLAY_COLOR:7:0:1]
        [PREFIX:NONE]
        [EDIBLE_VERMIN]
        [EDIBLE_COOKED]
        [EDIBLE_RAW]
