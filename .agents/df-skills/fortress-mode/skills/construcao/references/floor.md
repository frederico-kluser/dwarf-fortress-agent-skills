# Floor

> Fonte: [Floor](https://dwarffortresswiki.org/index.php/Floor) — Dwarf Fortress Wiki (GFDL/MIT)

A **floor** is a fixed map tile that creatures can walk upon (as opposed to *movable* features like bridges and hatches). A floor can be:

1.  natural, as found on the surface and in caverns
2.  artificial, as created by mining
3.  constructed
4.  implied, by constructing walls on the z-level below

Note that the different types of floors may be combined: constructed floors can be built over natural, artificial, or implied floors; and an implied floor can be added below any other type of floor. Though it is possible to create a floor with an empty tile below, all wall tiles will have an implied floor above them.

Most buildings can be built on any type of floor. Constructions can be built on any non-constructed floor--a constructed floor must be removed before any other construction can be installed.

It is not yet known how different types of floor affect the mood of the dwarves, but it sure is a fact that covering a muddy sand floor with a layer of ash log floor, or anything else for that matter, would be pleasing for any player.

## Constructing floors

Constructed floors can be built *en masse*. To do this, use the uild -\> onstruction -\> loor command. The keys ,, and are used to change size. Floors may be built on any square which does not already contain a structure, provided your dwarves can reach an adjacent square (this includes building a floor over empty air next to a floor, allowing for the construction of massive cantilevered floors). Diagonals cannot be built from, nor will they support constructions.

The important thing to remember is that all floors, walls, and anything built with the - keys are LIFO - "Last In, First Out". That means that the very last designation you make will be the very first thing your builders will work on next! Once you master this concept, it can be used to your advantage, but only if you can plan ahead.

It is also important to remember that you cannot build another construction on top of a constructed floor, but you can build constructions atop natural, artificial and implied floors.

As with all constructions, the "Wall/Floor Construction" labor is required to construct a floor.

When building floors, your builders will carry the material to the job site themselves. A useful tip when building large projects is to first make a stockpile nearby, and only allow one type of material in it. After it fills up, build only as many constructions as there are items in the stockpile. Wait for your haulers to refill the stockpile, then build the next section of the project.

When constructing a floor tile over a walkable tile, the constructing dwarf will move any items in the tile prior to construction. When constructing a floor tile over an unwalkable tile (such as a tree top) any items stuck in the tile will be destroyed when the construction is completed. When constructing a floor over an engraved floor the engravings will be destroyed.

## Removing floors

Natural and artificial floors can be removed by channeling (-); constructed floors can be removed with -. Implied floors may only be removed by deconstructing the wall on the level below. The material used to build the floor will be recovered after the deconstruction. Cave-ins, falling logs from felled trees as well as felling trees growing on soil floors that have had the layer directly under the trunk mined out can also remove floors.

When removing a constructed floor over a natural or artificial floor, the underlying floor will revert to the base layer type (meaning cast obsidian floors are lost).

Removing floors can cause cave-ins if done incorrectly. This often leads to fun if the floor happens to overhang the dining hall or other central area. Floors should **always** be removed in multiple steps, starting at the furthest locations from the support(s) and moving in.

### Examples

Key:

[TABLE]

#### 3×3 floor, supported in middle

This example usually has a staircase in the middle supporting it, instead of a wall below (in that case, there would need to be another access point for dwarves to remove the floor, which would make this example much more complicated).

##### Removing corners first

Floors are **not** supported diagonally, so removing all floor tiles orthogonal to another floor will result in a cave-in.

##### Leaving supports for all corner floors

Dwarves can stand on the red or grey tiles to remove floors. Dwarves will not remove floors that another dwarf is standing on, so if a dwarf decides to stand on a green floor, the removal job could be canceled.

## Bugs

- When removing a constructed floor over a natural or artificial floor, the underlying floor will revert to the base layer type (meaning gem clusters, ore deposits, engravings, etc. that were in the underlying floor are lost).

- An up/down stairway above a wall overrides the implied floor created by the wall. A flying creature can move diagonally into the stairway above the wall, then diagonally back out on the other side of the wall. This shortcut does not work for non-flying creatures (using ramps), nor does it allow liquid to flow through.

- Sometimes when removing flooring, 1/7 deep magma *may* appear in its place.
