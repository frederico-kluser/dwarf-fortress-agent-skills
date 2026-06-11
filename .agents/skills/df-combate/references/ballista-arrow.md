# Ballista arrow

> Fonte: [Ballista arrow](https://dwarffortresswiki.org/index.php/Ballista_arrow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Ballista arrows** are, essentially, giant arrows, created at a siege workshop and used as ammunition by a ballista. There are two types:

- Simple wooden ballista arrows, which are "assembled" from one unit of wood at the siege workshop by a siege engineer,
- And much stronger metal ones, which first requires the creation of a ballista arrowhead at a metalsmith's forge from three units of metal bars by a weaponsmith, and then final assembly with wood at the siege workshop by a siege engineer.

For wooden arrows, the type of wood that is used impacts its strength, where heavier types of wood such as glumprong or blood thorn are better; for metal arrows, the type of wood used for the shaft is irrelevant because the game treats the entire arrow as being made of metal. Both ballista arrowheads and the completed ballista arrows are stored in the Siege ammo section of Furniture/Siege Ammo stockpiles.

For such a big, cumbersome, inaccurate weapon, wooden ballista arrows are surprisingly ineffective, dealing only comparatively minor amounts of blunt damage. Metal ballista arrows, on the other hand, are extremely lethal, and can kill two fully-grown elephants standing in a line if the arrow hits squarely; any goblins you hit will be smeared all over the space on which they stood.

Creating arrowheads is tedious and resource-consuming, and both catapults and ballistas train the siege operator skill, at the same rate, when used. Since catapults use stones you can literally pick up off of the ground, they're a much better practice platform for your operator, whereas a ballista armed with *metal* arrows is a much stronger actual weapons platform. As such, there's never much reason to produce wooden ballista arrows.

Ballista arrows normally have a range of 200 tiles, but impacting a creature will subtract an amount from that range based on the weight of the arrow: arrows weighing 50Γ or less (i.e. adamantine and every type of wood) subtract 50 tiles per hit, arrows weighing 150Γ or more (i.e. every other vanilla weapons-grade metal) subtract just 5 tiles per hit, and everything in between would scale linearly.

    [ITEM_SIEGEAMMO:ITEM_SIEGEAMMO_BALLISTA]
    [NAME:ballista arrow:ballista arrows]
    [CLASS:BALLISTA]
