# Path

> Fonte: [Path](https://dwarffortresswiki.org/index.php/Path) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Pathing** is a videogame concept that refers to the path an AI selected to route from point A to B. It has important implications for fortress design, security design and framerate management.

## Basic movement

Creatures can move in the four cardinal directions (north, south, east, and west), and four diagonal directions (northeast, southeast, southwest, northwest), as long as the target space is not blocked. This means creatures can path through diagonal gaps. For example, this rat (`r`) can reach the cheese (`%`):

|  |  |
|----|----|
| r | ░ |
| ░ | % |

Creatures can move directly up or down, as long as the target space is not blocked and the movement is possible (via flying, climbing, swimming, stairs, etc.). Creatures can move diagonally across Z-levels only when both lateral and vertical movement are simultaneously possible (e.g., when using a ramp), with one exception[1] (see below). For example, this giant sparrow (`S`) can not attack the cat (`c`):

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| S | ░ | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| T | h | i | s |   | d | i | a | g | r | a | m |   | h | a | s |   | m | u | l | t | i | p | l | e |   | z | - | l | e | v | e | l | s | ! |   | P | r | e | s | s |
| \ |   | t | o |   | g | o |   | u | p |   | o | n | e |   | z | - | l | e | v | e | l | . |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ░ | ░ | ░ | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ░ |   | c | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ░ | ░ | ░ | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| T | h | i | s |   | d | i | a | g | r | a | m |   | h | a | s |   | m | u | l | t | i | p | l | e |   | z | - | l | e | v | e | l | s | ! |   | P | r | e | s | s |
| \> |   | t | o |   | g | o |   | d | o | w | n |   | o | n | e |   | z | - | l | e | v | e | l | . |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   | ░ | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| T | h | i | s |   | d | i | a | g | r | a | m |   | h | a | s |   | m | u | l | t | i | p | l | e |   | z | - | l | e | v | e | l | s | ! |   | P | r | e | s | s |
| \> |   | t | o |   | g | o |   | d | o | w | n |   | o | n | e |   | z | - | l | e | v | e | l | . |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

### Exception for diagonal movement between Z levels

Diagonal movement between Z-levels is possible when the floor is missing from the space above the wall, which would otherwise block movement. Flying and swimming creatures can pass through the gap caused by the missing floor. Common causes for a missing floor include building an up-down or down stair (without the matching up staircase below it), or constructing a wall underneath tree branches.[2] For example, this giant sparrow *can* attack the cat, because the down stairs (`>`) on level 2 has removed the floor, creating a hidden gap:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| S | ░ | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| T | h | i | s |   | d | i | a | g | r | a | m |   | h | a | s |   | m | u | l | t | i | p | l | e |   | z | - | l | e | v | e | l | s | ! |   | P | r | e | s | s |
| \ |   | t | o |   | g | o |   | u | p |   | o | n | e |   | z | - | l | e | v | e | l | . |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ░ | ░ | ░ | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ░ | \> | c | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| ░ | ░ | ░ | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| T | h | i | s |   | d | i | a | g | r | a | m |   | h | a | s |   | m | u | l | t | i | p | l | e |   | z | - | l | e | v | e | l | s | ! |   | P | r | e | s | s |
| \> |   | t | o |   | g | o |   | d | o | w | n |   | o | n | e |   | z | - | l | e | v | e | l | . |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   | ░ | ░ |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| T | h | i | s |   | d | i | a | g | r | a | m |   | h | a | s |   | m | u | l | t | i | p | l | e |   | z | - | l | e | v | e | l | s | ! |   | P | r | e | s | s |
| \> |   | t | o |   | g | o |   | d | o | w | n |   | o | n | e |   | z | - | l | e | v | e | l | . |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Path finding method

*Dwarf Fortress* uses the A* search algorithm (a nice demo) (confirmation), which quickly calculates the ideal path between points. Despite what this wiki has previously said, the heuristic used in *Dwarf Fortress* is admissible, and thus the ideal path is always found; whether your dwarf actually picks the right point B to go to is a different question.

Choosing the nearest raw materials uses the shortcut of checking the Manhattan distance from the dwarf's current position, rather than an actual search. Thus, when constructing things, the valid materials list will be ordered from nearest to farthest; this, however, ignores any walls or obstacles in the way. Workshops automatically path to the nearest valid raw materials; building things allows you to choose what to grab.

Note: The Manhatten distance does not really seem to be used in the current version to find the nearest (valid) material. That would mean that materials with x-distance n (and y-distance and z-distance both being zero) would be gathered before materials with x-distance (n-k), where 0

## Applications

For workshop jobs, the closest available valid material is used for the job. The simplest way to use pathing to your advantage is to surround a workshop with a stockpile accepting only specific raw materials that you want it to be using. While this is usually better handled by using linked stockpiles, it remains useful when trying to understand why, instead of decorating some beds in your furniture stockpile, your gem setter decides to fancify some commoners' coffins in the next-door mason's workshop.

The way pathing is handled should influence the way you design your fortress. An important part of fortress design is to be as closed as possible (again, the exact opposite of what the wiki has previously said), to reduce the amount of tiles searched overall; A\*, in edge cases, will search every single tile on the map, so making sure there are simply fewer tiles will speed up the game in those edge cases. Those edge cases are, generally, the only place where pathfinding actually has any major effect on performance.

Applications of pathing (aka pathing abuse). Note that they do see every path, so if the green bottom bridge is raised, they will take the caravan entrance instead.

Implications in security design are a bit more thorough. Hostile creatures and dwarves running errands are able to consider the entire map when making pathing choices, and their A\* pathfinding will mean that they will always take the shortest route, if there is a choice. This is a point separating trading caravans, which path to your trade depot, from goblin sieges, which look for the shortest path in instead. One clever exploit of this behavior is demonstrated at right; caravans will always take the winding, clean-top path, because that is where the trading post is, while incoming enemies will prefer the shorter, trapped bottom entrance.

### Doing the Calculation

Each tile will have a value, this value is in some way based on how close it brings us to the item and that tile's traffic value. Thus the procedure is something like this:

1.  First, we check all the tiles next to the target and mark their values.
2.  From there, repeatedly check all accessible tiles from the target until we reach the dwarf.
3.  From the dwarf, pick recursively the tiles with the lowest value, and you have a path.
4.  Now the dwarf will follow this path to get to the target.

Things that are wandering (Animals, wandering invaders) may use a combination of the above method with some random movement. For jobs that require chasing a moving thing, this procedure may be done over and over, or a different algorithm may be used.

Additionally, the following variations have been suggested, but nothing is certain:

- Dwarves may remember paths that have worked before and try them before anything else.
- Inaccessible items may be invisibly considered forbidden for a certain amount of time after a dwarf discovers it is inaccessible, and therefore not considered in pathing.

### Optimizations

To improve pathing speed and performance:

- Keep small stockpiles immediately next to workshops. This means Urist McCrafter doesn't have to do very much pathing to find their rocks (though it may cause Urist McHauler to do even more pathing).
- Keep Haulers near places where things will need to be moved from (excess stockpiles, mines, butcher's shops or other shops that have a high item yield).
- Make it easy to get in and out of the areas where workshops are.
- Staircases in rooms instead of in central areas should greatly improve pathing speeds.
- Applying traffic costs properly will greatly increase the speed of finding paths. Make corners of rooms higher cost and the center of major hallways and rooms with stockpiles and workshops lower cost. More on traffic.

### Splitted One-way

It's not possible to create areas path-able in one way only (though it was in 0.28, by exploiting a bug). However, it's possible to create a strong preference for pathing differently in different directions. A\* algorithm in itself allows asymmetry, which suggests that bias in its priorities at least sometimes can be exploited to split traffic by direction. Consider this floor diagram:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  |  | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  |
| ░ | R | R | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | H | H | ░ |  |  | ░ |  | → | → | → | → | → | → | → | → | → | → |  | ░ |  |
| \+ | \+ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | \+ | \+ |  |  | ↔ | ┤ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ├ | ↔ |  |
| ░ | H | H | \+ | \+ | \+ | \+ | \+ | \+ | \+ | \+ | R | R | ░ |  |  | ░ |  | ← | ← | ← | ← | ← | ← | ← | ← | ← | ← |  | ░ |  |
| ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  |  | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  |
| ░ |  | : |  | w | a | l | l |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| \+ |  | : |  | f | l | o | o | r |  | \- |  | n | o | r | m | a | l |  | t | r | a | f | f | i | c |  |  |  |  |  |
| H |  | : |  | f | l | o | o | r |  | \- |  | H | i | g | h |  | t | r | a | f | f | i | c |  |  |  |  |  |  |  |
| R |  | : |  | f | l | o | o | r |  | \- |  | R | e | s | t | r | i | c | t | e | d |  | t | r | a | f | f | i | c |  |

If this fragment is set up between a closed cave and outside, dwarves will always choose to pass through it via the left corridor, even if that corridor is farther both from the dwarf's original location and destination. Since A\* is "best-first", i.e. strongly prioritizes lower path cost in the immediate vicinity, we may guess that DF calculates path *from* the destination to the creature. (This seems more efficient if creatures more often need to path from open space *into* a dead-end or maze than vice versa, or the destination is cut off from open space more often than the creature.)

This isn't foolproof (e.g. pets ignore traffic designations and dorfs don't path *through* it from end to end when picking up something *within* it), or even too useful in itself (you need alternate paths to be very close - enough that the immediate traffic cost matters much more than difference in distance), but it does allow to e.g. make assumptions as to whether a dwarf arrives or leaves for pressure plate automation purpose, without forcing path retries (and attendant CPU load) inherent in "suddenly closed door"/"suddenly opened hatch" technique (even if you need a strict one-way, these methods can be combined, to make path retry an exception rather than rule).

The longer the space between entrance and exit (left and right in the diagram) of the two one-way-floors, the more likely dwarves will stick to the desired side even obstacles like animals and dwarves are in their way. Of course, there will be fewer actual collisions than predicted if everyone moves in the same direction.

**Warning:** Using Restricted traffic on floors dwarves have to pass — like the entrance of a fortress - leads to high pathing costs (and thus potentially FPS drop) because of searching for alternative routes!\[Verify\]

If you want to use this, keep those (path-through) restricted areas as small as possible. On the other side, the higher the restricted costs, the more likely dwarves stick to the correct site. The same is true for longer tunnels. And the longer the tunnel, the less additional pathing will be done. If the tunnel is at least as long as the costs of the restricted area, you don't have to bother additional costs. So, this should only be used for long tunnels. Never use it to control traffic inside your fort between rooms unless you restrict most of your fort's area!

## Other dwarves

It is possible for entities such as dwarves to walk over each other when necessary. However, moving over occupied tiles in this manner is much slower, and dwarves will try to path so that they can avoid it. This introduces an important consideration to fortress design.

If you have a long, 1-tile wide corridor which already has a dwarf moving through it, other dwarves who need to get from one side of the corridor to the other will try to avoid colliding with that dwarf, by pathing elsewhere. If it so happens that the corridor is long, and there are no nearby alternative routes, this may cause a very significant increase in pathfinding burden.

For this reason, it's best to make high-traffic routes at least 2 tiles wide, and avoid single doors and single stairs. This ensures that when a dwarf tries to find a detour around another dwarf in his way, he will be able to do so easily and without modifying his current path much.

|  |
|----|
| "Path" in other / Languages / Dwarven / : / nimar / Elven / : / alí / Goblin / : / snust / Human / : / anur |
