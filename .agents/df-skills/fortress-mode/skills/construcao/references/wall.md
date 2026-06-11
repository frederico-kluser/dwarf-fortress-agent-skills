# Wall

> Fonte: [Wall](https://dwarffortresswiki.org/index.php/Wall) — Dwarf Fortress Wiki (GFDL/MIT)

A **wall** is either a map tile or a construction that blocks access to creatures and fluids; though many creatures can climb many walls. The appearance of a constructed wall is similar to that of a smoothed natural wall, but it works the same as any filled tile composed of stone, clay or soil. Walls either occur naturally (e.g. a Rough-hewn Andesite Wall), or can be constructed. With constructed walls, it is possible to create multi-level buildings such as archery towers complete with roofs by creating floors on the layer above. A wall fills the tile it is in and creates a walkable space above it.

## Digging

As explained on the digging page, naturally occurring walls can be dug out using the igging ine command, or channel command . These tasks are carried out by dwarves with the mining labor activated.

Natural walls can be designated for soothing and enraving to improve the appearance and value of the wall from the menu. These tasks are carried out by dwarves with the stonecutter, engraver labor respectfully activated.

## Construction

Walls can be built *en masse*. To do this, use the uild -\> Costruction -\> wal command. Walls may be built on any square which does not already contain a structure, provided your dwarves can reach an adjacent square (this includes building a wall over empty air next to a floor, allowing for the construction of inverted pyramids). Diagonals cannot be built from, nor will they support constructions.

The important thing to remember is that all walls, floors, or anything built with the - keys are LIFO - "Last In, First Out". That means that the very **last** designation you make will be the very **first** thing your builders will work on next! Once you master this concept, it can be used to your advantage, but only if you can plan ahead.

It is also important to remember that you cannot build on top of a constructed floor, but you can build a wall on top of another constructed wall, even though the upper surface of a wall is otherwise indistinguishable from a constructed floor.

Constructed walls made from stones cannot be smoothed, but can be engraved or carved into fortifications (-ortifications). Unlike constructed fortifications, those created from walls retain an implied floor on the level above. As usual, the fortifications will block movement, but not liquids or small objects such as bolts.

Normal walls are considered 'rough'. By using stone, glass, wood, or metal blocks, higher-quality constructions can be built with increased value. This can be particularly important when trying to maximize the value of a noble's room.

The labor required to perform the construction can be found under Other Jobs, Wall/Floor Construction.

When building walls, your builders will carry the material to the job site themselves. A useful tip when building large projects is to first make a stockpile nearby, and only allow one type of material in it. After it fills up, build only as many constructions as there are items in the stockpile. Wait for your haulers to refill the stockpile, then build the next section of the project.

When constructing a wall over a walkable tile, the constructing dwarf will move any items in the tile prior to construction. When constructing a wall over an unwalkable tile (such as a tree top) any items stuck in the tile will be destroyed when the construction is completed.

### Building walls in damp conditions

When trying to build walls in damp conditions (such as when digging through an aquifer in a soil layer), you need to make sure that the area to be built on *and* the area the dwarf needs to stand on to build from are at 1/7 or 0/7 when you set the order to build the wall.

If the area the dwarf needs to stand on is 2/7 when the wall is designated to be built, then the dwarf will try to build the wall by standing in the space the wall will occupy, and will never complete the work.

If there are multiple areas, then at least one must be at 1/7, and the dwarf may ignore those which were at 2/7 or greater, even if they subsequently drop to 1/7 or dry out entirely.

## Removing Walls

To remove a wall, open the ining (Previously esignation) menu and select Remove Construction. This task will be carried out by a dwarf with the construction removal labor enabled.

## Notes

- Walls do not have any effect on noise.
- If a wall that is the only support for a structure is removed, it will collapse, most likely hurting any dwarves on or around it.
- If a tree is near your wall, sometimes dwarves will climb the wall to climb on the tree. If this happens, dwarves could get hurt from falling out of the tree.

## Bugs

- Dwarves will once again wall themselves out of the fortress (a regression caused by the fix for the "Dwarf cancels construction of Wall: Creature occupying site" errors). To avoid this behavior, make sure the building material you choose is "inside" the fortress (i.e. closer to your fortress center). Manufactured building materials (like blocks) provide much more control of the location, and consequently the direction the dwarf will approach the build site.
