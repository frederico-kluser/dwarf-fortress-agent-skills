# Blowdart

> Fonte: [Blowdart](https://dwarffortresswiki.org/index.php/Blowdart) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **blowdart** is a pointed projectile designed to be fired from a blowgun, a weapon normally only used by subterranean animal people. They consist of a wooden, bone, or metal spine, generally with some sort of plug to build pressure (unlike real life, blowdarts are made from only one material).

Blowguns are very difficult to acquire in fortress mode since dwarves cannot normally manufacture them, and none of the standard trading races produce them. If your dwarves do manage to procure a blowgun (as the result of a strange mood, or looted from indigenous animal people), they will find blowdarts even more difficult to obtain. Blowdarts can also be thrown or used in melee, though there are much better weapons.

As if blowdarts weren't handicapped enough, their reduced size, penetration, and speed make them strictly inferior to other projectiles, and the lack of any way to apply poison makes them even more underwhelming.

## Creating blowdarts

While blowdarts are nearly impossible to obtain in a standard game, the DFHack command "changeitem s ITEM_AMMO_BLOWDARTS" can be used to turn a selected stack of bolts into blowdarts. These blowdarts can then be exposed to a syndrome-causing contaminant to simulate poison.

## Bugs

- If a squad is assigned multiple ammo types, dwarves with "individual choice ranged" carry the wrong ammoBug:1374.

    [ITEM_AMMO:ITEM_AMMO_BLOWDARTS]
    [NAME:blowdart:blowdarts]
    [CLASS:BLOWDART]
    [SIZE:20]
    [ATTACK:EDGE:1:50:stick:sticks:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
