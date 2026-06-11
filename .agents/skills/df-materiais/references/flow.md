# Flow

> Fonte: [Flow](https://dwarffortresswiki.org/index.php/Flow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Water filling a channeled out hole.

*The term **flow** can be used to refer to several completely different things in Dwarf Fortress: things like miasma and smoke, and the mechanism by which water and magma move. This article describes the latter.*

**Flow** is a game mechanic used to simulate the motion of **fluids**. The two fluids that exist in *Dwarf Fortress* currently are **water** and **magma**. You can identify fluids that are flowing by looking for a tile that is blinking between `≈` and `~` tiles. If you have turned on SHOW_FLOW_AMOUNTS you will see the fluid **depth** indicator of `1` through `7` instead and will not be able to easily tell if the game considers a tile to be flowing or not. Flow is typically present any time a fluid is in motion, but there are some exceptions which confuse things a bit.

- Note: In the current release, flow does not seem to appear in magma. Magma follows the same rules of fluid motion and flow, it simply doesn't have flow in the sense that would allow it to power a water (*or magma, in the case*) wheel.

## Basic Fluid Motion

**Water** and **magma** both move in much the same way, following a fairly simple set of rules. The only difference between the motion of magma and water is that magma behaves differently with regards to pressure.

Fluids move mostly as one might expect: they will fall straight down if they can, or else they will spread out to the sides. Fluids can flow diagonally on the same z-level, but will never move sideways and down at the same time. Under basic fluid motion, fluid never moves back up, but it can appear to do so if pressure is involved.

Here is a quick example of how fluids can move to adjacent tiles. Also, as water moves to an adjacent tile, flow is generated in both tiles. This flow will remain for a short time before reverting to being non-flowing water. Falling water does *not* generate flow, so only the 3rd example will result in flow (in both tiles).

                           Before (side view)
                           ▒7▒       ▒7▒       ▒
                           ▒ ▒       ▒2▒       ▒7
                           ▒▒▒       ▒▒▒       ▒▒▒▒▒

                           After (side view)
                           ▒ ▒       ▒2▒       ▒
                           ▒7▒       ▒7▒       ▒43
                           ▒▒▒       ▒▒▒       ▒▒▒▒▒

- 1\. Fluids move down
- 2\. Fluids spread out to the sides

These rules are incomplete, however, without consideration of pressure.

## Fluids under pressure, aka Teleportation

Magma, which has no natural pressure, flows according to the rules of basic fluid motion. Water, however, can move by pressure when it falls down on top of full 7/7 water. In addition, pumps create pressure in both water and magma, and water entering the map from a stream or river follows pressure as well.

Fluids moving under **pressure** do not just move to adjacent tiles, they also trace a path through other full tiles of fluid trying to move to more distant tiles. Fluids moving under pressure can effectively teleport through other tiles that are already filled with fluid. When teleporting, fluids do not generate **any** flow, nor will they push objects around.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | 7 | ▒ |   | ▒ |
|   |   |   | B | e | f | o | r | e |   |   |   |   |   |   |   | ▒ | 7 | ▒ |   | ▒ |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | 7 | 7 | 7 | ▒ |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | ▒ |   | ▒ |
|   |   |   | A | f | t | e | r |   |   |   |   |   |   |   |   | ▒ | 7 | ▒ | 7 | ▒ |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | 7 | 7 | 7 | ▒ |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ |

When a fluid tries to move by pressure, it tries to trace a path through full 7/7 fluids going down, and horizontally, but *not* diagonally. In this way it is like basic flow, except that pressure works faster; fluid from the source is teleported to the open space at the end, rather than having to wait for open space to open up at the source via normal flow. This is why, for example, diagonal squeezes in channels make water flow slower (they block pressure, forcing it to only spread out sideways), and why rivers and streams on the map are usually full of 7/7 water until close to the edge of the map where the rules of basic fluid motion are draining the water off the map while pressure teleports new water from the source all the way down to the end.

What's more, unlike basic flow, the path pressure traces can even go back up--but never higher than the z-level of the first 7/7 tile on the path it was tracing. So it may appear that pressure 'pushes fluids up', but in fact it's only teleporting fluid to a level even or lower.

Thus the result is that pressure movement of fluids (especially water) is common and doesn't create very much flow. However rivers and streams still seem to have some kind of flow that powers water wheels, called natural flow.

## Fluid Displacement by Cave-in, aka Pistons

*(see also **magma piston)***

There's one way to push a fluid higher than its starting level, but it might be considered a bug in the flow mechanics and probably will be changed in following versions since it allows for what could be considered exploits.

A *natural* wall of any material **falling** onto either water *or* **magma** will teleport each tile of displaced fluid to open space directly above it, leaving 1 additional tile of open space directly above the wall itself:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   | S | t | a | r | t |   |   |   |   |   |   |   |   |   |   |   |   |   |   | S | t | e | p |   | 1 |   |   |   |   |   |   |   |   |   |   |   |   |   | S | t | e | p |   | 2 |
|   | ▒ |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | ▒ |   | ▒ |   |
|   | ▒ |   | I |   | ▒ |   |   |   | C | o | l | l | a | p | s | e |   |   |   | ▒ |   |   |   | ▒ |   |   |   |   | F | l | u | i | d |   |   |   |   |   | ▒ |   |   |   | ▒ |   |
|   | ▒ |   | ▒ |   | ▒ |   | - | - | - | - | - | - | - | - | - | - | - | \> |   | ▒ |   | 7 |   | ▒ |   | - | - | - | - | - | - | - | - | - | - | - | \> |   | ▒ |   |   |   | ▒ |   |
|   | ▒ |   |   |   | ▒ |   |   |   | S | u | p | p | o | r | t |   |   |   |   | ▒ |   |   |   | ▒ |   |   |   | S | p | r | e | a | d | s |   |   |   |   | ▒ | 2 | 3 | 2 | ▒ |   |
|   | ▒ | ▒ | 7 | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ |   |
|   | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ |   |

When done in a u-bend example, the pushing above original fluid level can be easily appreciated, although it breaks the laws of regular fluid physics:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   | S | t | a | r | t |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | S | t | e | p |   | 1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | S | t | e | p |   | 2 |   |   |   |   |   |
|   | ▒ |   | ▒ |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | ▒ |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | ▒ |   | ▒ |   | ▒ |   |   |   |   |
|   | ▒ |   | I |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   |   |
|   | ▒ |   | ▒ |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   |   |
|   | ▒ |   | ▒ |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | 7 |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   |   |
|   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   | C | o | l | l | a | p | s | e |   |   |   | ▒ |   | 7 |   | ▒ |   | ▒ |   |   |   |   | F | l | u | i | d |   |   |   |   |   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   |   |
|   | ▒ |   |   |   | ▒ |   | ▒ |   | - | - | - | - | - | - | - | - | - | - | - | \> |   | ▒ |   |   |   | ▒ |   | ▒ |   | - | - | - | - | - | - | - | - | - | - | - | \> |   | ▒ | 5 | 4 | 5 | ▒ |   | ▒ |   |   |   |   |
|   | ▒ | ▒ | 7 | ▒ | ▒ | 7 | ▒ |   |   |   | S | u | p | p | o | r | t |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | 7 | ▒ |   |   |   | S | p | r | e | a | d | s |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | 7 | ▒ |   |   |   |   |
|   | ▒ | ▒ | 7 | 7 | 7 | 7 | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | 7 | 7 | 7 | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | 7 | 7 | 7 | ▒ |   |   |   |   |
|   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |

This is the basic principle that the **magma piston** exploits, if you want to anticipate a future fix or simply want to simulate regular physics fluid behaviour, you can do something like this:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   | z | - | l | e | v | e | l |   |   |   | S | t | a | r | t |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | S | t | e | p |   | 1 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | S | t | e | p |   | 2 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | z | + | 0 |   |   |   | ▒ |   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | ▒ |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | z | - | 1 |   |   |   | ▒ |   | \| |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | z | - | 2 |   |   |   | ▒ |   | ▒ |   | ▒ |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | 7 |   | 7 |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | z | - | 3 |   |   |   | ▒ |   | ▒ |   | ▒ |   | ▒ |   | ▒ |   |   |   | C | o | l | l | a | p | s | e |   |   |   | ▒ |   | 7 |   | 7 |   | ▒ |   | ▒ |   |   |   |   | F | l | u | i | d |   |   |   |   |   | ▒ |   |   |   |   |   | ▒ |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | z | - | 4 |   |   |   | ▒ |   |   |   |   |   | ▒ | ? | ▒ |   | - | - | - | - | - | - | - | - | - | - | - | \> |   | ▒ |   |   |   |   |   | ▒ | ? | ▒ |   | - | - | - | - | - | - | - | - | - | - | - | \> |   | ▒ | 5 | 5 | 4 | 5 | 5 | ▒ | ? | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | z | - | 5 |   |   |   | ▒ | ▒ | 7 | 7 | 7 | ▒ | ▒ | 7 | ▒ |   |   |   | S | u | p | p | o | r | t |   |   |   |   | ▒ | ▒ | ▒ | 7 | ▒ | ▒ | ▒ | 7 | ▒ |   |   |   | S | p | r | e | a | d | s |   |   |   |   | ▒ | ▒ | ▒ | 7 | ▒ | ▒ | ▒ | 7 | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | z | - | 6 |   |   |   | ▒ | ▒ | 7 | 7 | 7 | 7 | 7 | 7 | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | 7 | ▒ | 7 | 7 | 7 | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | 7 | ▒ | 7 | 7 | 7 | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | z | - | 7 |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | z | - | 3 |   | T | o | p |   | V | i | e | w |   |   |   |   |   |   |   |   |   |   |   | z | - | 5 |   | T | o | p |   | V | i | e | w |   |   |   |   |   |   |   |   |   |   |   | z | - | 3 |   | T | o | p |   | V | i | e | w |   | ( | S | t | e | p |   | 1 | ) |   | z | - | 4 |   | T | o | p |   | V | i | e | w |   | ( | S | t | e | p |   | 2 | ) |
|   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ▒ |   |   |   |   |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   |   |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | 4 | 4 | 5 | 4 | 4 | ▒ |   |   |   |   |   |   |   |   |   |   |
|   |   | A | x | i | s |   |   |   | ▒ |   | ▒ | ▒ | ▒ |   | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | 7 | 7 | 7 | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | 7 | 7 | 7 |   | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | 4 | 5 | 5 | 5 | 4 | ▒ | ▒ | ▒ |   |   |   | A | x | i | s |   |
|   | - | - | - | - | - | - | - | - | ▒ |   | ▒ |   | ▒ |   | ▒ |   | ▒ | - | - | - | - | - | - | - | - | - | - | - | - | - | - | ▒ | ▒ | 7 | 7 | 7 | ▒ | ▒ | 7 | ▒ | - | - | - | - | - | - | - | - | - | - | - | - | - | - | ▒ |   | 7 |   | 7 |   | ▒ | ? | ▒ | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | ▒ | 5 | 5 | 4 | 5 | 5 | ▒ | ? | ▒ | - | - | - | - | - | - | - | - |
|   |   | C | u | t |   |   |   |   | ▒ |   | ▒ | ▒ | ▒ |   | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | 7 | 7 | 7 | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   | 7 | 7 | 7 |   | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | 4 | 5 | 5 | 5 | 4 | ▒ | ▒ | ▒ |   |   |   |   | C | u | t |   |
|   |   |   |   |   |   |   |   |   | ▒ |   |   |   |   |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ |   |   |   |   |   | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | 4 | 4 | 5 | 4 | 4 | ▒ |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |   |   |   |   |   |   |   |   |   |   |

This example involves dropping a giant *(minimum size 3x3x1)* donut/cylinder/tube of natural walls onto the fluid pool, given that it will teleport a donut/cylinder/tube of fluid in the same way *(step 1)* but after it spreads *(step 2)* it'll seem that the fluid actually went through the opening in the middle of the donut/cylinder/tube like a real fluid should behave, of course one exception it won't be pushed through the right tube like it should, you'll probably want to close the tile marked with a question mark "?" so it can give the impression of real fluid mechanics.

## Natural Flow

Many water sources such as rivers and brooks are constantly flowing with **natural flow**. This is different from other flow effects in that it is always considered to be flowing water. This remains true even when the water flows into a complete dead end channel or even when blocked off with a floodgate. Any channels that link up to a naturally flowing source will soon become naturally flowing water as long as they remain on the same z-level. Diagonal steps have no effect on natural flow although they can be used to change pressure.

Trying to move natural flow up or down to a different z-level may have unpredictable results. Pumping water from rivers and brooks on the surface always results in naturally flowing water. Water falling to a lower z-level almost never becomes naturally flowing. Draining water into aquifers is very likely to create natural flow, even if water is pumped from one channel to another. Draining water off the map edges horizontally through caverns or fortifications is the only way to create a natural flow underground.

Naturally flowing water, depending on its environment, flows in a specific direction - when SHOW_FLOW_AMOUNTS is disabled, water which flows directly into a wall will flash white while other water remains blue. This flow direction is important to note, since it affects the operation of water wheels: water which flows directly north or south will not power an east/west-aligned water wheel, and the opposite is also true. Diagonally flowing water, however, works for everything.

## Fluid Depth

Fluids can have a depth anywhere from 1 to 7. To see the depth of a tile of fluid you can look at it with k which will reveal the depth in the text at the right. Alternatively you can enable SHOW_FLOW_AMOUNTS which will replace the `≈` and `~` tiles with a numerical representation of the depth at all times. Turning on SHOW_FLOW_AMOUNTS does come with the drawback that you will no longer be able to see if a tile is flowing or not.

## Obstructions

Water can be stopped by most solid tiles. These include walls and buildings as well as closed floodgates, doors, and hatches. Exceptions are vertical grates, vertical bars, and fortifications, which will allow fluids to pass freely.

## Evaporation

Fluids that remain at a depth of 1/7 for long enough will evaporate. Evaporated fluids are simply removed from the game. In **hot** or **scorching** environments, murky pools can evaporate at greater depths.

## Bugs

- Flowing water seems to cause contaminants to multiply Bug:296
