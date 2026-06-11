# Gypsum plaster

> Fonte: [Gypsum plaster](https://dwarffortresswiki.org/index.php/Gypsum_plaster) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Gypsum plaster** powder (or just **plaster powder** on some screens) is produced at a kiln or magma kiln from gypsum, alabaster, selenite, or satinspar (but **not** anhydrite) and an empty bag. The production of gypsum plaster powder requires the furnace operating skill. It is used in the production of plaster casts, an item used by bone doctors to immobilize the broken bones of injured dwarves, serving the same role as splints.

Bags of plaster powder are automatically stored in chests located in hospital zones, provided there is room.

At a kiln, if the option to produce it is unavailable despite meeting all requirements, the command "make plaster powder" in the manager menu should be used.

## Gypsum plaster stockpiles

Gypsum plaster being applied to a wall.

No stockpile options exist for controlling the storage of gypsum plaster - although it is listed under the "Stone/Clay" material groups for Furniture, Blocks, and Finished Goods, these settings have no effect because such objects will never actually be made **of** gypsum plaster; gypsum plaster bags are always stockpiled in the "Furniture/Siege Ammo" category as "Bags", as though they were empty. They will not be stored in barrels or bins.

If you want all your plaster to be stored in your main hospital, simply maximize a limit to 999.

If you want to have a large amount of gypsum plaster stored in dedicated stockpile containing **only** gypsum plaster, you can exploit the hospital storage to force dwarves to move gypsum plaster to a particular location:

1.  Make a new z zone (dormitory for example), a 3×3 square works well for a small stockpile.
2.  After placing the zone, inspect (z) and then specify it as a  hospital.
3.  Set the hospital information ()
4.  Use  to reduce the Thread, Cloth, Splints, Crutches, Buckets and Soap to 0.
5.  Use  to manually type the limit of "Powder for casts" to the maximum (999).
6.  Place an empty chest in the middle of the hospital area (with bfh).
7.  Dwarves should now automatically move any available gypsum bags into the new hospital area. You can inspect the building contents by clicking on it to confirm the gypsum bags are placed inside the container.
8.  Remove the chest (click on it and choose ). The gypsum bags will explode out of the building in a 3x3 grid.
9.  Before the dwarves remove all the powder bags elsewhere, make a stockpile (using p-) under the gypsum bags. Specify the stockpile as only allowing "Furniture/Siege Ammo". Remove all types except for bags.
10. You may remove the hospital area if desired (z \> choose zone \> click ).

    [INORGANIC:PLASTER]
        [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
        [STATE_NAME_ADJ:ALL:gypsum plaster]
        [DISPLAY_COLOR:7:7:1][TILE:'#']
        [SOLID_DENSITY:2787]
        [IS_STONE]
        [HARDENS_WITH_WATER:INORGANIC:GYPSUM]
        [MATERIAL_VALUE:3]
        [NO_STONE_STOCKPILE]
        [STATE_COLOR:ALL_SOLID:IVORY]
