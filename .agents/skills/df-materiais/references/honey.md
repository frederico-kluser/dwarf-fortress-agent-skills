# Honey

> Fonte: [Honey](https://dwarffortresswiki.org/index.php/Honey) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Honey** is a product pressed from a honeycomb. Honey can be made into mead at a still (as a separate task) or used in cooking prepared meals.

Honeycombs are produced by honey bees at a hive, harvested as part of the beekeeping industry. In order to press the honeycomb, you must have a dwarf with the pressing labor active, a screw press, and empty jugs. A wax cake is produced as a byproduct, and a wax worker can use it to create wax crafts in the Craftsdwarf's workshop. Honey is the only animal product that can be brewed, and it, along with royal jelly, are the edible products of bees. Honey has the lowest value of 1, and is brewed into 5 mead, with a value of 2 each.

Honey jugs will be stored either in a finished goods stockpile allowing the storage of "tools" or a food stockpile set to allow "animal extracts - honey bee honey". Turning it into mead works regardless, but if bins are allowed on a finished goods stockpile where honey is stored, hauling of the bins can make the honey temporarily unavailable and force the cooking or brewing jobs to cancel.

Delicious!

|  |
|----|
| "Honey" in other / Languages / Dwarven / : / stetár / Elven / : / arifè / Goblin / : / stoz / Human / : / someg |

    [USE_MATERIAL_TEMPLATE:HONEY:CREATURE_EXTRACT_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:frozen honey bee honey]
        [STATE_NAME_ADJ:LIQUID:honey bee honey]
        [STATE_NAME_ADJ:GAS:boiling honey bee honey]
        [STATE_COLOR:ALL:AMBER]
        [DISPLAY_COLOR:6:0:0]
        [PREFIX:NONE]
        [EDIBLE_VERMIN]
        [EDIBLE_COOKED]
        [EDIBLE_RAW]
        [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_CREATURE_MAT:MEAD]
