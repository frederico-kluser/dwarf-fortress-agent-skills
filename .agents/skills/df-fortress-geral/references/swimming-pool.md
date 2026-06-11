# Swimming pool

> Fonte: [Swimming pool](https://dwarffortresswiki.org/index.php/Swimming_pool) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

A swimming pool is a chamber filled with less than 7/7 deep water. Its design can be similar to that of a drowning chamber, except you want to use it on your own dwarves - to teach them to swim.

A dwarf in the water will gain the ability to swim very fast - sadly, not fast enough to prevent death from drowning. While water with a depth of 7/7 is deadly for non-swimmers, you can safely use water at depths from 4/7 to 6/7 to teach dwarves how to swim without risk of drowning. The speed of learning is independent of the depth, but water with a depth of less than 4/7 is not deep enough to make a dwarf swim, and therefore learn anything.

Training your dwarves just requires a place of constant or temporary 4/7 to 6/7 depth water. Military orders or making rooms a meeting hall will not entice dwarves into the water, so you may need to prevent them from leaving an area (by locking the door, for example) and then fill the area with the required amount of water, or dump them in from above using a retracting bridge.

Swimming, since it involves no activity, can be potentially useful to train weaker, disabled or injured dwarves, whose conditions might go away or become manageable with an attribute boost to strength, endurance, willpower, etc.

A fully automated method to train idlers is to use water flowing over a 1-Z-level drop, with a 1-wide meeting zone at the top of the ledge, and a swimming pool at the bottom. Idlers will go to the meeting zone, be swept over the side into the pool and swim to the ramp, and repeat this for as long as they are idle. The meeting zone must have a low enough rate of flow that it has unsubmerged tiles, so dwarves voluntarily move into it. This can be accomplished with tricks like restricting flow through diagonal passages (see Pressure for details). Be aware that in recent versions, dwarves can now suffer injuries more easily when falling, so this method can cause serious ~~harm~~ fun when the dwarves are washed over the edge. Constructing the landing zone out of lighter materials will help prevent serious complications.

    Diagram of the 'fully automated' configuration described above:

     .... - (pool continues as desired)
    ║≈≈≈≈║  - depth 4-6 swimming pool on Z-1
    ║+++▲║  - dropoff / entrance ramp from above
    ║~~~~║ - meeting hall, depth 0-3
    ╚╗%╔═╝
     ║%║ - screw pump (S->N)
     ║.║    - limited pump source (e.g. depth ~4-per-tick tile on Z-1)
     ╚═╝
    Not pictured: exit from the swimming pool, preferably close to the entrance ramp to minimize delays in training.

### Minecart training

With the addition of minecarts, a safe, automated swimming experience can be almost guaranteed. Originally, the design involved hauling dwarves down into a pond and forcing them to swim back out.[1] However, it was discovered that dwarves gain swimming skill while simply riding in the minecart. A simple loop track which descends 1 Z-level into a pool of water then climbs back out will train your dwarves quickly and conveniently. It is advisable to ensure your pond has a uniform depth, because fluid flow can interfere with the minecart and may even knock it off-track; see Minecart logic for details. A depth of 4/7 or 5/7 is ideal. Note that water will slow the minecart considerably; if you use impulse ramps instead of rollers, you'll want one impulse ramp after roughly 10 tiles of 4/7 water.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  |  |  |  |  |  |  |  |  |  |  |  | z |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | z | \+ | 1 |  |  |  |  |  |  |  |  |  |  |  |
|  | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  |
|  | ░ | ╔ | ═ | ═ | ▲ | ═ | ═ | ═ | ═ | ═ | ═ | ═ | ═ | ═ | ═ | ▲ | ═ | ═ | ═ | ═ | ═ | ═ | ╗ | ░ |  |  |  | ░ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ░ |  |
|  | ░ | ║ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ║ | ░ |  |  |  | ░ |  | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  | ░ |  |
|  | ░ | ╚ | ═ | ═ | ═ | ═ | ▲ | ═ | ═ | ═ | ▲ | ░ | ░ | ░ | ▲ | ═ | ═ | ═ | ═ | ═ | ═ | ▲ | ╝ | ░ |  |  |  | ░ |  |  |  |  |  |  |  |  |  | ▼ | ╗ | \+ | ╞ | ▼ |  |  |  |  |  |  |  |  | ░ |  |
|  | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ║ | ^ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ | ░ |  |
|  |  |  |  |  |  |  |  |  |  |  | ░ | \+ | ░ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ░ | H | \+ | ░ |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | ░ | \+ | ░ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ░ | ░ | \+ | ░ |  |  |  |  |  |  |  |  |  |  |  |

A large swimming track

1.  Carve the tracks and add impulse ramps (shown) or rollers on level z.
2.  Optionally, add statues or other buildings along the tracks for your dwarves to admire. (Make sure to leave the corner walls intact).
3.  Fill the track section on layer z with 4/7 water.
4.  Link the pressure plate '^' to the hatch cover 'H' (this is necessary to automatically dispose of worn clothing that dwarves drop at the end of the ride).
5.  Set stop 1 to ride down the ramp to the east immediately/always.
6.  Assign a minecart to the route (lightweight wooden minecarts are recommended in case of collisions).
7.  Dwarves with the "Push/Haul Vehicles" labor enabled will now automatically train swimming.
